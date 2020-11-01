import unittest


class TasksTest(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests models
    """

    def setUp(self):
        from gooutsafe import create_app
        create_app()