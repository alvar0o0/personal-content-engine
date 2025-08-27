import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar la API key desde el archivo .env
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# Configurar el modelo de Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def build_prompt(raw_log):
    """Construye el prompt para que la IA extraiga los 3 puntos clave."""
    
    prompt = f"""
    Actúa como mi socio estratégico para mi #buildinpublic. Tu estilo debe ser 'hacker/dev': conciso, directo al grano, técnico pero claro.

    Voy a pasarte mi "brain dump" del día en prosa. Tu misión es leerlo, entenderlo y extraer los 3 puntos más importantes para transformarlos en un único tweet en inglés.

    Los 3 puntos que extraigas deben idealmente ser:
    1. Un avance o logro concreto.
    2. Un problema, bloqueo o reto que enfrenté.
    3. Un aprendizaje, insight o lección clave.

    Este es mi "brain dump":
    ---
    {raw_log}
    ---

    Ahora, genera el tweet usando esta plantilla EXACTA:
    [TEMA #DÍA]: <Crea un título conciso basado en el texto>

    → <El avance o logro que extrajiste>
    → <El problema o reto que extrajiste>
    → <El aprendizaje o insight que extrajiste>

    #buildinpublic

    **REGLAS IMPORTANTES:**
    - No añadas ningún comentario extra. Solo el tweet.
    - El número del día no lo sabes, así que déjalo como '#DÍA' para que yo lo reemplace.
    - El TEMA tampoco lo sabes, déjalo como 'TEMA' para que yo lo reemplace.
    - Sé súper conciso y usa el tono del texto original.
    """
    return prompt

def main():
    """Función principal para correr el motor de contenido."""
    try:
        with open('log.txt', 'r', encoding='utf-8') as f:
            raw_log_content = f.read()

        if not raw_log_content.strip():
            print("El archivo log.txt está vacío. Añade tu log del día.")
            return

        # Construir el prompt y generar contenido
        prompt_final = build_prompt(raw_log_content)
        response = model.generate_content(prompt_final)

        # Imprimir la respuesta de forma clara
        print(response.text.strip())

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'log.txt'. Créalo y añade tu log.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()