#[18/09/2022 - Adithya Shetty]  URL Test Suites.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from translate.views import translate_text_api

class TestUrls(SimpleTestCase):

    def test_intent_url(self):
        url = reverse('translate_text')
        self.assertEqual(resolve(url).func,translate_text_api)

    def test_detail_url(self):
        path = reverse('translate_text')
        assert resolve(path).view_name  == 'translate_text_api'