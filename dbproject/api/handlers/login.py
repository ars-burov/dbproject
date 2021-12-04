from datetime import datetime
from aiohttp_apispec import docs
from aiohttp.web_response import Response
from .base import BaseView
from dbproject.db.schema import Auth
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import *

class RegisterView(BaseView):
    URL_PATH = '/register'
    
    @docs(summary='Register')
    async def get(self):
        # username = request.args.get('username')
        # email = request.args.get('email')
        # password = request.args.get('password')
        # password_hash = generate_password_hash(password)
        # role = request.args.get('role')
        
        username = "test"
        password_hash = "test"
        role = "t"
        email = "test"
        # tbl_last_update = str(datetime.timestamp)
    
        insert_string = '''INSERT INTO public.auth(id, password, role, email, tbl_last_update)
	                      VALUES ({0}, {1}, {2}, {3});'''.format(username, password_hash, role, email)
        
        # insert_string = '''SELECT * FROM auth'''
        pg_resp = await self.pg.execute(insert_string)
        # json_string = jsonify({'user_added': True})
        
        return Response(body=f'{insert_string}')
    
class LoginView(BaseView):
    URL_PATH = '/login'
    
    @docs(summary='Login')
    async def get(self):
        return Response(body=f'Login')
    

# @create_app.route('/register', methods=["GET", "POST"])
# def register():
#     id = request.args.get('id')
#     password = request.args.get('password')
#     password_hash = generate_password_hash(password)
#     role = request.args.get('role')
#     email = request.args.get('email')
#     account = Table('auth', metadata, autoload=True)
#     engine.execute(account.insert(), 
#                    id=id,
#                    password=password_hash,
#                    role=role,
#                    email=email, 
#                    )
#     return jsonify({'user_added': True})


# @create_app.route('/sign_in', methods=["GET", "POST"])
# def sign_in():
#     id_entered = request.args.get('id')
#     password_entered = request.args.get('password')
#     user = session.query(Auth).filter(or_(Auth.id == id_entered, Auth.email == id_entered)
#                                           ).first()
#     if user is not None and check_password_hash(user.password, password_entered):
#         return jsonify({'signed_in': True})
#     return jsonify({'signed_in': False})
