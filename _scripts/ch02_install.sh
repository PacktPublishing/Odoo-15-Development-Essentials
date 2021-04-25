sudo apt update
sudo apt upgrade
sudo apt install postgresql # Installs PostgreSQL
sudo service postgresql start
sudo su -c "createuser -s $USER" postgres # Creates db superuser
sudo apt install git 
sudo apt install python3-dev python3-pip python3-wheel python3-venv
sudo apt install build-essential libpq-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev

mkdir ~/work14
cd ~/work14
git clone https://github.com/odoo/odoo.git -b 14.0 --depth=1

python3 -m venv ~/work14/env14
source ~/work14/env14/bin/activate
pip install -U pip
pip install -r ~/work14/odoo/requirements.txt
pip install -e ~/work14/odoo

odoo -d 14-demo --stop-after-init
odoo -c ~/work14/14-demo.conf --save --stop

cd ~/work14
git clone https://github.com/PacktPublishing/Odoo-14-Development-Essentials.git library
odoo -d 14-library --addons-path="./library,./odoo/addons" --save --stop
