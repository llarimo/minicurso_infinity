#! .venv\Scripts\python.exe

import requests
import json

class CapybaraChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.historico_conversa = []

    def mensagem(self, quem, conversa):
        guardar = {
            "role": quem.lower(),
            "content": conversa
        }
        self.historico_conversa.append(guardar)

    def autorizacoes(self, pedido):
        self.mensagem("user", pedido)
        
        headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
        "X-Title": "CapybaraBot"
        }
    
        payload = {
        "model": "openai/gpt-3.5-turbo",  
        "messages": self.historico_conversa,  
        "temperature": 0.7
        }


        try:
            resposta = requests.post(self.base_url, headers=headers, json=payload)  
            resposta.raise_for_status()  
            dado_resposta = resposta.json()
            importante_resposta = dado_resposta['choices'][0]['message']['content']
            self.mensagem("Capybara", importante_resposta)
            return importante_resposta
        except Exception as e:
            print(f"Erro: {e}")
            return "Desculpe, ocorreu um erro."

if __name__ == "__main__":
    # NUNCA coloque a API key direto no código!
    API_KEY = input("Digite sua API Key (ela ficará oculta): ")
    Capybara = CapybaraChatbot(API_KEY)
    
    print("Capybara Bot DeepSeek - Digite 'sair' para encerrar")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            break
        response = Capybara.autorizacoes(user_input)
        print(f"Capybara: {response}")