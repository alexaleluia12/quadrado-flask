#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, render_template, request, jsonify

# TODO
# corigir porque o angularjs nao esta interando sobre o valor retornado pelo ajax

class Controle():
    stade  = True
    SIZE   = 10
    init   = 1
    end    = 10
      
    def increse(self):
        self.init += self.SIZE
        self.end += self.SIZE
        return range(self.init, self.end + 1)
    
    


app = Flask(__name__)


n = Controle();

@app.route("/", methods=["GET", "POST"])
def home():
    if n.stade:
        n.stade = False
        return render_template('index.html', numList=range(n.init, n.end + 1))

@app.route('/numdata')
def api():
    val = request.args.get('op', 0, type=int)
    return jsonify(numList=n.increse())
    

if __name__ == "__main__":
	app.run(debug=True)    
