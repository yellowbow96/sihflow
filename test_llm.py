from transformers import pipeline

def main():
    # Load a small LLM for quick testing (works on CPU in Codespaces)
    generator = pipeline("text-generation", model="distilgpt2")

    prompt = "LLM Large Language Model future "
    result = generator(prompt, max_length=80, num_return_sequences=1)

    print("🤖 LLM Output:\n")
    print(result[0]["generated_text"])

if __name__ == "__main__":
    main()
