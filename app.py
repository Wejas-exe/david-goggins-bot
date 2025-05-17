from flask import Flask, render_template, request
from goggins_prompt import get_goggins_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        try:
            user_input = request.form["user_input"]
            response = get_goggins_response(user_input)
        except Exception as e:
            response = f"Error: {str(e)}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)