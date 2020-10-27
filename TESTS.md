# How write tests for GoOutSafe

Due to Flask initialization issue, we have to write
a setup method for all unittest.TestCase classes.

The following example represents a very simple 
design pattern to be used when you write test cases.


```python
import unittest

class TestMyClass(unittest.TestCase):
    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        '''
            now you can import all 
            objects you need for testing,
            and set it as class properties
        '''
        from gooutsafe.models import restaurant
        self.restaurant = restaurant

    def test_restaurant(self):
        rest = self.restaurant.Restaurant()
        # test it
``` 

In this way we fix the issue by
executing the Flask initialization code in the setUp method, that is executed before all
test cases execution.

