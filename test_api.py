import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_lists(self):
        response = self.client.get('/lists')
        self.assertEqual(response.status_code, 200)
        lists_data = json.loads(response.data)
        self.assertIsInstance(lists_data, list)

    def test_add_and_delete_list(self):
        # Neue Liste hinzufügen
        new_list = {'name': 'Test List'}
        response = self.client.post('/list', data=json.dumps(new_list),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        created_list = json.loads(response.data)
        list_id = created_list['id']

        # Liste löschen
        response = self.client.delete(f'/list/{list_id}')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result.get('msg'), 'Liste erfolgreich gelöscht')

    def test_add_entry(self):
        # Füge einen Eintrag zu einer bestehenden Liste hinzu
        list_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'  # Existierende Liste aus den initialen Daten
        entry_data = {'name': 'Test Entry', 'description': 'Test description'}
        response = self.client.post(f'/todo-list/{list_id}/entry', data=json.dumps(entry_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        entry = json.loads(response.data)
        self.assertEqual(entry['name'], 'Test Entry')

if __name__ == '__main__':
    unittest.main()
