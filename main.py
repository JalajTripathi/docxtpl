from flask import Flask, send_file, render_template, request
from flask.wrappers import Request
import generate

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("dashboard.html")

@app.route("/gen", methods=['POST'])
def gen_docx():
    formData = {}
    formData['विक्रय_मूल्य'] = request.form['विक्रय_मूल्य']
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


    half = formData['विक्रय_मूल्य']
    print("FormData_0: ", int(half)/2)
    half = int(half)/2
    print("FormData_1: ", (half))
    formData['अर्ध_विक्रय_मूल्य'] = half

    # print("FormData_1: ", formData['चौहद्दी_गाटा_संख्या'][1])
    template = 'temp.docx'
    document = generate.from_template(template, formData)
    document.seek(0)
    return send_file(
        document, mimetype='application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='Agriculture.docx')
 
if __name__ == "__main__":
    app.run(debug=True)