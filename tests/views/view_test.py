import unittest


class ViewTest(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests views
    """
    app = None

    def setUp(self):
        from gooutsafe import create_app
        self.app = create_app()
        self.app = self.app.test_client()
        self.app.testing = True 


if __name__ == '__main__':
    unittest.main()
