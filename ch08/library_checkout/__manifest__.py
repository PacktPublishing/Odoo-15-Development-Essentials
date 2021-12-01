{
    "name": "Library Book Checkout",
    "description": "Members can borrow books from the library.",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "depends": ["library_member", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/checkout_mass_message_wizard_view.xml",
        "views/library_menu.xml",
        "views/checkout_view.xml",
        "data/stage_data.xml",
    ],
}
