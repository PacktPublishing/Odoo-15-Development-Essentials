{
  "name": "Library Website",
  "description": "Create and check book checkout requests.",
  "author": "Daniel Reis",
  "license": "AGPL-3",
  "depends": [
    "library_checkout",
    "portal",
  ],
  "data": [
    "security/ir.model.access.csv",
    "security/library_security.xml",
    "views/main_templates.xml",
    "views/portal_templates.xml",
  ],
  "assets": {
    "web.assets_backend": {
      "library_portal/static/src/css/library.css",
    }
  },
}
