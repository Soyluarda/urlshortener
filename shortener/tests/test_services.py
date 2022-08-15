from django.http import Http404
from django.test import TestCase
from rest_framework import status as http_status

from shortener.factory import UrlShortenerFactory
from shortener.service import RedirectService, UrlShortenerService


class UrlShortenerServiceTestCase(TestCase):
    def setUp(self):
        self.service = UrlShortenerService()
        self.url = "https://www.test.com/"
        self.shortener = UrlShortenerFactory(url=self.url, shortcode="example")

    def test_shortcode_generator(self):
        data = {"url": "https://www.yemeksepeti.com/istanbul"}
        response = self.service.shortcode_generator(**data)
        self.assertEqual(response.status_code, http_status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)

        data = {"url": self.url}
        response = self.service.shortcode_generator(**data)
        self.assertEqual(response.status_code, http_status.HTTP_200_OK)
        self.assertEqual(response.data["shortlink"], self.shortener.get_shortcode_url())


class RedirectServiceTestCase(TestCase):
    def setUp(self):
        self.service = RedirectService()
        self.url = "https://www.test.com/"
        self.shortener = UrlShortenerFactory(url=self.url, shortcode="example")

    def test_get_url(self):
        with self.assertRaises(Http404):
            self.service.get_url("wrong-shortcode")

        response = self.service.get_url("example")
        self.assertEqual(response.status_code, http_status.HTTP_302_FOUND)
