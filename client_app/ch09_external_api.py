from xmlrpc import client


# The common XML.RPC endpoint

srv = "http://localhost:8069"
common = client.ServerProxy("%s/xmlrpc/2/common" % srv)
common.version()
# Result: {'server_version': '14.0', 'server_version_info': [14, 0, 0, 'final', 0, ''], 'server_serie': '14.0', 'protocol_version': 1}

db, user, password = "14-library", "admin", "admin"
uid = common.authenticate(db, user, password, {})
print(uid)


# The object XML-RPC endpoint

api = client.ServerProxy('%s/xmlrpc/2/object' % srv)
api.execute_kw(db, uid, password, "res.users", "search_count", [[]])

api.execute_kw(db, uid, password, "res.users", "read", [2, ["login", "name", "company_id"]])
# Result: [{'id': 2, 'login': 'admin', 'name': 'Mitchell Admin', 'company_id': [1, 'YourCompany']}]

domain = [("login", "=", "admin")]
api.execute_kw(db, uid, password, "res.users", "search", [domain])
# Result : [2]

api.execute_kw(db, uid, password, "res.users", "search_read", [domain, ["login", "name"]])
# Result: [{'id': 2, 'login': 'admin', 'name': 'Mitchell Admin'}]

# Same call, using keyword arguments instead of positional arguments
api.execute_kw(db, uid, password, "res.users", "search_read", [], {"domain": domain, "fields": ["login", "name"]})


# Calling other API methods

x = api.execute_kw(db, uid, password, "res.partner", "create", [{'name': 'Packt Pub'}])
print(x)
api.execute_kw(db, uid, password, "res.partner", "write", [[x], {'name': 'Packt Publishing'}])
api.execute_kw(db, uid, password, "res.partner", "read", [[x], ["name"]])
api.execute_kw(db, uid, password, "res.partner", "unlink", [[x]])
api.execute_kw(db, uid, password, "res.partner", "read", [[x]])
