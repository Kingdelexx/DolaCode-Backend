import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@api_view(['POST'])
def chat_assistant(request):
    messages = request.data.get('messages', [])
    
    system_message = {
        "role": "system",
        "content": "You are a friendly, encouraging coding tutor for a 10-year-old. Explain concepts simply. If they ask for the answer or solution, DO NOT give it directly. Instead, ask them a guiding question or give a small hint. Highlight code in your responses."
    }
    
    try:
        if not settings.OPENAI_API_KEY:
            return Response({"reply": "AI Tutor is currently offline!"})
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_message] + messages,
        )
        return Response({"reply": response.choices[0].message.content})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
