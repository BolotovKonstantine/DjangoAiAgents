from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Agent, Dialog
from .forms import PromptForm
from http import HTTPStatus
from dashscope import Application
import dashscope

# Set the base URL
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'


@login_required
def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agent_list.html', {'agents': agents})


@login_required
def agent_detail(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    dialogs = Dialog.objects.filter(user=request.user, agent=agent).order_by('-created_at')

    # Assign the API key to dashscope
    dashscope.api_key = agent.api_key

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt_text = form.cleaned_data['prompt']

            try:
                # Call the API
                response = Application.call(
                    app_id=agent.app_id,
                    prompt=prompt_text
                )

                # Debug info
                print(f"Response type: {type(response)}")

                # Access response data using dictionary-like methods
                status = response.get('status_code', None)
                if status is None and hasattr(response, 'status_code'):
                    status = response.status_code

                if status != HTTPStatus.OK:
                    # Get error details safely
                    request_id = getattr(response, 'request_id', None) if hasattr(response,
                                                                                  'request_id') else response.get(
                        'request_id', 'N/A')
                    code = getattr(response, 'status_code', None) if hasattr(response, 'status_code') else response.get(
                        'status_code', 'N/A')
                    message = getattr(response, 'message', None) if hasattr(response, 'message') else response.get(
                        'message', 'N/A')

                    error = (
                        f"API Error:\n"
                        f"request_id={request_id}\n"
                        f"code={code}\n"
                        f"message={message}\n"
                    )
                    return render(
                        request,
                        'agent_detail.html',
                        {'agent': agent, 'form': form, 'error': error}
                    )
                else:
                    # Get the output safely
                    if hasattr(response, 'output'):
                        output = response.output
                    else:
                        # Try dictionary access
                        output = response.get('output', str(response))

                    # Convert to string if needed
                    if not isinstance(output, str):
                        output = str(output)

                    # Save the dialog
                    Dialog.objects.create(
                        user=request.user,
                        agent=agent,
                        prompt=prompt_text,
                        response=output
                    )

                    return redirect('agent_detail', agent_id=agent.id)

            except Exception as e:
                error = f"API Error: {str(e)}\nType: {type(e).__name__}"
                import traceback
                error += f"\n\nTraceback:\n{traceback.format_exc()}"

                # Print to console for debugging
                print(error)

                return render(
                    request,
                    'agent_detail.html',
                    {'agent': agent, 'form': form, 'error': error}
                )

    else:
        form = PromptForm()

    return render(
        request,
        'agent_detail.html',
        {'agent': agent, 'form': form, 'dialogs': dialogs}
    )
