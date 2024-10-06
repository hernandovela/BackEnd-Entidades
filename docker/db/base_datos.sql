-- Crear tabla de entidades si no existe
CREATE TABLE IF NOT EXISTS entities (
    id SERIAL PRIMARY KEY,          -- Identificador único para cada entidad
    name VARCHAR(100) NOT NULL      -- Nombre de la entidad (obligatorio)
);

-- Crear tabla de empleados si no existe
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,          -- Identificador único para cada empleado
    name VARCHAR(100) NOT NULL,     -- Nombre del empleado (obligatorio)
    role VARCHAR(50) NOT NULL,      -- Rol del empleado (obligatorio, ej. 'admin', 'user')
    entity_id INT NOT NULL,         -- Clave foránea que apunta a la entidad
    FOREIGN KEY (entity_id) 
        REFERENCES entities(id)     -- Relación con la tabla de entidades
        ON DELETE CASCADE           -- Si se elimina una entidad, se eliminan sus empleados
);

-- Crear un índice para optimizar consultas por entidad en la tabla de empleados
CREATE INDEX IF NOT EXISTS idx_entity_id ON employees (entity_id);
