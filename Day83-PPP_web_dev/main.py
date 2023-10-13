"""
Using what you have learnt about web development, build your own portfolio website.
This can be designed any way you want. It's the place to show off your skills and the things you've built.
Take inspiration from other developers but try not to copy their designs. Because this is about showing off what you can do!
Use what you've learnt from Day 65 and plan out your website. Think about design, UI, UX, colour schemes, fonts. 
Don't build the website for other people, build it to make yourself proud.
If you want, deploy and host the website to share with other students so we can admire your hard work!

What kind of website do I want to build? 

(my own logo)       Home    About   Git    Contact

Approach:
1. Make a web page (can be without any content or images)
2. Add images (probably use pre-made bootstrap?) Section 59
3. Make buttons function (by clicking the button, url will be directed to another page)
4. 

"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, URL
from flask_ckeditor import CKEditor, CKEditorField
import requests
import os


app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
# Bootstrap5(app)

# Connect to CKEditor
# ckeditor = CKEditor()
# ckeditor.init_app(app)


# WTForm
# class ContactForm(FlaskForm):
#     name     = StringField(label="Name", validators=[DataRequired()])
#     email    = StringField(label="Email", validators=[DataRequired(), Email()])
#     subject  = StringField(label="Subject")
#     message  = CKEditorField(label="Message", validators=[DataRequired()]) 
#     submit   = SubmitField("Submit")
    

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
    # contact_form = ContactForm()
    # if contact_form.validate_on_submit(): # validate_on_submit() verifies if "POST" method or not as well
    #     return redirect(url_for("home"))
    return render_template("contact.html") #, form=contact_form)

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)




