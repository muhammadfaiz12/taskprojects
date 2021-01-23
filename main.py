from flask import Flask, render_template, jsonify
from db import init_db
from logic import show_all_day

app = Flask(__name__)
db = init_db(app)

@app.route('/')
def index():
   return "hello world"

# create
@app.route('/day/create', methods = ['POST'])
def create_day():
   return "this is create endpoint"

@app.route('/day/view')
def view_day():
   # 1. ambil data dari database, 
   # 2. Konek ke database
   # [{"name":"monday", "hours": 8, ...}, {"name":"monday", "hours": 8, ...}]
   res = show_all_day(db)
   return jsonify(res)

@app.route('/day/delete')
def delete_day():
   return "this is delete endpoint"

if __name__ == '__main__':
   app.run(debug = True)