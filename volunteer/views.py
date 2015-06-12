from django.shortcuts import render

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from volunteer.models import Text


def app(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Oxfam_Vol_App_Form.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    p.read()
    p.showPage()
    return response


def index(request):
    context_dict = {}

    textWrapper = Text.objects.get(id=1)

    context_dict['mission'] = textWrapper.mission
    context_dict['description'] = textWrapper.description
    context_dict['getinvolved'] = textWrapper.getinvolved
    context_dict['donate'] = textWrapper.donate

    return render(request, 'volunteer/index.html', context_dict)