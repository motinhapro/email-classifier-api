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

if __name__ == "__main__":
    email_produtivo = """
    Olá, estou com erro ao acessar o sistema.
    Podem me ajudar?
    """
    
    print("Testando email PRODUTIVO...")
    res1 = email_classifier(email_produtivo)
    print(f"Classificação: {res1.get('classificacao')}")
    print(f"Confiança: {res1.get('confianca')}")
    print(f"Texto sugerido: {res1.get('resposta sugerida')}")
    print()

    email_improdutivo = """
    Olá equipe!
    Feliz Natal a todos! 🎄
    Desejo um ótimo ano novo cheio de realizações!
    """

    print("Testando email IMPRODUTIVO...")
    res2 = email_classifier(email_improdutivo)
    print(f"Classificação: {res2.get('classificacao')}")
    print(f"Confiança: {res2.get('confianca')}")
    print(f"Texto sugerido: {res2.get('resposta sugerida')}")
    print()
    
    
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