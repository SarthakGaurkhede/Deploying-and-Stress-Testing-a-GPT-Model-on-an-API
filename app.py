from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
