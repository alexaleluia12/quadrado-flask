#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, render_template, request, jsonify

# TODO

class Quadrado(object):
    _size   = 9
    _rangeNun = 1
    _initDefault = 1
    _endDefault = 10
    def getList(self, init, end):
        """ return a list of int between (init, end) inclusive 
        
        Diference between end and init should be 9, otherwise 
        [1,2...10] given.
        """
        sanityInt = end - init
        if self._size == sanityInt:
            return list(range(init, end + self._rangeNun))
        return list(range(self._initDefault, self._endDefault + self._rangeNun))

app = Flask(__name__)


square = Quadrado();

@app.route("/")
def home():
    return render_template('index.html', numList=square.getList(1, 10))


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
	pass#app.run()    
