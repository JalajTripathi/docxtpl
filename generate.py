from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import json

def get_context(formData):
    """ You can generate your context separately since you may deal with a lot 
        of documents. You can carry out computations, etc in here and make the
        context look like the sample below.
    """
    gata = len(formData['चौहद्दी_गाटा_संख्या'])
    # abc = dict()
    gata_data = []
    if (gata>1):
        for i in range(gata):
            abc = [{
                    "गाटा_संख्या" : formData['चौहद्दी_गाटा_संख्या'][i],
                    "पूरब" : formData['पूरब'][i],
                    "पश्चिम": formData['पश्चिम'][i],
                    "उत्तर": formData['उत्तर'][i],
                    "दक्षिण": formData['दक्षिण'][i] 
                }]
            # abc.append(abc)
            gata_data += abc
            # n = { "test"+str(i) : abc }

    print("N: ", gata_data)
            # print(abc)
    # abc = json.loads(abc)
    # print(abc)
            
    return {
        'मालियत': formData['मालियत'],
        'विक्रय_मूल्य': formData['विक्रय_मूल्य'],
        'देय_स्टाम्प': formData['देय_स्टाम्प'],
        'क्षेत्र_दर': formData['क्षेत्र_दर'],
        'ग्राम': formData['ग्राम'],
        'सम्पत्ति_का_विवरण': formData['सम्पत्ति_का_विवरण'],
        'संपत्ति_का_क्षेत्रफल': formData['संपत्ति_का_क्षेत्रफल'],
        'प्रतिफल_की_धनराशि': formData['प्रतिफल_की_धनराशि'],
        'विक्रेता_का_विवरण': formData['विक्रेता_का_विवरण'],
        'क्रेता_का_विवरण': formData['क्रेता_का_विवरण'],
        'abc': gata_data,
        'a' : formData['अनुमति'],
        'ग्राम_कोड' : formData['ग्राम_कोड'],
        'अर्ध_विक्रय_मूल्य' : formData['अर्ध_विक्रय_मूल्य']
    }


def from_template(template, formData):
    #target_file = StringIO()

    template = DocxTemplate(template)
    context = get_context(formData)  # gets the context used to render the document

    # print("Context: ", context)

    # img_size = Cm(7)  # sets the size of the image
    # sign = InlineImage(template, signature, img_size)
    # context['signature'] = sign  # adds the InlineImage object to the context

    target_file = BytesIO()
    print("Debug 1", target_file)
    template.render(context)
    template.save(target_file)


    return target_file
