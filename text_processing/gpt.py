from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Define input text to be evaluated
input_text = " Hi, my name is Mark and I'm the intern pharmacist today. Are you miss Jordan Davis? I am. Great."

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text based on input
output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)

# Decode generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated evaluation:", generated_text)