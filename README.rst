==================
Website CRM Notify
==================

This module provides the following functions:

* When someone sends an inquiry from "Contact us" page on website,
  a notification email is sent to the user set as hard value within the template.

This module depends on ``wbsite_crm`` module.


Installation
============

No special instructions.


Configration
============

* Go to *Settings > Technical > Email > Templates* and select "Contact Form Notify",
  and edit the email template according to your needs.

By default, an email is sent to the email addresses of the following:

* the company (for the purpose of notification)

The body of the email includes all the information the sender inputs (Name, Company, Question etc.).


Usage
=====

Your customer comes to "Contact us" page of your website and fills in the form.
An email is sent out with the input content when the form is submitted.
