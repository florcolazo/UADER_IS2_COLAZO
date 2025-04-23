import openai

# Reemplazá esto con tu API Key real
openai.api_key = "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"

def obtener_respuesta_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo"
,
        messages=[
            {"role": "system", "content": "Sos un asistente útil."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message["content"]

def main():
    print("Chat con GPT (escribí 'salir' para terminar)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "salir":
            break
        if not user_input.strip():
            print("Por favor, escribí algo.")
            continue
        try:
            print(f"You: {user_input}")
            respuesta = obtener_respuesta_chatgpt(user_input)
            print(f"chatGPT: {respuesta}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()