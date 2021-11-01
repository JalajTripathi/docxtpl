from flask import Flask, send_file, render_template, request, make_response, redirect
from flask.wrappers import Request
import generate, datetime

import os
import sys

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)

# app = Flask(__name__)

@app.route("/")
def index():
    if getCookie():
        print("Cookie Found")
        return render_template('agreement_selection.html')
    else:
        return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "ashok.srivastava63@gmail.com" and password == "aks@2021":
        cookie = setCookie(username)
        print("loggedIN: ", cookie.headers['Set-Cookie'])
        return cookie
    else:
        return render_template('login.html', error="Wrong combination of username and password! Try again!")

def setCookie(username):
    resp = make_response(redirect('/agreement_selection'))
    resp.set_cookie('userID', username, secure = True, max_age=None)
    return resp

@app.route("/agreement_selection", methods=['GET'])
def agreement_selection():
    if request.method == "GET":
        return render_template('agreement_selection.html')
    

@app.route("/gen", methods=['POST', 'GET'])
def gen_docx():
    if request.method == "POST":
        formData = {}
        formData['विक्रय_मूल्य'] = request.form['विक्रय_मूल्य']
        formData['विक्रय_मूल्य_शब्दों_में'] = request.form['विक्रय_मूल्य_शब्दों_में']
        formData['मालियत'] = request.form['मालियत']
        formData['देय_स्टाम्प'] = request.form['देय_स्टाम्प']
        formData['क्षेत्र_दर'] = request.form['क्षेत्र_दर']
        formData['ग्राम_कोड'] = request.form['ग्राम_कोड']
        formData['ग्राम'] = request.form['ग्राम']
        formData['सम्पत्ति_का_विवरण'] = request.form['सम्पत्ति_का_विवरण']
        formData['संपत्ति_का_क्षेत्रफल'] = request.form['संपत्ति_का_क्षेत्रफल']
        formData['प्रतिफल_की_धनराशि'] = request.form['प्रतिफल_की_धनराशि']
        formData['विक्रेता_का_विवरण'] = request.form['विक्रेता_का_विवरण']
        formData['क्रेता_का_विवरण'] = request.form['क्रेता_का_विवरण']
        formData['चौहद्दी_गाटा_संख्या'] = request.form.getlist('चौहद्दी_गाटा_संख्या[]')
        formData['पूरब'] = request.form.getlist('पूरब[]')
        formData['पश्चिम'] = request.form.getlist('पश्चिम[]')
        formData['उत्तर'] = request.form.getlist('उत्तर[]')
        formData['दक्षिण'] = request.form.getlist('दक्षिण[]')
        formData['अनुमति'] = request.form['a']
        formData['विक्रेता_का_आधार'] = request.form['विक्रेता_का_आधार']
        formData['विक्रेता_का_फ़ोन'] = request.form['विक्रेता_का_फ़ोन']
        formData['विक्रेता_का_पैन'] = request.form['विक्रेता_का_पैन']
        formData['क्रेता_का_आधार'] = request.form['क्रेता_का_आधार']
        formData['क्रेता_का_फ़ोन'] = request.form['क्रेता_का_फ़ोन']
        formData['क्रेता_का_पैन'] = request.form['क्रेता_का_पैन']
        formData['गवाहान_का_नाम_1'] = request.form['गवाहान_का_नाम_1']
        formData['गवाहान_का_पता_1'] = request.form['गवाहान_का_पता_1']
        formData['गवाहान_का_फ़ोन_1'] = request.form['गवाहान_का_फ़ोन_1']
        formData['गवाहान_का_पिता_का_नाम_1'] = request.form['गवाहान_का_पिता_का_नाम_1']
        formData['लिंग_1'] = request.form['लिंग_1']
        formData['गवाहान_का_नाम_2'] = request.form['गवाहान_का_नाम_2']
        formData['गवाहान_का_पता_2'] = request.form['गवाहान_का_पता_2']
        formData['गवाहान_का_फ़ोन_2'] = request.form['गवाहान_का_फ़ोन_2']
        formData['गवाहान_का_पिता_का_नाम_2'] = request.form['गवाहान_का_पिता_का_नाम_2']
        formData['लिंग_2'] = request.form['लिंग_2']
        formData['सड़क_की_स्थित'] = request.form['सड़क_की_स्थित']
        formData['मसविदाकर्ता'] = request.form['मसविदाकर्ता']
        today_date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").strftime("%d.%m.%Y")
        formData['दिनांक'] = today_date
        half = formData['विक्रय_मूल्य']
        half = int(half)/2
        formData['अर्ध_विक्रय_मूल्य'] = half
        template = 'agriculture_template.docx'
        document = generate.from_template(template, formData, form_type = "agriculture")
        document.seek(0)
        return send_file(
            document, mimetype='application/vnd.openxmlformats-'
            'officedocument.wordprocessingml.document', as_attachment=True,
            attachment_filename='Agriculture.docx')
    else:
        return render_template('agriculture.html')

