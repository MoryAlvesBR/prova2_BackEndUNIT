from flask import Flask, request
from flask_restful import Resource, Api, Resquest
from cadastrosimples_banco import Users, init_db
import json
import jwt

app = Flask(__name__)
api = Api(app)

@app.route('/User',methods = ['POST','GET'])
    def post(self):
        body = json.loads(request.data)
        NewUser = User(nome=body["nome"],
                       idade=body["idade"],
                       login=body["login"],
                       senha=body["senha"])
        NewUser.save()

    def get(self, id):
        try:
            user = Users.query.filter_by(id=id).first()
            response = {
                "nome": Users.nome,
                "id": Users.id
            }

@app.route('/login',methods = ['POST'])
    def login():
        if request.method == 'POST':
            login = request.form['email']
            senha = request.form['password']
        return "Email: " + email + " <br> " + "Password: " + password

class Auth(Resource):
    def post(self):
        key = "abcx123"
        Users = json.loads(request.data)
        payload = {
            "user": "James",
            "login": Users["jamesMory"]
        }
        encoded = jwt.encode(payload, key)
        response = {
            "jwt-token": encoded
        }
        return response
    except:
        return {"error": "Bad request"}

    def get(self):
        try:
            token = request.headers.get('authorization')
            payload = jwt.decode(jwt, "abcx123")
            return {"ok": "ok"}
        except:
            return {"error": "error"}

api.add_Resource(Auth, '/signin')

if __name__ == '__main__':