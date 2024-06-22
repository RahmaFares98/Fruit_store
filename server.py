from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    form_data = request.form
    print(form_data)
    first_name = (request.form.get('first_name'))
    last_name = (request.form.get('last_name'))
    Strawberry_count = int(request.form.get('strawberry', 0))
    Raspberry_count = int(request.form.get('raspberry', 0))
    Apple_count = int(request.form.get('apple', 0))
    total_count = Apple_count+Strawberry_count+Raspberry_count
    print(f"Charging {first_name} for {total_count} fruits")
    return render_template('checkout.html', data=form_data, first_name=first_name,last_name=last_name ,Apple_count=Apple_count, Strawberry_count=Strawberry_count, Raspberry_count=Raspberry_count, total_count=total_count)


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    