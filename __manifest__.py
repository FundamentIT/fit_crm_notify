# -*- coding: utf-8 -*-
# Copyright 2018 Fundament IT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'FIT CRM Notification',
    'category': 'Website',
    'version': '10.0.1.0.1',
    'author': 'Fundament IT',
    'website': 'https://fundament.it/',
    'licence': 'AGPL-3',
    'depends': ['website_crm'],
    'summary':"""""",
    'description': """
Sends notification email when contact form is submitted.
    """,
    'data': [
        'data/fit_crm_notify_data.xml',
    ],
    'installable': True,
}
