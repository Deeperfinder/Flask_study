import numpy as np
from App import create_app


app = create_app()


# @app.route('/index/')
# def index():
#     #return '<b> Flask index <b>'
#     #模板渲染
#     number = np.random.rand(3, 3)
#     return render_template('index.html', name = number)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')