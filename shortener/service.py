from random import choices
from string import ascii_letters

from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response

from shortener.models import UrlShortener

SHORTCODE_LENGTH = getattr(settings, "SHORTCODE_LENGTH", 5)


class UrlShortenerService:
    def shortcode_generator(self, url):
        random_string = "".join(choices(ascii_letters, k=SHORTCODE_LENGTH))
        shortcode = random_string
        is_shortener = UrlShortener.objects.filter(url=url)
        if is_shortener.exists():
            return Response(
                {"shortlink": is_shortener.get().get_shortcode_url()},
                status=status.HTTP_200_OK,
            )

        if not UrlShortener.objects.filter(shortcode=shortcode).exists():
            url = UrlShortener(url=url, shortcode=shortcode)
            url.save()

            return Response(
                {"shortlink": url.get_shortcode_url()}, status=status.HTTP_201_CREATED
            )

        return self.shortcode_generator(url=url)


class RedirectService:
    def get_url(self, shortcode):
        url = UrlShortener.objects.filter(shortcode=shortcode)
        if not url:
            raise Http404()

        url = url.get()
        url.clicked()
        return HttpResponseRedirect(url.url)
