"""
To run this script, using click-odoo:

  $ pip3 install -e /path/to/odoo
  $ pip3 install click-odoo
  $ click-odoo -c my.conf -b mydb myscript.py

To try the code in the interactive shell:

  $ pip3 install -e /path/to/odoo
  $ odoo shell -c my.conf

Inspecting the Odoo shell execution environment:

>>> self
res.users(1,)
>>> self._name
'res.users'
>>> self.name
'System'
>>> self.login
'__system__'

>>> self.env  # doctest: +ELLIPSIS
<odoo.api.Environment object at ...>

>>> self.env["res.partner"].search([("display_name", "like", "Azure")])
res.partner(14, 26, 33, 27)

The environment context:

>>> self.env.context
{'lang': 'en_US', 'tz': 'Europe/Brussels'}

>>> self.env.ref('base.user_root')
res.users(1,)

Querying data with recordsets and domains:

>>> self.env['res.partner'].search([('display_name', 'like', 'Lumber')])
res.partner(15, 34)
>>> self.env['res.partner'].browse([15, 34])
res.partner(15, 34)

Group by fields and aggregate data:

>>> self.env["res.partner"].read_group([("display_name", "like", "Azure")], fields=["state_id:count_distinct",], groupby=["country_id"], lazy=False)  # doctest: +ELLIPSIS
[{'__count': 4, 'state_id': 1, 'country_id': (233, <odoo.tools.func.lazy object at ...>), '__domain': ['&', ('country_id', '=', 233), ('display_name', 'like', 'Azure')]}]

Accessing data on recordsets:

>>> print(self.name)
System

>>> for rec in self: print(rec.name)
System


The following dot-notation field access is safe transversing empty records:

>>> self.company_id
res.company(1,)
>>> self.company_id.name
'YourCompany'
>>> self.company_id.currency_id
res.currency(1,)
>>> self.company_id.currency_id.name
'EUR'

>>> self.company_id.parent_id
res.company()
>>> self.company_id.parent_id.name
False

Accessing date and time values:

>>> self.browse(2).login_date  # doctest: +ELLIPSIS
datetime.datetime(...)

Using object-style value assignment:

>>> root = self.env["res.users"].browse(1)
>>> print(root.name)
System
>>> root.name = "Superuser"
>>> print(root.name)
Superuser
>>> root.name = "System"

>>> from datetime import date
>>> self.date = date(2020, 12, 1)
>>> self.date
datetime.date(2020, 12, 1)
>>> self.date = "2020-12-02"
>>> self.date
datetime.date(2020, 12, 2)

# import base64
# blackdot_binary = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x04\x00\x00\x00\xb5\x1c\x0c\x02\x00\x00\x00\x0bIDATx\xdacd\xf8\x0f\x00\x01\x05\x01\x01'\x18\xe3f\x00\x00\x00\x00IEND\xaeB`\x82"
# self.image_1920 = base64.b64decode(blackdot_binary)

>>> self.child_ids = None
>>> self.child_ids
res.partner()

>>> mycompany_partner = self.company_id.partner_id
>>> myaddress = self.partner_id
>>> mycompany_partner.child_ids = mycompany_partner.child_ids | myaddress
>>> mycompany_partner.child_ids |= myaddress

>>> Partner = self.env['res.partner']
>>> recs = Partner.search( [("name", "ilike", "Azure")])
>>> recs.write({"comment": "Hello!"})
True

Creating and deleting records:

>>> Partner = self.env['res.partner']
>>> new = Partner.create({'name': 'ACME', 'is_company': True})
>>> print(new)  # doctest: +ELLIPSIS
res.partner(...,)

>>> new.unlink()
...
True

>>> demo = self.env.ref('base.user_demo')
>>> new = demo.copy({'name': 'John', 'login': 'john@example.com'})
>>> new.unlink()
...
True

Adding and subtracting time:

>>> from datetime import date
>>> date.today()  # doctest: +ELLIPSIS
datetime.date(...)
>>> from datetime import timedelta
>>> date(2020, 11, 3) + timedelta(days=7)
datetime.date(2020, 11, 10)

>>> from dateutil.relativedelta import relativedelta
>>> date(2020, 11, 3) + relativedelta(years=1, months=1)
datetime.date(2021, 12, 3)

>>> from odoo.tools import date_utils
>>> from datetime import datetime
>>> now = datetime(2020, 11, 3, 0, 0, 0)
>>> date_utils.start_of(now, 'week')
datetime.datetime(2020, 11, 2, 0, 0)
>>> date_utils.end_of(now, 'week')
datetime.datetime(2020, 11, 8, 23, 59, 59, 999999)
>>> today = date(2020, 11, 3)
>>> date_utils.add(today, months=2)
datetime.date(2021, 1, 3)
>>> date_utils.subtract(today, months=2)
datetime.date(2020, 9, 3)

Converting date and time objects to a text representation:

>>> from datetime import date
>>> date(2020, 11, 3).strftime("%d/%m/%Y")
'03/11/2020'


Converting text-represented dates and times:

>>> from odoo import fields
>>> fields.Datetime.to_datetime("2020-11-21 23:11:55")
datetime.datetime(2020, 11, 21, 23, 11, 55)

>>> from datetime import datetime
>>> datetime.strptime("03/11/2020", "%d/%m/%Y")
datetime.datetime(2020, 11, 3, 0, 0)

>>> from datetime import datetime
>>> import pytz
>>> naive_date = datetime(2020, 12, 1, 0, 30, 0)
>>> client_tz = self.env.context["tz"]
>>> client_date = pytz.timezone(client_tz).localize(naive_date)
>>> utc_date = client_date.astimezone(pytz.utc)
>>> print(utc_date)
2020-11-30 23:30:00+00:00

Recordset operations:

>>> rs0 = self.env["res.partner"].search([("display_name", "like", "Azure")])
>>> len(rs0)  # how many records?
4
>>> rs0.filtered(lambda r: r.name.startswith("Nicole"))
res.partner(27,)
>>> rs0.filtered("is_company")
res.partner(14,)
>>> rs0.mapped("name")
['Azure Interior', 'Brandon Freeman', 'Colleen Diaz', 'Nicole Ford']
>>> rs0.sorted("name", reverse=True).mapped("name")
['Nicole Ford', 'Colleen Diaz', 'Brandon Freeman', 'Azure Interior']
>>> rs0.mapped(lambda r: (r.id, r.name))
[(14, 'Azure Interior'), (26, 'Brandon Freeman'), (33, 'Colleen Diaz'), (27, 'Nicole Ford')]

Executing raw SQL:

>>> self.env.cr.execute("SELECT id, login FROM res_users WHERE login=%s OR id=%s", ("demo", 1))
>>> self.env.cr.fetchall()
[(6, 'demo'), (1, '__system__')]
>>> self.env.cr.execute("SELECT id, login FROM res_users WHERE login=%(login)s OR id=%(id)s", {"login": "demo", "id": 1})
>>> self.env.cr.dictfetchall()
[{'id': 6, 'login': 'demo'}, {'id': 1, 'login': '__system__'}]
"""


import doctest


self = env.user
doctest.testmod(verbose=True, raise_on_error=False)
