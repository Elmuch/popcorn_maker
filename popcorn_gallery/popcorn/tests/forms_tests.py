from django.test import TestCase
from ..forms import ProjectForm


class PopcornFormTests(TestCase):

    def test_project_form(self):
        data = {
            'name': 'Awesome project!',
            'data': {'foo': 'foo'},
            'html': '<!DOCTYPE html>',
            'template': 'basic',
            }
        form = ProjectForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['data'], '{"foo": "foo"}')

    def test_invalid_form(self):
        data = {
            'name': 'Awesome project!',
            'template': 'basic',
            }
        form = ProjectForm(data)
        self.assertFalse(form.is_valid())

    def test_invalid_json(self):
        data = {
            'name': 'Awesome project!',
            'template': 'basic',
            'data': 2 + 1j,
            }
        form = ProjectForm(data)
        self.assertFalse(form.is_valid())
