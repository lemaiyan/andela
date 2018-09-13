from app.models import Cache
import requests


def get_image(dimensions, text, foreground='f00', background='ccccccc'):
    """ Function to fetch the image

    :param dimensions:
    :param text:
    :param foreground:
    :param background:
    :return:
    """
    try:
        record = Cache.objects.get(dimension=dimensions, text=text)
        return record
    except Cache.DoesNotExist:
        url = "https://dummyimage.com/{dimension}/{background}/" \
              "{foreground}.png&text={text}".format(
                dimension=dimensions,
                background=background,
                foreground=foreground,
                text=text
            )
        response = requests.get(url=url)
        cached = Cache.objects.create(
            dimension=dimensions,
            text=text,
            content=response.text,
            status=response.status_code
        )
        return cached
