from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Sergio Passos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb.pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='sergio.passos02@gmail.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                         value='41-992422196')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='sergio.passos02@gmail.com')
        self.assertEqual('sergio.passos02@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Sérgio Passos',
            slug='sergio-passos',
            photo='http://hbn.link/hb-pic'
        )
        s.contact_set.create(kind=Contact.EMAIL, value='sergio.passos02@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='41-992422196')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['sergio.passos02@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['41-992422196']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
