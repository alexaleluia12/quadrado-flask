from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# TODO
# atualizar o angular js tmb *


class Quadrado(object):
    _end_default = 10
    _size = 9
    _range_nun = 1
    _init_default = 1

    def get_list(init, end):
        """ return a list of int between (init, end) inclusive

        Diference between end and init should be 9, otherwise
        [1,2...10] given.
        """
        sanity_int = end - init
        if Quadrado._size == sanity_int:
            return list(range(init, end + Quadrado._range_nun))
        return list(range(Quadrado._init_default,
                          Quadrado._end_default + Quadrado._range_nun))

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template('index.html', numList=Quadrado.get_list(1, 10))


@app.route('/numdata')
def api():
    lst = []
    init = request.args.get('init', 1, type=int)
    end = request.args.get('end', 10, type=int)
    lst = Quadrado.get_list(init, end)
    return jsonify(numList=lst)


if __name__ == "__main__":
    app.run()
