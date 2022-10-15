from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(
        __name__,
        static_folder = 'static',
        static_url_path= '/css'
        )
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin',methods=["POST"])
def signin():
    acc = request.form["account"]
    psw = request.form["password"]

    if acc == "test" and psw == "test":
        session['state'] = 'login'
        print(session)
        return redirect("/member")
    elif acc == "" or psw == "":
        return redirect("/error?message=empty")
    else:
        return redirect("/error?message=fail") 

@app.route('/member')
def success():
    userState = session.get('state')
    print(session)
    if userState != 'login':
        return redirect('/')
    else:
        return render_template('member.html') 

@app.route('/error')
def fail():
    word = request.args.get('message')
    if word == "empty":
        return render_template('empty.html')
    else:
        return render_template('fail.html')

@app.route('/signout', methods=["GET"])
def signout():
    session['state'] = 'logout'
    return redirect('/')

if __name__ == "__main__":
    app.run(port = 3000, debug = True)