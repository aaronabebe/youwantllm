import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmailSignupForm
from .models import SignUp


def load_data(path):
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)
        data = []
        for row in reader:
            row = {k: v for k, v in zip(header, row)}
            data.append(row)

    return header, data


def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="llm_pricing.csv"'

    writer = csv.writer(response)
    # Assuming 'header' is a list of your column names and 'data' is your table data
    header, data = load_data("data.csv")

    writer.writerow(header)
    for row in data:
        writer.writerow([v for k, v in row.items()])  # Adjust this line based on your model

    return response


def email_signup(request):
    if request.method == 'POST':
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save the email to a database or subscribe it to a mailing list)
            email = form.cleaned_data["email"]
            SignUp.objects.create(email=email)
            return redirect('/')  # Redirect to a new URL


def index(request):
    header, data = load_data("data.csv")
    form = EmailSignupForm()
    return render(
        request,
        "index.html",
        {
            "header": header,
            "data": data,
            "last_update": "Fri Jan 30 16:22:37 2024",
            "form": form,
        }
    )
