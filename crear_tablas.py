import psycopg2

# Configuración de la conexión
conn = psycopg2.connect(
    dbname="empresa",
    user="curro",
    password="1",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Crear tablas
crear_tablas = """
-- Tabla de departamentos
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de cargos
CREATE TABLE IF NOT EXISTS cargos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    salario_base DECIMAL(10,2) NOT NULL
);

-- Tabla de empleados
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento_id INTEGER,
    cargo_id INTEGER,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    FOREIGN KEY (cargo_id) REFERENCES cargos(id) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

-- Tabla de proyectos
CREATE TABLE IF NOT EXISTS proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,
    departamento_id INTEGER,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

-- Tabla intermedia de asignaciones (Empleados en proyectos)
CREATE TABLE IF NOT EXISTS asignaciones_proyectos (
    id SERIAL PRIMARY KEY,
    empleado_id INTEGER,
    proyecto_id INTEGER,
    fecha_asignacion DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);
"""
cur.execute(crear_tablas)

# Insertar datos
inserts = """
-- Insertar departamentos
INSERT INTO departamentos (nombre) VALUES 
('Recursos Humanos'),
('Tecnología'),
('Marketing'),
('Ventas'),
('Finanzas');

-- Insertar cargos
INSERT INTO cargos (nombre, salario_base) VALUES 
('Gerente', 5000.00),
('Analista', 3000.00),
('Desarrollador', 4000.00),
('Contador', 3500.00),
('Ejecutivo de Ventas', 3200.00);

-- Insertar empleados
INSERT INTO empleados (nombre, apellido, email, fecha_contratacion, departamento_id, cargo_id) VALUES 
('Juan', 'Pérez', 'juan.perez@empresa.com', '2020-05-10', 2, 3),
('Ana', 'González', 'ana.gonzalez@empresa.com', '2018-08-15', 1, 1),
('Carlos', 'Martínez', 'carlos.martinez@empresa.com', '2019-11-20', 3, 2),
('Sofía', 'Rodríguez', 'sofia.rodriguez@empresa.com', '2021-01-25', 4, 5),
('Diego', 'Fernández', 'diego.fernandez@empresa.com', '2017-09-30', 5, 4),
('Laura', 'Méndez', 'laura.mendez@empresa.com', '2019-06-18', 2, 3),
('Pedro', 'Ramírez', 'pedro.ramirez@empresa.com', '2020-12-01', 3, 2),
('Mariana', 'López', 'mariana.lopez@empresa.com', '2016-07-22', 1, 1);

-- Insertar proyectos
INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, departamento_id) VALUES 
('Sistema de Gestión', 'Desarrollo de un software de gestión para la empresa', '2023-01-10', NULL, 2),
('Campaña Publicitaria', 'Estrategia de marketing para el lanzamiento de un nuevo producto', '2023-02-15', '2023-06-30', 3),
('Expansión de Mercado', 'Estrategia para expandir la empresa a nivel internacional', '2023-03-01', NULL, 4),
('Automatización Financiera', 'Implementación de herramientas de automatización en finanzas', '2023-04-20', NULL, 5);

-- Insertar asignaciones de empleados a proyectos
INSERT INTO asignaciones_proyectos (empleado_id, proyecto_id) VALUES 
(1, 1),
(2, 2),
(3, 2),
(4, 3),
(5, 4),
(6, 1),
(7, 3),
(8, 4);
"""
cur.execute(inserts)

# Confirmar cambios y cerrar conexión
conn.commit()
cur.close()
conn.close()

print("Tablas creadas e información insertada correctamente.")
