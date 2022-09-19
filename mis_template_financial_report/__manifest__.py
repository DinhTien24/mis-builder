# Copyright 2020 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Profit & Loss / Balance sheet MIS templates",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "author": "Hunki Enterprises BV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/mis-builder",
    "category": "Localization",
    "depends": ["mis_builder"],
    "data": [
        "data/mis_report_style.xml",
        "data/mis_report.xml",
        "data/mis_report_kpi.xml",
        "data/mis_report_subreport.xml",
        "views/mis_report_instance_views.xml",
        "views/templates.xml",
    ],
    "qweb": ["static/src/xml/mis_template_financial_report.xml"],
    "web.report_assets_common": [
        "mis_template_financial_report/static/src/css/mis_template_financial_report.css",
    ],
    "web.assets_backend": [
        "mis_template_financial_report/static/src/css/mis_template_financial_report.css",
    ],
    "maintainers": ["hbrunn"],
}