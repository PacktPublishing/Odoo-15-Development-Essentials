from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)
        self.Book = self.env["library.book"]
        self.book1 = self.Book.create({
            "name": "Odoo Development Essentials",
            "isbn": "879-1-78439-279-6"})

    def test_book_create(self):
        "New Books are active by default"
        self.assertEqual(
            self.book1.active, True
        )

    def test_check_isbn(self):
        "Check valid ISBN"
        self.assertTrue(self.book1._check_isbn)
