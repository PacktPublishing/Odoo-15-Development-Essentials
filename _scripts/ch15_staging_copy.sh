dropdb odoo-stage
createdb --owner=odoo odoo-stage
pg_dump odoo-prod | psql -d odoo-stage
sudo su - odoo
cd ~/.local/share/Odoo/filestore/
cp -r odoo-prod odoo-stage
exit
