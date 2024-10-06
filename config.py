import os  # Importamos el módulo os para acceder a variables de entorno

class Config:
    # Configuración de la URI de la base de datos usando variables de entorno
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5433/{os.getenv('POSTGRES_DB')}"
    
    # Deshabilitamos el rastreo de modificaciones de SQLAlchemy para mejorar el rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Clave secreta para firmar los tokens JWT, obtenida desde una variable de entorno o usando un valor por defecto
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'supersecretkey')  
