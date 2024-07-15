from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class Test(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
    def test_home_page_response_template(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'home.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
    def test_about_page_response_template(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'about.html')

    def test_contact_page_status_code(self):
        url = reverse('contact')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
    def test_contact_page_response_template(self):
        url = reverse('contact')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'contact.html')