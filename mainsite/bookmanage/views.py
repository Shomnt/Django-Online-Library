from django.shortcuts import render


# Create your views here.

def user_page_download(request):
    """ A function that returns the book's download page. """
    pass


def user_page_proposal(request, status):
    """ Function that returns the page of the request with its current status. """
    pass


def user_page_list(request):
    """ A function that returns a page with a list of abandoned requests. """
    pass


def moderator_page_list(request):
    """ A function that returns a page with a list of requests awaiting moderation. """
    pass


def moderator_page_check(request):
    """ A function that returns the moderation page of the application. """
    pass
