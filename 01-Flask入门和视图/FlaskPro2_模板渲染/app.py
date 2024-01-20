from flask import Flask, render_template
import numpy as np
app = Flask(__name__)


@app.route('/')
def home():
    return "flask home"

@app.route('/index/')
def index():
    #return '<b> Flask index <b>'
    #模板渲染
    number = np.random.rand(3, 3)
    return render_template('../FlaskPro5_请求与响应/App/templates/index.html', name = number)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')