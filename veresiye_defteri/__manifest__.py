{
    'name': 'Veresiye Defteri',
    'version': '1.0',
    'summary': 'Müşteri veresiye takibi',
    'author': 'Your Company',
    'category': 'Accounting',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/ledger_views.xml',
        'report/receipt_report.xml',
    ],
    'installable': True,
    'application': True,
}
