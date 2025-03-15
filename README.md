# Overview
This project represents my exploration into building AI-integrated web applications using modern frameworks. DjangoAiAgents is a web platform designed to facilitate interactions with various AI agents through a unified interface, allowing users to communicate with different AI models using their respective APIs.
To start the server on your computer, navigate to the project directory and run:
``` 
python manage.py runserver
```
Then open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.
The purpose of this project is to create a flexible framework for interacting with diverse AI models through a single, consistent interface. This approach streamlines the process of working with multiple AI services while providing a clean user experience and maintaining security through proper API key management.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages
The application consists of several interconnected web pages:
1. **Login Page** - Users must authenticate to access the application, ensuring that AI interactions are properly associated with user accounts and secured.
2. **Agent List** - After login, users are presented with a list of available AI agents. Each agent represents a different AI service configured in the system.
3. **Agent Detail** - When selecting an agent, users can see details about that specific AI service and interact with it through a dialog interface. This page displays:
    - Agent information (name, description)
    - A form to submit prompts to the AI
    - A history of previous dialogs with this agent, ordered by recency

The application dynamically creates dialog histories for each user-agent interaction, preserving the conversation history and making it available for future reference.

# Development Environment
This project was developed using:
- PyCharm Professional Edition as the primary IDE
- Git for version control
- Django web framework for the backend
- HTML, CSS, and JavaScript for frontend functionality

The software is built with:
- Python as the main programming language
- Django web framework for MVC architecture
- Dashscope client library for AI integrations
- SQLite database for data persistence
- Authentication system provided by Django

# Useful Websites
The following resources were instrumental in developing this project:
- [Django Documentation](https://docs.djangoproject.com/)
- [Dashscope API Documentation](https://help.aliyun.com/product/427223.html)
- [Python HTTP Requests Library](https://requests.readthedocs.io/)
- [Bootstrap CSS Framework](https://getbootstrap.com/)

# Future Work
Items to improve in future versions:
- Implement real-time chat functionality using WebSockets
- Add support for additional AI agent providers beyond Dashscope
- Create a user preference system to customize AI interaction settings
- Implement dialog export functionality to save conversations
- Enhance security with additional layers of API key protection
