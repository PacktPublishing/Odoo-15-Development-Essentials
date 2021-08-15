# Dowload Odoo code updates
sudo su - odoo
cd /opt/odoo/odoo14
git tag --force 14-last-prod
git pull

# Start Staging service
source /opt/odoo/env14/bin/activate
odoo -c /etc/odoo/odoo.conf -d odoo-stage --http-port=8080
exit
