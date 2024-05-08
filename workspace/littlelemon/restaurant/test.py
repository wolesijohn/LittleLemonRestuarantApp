from django.test import TestCase

from .models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item= Menu.objects.create(title="icecream",price='80')
        self.assertEqual(item,"icecream : 80")