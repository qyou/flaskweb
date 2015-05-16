# -*- coding: utf-8 -*-

import os
from werkzeug import secure_filename
from flask import Flask
from flask import url_for # for static files
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import flash

from models import Album

app = Flask(__name__)
app.secret_key = os.urandom(24) # use for login

@app.route('/')
def index():
    return render_template('index.html', title=u'主页')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'summer' and request.form['password'] == 'youqiang':
            session['login'] = True
            return redirect(url_for('index'))
        else:
            flash('Wrong username or password!')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method=='POST':
        flash("注册成功")
        return redirect(url_for('index'))
    else:
        return render_template('sign.html', title=u'注册')


@app.route('/contact')
def contact():
    return render_template('contact.html', title=u'联系我们')

# TODO: need to add the next code 
@app.route('/album', methods=['GET', 'POST'])
def album():
    upload = 'upload-file'
    savedir = os.path.join(os.path.dirname(__file__), 'static', 'upload')    
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    if request.method=='POST':
        f = request.files[upload]
        f.save(os.path.join(savedir, secure_filename(f.filename)))
        return render_template('upload.html', filename=secure_filename(f.filename), title=u"上传")
    album = Album()
    return render_template('album.html', upload=upload, album=album, title=u'相簿')
    # return render_template('album.html', upload=upload,  title=u'相簿')

# TODO: 
@app.route('/message')
def message():
    return render_template('message.html', title=u'留言簿')
# TODO: 
@app.route('/email')
def email():
    return render_template('email.html', title=u'邮件系统')

def main():
    app.run(debug=False)
    
if __name__ == '__main__':
    main()
