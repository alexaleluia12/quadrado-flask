#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, render_template, request, jsonify

# TODO



class Controle():
    stade  = True
    SIZE   = 10
    
    def __init__(self):
        self.init   = 1
        self.end    = 10
    
    def reset(self):
        self.init = 1
        self.end = 10
      
    def increse(self):
        self.init += self.SIZE
        self.end  += self.SIZE
        return range(self.init, self.end + 1)
    
    def decrese(self):
        self.init -= self.SIZE
        self.end  -= self.SIZE
        return range(self.init, self.end + 1)
    


app = Flask(__name__)


n = Controle();

@app.route("/")
def home():
    if n.stade:
        n.stade = False
        return render_template('index.html', numList=range(n.init, n.end + 1))
    else:
        n.reset()
        return render_template('index.html', numList=range(n.init, n.end + 1))

@app.route('/numdata')
def api():
    listToReturn = None
    val = request.args.get('op', 0, type=int)
    if val == 1:
        listToReturn = n.increse()
    elif val == -1:
        listToReturn = n.decrese()
    else:
        listToReturn = range(1, n.SIZE + 1)
        
    return jsonify(numList=listToReturn)
    

if __name__ == "__main__":
	app.run(debug=True)    
