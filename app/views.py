from app.utils import get_image
from django.http import HttpResponse


def get_image_view(request, dimensions, text):
    resp = get_image(dimensions, text)
    return HttpResponse(resp.content)
