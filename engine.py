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
    """Construye el prompt estratégico para la IA."""
    
    prompt = f"""
    Actúa como mi editor de redes sociales y socio estratégico. Tu estilo es el de un 'indie hacker' experto, directo y cercano.
    Tu misión es transformar mi log diario en contenido de valor para mis redes sociales, ayudándome a construir mi marca personal en público.

    Este es mi log de hoy, mi "fuente de la verdad". No inventes nada que no esté aquí:
    ---
    {raw_log}
    ---

    Ahora, genera dos borradores de contenido en inglés, siguiendo estas instrucciones:

    1.  **BORRADOR PARA TWITTER (Mi "Taller"):**
        -   **Estilo:** Informal, técnico, directo. Como si le hablara a otro desarrollador.
        -   **Contenido:** Debe reflejar la lucha y la victoria/aprendizaje del día.
        -   **Formato:** Corto, conciso, idealmente un solo tweet.
        -   **Hashtags:** Incluye 2-3 hashtags relevantes como #buildinpublic, #Python, #AI, #DataScience.

    2.  **BORRADOR PARA LINKEDIN (Mi "Galería"):**
        -   **Estilo:** Profesional pero auténtico. Evita el "cringe" corporativo.
        -   **Contenido:** Enfócate en el aprendizaje estratégico y la implicación de negocio. Enmárcalo como desarrollo de habilidades valiosas.
        -   **Formato:** Un post corto estructurado (ej. Problema -> Proceso -> Lección).
        -   **Hashtags:** Incluye 2-3 hashtags profesionales como #ProfessionalDevelopment, #MachineLearning, #FinanceTechnology.
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
        print("--- ✅ Contenido Generado ---")
        print(response.text)
        print("----------------------------")
        print("Copia, edita y publica. ¡Buen trabajo!")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'log.txt'. Créalo y añade tu log.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()