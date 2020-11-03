from .view_test import ViewTest
from flask import template_rendered
import unittest

class TestAuth(ViewTest):

    def setUp(self):
        super(TestAuth, self).setUp()

    def test_login_logout(client):
        pass