# tests/test_api.py

import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask application
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_lists(self):
        """Test retrieving all to-do lists."""
        response = self.client.get('/lists')
        self.assertEqual(response.status_code, 200)
        lists_data = json.loads(response.data)
        self.assertIsInstance(lists_data, list)

    def test_add_and_delete_list(self):
        """Test creating a new to-do list and then deleting it."""
        # Create a new list via POST /list
        new_list = {'name': 'Test List'}
        response = self.client.post('/list', data=json.dumps(new_list),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        created_list = json.loads(response.data)
        list_id = created_list['id']
        self.assertIn('name', created_list)
        self.assertEqual(created_list['name'], 'Test List')

        # Delete the newly created list via DELETE /list/<list_id>
        delete_response = self.client.delete(f'/list/{list_id}')
        self.assertEqual(delete_response.status_code, 200)
        result = json.loads(delete_response.data)
        self.assertEqual(result.get('msg'), 'Liste erfolgreich gelöscht')

    def test_add_entry(self):
        """Test adding a new to-do entry to an existing list."""
        # Use an existing list ID from the initial data
        list_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
        entry_data = {'name': 'Test Entry', 'description': 'Test description'}
        response = self.client.post(f'/todo-list/{list_id}/entry', data=json.dumps(entry_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        entry = json.loads(response.data)
        self.assertEqual(entry.get('name'), 'Test Entry')
        self.assertEqual(entry.get('description'), 'Test description')
        self.assertEqual(entry.get('list'), list_id)

if __name__ == '__main__':
    unittest.main()
