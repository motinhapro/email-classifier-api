import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def email_classifier(email: str) -> dict:
    
    prompt = f"""Você é um assistente que classifica emails corporativos. 
    
    Tarefa: Classifique o email abaixo como PRODUTIVO ou IMPRODUTIVO.

    Definições:
    -PRODUTIVO: precisa de ação (dúvidas, problemas, solitações)
    -IMPRODUTIVO: não precisa de ação (agradecimentos, spam, felicitações)

    EMAIL:{email}

    Responda apenas com um JSON neste formato:

    {{
        "classificacao: "PRODUTIVO ou IMPRODUTIVO",
        "confianca": 0.95,
        "razao": "explicacao ou classificacao",
        "resposta sugerida": "resposta profissional ao email"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        ai_response = response.choices[0].message.content
    
        ai_response = json.loads(ai_response)

        return ai_response
    
    except json.JSONDecodeError:
        return {
            "erro": True,
            "mensagem": "IA não retornou um JSON válido"
        }
    
    except Exception as e:
        return {
            "erro": True,
            "mensagem": f"Erro ao classificar: {str(e)}"
        }
    
def extract_text_pdf(file_path: str) -> str:
    
    try:
        from PyPDF2 import PdfReader

        reader = PdfReader(file_path)
        text=""

        for page in reader.pages:
            text+=page.extract_text() + "\n"

        return text.strip()
    
    except Exception as e:
        raise Exception(f"Erro ao ler o PDF: {str(e)}")