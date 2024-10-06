from db import db  # Importamos la instancia de la base de datos desde db.py

# Definimos la clase Entity, que representa la tabla 'entities' en la base de datos
class Entity(db.Model):
    __tablename__ = 'entities'  # Especificamos el nombre de la tabla
    
    id = db.Column(db.Integer, primary_key=True)  # Columna de ID que es clave primaria
    name = db.Column(db.String(100), nullable=False)  # Columna para el nombre de la entidad, no puede ser nula
    employees = db.relationship('Employee', backref='entity', lazy=True)  # Relación uno a muchos con la tabla 'employees'

# Definimos la clase Employee, que representa la tabla 'employees' en la base de datos
class Employee(db.Model):
    __tablename__ = 'employees'  # Especificamos el nombre de la tabla
    
    id = db.Column(db.Integer, primary_key=True)  # Columna de ID que es clave primaria
    name = db.Column(db.String(100), nullable=False)  # Columna para el nombre del empleado, no puede ser nula
    role = db.Column(db.String(50), nullable=False)  # Columna para el rol del empleado, no puede ser nula
    entity_id = db.Column(db.Integer, db.ForeignKey('entities.id'), nullable=False)  # Columna de clave foránea que referencia a la tabla 'entities'