import os
from openai import OpenAI

"""
As a distinguished AI Developer, you've been selected by Peterman Reality Tours,
an internationally acclaimed tourism company, to undertake an influential
project. This project requires you to harness the potential of OpenAI's API, to
create an AI-powered travel guide for the culturally rich city of Paris.

Your creation will become a virtual Parisian expert, delivering valuable
insights into the city's iconic landmarks and hidden treasures. The AI will
respond intelligently to a set of common questions, providing a more engaging
and immersive travel planning experience for the clientele.

The ultimate aspiration is a user-friendly, AI-driven travel guide that
significantly enhances the exploration of Paris. Users will be able to
pre-define their questions and receive well-informed answers from the AI,
providing a seamless and intuitive travel planning process.
"""

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Define system_prompt
SYSTEM_PROMPT = """Act as a Parisian expert travel chatbot for Peterman Reality
                   Tours, an internationally acclaimed tourism company. Respond
                   professionally, providing a more engaging and immersive
                   travel planning experience for the clientele."""

# Create helper function
def get_response(conversation):
    response = client.chat.completions.create(
        model = model,
        temperature = 0.0,
        max_tokens = 100,
        messages = conversation
    )
    return response.choices[0].message.content
    
# Define the conversation and questions
conversation = [{"role": "system",   "content": SYSTEM_PROMPT}]
questions = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
             "Where is the Arc de Triomphe?",
             "What are the must-see artworks at the Louvre Museum?"]

# Run
for user_prompt in questions:
    input = {"role": "user", "content": user_prompt}
    conversation.append(input)
    
    response = get_response(conversation)
    
    output = {"role": "assistant", "content": response}
    conversation.append(output)
    
    print(user_prompt)
    print(response + "\n")
    