@app.route("/residential_form", methods=['POST', 'GET'])
def residential():
    if request.method=="POST":
        formData = {}
        formData['विक्रय_मूल्य'] = request.form['विक्रय_मूल्य']
        formData['विक्रय_मूल्य_शब्दों_में'] = request.form['विक्रय_मूल्य_शब्दों_में']
        formData['मालियत'] = request.form['मालियत']
        formData['देय_स्टाम्प'] = request.form['देय_स्टाम्प']
        formData['क्षेत्र_दर'] = request.form['क्षेत्र_दर']
        formData['ग्राम_कोड'] = request.form['ग्राम_कोड']
        formData['ग्राम'] = request.form['ग्राम']
        formData['सम्पत्ति_का_विवरण'] = request.form['सम्पत्ति_का_विवरण']
        formData['संपत्ति_का_क्षेत्रफल'] = request.form['संपत्ति_का_क्षेत्रफल']
        formData['प्रतिफल_की_धनराशि'] = request.form['प्रतिफल_की_धनराशि']
        formData['विक्रेता_का_विवरण'] = request.form['विक्रेता_का_विवरण']
        formData['क्रेता_का_विवरण'] = request.form['क्रेता_का_विवरण']
        formData['चौहद्दी_गाटा_संख्या'] = request.form.getlist('चौहद्दी_गाटा_संख्या[]')
        formData['पूरब'] = request.form.getlist('पूरब[]')
        formData['पश्चिम'] = request.form.getlist('पश्चिम[]')
        formData['उत्तर'] = request.form.getlist('उत्तर[]')
        formData['दक्षिण'] = request.form.getlist('दक्षिण[]')
        formData['अनुमति'] = request.form['a']
        formData['विक्रेता_का_आधार'] = request.form['विक्रेता_का_आधार']
        formData['विक्रेता_का_फ़ोन'] = request.form['विक्रेता_का_फ़ोन']
        formData['विक्रेता_का_पैन'] = request.form['विक्रेता_का_पैन']
        formData['क्रेता_का_आधार'] = request.form['क्रेता_का_आधार']
        formData['क्रेता_का_फ़ोन'] = request.form['क्रेता_का_फ़ोन']
        formData['क्रेता_का_पैन'] = request.form['क्रेता_का_पैन']
        formData['चेक_संख्या'] = request.form.getlist('चेक_संख्या[]')
        formData['बैंक'] = request.form.getlist('बैंक[]')
        formData['शाखा'] = request.form.getlist('शाखा[]')
        formData['मूल्य'] = request.form.getlist('मूल्य[]')
        formData['दिनांकित'] = request.form.getlist('दिनांकित[]')
        formData['गवाहान_का_नाम_1'] = request.form['गवाहान_का_नाम_1']
        formData['गवाहान_का_पता_1'] = request.form['गवाहान_का_पता_1']
        formData['गवाहान_का_फ़ोन_1'] = request.form['गवाहान_का_फ़ोन_1']
        formData['गवाहान_का_पिता_का_नाम_1'] = request.form['गवाहान_का_पिता_का_नाम_1']
        formData['लिंग_1'] = request.form['लिंग_1']
        formData['गवाहान_का_नाम_2'] = request.form['गवाहान_का_नाम_2']
        formData['गवाहान_का_पता_2'] = request.form['गवाहान_का_पता_2']
        formData['गवाहान_का_फ़ोन_2'] = request.form['गवाहान_का_फ़ोन_2']
        formData['गवाहान_का_पिता_का_नाम_2'] = request.form['गवाहान_का_पिता_का_नाम_2']
        formData['लिंग_2'] = request.form['लिंग_2']
        formData['सड़क_की_स्थित'] = request.form['सड़क_की_स्थित']
        formData['मसविदाकर्ता'] = request.form['मसविदाकर्ता']
        today_date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").strftime("%d-%m-%Y")
        formData['दिनांक'] = today_date
        half = formData['विक्रय_मूल्य']
        half = int(half)/2
        formData['अर्ध_विक्रय_मूल्य'] = half
        template = 'residential_template.docx'
        document = generate.from_template(template, formData, form_type = "residential")
        document.seek(0)
        return send_file(
            document, mimetype='application/vnd.openxmlformats-'
            'officedocument.wordprocessingml.document', as_attachment=True,
            attachment_filename='Residential_'+str(datetime.datetime.now())+'.docx')
    else:
        return render_template("residential.html")

@app.route("/getCookie", methods=['GET'])
def getCookie():
    userCookie = request.cookies.get('userID')
    return userCookie
 
if __name__ == "__main__":
    app.run(debug=True)
