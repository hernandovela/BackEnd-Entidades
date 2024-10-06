from flask import Flask
from db import db  # Importamos db desde el nuevo archivo para gestionar la base de datos
from flask_jwt_extended import JWTManager  # Módulo de JWT para la autenticación
from routes import api_blueprint  # Importamos el blueprint que contiene las rutas de la API
from auth import jwt_blueprint  # Importamos el blueprint que maneja la autenticación con JWT
from flask_cors import CORS  # Para habilitar CORS (Cross-Origin Resource Sharing)

app = Flask(__name__)  # Creamos la instancia de Flask
CORS(app, origins=["*"])  # Habilitamos CORS para permitir peticiones desde cualquier origen

# Configuración
app.config.from_object('config.Config')  # Cargamos la configuración desde el objeto 'Config' del archivo config.py

# Inicializamos la base de datos y el manejo de JWT
db.init_app(app)  # Vinculamos la aplicación con la base de datos usando SQLAlchemy
jwt = JWTManager(app)  # Inicializamos JWTManager para manejar la autenticación

# Registramos los blueprints de las rutas y autenticación
app.register_blueprint(api_blueprint)  # Registramos el blueprint que maneja las rutas de la API
app.register_blueprint(jwt_blueprint)  # Registramos el blueprint que maneja la autenticación JWT

if __name__ == '__main__':  # Ejecutamos la aplicación solo si se ejecuta este archivo directamente
    app.run(debug=True, host='0.0.0.0')  # Iniciamos la aplicación en modo debug, accesible desde cualquier dirección IP
