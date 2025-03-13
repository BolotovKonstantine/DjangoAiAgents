from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Agent, Dialog
from .forms import PromptForm
import requests


@login_required
def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agent_list.html', {'agents': agents})


@login_required
def agent_detail(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    dialogs = Dialog.objects.filter(user=request.user, agent=agent).order_by('-created_at')

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            # Вызов API Alibaba
            headers = {'Authorization': f'Bearer {agent.api_key}'}
            data = {'prompt': form.cleaned_data['prompt']}

            try:
                response = requests.post(
                    agent.api_url,
                    headers=headers,
                    json=data
                )
                response_data = response.json()

                # Сохранение диалога
                Dialog.objects.create(
                    user=request.user,
                    agent=agent,
                    prompt=data['prompt'],
                    response=response_data.get('result', '')
                )

                return redirect('agent_detail', agent_id=agent.id)

            except Exception as e:
                error = f"API Error: {str(e)}"
                return render(request, 'agent_detail.html',
                              {'agent': agent, 'form': form, 'error': error})
    else:
        form = PromptForm()

    return render(request, 'agent_detail.html',
                  {'agent': agent, 'form': form, 'dialogs': dialogs})