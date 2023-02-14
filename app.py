from flask import Flask, redirect, render_template, request, json, url_for

app = Flask(__name__)


@app.route('/', endpoint='index')
def index():  # put application's code here
    return render_template('inedx.html')


users = []


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('password')
        repwd = request.form.get('repassword')

        if pwd == repwd:
            users.append(request.form.to_dict())
            print(request.args)
            return redirect('/')
        else:
            return '两次密码不一致'
    return render_template('register.html')


@app.route('/show')
def show():
    return json.dumps(users)


@app.route('/test',)
def test():
    url = url_for('index')
    print(url)
    return 'url'

if __name__ == '__main__':
    app.run(debug=True)
