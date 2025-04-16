from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Conversation
from .nlp import generate_response  # Assurez-vous que cette fonction est définie dans nlp.py  
import json

@method_decorator(csrf_exempt, name='dispatch')
class ChatView(View):
    def post(self, request):
        try:
            # Récupérer l'entrée utilisateur
            data = json.loads(request.body)
            user_input = data.get("message", "").strip()

            if not user_input:
                return JsonResponse({"error": "Le message est vide"}, status=400)

            # Générer une réponse
            response = generate_response(user_input)

            # Sauvegarder la conversation dans la base de données
            conversation = Conversation.objects.create(user_input=user_input, response=response)

            # Retourner la réponse
            return JsonResponse({"response": response}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request):
        # Récupérer l'historique des conversations
        conversations = Conversation.objects.all().order_by('-timestamp')
        data = [
            {"user_input": conv.user_input, "response": conv.response, "timestamp": conv.timestamp}
            for conv in conversations
        ]
        return JsonResponse(data, safe=False, status=200)