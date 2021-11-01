from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import json

def get_agriculture_context(formData):
    gata = len(formData['चौहद्दी_गाटा_संख्या'])
    gata_data = []
    for i in range(gata):
        abc = [{
                "गाटा_संख्या" : formData['चौहद्दी_गाटा_संख्या'][i],
                "पूरब" : formData['पूरब'][i],
                "पश्चिम": formData['पश्चिम'][i],
                "उत्तर": formData['उत्तर'][i],
                "दक्षिण": formData['दक्षिण'][i] 
            }]
        gata_data += abc

    return {
        'मालियत': formData['मालियत'],
        'विक्रय_मूल्य': formData['विक्रय_मूल्य'],
        'विक्रय_मूल्य_शब्दों_में' : formData['विक्रय_मूल्य_शब्दों_में'],
        'देय_स्टाम्प': formData['देय_स्टाम्प'],
        'क्षेत्र_दर': formData['क्षेत्र_दर'],
        'ग्राम': formData['ग्राम'],
        'सम्पत्ति_का_विवरण': formData['सम्पत्ति_का_विवरण'],
        'संपत्ति_का_क्षेत्रफल': formData['संपत्ति_का_क्षेत्रफल'],
        'प्रतिफल_की_धनराशि': formData['प्रतिफल_की_धनराशि'],
        'विक्रेता_का_विवरण': formData['विक्रेता_का_विवरण'],
        'विक्रेता_का_आधार' : formData['विक्रेता_का_आधार'],
        'विक्रेता_का_फ़ोन' : formData['विक्रेता_का_फ़ोन'],
        'विक्रेता_का_पैन' : formData['विक्रेता_का_पैन'],
        'क्रेता_का_विवरण': formData['क्रेता_का_विवरण'],
        'क्रेता_का_आधार' : formData['क्रेता_का_आधार'],
        'क्रेता_का_फ़ोन' : formData['क्रेता_का_फ़ोन'],
        'क्रेता_का_पैन' : formData['क्रेता_का_पैन'],
        'abc': gata_data,
        'a' : formData['अनुमति'],
        'ग्राम_कोड' : formData['ग्राम_कोड'],
        'अर्ध_विक्रय_मूल्य' : formData['अर्ध_विक्रय_मूल्य'],
        'गवाहान_का_नाम_1' : formData['गवाहान_का_नाम_1'],
        'गवाहान_का_पता_1' : formData['गवाहान_का_पता_1'],
        'गवाहान_का_फ़ोन_1' : formData['गवाहान_का_फ़ोन_1'],
        'गवाहान_का_पिता_का_नाम_1' : formData['गवाहान_का_पिता_का_नाम_1'],
        'लिंग_1' : formData['लिंग_1'],
        'गवाहान_का_नाम_2' : formData['गवाहान_का_नाम_2'],
        'गवाहान_का_पता_2' : formData['गवाहान_का_पता_2'],
        'गवाहान_का_फ़ोन_2' : formData['गवाहान_का_फ़ोन_2'],
        'गवाहान_का_पिता_का_नाम_2' : formData['गवाहान_का_पिता_का_नाम_2'],
        'लिंग_2' : formData['लिंग_2'],
        'सड़क_की_स्थित' : formData['सड़क_की_स्थित'],
        'मसविदाकर्ता' : formData['मसविदाकर्ता'],
        'दिनांक' : formData['दिनांक']
    }

def get_residential_context(formData):
    gata = len(formData['चौहद्दी_गाटा_संख्या'])
    gata_data = []
    for i in range(gata):
        abc = [{
                "गाटा_संख्या" : formData['चौहद्दी_गाटा_संख्या'][i],
                "पूरब" : formData['पूरब'][i],
                "पश्चिम": formData['पश्चिम'][i],
                "उत्तर": formData['उत्तर'][i],
                "दक्षिण": formData['दक्षिण'][i] 
            }]
        gata_data += abc
    cheque = len(formData['चेक_संख्या'])
    cheque_data = []
    for i in range(cheque):
        cheque_json = [{
                "चेक_संख्या" : formData['चेक_संख्या'][i],
                "बैंक" : formData['बैंक'][i],
                "शाखा": formData['शाखा'][i],
                "मूल्य": formData['मूल्य'][i],
                "दिनांकित": formData['दिनांकित'][i] 
            }]
        cheque_data += cheque_json

    return {
        'मालियत': formData['मालियत'],
        'विक्रय_मूल्य': formData['विक्रय_मूल्य'],
        'विक्रय_मूल्य_शब्दों_में' : formData['विक्रय_मूल्य_शब्दों_में'],
        'देय_स्टाम्प': formData['देय_स्टाम्प'],
        'क्षेत्र_दर': formData['क्षेत्र_दर'],
        'ग्राम': formData['ग्राम'],
        'सम्पत्ति_का_विवरण': formData['सम्पत्ति_का_विवरण'],
        'संपत्ति_का_क्षेत्रफल': formData['संपत्ति_का_क्षेत्रफल'],
        'प्रतिफल_की_धनराशि': formData['प्रतिफल_की_धनराशि'],
        'विक्रेता_का_विवरण': formData['विक्रेता_का_विवरण'],
        'विक्रेता_का_आधार' : formData['विक्रेता_का_आधार'],
        'विक्रेता_का_फ़ोन' : formData['विक्रेता_का_फ़ोन'],
        'विक्रेता_का_पैन' : formData['विक्रेता_का_पैन'],
        'क्रेता_का_विवरण': formData['क्रेता_का_विवरण'],
        'क्रेता_का_आधार' : formData['क्रेता_का_आधार'],
        'क्रेता_का_फ़ोन' : formData['क्रेता_का_फ़ोन'],
        'क्रेता_का_पैन' : formData['क्रेता_का_पैन'],
        'abc': gata_data,
        'cheque_info' : cheque_data,
        'अनुमति' : formData['अनुमति'],
        'ग्राम_कोड' : formData['ग्राम_कोड'],
        'अर्ध_विक्रय_मूल्य' : formData['अर्ध_विक्रय_मूल्य'],
        'गवाहान_का_नाम_1' : formData['गवाहान_का_नाम_1'],
        'गवाहान_का_पता_1' : formData['गवाहान_का_पता_1'],
        'गवाहान_का_फ़ोन_1' : formData['गवाहान_का_फ़ोन_1'],
        'गवाहान_का_पिता_का_नाम_1' : formData['गवाहान_का_पिता_का_नाम_1'],
        'लिंग_1' : formData['लिंग_1'],
        'गवाहान_का_नाम_2' : formData['गवाहान_का_नाम_2'],
        'गवाहान_का_पता_2' : formData['गवाहान_का_पता_2'],
        'गवाहान_का_फ़ोन_2' : formData['गवाहान_का_फ़ोन_2'],
        'गवाहान_का_पिता_का_नाम_2' : formData['गवाहान_का_पिता_का_नाम_2'],
        'लिंग_2' : formData['लिंग_2'],
        'सड़क_की_स्थित' : formData['सड़क_की_स्थित'],
        'मसविदाकर्ता' : formData['मसविदाकर्ता'],
        'दिनांक' : formData['दिनांक']
    }


def from_template(template, formData, form_type):
    print("Form Type: ", form_type)
    template = DocxTemplate(template)
    if form_type == "agriculture":
        context = get_agriculture_context(formData)
    elif form_type == "residential":
        context = get_residential_context(formData)
    target_file = BytesIO()
    template.render(context)
    template.save(target_file)
    return target_file
