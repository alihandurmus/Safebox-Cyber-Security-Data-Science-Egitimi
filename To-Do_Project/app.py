from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask import Flask , request, render_template, redirect , url_for

# from sqlalchemy import create_engine, Column,String,Integer,Boolean
# from sqlalchemy.orm import sessionmaker ,declarative_base
app = Flask(__name__)
# engine = create_engine('postgresql://postgres:123456789@localhost:5432/todo.db', echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/todo.db'#database e bağlanma
db = SQLAlchemy(app)
class Todo(db.Model):#Model Tanımlama
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
#Base.metadata.create_all(engine)

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('index.html' , incomplete=incomplete, complete=complete)
@app.route('/add',methods=['POST'])#CRUD işlemleri
def add():
    todo = Todo(text=request.form['todoitem'],complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)