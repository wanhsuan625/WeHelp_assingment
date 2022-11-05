from flask import Flask,render_template,redirect,session,request,jsonify
import mysql.connector

app = Flask(
        __name__,
        static_folder = 'static',
        static_url_path = '/css/'
)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

dbconfig = {
    "host":"localhost",
    "user":"root",
    "password":"aa22bb33",
    "database":"website"
}
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "my_pool",
    pool_size = 5,
    pool_reset_session = True,
    **dbconfig
)

@app.route('/')
def home():
    return render_template("index.html")

# 註冊設置
@app.route('/signup', methods=["POST"])
def signup():
    name = request.form["name"]
    usr = request.form["username"]
    psw = request.form["password"]

    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()

        sql_up = "select * from member where username = %s"    
        cursor.execute(sql_up, (usr,))
        result = cursor.fetchone()
        if result != None:
            return redirect('/error?message=帳號已經被註冊')
        else:
            sql_up = "insert into member(name, username, password) values(%s,%s,%s)"
            val_up = (name,usr,psw)
            cursor.execute(sql_up,val_up)
            connection_object.commit()
            return redirect('/')
    finally:
        cursor.close()
        connection_object.close()

    
# 登入設置
@app.route('/signin', methods=["POST"])
def signin():
    usr0 = request.form["username0"]
    psw0 = request.form["password0"]

    if usr0 == "" or psw0 == "":
        return redirect('/error?message=請輸入帳號、密碼')
    
    connection_object = connection_pool.get_connection()
    cursor =  connection_object.cursor()
    sql_in = "select * from member where username = %s and password = %s"
    val_in = (usr0,psw0)
    cursor.execute(sql_in,val_in)
    result_in = cursor.fetchone()
    cursor.close()
    connection_object.close()

    if result_in != None:
        session["state"] = "login"
        session["user"] = result_in
        return redirect('/member')
    else:
        return redirect('/error?message=帳號或密碼輸入錯誤')

# 會員頁面
@app.route('/member')
def member():
    userState = session.get("state")
    userName = session.get("user")

    if userState != "login":
        return redirect('/')
    else:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        sql_content = "select member.name, message.content from member inner join message on member.id = message.member_id order by message.time desc"
        cursor.execute(sql_content)
        result_content = cursor.fetchall()
        cursor.close()
        connection_object.close()
        return render_template("member.html", name = userName[1], content = result_content)

# 留言頁面
@app.route('/message', methods=["POST"])
def message():
    userdata = session.get("user")
    content = request.form["message"]
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        sql_msg = "insert into message(member_id,content) values(%s,%s)"
        val_msg = (userdata[0], content)
        cursor.execute(sql_msg,val_msg)
        connection_object.commit()       
        return redirect('/member')
    except:
        return "Unexpected Error"
    finally:
        cursor.close()
        connection_object.close()

# 失敗頁面
@app.route('/error')
def error():
    msg = request.args.get("message")
    return render_template("error.html",error = msg)

# 登出設置
@app.route('/signout', methods=["GET"])
def signout():
    session.clear()
    return redirect('/')

# 查詢會員資料的 API
@app.route('/api/member',methods=["GET", "PATCH"])
def api():
    userState = session.get("state")
    if request.method == "GET":
        if userState != 'login':
            return jsonify({"data": None})
        else:
            username = request.args.get("username", None)
            connection_object = connection_pool.get_connection()
            cursor =  connection_object.cursor()
            sql_mem = "select * from member where username = %s"
            val_mem = (username,)
            cursor.execute(sql_mem, val_mem)
            result_userdata = cursor.fetchone()
            if result_userdata == None:
                return jsonify({"data": None})
            else:
                data = {"id": result_userdata[0],
                        "name": result_userdata[1],
                        "username": result_userdata[2]}
                return jsonify({"data": data})

    # 更新會員姓名
    elif request.method == "PATCH":
        if userState != 'login':
            return jsonify({"error": "true"})
        else:
            userdata = session.get("user")
            newname = request.get_json().get("name")
            connection_object = connection_pool.get_connection()
            cursor = connection_object.cursor()
            sql_update = "update member set name = %s where username = %s"
            val_update = (newname,userdata[2])
            cursor.execute(sql_update,val_update)
            connection_object.commit()
            cursor.close()
            connection_object.close()
            
            return jsonify({"ok": "true"})

if __name__ == '__main__':
    app.run(port=3000, debug=True)