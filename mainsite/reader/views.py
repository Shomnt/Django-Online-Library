from django.shortcuts import render
import ebooklib
from ebooklib import epub


def read_page(request, book: str, chapter: int):
    """ Function returning the page view of the reader """
    try:
        book = epub.read_epub(f"..\\..\\Django-Online-Library\\books\\{book}.epub")
    except:
        return render(request, "book_page_none_book.html")
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())

    if chapter >= len(chapters):
        return render(request, "book_page_none_page.html")
    else:
        return render(request, "book_page.html", context={"body": chapters[chapter]})


def check_book(book_name: str):
    """
    The function returns the path to the book with the passed title.
    If there is no such book, it returns an empty string.
    """

    pass
