from flask import Flask, render_template

app = Flask(__name__, template_folder=".", static_folder="Static", static_url_path="/assets")


@app.route('/')
def home():
    return render_template("Template/index.html")


@app.route('/index.html')
def index_page():
    return render_template("Template/index.html")


@app.route('/dashboard1')
@app.route('/dashboard1.html')
def dashboard1_page():
    return render_template("Template/dashboard1.html")


@app.route('/dashboard2')
@app.route('/dashboard2.html')
def dashboard2_page():
    return render_template("Template/dashboard2.html")


@app.route('/story')
@app.route('/story.html')
def story_page():
    return render_template("Template/story.html")


if __name__ == '__main__':
    app.run(debug=True)