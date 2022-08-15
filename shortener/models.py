from django.contrib.sites.models import Site
from django.db import models
from django.db.models import F


class UrlShortener(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=15, unique=True, blank=True, null=True)
    count = models.IntegerField(default=0)

    def clicked(self):
        self.count = F("count") + 1
        self.save(update_fields=["count"])

    def get_shortcode_url(self):
        current_site = Site.objects.get_current()
        url = "https://{site}/{shortcode}".format(
            site=current_site.domain, shortcode=self.shortcode
        )
        return url
