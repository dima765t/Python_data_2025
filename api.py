from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = None
    entered_address = None
    entered_area = None
    entered_room_num = None
    if request.method == 'POST':
        entered_address = request.form.get('address')
        entered_area = request.form.get('area')
        entered_room_num = request.form.get('room_num')
        predicted_price = f"Predicted price for {entered_room_num} rooms at {entered_address} with area {entered_area} is 4,200 ש״ח"
    return render_template('index.html', predicted_price=predicted_price, entered_address=entered_address, entered_area=entered_area, entered_room_num=entered_room_num)

if __name__ == '__main__':
    app.run(debug=True, port=5001)