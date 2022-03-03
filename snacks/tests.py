from django.test import TestCase
from django.urls import reverse
from .models import Snacks
from django.contrib.auth import get_user_model

class SnacksTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user (username='tester', email='tester@email.com', password='pass')

    self.snack = Snacks.objects.create(name='oreos', purchaser=self.user, description='yum')

  def test_string_representation(self):
    self.assertEqual(str(self.snack), 'oreos')

  def test_snack_name(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_list_page_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')
