import flask
from flask import request
from testrunner import clear_dir


render_template = flask.render_template  # Pointing to local module.
Flask = flask.Flask  # Pointing to local module.
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test_validation', methods=['POST'])
def validate():
    cep = request.form.get('cep')
    results = clear_dir(cep)
    # template_table = jinja_env.get_template('validate.html')
    # return template_table.render()
    return render_template('validation_page.html', results=results)


if __name__ == '__main__':
     app.run(debug=True, port=6035)