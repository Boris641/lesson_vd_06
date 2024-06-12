from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        city = request.form.get('city')
        content = request.form.get('content')
        age = request.form.get('age')
        if title and content:
            posts.append({'title': title,  'content': content, 'age': age, 'city': city})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)

