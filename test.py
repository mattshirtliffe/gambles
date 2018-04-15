import unittest

from client import Gambles

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.client = Gambles()
        data = {"first_name": "Matthew", "last_name": "Shirtliffe"}
        response = self.client.store('test', data, key="doc")

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
        response = self.client.list_buckets()
        self.assertIn('buckets', response)

    def test_store(self):
        data = {"first_name":"Matthew","last_name":"Shirtliffe"}
        response = self.client.store('test',data,key="doc")
        self.assertIn('first_name', response)

    def test_get(self):
        response = self.client.get('test',"doc")
        self.assertIn('first_name', response)

    def test_fetch(self):
        response = self.client.fetch('test',"doc")
        self.assertIn('first_name', response)

    @unittest.skip("Not implemented yet")
    def test_update(self):
        self.assertTrue(False)

    def test_delete(self):
        response = self.client.delete('test', key="doc")
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()