import unittest

from flask import template_rendered, url_for

from .view_test import ViewTest


class TestRestaurant(ViewTest):

    @classmethod
    def setUpClass(cls):
        super(TestRestaurant, cls).setUpClass()
    
    def test_restaurants(self):
        with self.app.test_request_context():
            rv = self.client.get(url_for('restaurants._restaurants'))
            print(rv.data)
            assert rv.status_code == 200

    def test_restaurants_sheet(self):
        data = {'restaurant_id': 123423}
        with self.app.test_request_context():
            rv = self.client.get(url_for('restaurants.restaurant_sheet'), data=data)
            print(rv.data)
            assert rv.status_code == 200
