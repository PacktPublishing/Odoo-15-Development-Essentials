{
    "name": "Library Book Checkout",
    "description": "Members can borrow books from the library.",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "depends": ["library_member", "mail", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/checkout_mass_message_wizard_view.xml",
        "views/library_menu.xml",
        "views/checkout_view.xml",
        "views/checkout_kanban_view.xml",  # Ch11
        "data/stage_data.xml",
        # "views/assets.xml",  # Ch11, until Odoo 14
    ],
    "assets": {  # Ch11, since Odoo 15
        "web.assets_backend": {
            "library_checkout/static/src/css/checkout.css",
            "library_checkout/static/src/js/checkout.js",
        }
    }
}
