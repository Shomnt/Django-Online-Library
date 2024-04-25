from django.shortcuts import render


# Create your views here.

def catalog_page(request):
    """ A function that returns a catalog page """
    pass


def main_page(request):
    """ A function that returns the home page  """
    pass


def personal_library_page(request):
    """ A function that returns the page of a personal bibliography """
    pass


def search(request, search_text: str):
    """ Search function to find a book, author or tag by text """
    pass


def change_book_status(request):
    """ Function for changing the status of a book in the personal library """
    pass


def book_page(request, book_name: str):
    """ A function that returns the page of a book """
    pass
