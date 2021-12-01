sudo su - odoo
mkdir /opt/odoo/stage
cp -r /opt/odoo/odoo14/ /opt/odoo/stage/
cp -r /opt/odoo/library/ /opt/odoo/stage/  # custom code
python3 -m venv /opt/odoo/env-stage
source /opt/odoo/env-stage/bin/activate
pip install -r /opt/odoo/stage/odoo14/requirements.txt
pip install -e /opt/odoo/stage/odoo14
exit
