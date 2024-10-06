
# Backend - Proyecto IXF

Este proyecto utiliza Python para la creación de una API y el manejo de base de datos con PostgreSQL.

## Requisitos

- Python 3.x [Descargar Python](https://www.python.org/downloads/)
- Docker [Descargar Docker](https://www.docker.com/)
- PostgreSQL [Descargar PostgreSQL](https://www.postgresql.org/download/)
- Git [Descargar Git](https://git-scm.com/)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/hernandovela/BackEnd-Entidades.git
   cd BackEnd-Entidades
   ```

2. Crear y activar el entorno virtual:

   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En Linux/macOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno en `.env`:
   ```bash
   POSTGRES_USER=vela  
   POSTGRES_PASSWORD=vela1234  
   POSTGRES_DB=entidades  
   ```

5. Levantar la base de datos:
   ```bash
   docker-compose up -d
   ```

6. Ejecutar el backend:
   ```bash
   python app.py
   ```

## Comandos útiles

- Para detener la base de datos:
  ```bash
  docker-compose down
  ```
