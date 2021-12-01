sudo apt update
sudo apt upgrade

# Install PostgreSQL database
sudo apt install postgresql
sudo su -c "createuser -s $USER" postgres # Creates db superuser

# Install Odoo system dependencies
sudo apt install git python3-dev python3-pip python3-wheel python3-venv
sudo apt install build-essential libpq-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev

# Install wkhtml2pdd, to generate PDF reports
wget "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.focal_amd64.deb" -O /tmp/wkhtml.deb
sudo dpkg -i /tmp/wkhtml.deb
sudo apt-get -fy install  # Fix dependency errors

# Setup Odoo service dedicated user, for better security
sudo adduser --home=/opt/odoo --disabled-password --gecos "Odoo" odoo
sudo su -c "createuser odoo" postgres
createdb --owner=odoo odoo-prod  # odoo-prod is the production database


# Install Odoo from source code
sudo su - odoo
git clone https://github.com/odoo/odoo.git /opt/odoo/odoo14 -b 14.0 --depth=1
git clone https://github.com/PacktPublishing/Odoo-12-Development-Essentials-Fourth-Edition /opt/odoo/library
python3 -m venv /opt/odoo/env14
source /opt/odoo/env14/bin/activate
pip install -r /opt/odoo/odoo14/requirements.txt
pip install -e /opt/odoo/odoo14
exit

# Setup Odoo configuration file
/opt/odoo/env14/bin/odoo -c /opt/odoo/odoo.conf --save --stop-after-init -d odoo-prod
--db-filter="^odoo-prod$" --without-demo=all --proxy-mode --addons-path="/opt/odoo/odoo14/addons,/opt/odoo/library"
sudo mkdir /etc/odoo
sudo cp /opt/odoo/odoo.conf /etc/odoo/odoo.conf
sudo chown -R odoo /etc/odoo
sudo chmod u=r,g=rw,o=r /etc/odoo/odoo.conf  # for extra hardening
sudo mkdir /var/log/odoo
sudo chown odoo /var/log/odoo

# Setup systemd service
sudo cp odoo.service /lib/systemd/system/odoo.service
sudo systemctl enable odoo.service
sudo systemctl start odoo
# sudo systemctl status odoo
# sudo systemctl stop odoo

# Create self signed certificate
sudo mkdir /etc/ssl/nginx && cd /etc/ssl/nginx
sudo openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
sudo chmod a-wx *            # make files read only
sudo chown www-data:root *   # access only to www-data group


# Install Nginx
sudo apt-get install nginx
sudo service nginx start
sudo rm /etc/nginx/sites-enabled/default
sudo cp odoo.nginx /etc/nginx/sites-available/odoo
sudo ln -s /etc/nginx/sites-available/odoo /etc/nginx/sites-enabled/odoo
sudo service nginx reload
