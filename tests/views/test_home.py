from .view_test import ViewTest
from flask import template_rendered
import unittest

class TestHome(ViewTest):

    @classmethod
    def setUpClass(cls):
        super(TestHome, cls).setUpClass()

    def test_get_home(self):
        rv = self.client.get('/')    
        assert rv.status_code == 200

    def test_post_home(self):
        rv = self.client.post('/', data= {'search_field': 'ciao', 'filters': 'Name'})
        assert rv.status_code == 200

    def test_search_restaurant(self):
        data = dict(keyword='ciao', filters='Name')
        rv = self.client.get('/search', data=data)
        assert rv.status_code == 200