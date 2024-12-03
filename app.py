from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__, template_folder='Template')

def generate_password(min_length, max_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length or (len(pwd) < max_length and (not has_number or not has_special)):
        char = random.choice(characters)
        pwd += char
        if char in digits:
            has_number = True
        if char in special:
            has_special = True

    return pwd[:max_length] if len(pwd) > max_length else pwd

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    min_length = data.get('min_length')
    max_length = data.get('max_length')
    numbers = data.get('numbers', True)
    special_characters = data.get('special_characters', True)

    if min_length > max_length:
        return jsonify({'error': 'Minimum length cannot be greater than maximum length!'}), 400

    password = generate_password(min_length, max_length, numbers, special_characters)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)