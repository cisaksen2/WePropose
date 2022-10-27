from django.urls import path
from .views import indexPageView
from .views import datePageView
from .views import contactPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("date/", datePageView, name="date"),
    path("contact/", contactPageView, name="contact")
]
