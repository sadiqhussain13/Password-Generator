from flask import Flask, render_template, request
import random
import string

app = Flask(__name__, template_folder='Template')

def generate_password(min_length, max_length, numbers=True, special_characters=True):
    if max_length < min_length:
        raise ValueError("Maximum length cannot be less than minimum length.")

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        if len(pwd) >= max_length:
            break

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        min_length = int(request.form.get('min_length'))
        max_length = int(request.form.get('max_length'))
        include_numbers = request.form.get('include_numbers') == 'on'
        include_specials = request.form.get('include_specials') == 'on'

        # Check if max_length is less than min_length
        if max_length < min_length:
            return render_template(
                'index.html',
                error="Max length cannot be less than Min length."
            )

        # Generate password if inputs are valid
        password = generate_password(min_length, max_length, include_numbers, include_specials)
        return render_template('index.html', password=password)

    except ValueError:
        return render_template(
            'index.html',
            error="Please enter valid numbers for min and max lengths."
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8080)