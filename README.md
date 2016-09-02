# quadrado-flask

![quadrado](img/img.png)
--
This project uses:

Flask<br/>
Bootstrap<br/>
AngularJs

--
You should have this things instaled:<br/>
make * optional<br/>
git<br/>
pip<br/>
python 3+<br/>
virtualenv<br/>

\* Run local
```sh
# I omit $
# download and prepare the environment
git clone https://github.com/alexaleluia12/quadrado-flask.git
cd quadrado-flask
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt

# actualy run the server
make run
# or
python quadrado.py

```
\* Cancel: Ctrl + c<br/>
\* Get out virtualenv: `$ deactivate`

--
Run test
```sh
cd tests
PYTHONPATH=.. python quadrado_test.py
```
