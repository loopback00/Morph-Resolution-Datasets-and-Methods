import ollama


MODEL_NAME = "qwen2.5:32b"


prompt_text = "讲个笑话"

try:
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt_text,
            },
        ]
    )
    answer = response['message']['content']
    print("Model's Answer:", answer.strip())

except Exception as e:
    print(f"An error occurred: {e}")

