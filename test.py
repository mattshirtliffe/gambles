import unittest

from client import Gambles

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.client = Gambles()

    def test_ping(self):
        response = self.client.ping()
        self.assertEqual(response.text, 'OK')
        self.assertEqual(response.status_code, 200)

    def test_stats(self):
        response = self.client.stats()
        self.assertIn('vnode_gets',response)

    def test_resources(self):
        # TODO need to do something with the html response for resources
        # Could convert to json?
        response = self.client.resources()
        self.assertTrue(True)

    def test_get_buckets(self):
        response = self.client.get_buckets()
        self.assertIn('buckets', response)


if __name__ == '__main__':
    unittest.main()