from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubsriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Sérgio Passos',
            cpf = '12345678901',
            email = 'sergio.passos02@gmail.com',
            phone = '41-992422196'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
