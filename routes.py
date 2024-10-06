from flask import Blueprint, request, jsonify  # Importamos funciones para crear blueprints y manejar solicitudes/respuestas
from flask_jwt_extended import jwt_required  # Decorador para proteger rutas con JWT
from db import db  # Importamos la instancia de la base de datos desde db.py
from models import Entity, Employee  # Importamos los modelos de la base de datos
from auth import admin_required  # Importamos el decorador que verifica si el usuario es administrador

api_blueprint = Blueprint('api', __name__)  # Creamos un blueprint para las rutas de la API

# Rutas para Entidades

@api_blueprint.route('/entities', methods=['GET'])
@jwt_required(optional=True)  # Ruta protegida opcionalmente por JWT
def get_entities():
    entities = Entity.query.all()  # Consultamos todas las entidades en la base de datos
    result = [{"id": e.id, "name": e.name} for e in entities]  # Convertimos el resultado a una lista de diccionarios
    return jsonify(result), 200  # Retornamos los resultados en formato JSON con código de estado 200 (OK)

@api_blueprint.route('/entities', methods=['POST'])
@admin_required  # Ruta protegida, solo accesible por administradores
def create_entity():
    data = request.get_json()  # Obtenemos los datos enviados en la solicitud
    new_entity = Entity(name=data['name'])  # Creamos una nueva entidad con el nombre proporcionado
    db.session.add(new_entity)  # Añadimos la nueva entidad a la sesión de la base de datos
    db.session.commit()  # Guardamos los cambios en la base de datos
    return jsonify({"message": "Entity created"}), 201  # Retornamos un mensaje de éxito con código de estado 201 (creado)

@api_blueprint.route('/entities/<int:id>', methods=['PUT'])
@admin_required  # Ruta protegida, solo accesible por administradores
def update_entity(id):
    data = request.get_json()  # Obtenemos los datos enviados en la solicitud
    entity = Entity.query.get(id)  # Buscamos la entidad por su ID
    if entity:
        entity.name = data['name']  # Actualizamos el nombre de la entidad
        db.session.commit()  # Guardamos los cambios en la base de datos
        return jsonify({"message": "Entity updated"}), 200  # Retornamos un mensaje de éxito con código 200 (OK)
    return jsonify({"message": "Entity not found"}), 404  # Si no se encuentra la entidad, retornamos un mensaje de error con código 404 (no encontrado)

@api_blueprint.route('/entities/<int:id>', methods=['DELETE'])
@admin_required  # Ruta protegida, solo accesible por administradores
def delete_entity(id):
    entity = Entity.query.get(id)  # Buscamos la entidad por su ID
    if entity:
        db.session.delete(entity)  # Eliminamos la entidad
        db.session.commit()  # Guardamos los cambios en la base de datos
        return jsonify({"message": "Entity deleted"}), 200  # Retornamos un mensaje de éxito con código 200 (OK)
    return jsonify({"message": "Entity not found"}), 404  # Si no se encuentra la entidad, retornamos un mensaje de error con código 404 (no encontrado)

# Rutas para Empleados

@api_blueprint.route('/employees', methods=['GET'])
@jwt_required(optional=True)  # Ruta protegida opcionalmente por JWT
def get_employees():
    employees = Employee.query.all()  # Consultamos todos los empleados en la base de datos
    result = [{"id": e.id, "name": e.name, "role": e.role, "entity_id": e.entity_id} for e in employees]  # Convertimos el resultado a una lista de diccionarios
    return jsonify(result), 200  # Retornamos los resultados en formato JSON con código de estado 200 (OK)

@api_blueprint.route('/employees', methods=['POST'])
@admin_required  # Ruta protegida, solo accesible por administradores
def create_employee():
    data = request.get_json()  # Obtenemos los datos enviados en la solicitud
    new_employee = Employee(name=data['name'], role=data['role'], entity_id=data['entity_id'])  # Creamos un nuevo empleado con los datos proporcionados
    db.session.add(new_employee)  # Añadimos el nuevo empleado a la sesión de la base de datos
    db.session.commit()  # Guardamos los cambios en la base de datos
    return jsonify({"message": "Employee created"}), 201  # Retornamos un mensaje de éxito con código de estado 201 (creado)

@api_blueprint.route('/employees/<int:id>', methods=['PUT'])
@admin_required  # Ruta protegida, solo accesible por administradores
def update_employee(id):
    data = request.get_json()  # Obtenemos los datos enviados en la solicitud
    employee = Employee.query.get(id)  # Buscamos al empleado por su ID
    if employee:
        employee.name = data['name']  # Actualizamos el nombre del empleado
        employee.role = data['role']  # Actualizamos el rol del empleado
        db.session.commit()  # Guardamos los cambios en la base de datos
        return jsonify({"message": "Employee updated"}), 200  # Retornamos un mensaje de éxito con código 200 (OK)
    return jsonify({"message": "Employee not found"}), 404  # Si no se encuentra al empleado, retornamos un mensaje de error con código 404 (no encontrado)

@api_blueprint.route('/employees/<int:id>', methods=['DELETE'])
@admin_required  # Ruta protegida, solo accesible por administradores
def delete_employee(id):
    employee = Employee.query.get(id)  # Buscamos al empleado por su ID
    if employee:
        db.session.delete(employee)  # Eliminamos al empleado
        db.session.commit()  # Guardamos los cambios en la base de datos
        return jsonify({"message": "Employee deleted"}), 200  # Retornamos un mensaje de éxito con código 200 (OK)
    return jsonify({"message": "Employee not found"}), 404  # Si no se encuentra al empleado, retornamos un mensaje de error con código 404 (no encontrado)