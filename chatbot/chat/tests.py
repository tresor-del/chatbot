from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class ChatViewTests(TestCase):

    def setup(self):
        self.client = Client()
        self.url = reverse('chat')
        self.chat_view_url = reverse('chat_view')
        self.data = {
            'message': 'Bonjour comment tu vas ?'
        }
    
    def test_post_chat_view(self):
        """
        Teste la methode post de la classe ChatView pour s'assurer qu'elle renvoie un statut 200
        """
        response = self.client.post(reverse('chat'), data=self.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_chat_view(self):
        """"
        Teste la methode get de la classe ChatView pour s'assurer qu'elle renvoie un statut 200
        """
        respone = self.client.get(self.chat_view_url)
        self.assertEqual(respone.status_code, 200)
    
    def test_template_rendering(self):
        """
        Teste le rendu du template chat.html
        """
        response = self.client.get(self.chat_view_url)
        self.assertTemplateUsed(response, 'chat.html')

        