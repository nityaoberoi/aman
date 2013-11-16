#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wtforms import Form, TextField, validators


class ContactUsForm(Form):
    name = TextField('Name', [validators.Length(min=2, max=50)])
    email = TextField('Email Address', [validators.Length(min=6, max=40)])
    subject = TextField('Subject', [validators.Length(min=0, max=100)])
    message = TextField('Subject', [validators.Length(min=5, max=800)])
