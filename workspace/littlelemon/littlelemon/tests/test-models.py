from django.test import TestCase

from LittleLemonFinal.restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item= Menu.objects.create(title='icecream',price=80,inventory=100)
        self.assertEqual(item,"icecream : 80")