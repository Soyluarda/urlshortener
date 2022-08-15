from django.urls import path

from shortener.views import RedirectView, UrlShortenerView

urlpatterns = [
    path("urls/", UrlShortenerView.as_view(), name="urls"),
    path("<str:shortcode>/", RedirectView.as_view(), name="shortcode"),
]
