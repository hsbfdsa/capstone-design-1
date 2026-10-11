import os
from openai import OpenAI


class Chatbot:
    """
    Description here
    """

    def __init__(self):
        self.client = OpenAI(
            api_key="OPEN_API_KEY",
            # organization=os.getenv('OPENAI_ORGANIZATION')
        )
        self.model = "gpt-3.5-turbo"
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
        
    
    def ask(self, user_prompt):
        self.messages.append(
            {"role": "user", "content": user_prompt}
        )
        res = self.__ask__()
        return res
    
        
    def __ask__(self):       
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        response = completion.choices[0].message.content
        self.messages.append(
            {"role": "assistant", "content": response}
        )
        return response
    
    
    def show_messages(self):
        return self.messages
    
    
    def clear(self):
        self.messages.clear()
        
        
