#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template, request
from flask.ext.mail import Message, Mail
from forms import ContactUsForm


mail = Mail()
app = Flask(__name__)
app.config.from_pyfile('config.py')
mail.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/programs/usa/')
def usa():
    return render_template('programs/usa.html')


@app.route('/programs/canada/')
def canada():
    return render_template('programs/canada.html')


@app.route('/programs/europe/')
def eu():
    return render_template('programs/eu.html')


@app.route('/partnerships/')
def partnerships():
    return render_template('partnerships.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    success = False
    form = ContactUsForm(request.form)
    if request.method == 'POST':
        send_email(form)
        success = True
        form = ContactUsForm()
    return render_template('contact.html', form=form, success=success)


@app.route('/faqs/')
def faqs():
    return render_template('faq.html')


@app.route('/tos/')
def terms():
    return render_template('terms.html')


def send_email(form):

    recipients = ['nitya.oberoi@gmail.com']

    name = form.name.data
    email = form.email.data
    subject = "Aman Investments Contact Form: {}".format(form.subject.data)

    msg = Message(subject, sender=email, recipients=recipients)

    msg.body = """
      Name: {} \n
      Email: {} \n
      Subject: {} \n
      Message: {}
      """.format(name, email, subject, form.message.data)

    mail.send(msg)


if __name__ == "__main__":
    app.run()
