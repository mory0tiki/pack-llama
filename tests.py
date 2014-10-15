from django.test import TestCase, Client
import json

class SavePackTestCase(TestCase):
    
    client = None


    def setUp(self):
        self.client = Client()

    def test_saving_pack(self):
        response = self.client.post('/pack_llama/pack/', data={"message": "0000000001;1393;07;20;11;07;30;02;01;001;"})
        #print response.content
        result = json.loads(response.content)
        self.assertTrue(result["result"], "Can't save the request")
