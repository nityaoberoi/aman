#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template
from forms import ContactUsForm

app = Flask(__name__)


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


@app.route('/programs/eu/')
def eu():
    return render_template('programs/eu.html')


@app.route('/partnerships/')
def partnerships():
    return render_template('partnerships.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/faqs/')
def faqs():
    return render_template('faq.html')


@app.route('/tos/')
def terms():
    return render_template('terms.html')


def send_email(form):
    print "Form is done!"


if __name__ == "__main__":
    app.run(debug=True)
