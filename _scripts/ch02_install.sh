sudo apt update
sudo apt upgrade
sudo apt install postgresql # Installs PostgreSQL
sudo service postgresql start
sudo su -c "createuser -s $USER" postgres # Creates db superuser
sudo apt install git
sudo apt install python3-dev python3-pip python3-wheel python3-venv
sudo apt install build-essential libpq-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev

mkdir ~/work15
cd ~/work15
git clone https://github.com/odoo/odoo.git -b 15.0 --depth=1

python3 -m venv ~/work15/env15
source ~/work15/env15/bin/activate
pip install -U pip
pip install -r ~/work15/odoo/requirements.txt
pip install -e ~/work15/odoo

odoo -d 15-demo --stop-after-init
odoo -c ~/work15/15-demo.conf --save --stop

cd ~/work15
git clone https://github.com/PacktPublishing/Odoo-15-Development-Essentials.git library
odoo -d 15-library --addons-path="./library,./odoo/addons" --save --stop
