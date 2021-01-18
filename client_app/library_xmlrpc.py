import xmlrpc.client


class LibraryAPI():

    def __init__(self, host, port, db, user, pwd):
        common = xmlrpc.client.ServerProxy(
            "http://%s:%d/xmlrpc/2/common" % (host, port))
        self.api = xmlrpc.client.ServerProxy(
            "http://%s:%d/xmlrpc/2/object" % (host, port))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = "library.book"

    def _execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, arg_list, kwarg_dict or {})

    def search_read(self, title=None):
        domain = [("name", "ilike", title)] if title else []
        fields = ["id", "name"]
        return self._execute("search_read", [domain, fields])

    def create(self, title):
        vals = {"name": title}
        return self._execute("create", [vals])

    def write(self, id, title):
        vals = {"name": title}
        return self._execute("write", [[id], vals])

    def unlink(self, id):
        return self._execute("unlink", [[id]])

if __name__ == "__main__":
    # Sample test configurations
    host, port, db = "localhost", 8069, "14-library"
    user, pwd = "admin", "admin"
    api = LibraryAPI(host, port, db, user, pwd)
    from pprint import pprint
    pprint(api.search_read())
