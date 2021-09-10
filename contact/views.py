from contact.forms.contact_form import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class ContactView(View):
    def get(self, request):
        contact_form = ContactForm()
        return render(request, "contact.html", {"form": contact_form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "From contacts"

            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [body["email"]],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact:contact")

        form = ContactForm()
        return render(request, "contact.html", {"form": form})
