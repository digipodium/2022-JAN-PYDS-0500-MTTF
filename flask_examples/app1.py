from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.orm import sessionmaker
from database import WebTest
from sqlalchemy.engine import create_engine


app = Flask(__name__)
app.secret_key = 'some_secret'

def opendb():
    engine =  create_engine('sqlite:///app.sqlite3', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website = request.form.get('website')
        title =  request.form.get('title')
        category = request.form.get('category')
        has_ip = request.form.get('ip')
        if not website or not title or not category:
            flash('Please enter both a website and a title and category', 'danger')
        else:
            has_ip = True if has_ip else False
            db = opendb()
            wt = WebTest(url=website,title=title,category=category,get_ip=has_ip)
            db.add(wt)
            db.commit()
            db.close()
            flash("the details have been saved", 'success')
        return redirect('/')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 