from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(str(data))


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        sub = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, sub, message])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "did not save to database"
    else:
        return "Someting went wrong"
    return '  '
