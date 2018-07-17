# -*- coding: utf-8 -*-
# Copyright 2018 Fundament IT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import odoo
_logger = logging.getLogger(__name__)


class WebsiteForm(odoo.addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        _logger.info('START INSERT RECORD')
        record_id = super(WebsiteForm, self).insert_record(request, model, values, custom, meta)
        _logger.info('INSERTED RECORD: '+ str(record_id))

        if model.model == 'crm.lead':
            _logger.info('IS CRM LEAD')
            template = request.env.ref('fit_crm_notify.fit_crm_notify_mail', False)
            _logger.info('REQUESTED TEMPLATE')
            if template:
                _logger.info('FOUND TEMPLATE, START MAIL SENDING')
                mail_id = template.sudo().send_mail(record_id, force_send=True)
                _logger.info('MAIL SEND: '+str(mail_id))

        return record_id
