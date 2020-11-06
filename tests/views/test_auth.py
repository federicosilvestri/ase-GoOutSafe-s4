from .view_test import ViewTest


class TestAuth(ViewTest):

    @classmethod
    def setUpClass(cls):
        super(TestAuth, cls).setUpClass()

    def test_get_auth(self):
        rv = self.client.get('/login')
        assert rv.status_code == 200
