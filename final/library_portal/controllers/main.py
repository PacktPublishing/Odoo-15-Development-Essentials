from odoo import http


class Main(http.Controller):

    @http.route("/library/catalog", auth="public", website=True)
    def catalog(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.sudo().search([])
        res =  http.request.render(
            "library_portal.book_catalog",
            {"books": books},
        )
        return res
