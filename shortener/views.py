from rest_framework.generics import GenericAPIView, ListCreateAPIView

from shortener.models import UrlShortener
from shortener.serializers import UrlShortenerSerializer
from shortener.service import RedirectService, UrlShortenerService


class UrlShortenerView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UrlShortenerSerializer
    service = UrlShortenerService()

    def get_queryset(self):
        return UrlShortener.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = self.service.shortcode_generator(serializer.validated_data["url"])
        return response


class RedirectView(GenericAPIView):
    service = RedirectService()

    def get(self, request, shortcode, *args, **kwargs):
        response = self.service.get_url(shortcode=shortcode)
        return response
