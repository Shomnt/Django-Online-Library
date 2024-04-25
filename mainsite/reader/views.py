from django.shortcuts import render
from django.http import HttpResponse
from html_from_epub import convert
import ebooklib
from ebooklib import epub


# Create your views here.

def read_page(request, book: str, page: int):
    """ Function returning the page view of the reader """
    book = epub.read_epub(f"C:\\Users\\lesha\\Desktop\\Django-Online-Library\\books\\{book}.epub")
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return render(request, "book_page.html", context={"body": chapters[page]})


def check_book(book_name: str):
    """
    The function returns the path to the book with the passed title.
    If there is no such book, it returns an empty string.
    """
    pass
