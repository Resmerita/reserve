from contact.views import ContactView
from django.urls import path


app_name = "contact"

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
]
