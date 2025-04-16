from transformers import AutoModelForCausalLM, AutoTokenizer

# Charger le modèle NLP
model_name = "gpt2"  # Vous pouvez utiliser un modèle plus avancé si nécessaire
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)