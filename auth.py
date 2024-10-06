from flask import Blueprint, request, jsonify  # Importamos las clases necesarias para crear blueprints y manejar solicitudes/respuestas
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity  # Funciones JWT para generar tokens y proteger rutas
from functools import wraps  # wraps nos permite decorar funciones sin alterar sus propiedades originales

jwt_blueprint = Blueprint('auth', __name__)  # Creamos un blueprint para las rutas relacionadas con JWT y autenticación

# Usuarios simulados para autenticación
users = {
    'admin': {'password': 'adminpassword', 'role': 'admin'},  # Usuario administrador con contraseña y rol
    'user': {'password': 'userpassword', 'role': 'user'}  # Usuario regular con contraseña y rol
}

@jwt_blueprint.route('/login', methods=['POST'])  # Definimos la ruta para login, que solo acepta peticiones POST
def login():
    data = request.get_json()  # Obtenemos los datos de la solicitud en formato JSON
    username = data.get('username')  # Extraemos el nombre de usuario
    password = data.get('password')  # Extraemos la contraseña
    
    user = users.get(username)  # Buscamos el usuario en el diccionario de usuarios

    if user and user['password'] == password:  # Si el usuario existe y la contraseña es correcta
        access_token = create_access_token(identity={'username': username, 'role': user['role']})  # Creamos un token de acceso con la identidad del usuario
        return jsonify(access_token=access_token), 200  # Retornamos el token de acceso y un estado 200 (OK)
    
    return jsonify({"msg": "Invalid credentials"}), 401  # Si las credenciales son inválidas, retornamos un mensaje de error y un estado 401 (no autorizado)

def admin_required(fn):
    @wraps(fn)  # Usamos wraps para mantener el nombre original de la función decorada
    @jwt_required()  # Requerimos que el usuario esté autenticado con un token válido
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()  # Obtenemos la identidad del usuario desde el token
        if identity['role'] != 'admin':  # Verificamos si el rol del usuario es 'admin'
            return {"msg": "Admin privileges required"}, 403  # Si no es admin, retornamos un mensaje de error y un estado 403 (prohibido)
        return fn(*args, **kwargs)  # Si es admin, ejecutamos la función decorada
    return wrapper  # Retornamos la función decorada
