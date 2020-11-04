from .view_test import ViewTest
from flask import template_rendered
import unittest

class TestAuth(ViewTest):

    def setUp(self):
        super(TestAuth, self).setUp()

    def test_get_auth(self):
        rv = self.app.get('/login')    
        assert rv.status_code == 200