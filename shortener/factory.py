from factory import fuzzy
from factory.django import DjangoModelFactory

from shortener.models import UrlShortener


class UrlShortenerFactory(DjangoModelFactory):
    url = fuzzy.FuzzyText(length=15)
    shortcode = fuzzy.FuzzyText(length=15)

    class Meta:
        model = UrlShortener
