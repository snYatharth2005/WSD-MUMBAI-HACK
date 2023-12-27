# myai_app/views.py
from django.shortcuts import render
import openai

def open_ai_call(message):
    api_key = "Your Open-ai API ID" #you can get it from https://platform.openai.com/
    openai.api_key = api_key

    prompt = f"You are a cool gen-z ecologist and biologist.\nUser: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        top_p=1,
    )

    output = response['choices'][0]['text'].strip()
    return output

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        chatbot_response = open_ai_call(user_input)

        return render(request, 'dashboard.html', {'chatbot_response': chatbot_response})
    else:
        return render(request, 'dashboard.html')
