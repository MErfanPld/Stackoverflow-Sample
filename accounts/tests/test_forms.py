from django.test import SimpleTestCase
from accounts.forms import UserRegistrationForm, ProfileImageForm
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class TestRegistrationForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserRegistrationForm(data={'username': 'adel', 'email': 'adel@gmail.com', 'password': '1234'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestProfileImageForm(SimpleTestCase):
    def test_valid_data(self):
        upload_file = open(f'{settings.AWS_LOCAL_STORAGE}/wp4676613-4k-pc-wallpapers.png', 'br')
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = ProfileImageForm(file_dict)
        self.assertTrue(form.is_valid())


