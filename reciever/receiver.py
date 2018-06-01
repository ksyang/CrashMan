# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
from flaskext.mysql import MySQL
import json

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123123'
app.config['MYSQL_DATABASE_DB'] = 'crashMan'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/crash", methods=['POST', '', 'PUT', 'DELETE'])
def crash():
   if request.method == 'POST':           #get crash      
      fuzzer = request.form['fuzzer']
      fuzzingProgram = request.form['fuzzingProgram']
      alias = request.form['alias']
      pingPort = request.form['pingPort']

      con = mysql.connect()
      cursor = con.cursor()
      query = "INSERT INTO dashboard_vm (VM_Name, VM_ip, Fuzzer, Program, Port) VALUES ('%s', '%s', '%s', '%s', '%s')" % (alias, request.remote_addr ,fuzzer, fuzzingProgram, pingPort)
      cursor.execute(query)
      con.commit()
      cursor.close()
      sendData = {'result': 'success'}
      json_data = json.dumps(sendData, ensure_ascii=False)
      res = make_response(json_data)
      res.headers['Content-Type'] = 'application/json'
      return res

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=1337, debug=True)
