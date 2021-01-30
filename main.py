from flask import Flask, render_template, jsonify, request
from db import init_db
from logic import show_all_day, insert_day, delete_day

app = Flask(__name__)
db = init_db(app)

@app.route('/')
def index():
   return "hello world"

# create
@app.route('/day/create', methods = ['POST'])
def create_day():
   #butuh info apa aja? name, allowed hour
   # 1. Baca Requestnya
   print(request.get_json())
   body = request.get_json()
   # 2. Validasi Requestnya
   is_valid = create_day_validation(body)
   if not is_valid:
      return {"Message": "Request tidak valid"}, 400
   # 3. Laksanakan Requestnya 
   res = insert_day(db, body["name"], body["allowed_hours"])
   # 4. Ngebalikin respon nya
   result = {"Message": "Sukses Ditambahkan"}
   return result

@app.route('/day/view')
def view_day():
   # 1. ambil data dari database, 
   # 2. Konek ke database
   # [{"name":"monday", "hours": 8, ...}, {"name":"monday", "hours": 8, ...}]
   res = show_all_day(db)
   return jsonify(res)

@app.route('/day/delete', methods = ['POST'])
def delete_day_handler():
   #butuh info apa aja? id
   # 1. Baca Requestnya
   print(request.get_json())
   body = request.get_json()
   # 2. Validasi Requestnya
   is_valid = delete_day_validation(body)
   if not is_valid:
      return {"Message": "Request tidak valid"}, 400
   # 3. Laksanakan Requestnya 
   rowCount = delete_day(db, body["id"])
   # 4. Ngebalikin respon nya
   if rowCount == 0:
      result = {"message": "ID tidak ada", "jumlah_record_terhapus": rowCount}
   else:
      result = {"message": "Sukses Terhapus", "jumlah_record_terhapus": rowCount}
   return result

def create_day_validation(body) -> bool:
   expected_field = ["name", "allowed_hours"]
   sent_field = list(body.keys())
   
   result = True
   for body_field in sent_field:
      if body_field in expected_field:
         result = result and True  
      else:
         result = result and False
   return result

def delete_day_validation(body) -> bool:
   expected_field = ["id"]
   sent_field = list(body.keys())
   
   result = True
   for body_field in sent_field:
      if body_field in expected_field:
         result = result and True  
      else:
         result = result and False
   return result

if __name__ == '__main__':
   app.run(debug = True)