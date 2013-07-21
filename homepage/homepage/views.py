from django.http import HttpResponse

__author__ = 'arjunnaik'

def home(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("This is the home page.")
