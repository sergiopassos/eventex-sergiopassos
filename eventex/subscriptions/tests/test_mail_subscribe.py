from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Sérgio Passos', cpf='12345678901',
                    email='sergio.passos02@gmail.com', phone='41-99242-2196')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'sergio.passos02@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Sérgio Passos',
            '12345678901',
            'sergio.passos02@gmail.com',
            '41-99242-2196',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
