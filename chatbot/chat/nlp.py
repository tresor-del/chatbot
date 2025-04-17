from transformers import AutoModelForCausalLM, AutoTokenizer

# Modèle plus léger que GPT-Neo : distilgpt2
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # important !

model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt, max_length=100, temperature=0.7, top_p=0.9, num_return_sequences=1):
    try:
        encoded_input = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512, padding=True)
        input_ids = encoded_input["input_ids"]
        attention_mask = encoded_input["attention_mask"]

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            num_return_sequences=num_return_sequences,
            pad_token_id=tokenizer.pad_token_id,
            do_sample=True
        )

        return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

    except Exception as e:
        return [f"Erreur lors de la génération de la réponse : {e}"]
