from .view_test import ViewTest
from flask import template_rendered
import unittest

class TestHome(ViewTest):

    def setUp(self):
        super(TestHome, self).setUp()

    def test_get_home(self):
        rv = self.app.get('/')    
        self.assertEqual(rv.status_code, 200) 
    
    """def test_get_template(self):
        self.app.get('/')
        self.assert_template_used("index.html")"""