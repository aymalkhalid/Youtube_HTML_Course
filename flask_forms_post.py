from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form from lecture_8.html as a template string
form_html = '''
'''

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        favorite_color = request.form.get('color', '')
        hobbies = request.form.getlist('interests')
        message = request.form.get('message', '')
        country = request.form.get('Country', '')
        # Write only the user's data to a simple text file (not the whole form)
        with open('example.txt', 'a', encoding='utf-8') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Password: {password}\n")
            f.write(f"Favorite Color: {favorite_color}\n")
            f.write(f"Hobbies: {', '.join(hobbies)}\n")
            f.write(f"Message: {message}\n")
            f.write(f"Country: {country}\n")
            f.write("---\n")
        return render_template_string(form_html, success=True)
    return render_template_string(form_html, success=False)

if __name__ == '__main__':
    app.run(debug=True)
