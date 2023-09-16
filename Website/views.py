from flask import Blueprint, render_template, request, jsonify, redirect, url_for

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

views = Blueprint(__name__, "views")
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/resources")
def resources():
    return render_template("resources.html")
@views.route("/tutor")
def tutor():
    return render_template("tutor.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

@views.route("/reading")
def reading():
    return render_template("reading.html")

@views.route("/math")
def math():
    return render_template("math.html")
@views.route("/writing")
def grammar():
    return render_template("writing.html")
@views.route("/about_us")
def about_us():
    return render_template("about_us.html")


@views.route("/contact", methods=["POST"])
def handle_contact_form():
    if request.content_type.startswith('application/json'):
        data = request.get_json(force=True, silent=True)
    else:
        data = request.form

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    send_email(name, email, message)

    return redirect(url_for('views.thank_you'))

def send_email(name, email, message):
    smtp_host = "smtp.gmail.com"  
    smtp_port = 587  
    sender_email = "ddda4168@gmail.com"
    sender_password = "atsastoaksiooent"

    subject = "New Contact Form Submission"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = sender_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
@views.route("/submit_tutor", methods=["POST"])
def submit_tutor():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        experience = request.form.get("experience")
        sat_score = request.form.get("SAT Score")

        send_tutor_application_email(name, email, experience, sat_score)

        return redirect(url_for('views.thank_you'))

    return redirect(url_for('views.tutor'))

def send_tutor_application_email(name, email, experience, sat_score):
    smtp_host = "smtp.gmail.com" 
    smtp_port = 587  
    sender_email = "ddda4168@gmail.com" 
    sender_password = "atsastoaksiooent"  

    subject = "Tutor Application"
    body = f"Name: {name}\nEmail: {email}\nExperience: {experience}\nSAT Score: {sat_score}\n\nThank you for applying to be a tutor."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = sender_email  

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [sender_email], msg.as_string())
