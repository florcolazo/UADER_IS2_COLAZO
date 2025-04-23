import openai

# Configura tu clave API de OpenAI
openai.api_key = "tu-api-key"

def obtener_respuesta(prompt):
    try:
        # Llamada a la API de OpenAI para obtener la respuesta
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Asegúrate de tener acceso a este modelo
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error al contactar con la API: {e}"

def main():
    while True:
        try:
            # Entrada del usuario
            user_input = input("You: ")
            if user_input.lower() == 'salir':
                print("Fin del programa.")
                break
            elif user_input:
                print(f"You: {user_input}")
                
                # Obtener respuesta de ChatGPT
                response = obtener_respuesta(user_input)
                print(f"chatGPT: {response}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()