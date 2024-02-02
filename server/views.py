import csv
import time

from django.shortcuts import render, redirect

from .forms import EmailSignupForm


def load_data(path):
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)
        data = []
        for row in reader:
            row = {k: v for k, v in zip(header, row)}
            data.append(row)

    return header, data


def email_signup(request):
    if request.method == 'POST':
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save the email to a database or subscribe it to a mailing list)
            print(form.data["email"])
            return redirect('/')  # Redirect to a new URL


def index(request):
    header, data = load_data("data.csv")
    last_update = time.asctime()
    form = EmailSignupForm()
    return render(
        request,
        "index.html",
        {
            "header": header,
            "data": data,
            "last_update": last_update,
            "form": form,
        }
    )
