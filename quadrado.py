#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, render_template, request


class Controle():
	inicio = True
		
	

app = Flask(__name__)


n = Controle();
original = (0,9)
SIZE = 10
inicio = 0
fim = 10
@app.route("/", methods=["GET", "POST"])
def home():
	global inicio, fim
	numList = []
	
	if n.inicio: 
		numList = range(inicio, fim)
		n.inicio = False
		return render_template('index.html', inicio=inicio, fim=fim, numList=numList)		
	else:
		try: 
			userInicio = int(request.args["numero"])
			if userInicio > inicio: 
				inicio = fim
				fim += SIZE
				numList = range(inicio, fim)
				return render_template('index.html', inicio=inicio, fim=fim, numList=numList)
			else:
				if userInicio - SIZE > 0 :
					fim = inicio
					inicio -= SIZE
					numList = range(inicio, fim )
					return render_template('index.html', inicio=inicio, fim=fim, numList=numList)
					
				else:
					inicio, fim = original
					numList = range(inicio, fim)
					return render_template('index.html', inicio=inicio, fim=fim, numList=numList)
		
		except ValueError:
			inicio, fim = original
			numList = range(inicio, fim)
			return render_template('index.html', inicio=inicio, fim=fim, numList=numList)
	
    
    

if __name__ == "__main__":
	app.run(debug=True)    
