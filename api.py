from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = None
    if request.method == 'POST':
        # Get form data if you want to use it
        # address = request.form.get('address')
        # room_num = request.form.get('room_num')
        # ... add more fields as needed
        predicted_price = "4,200 ש״ח"  
    return render_template('index.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True, port=5001)