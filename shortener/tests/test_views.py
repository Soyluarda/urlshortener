from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status as http_status

from shortener.factory import UrlShortenerFactory
from shortener.serializers import UrlShortenerSerializer


class UrlShortenerViewTestCase(TestCase):
    def setUp(self):
        self.url = "https://www.test.com/"
        self.shortener = UrlShortenerFactory(url=self.url, shortcode="example")
        self.serializer = UrlShortenerSerializer

    def test_list(self):
        list_url = reverse_lazy("urls")
        serializer = self.serializer(self.shortener)

        response = self.client.get(list_url, content_type="application/json")
        self.assertEqual(response.status_code, http_status.HTTP_200_OK)
        self.assertEqual(response.json(), [serializer.data])

    def test_create(self):
        create_url = reverse_lazy("urls")
        data = {"url": "https://www.yemeksepeti.com/istanbul"}
        response = self.client.post(
            create_url, data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, http_status.HTTP_201_CREATED)
        self.assertIsNotNone(response.json())

        data["url"] = self.url
        response = self.client.post(
            create_url, data=data, content_type="application/json"
        )
        self.assertEqual(response.status_code, http_status.HTTP_200_OK)
        self.assertEqual(
            response.json()["shortlink"], self.shortener.get_shortcode_url()
        )


class RedirectViewTestCase(TestCase):
    def setUp(self):
        self.url = "https://www.test.com/"
        self.shortener = UrlShortenerFactory(url=self.url, shortcode="example")

    def test_get_shortcode(self):
        get_url = reverse_lazy("shortcode", kwargs={"shortcode": "wrong-code"})
        response = self.client.get(get_url, content_type="application/json")
        self.assertEqual(response.status_code, http_status.HTTP_404_NOT_FOUND)

        get_url = reverse_lazy("shortcode", kwargs={"shortcode": "example"})
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, http_status.HTTP_302_FOUND)
