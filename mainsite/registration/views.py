from django.shortcuts import render


# Create your views here.

def start_registration_page(request):
    """ Function that displays the registration page """
    pass


def personal_account_page(request):
    """ Function displaying the personal account page """
    pass


def registration_confirm(request, name_fields: str, mail_field: str, pass_field: str, pass_conf_field: str):
    """
    The function takes the current values of the page fields,
    checks them, and then either puts them into
    the database or triggers an error output.
    """
    pass


def input_err(request, errors: list):
    """
    Accepts the list of errors made when entering
    registration data, displays the corresponding messages to the user
    """
    pass
