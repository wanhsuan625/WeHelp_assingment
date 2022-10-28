from flask import Flask,render_template,redirect,session,request
import mysql.connector

app = Flask(
        __name__,
        static_folder = 'static',
        static_url_path = '/css/'
)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aa22bb33",
  database="website"
)
cursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('index.html')

# 註冊設置
@app.route('/signup', methods=["POST"])
def signup():
    name = request.form["name"]
    usr = request.form["username"]
    psw = request.form["password"]

    sql = "select * from member where username = %s"    
    cursor.execute(sql, (usr,))
    result = cursor.fetchone()
    if result != None:
        return redirect('/error?message=帳號已經被註冊')
    else:
        sql_up = "insert into member(name, username, password) values(%s,%s,%s)"
        val_up = (name,usr,psw)
        cursor.execute(sql_up,val_up)
        mydb.commit()
        return redirect('/')
    
# 登入設置
@app.route('/signin', methods=["POST"])
def signin():
    usr0 = request.form["username0"]
    psw0 = request.form["password0"]

    if usr0 == "" or psw0 == "":
        return redirect('/error?message=請輸入帳號、密碼')
    
    sql_in = "select * from member where username = %s and password = %s"
    val_in = (usr0,psw0)
    cursor.execute(sql_in,val_in)
    result_in = cursor.fetchone()
    if result_in != None:
        session['state'] = 'login'
        session['user'] = result_in
        print(session)
        return redirect('/member')
    else:
        return redirect('/error?message=帳號或密碼輸入錯誤')

# 會員頁面
@app.route('/member')
def member():
    userState = session.get('state')
    userName = session.get('user')
    if userState != 'login':
        return redirect('/')
    else:
        return render_template('member.html', name = userName[1])

# 失敗頁面
@app.route('/error')
def error():
    msg = request.args.get('message')
    return render_template('fail.html',error = msg)

# 登出設置
@app.route('/signout', methods=["GET"])
def signout():
    session['state'] = 'logout'
    return redirect('/')

if __name__ == '__main__':
    app.run(port=3000)