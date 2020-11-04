from .view_test import ViewTest
from flask import template_rendered
import unittest

class TestHome(ViewTest):

    def setUp(self):
        super(TestHome, self).setUp()

    def test_get_home(self):
        rv = self.app.get('/')    
        assert rv.status_code == 200