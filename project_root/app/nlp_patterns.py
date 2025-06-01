patterns = {
    "empleado_salario_max": {
        "keywords": ["empleado", "sueldo", "mas alto",],
        "sql": """
            SELECT e.nombre, e.apellido, c.salario_base
            FROM empleados e
            JOIN cargos c ON e.cargo_id = c.id
            ORDER BY c.salario_base DESC
            LIMIT 1;
        """
    },
    "proyectos_por_departamento": {
        "keywords": ["proyectos", "departamento", "de"],
        "sql_template": """
            SELECT p.nombre, p.descripcion
            FROM proyectos p
            JOIN departamentos d ON p.departamento_id = d.id
            WHERE LOWER(d.nombre) LIKE LOWER('%{departamento}%');
        """
    },
    "empleados_despues_fecha": {
        "keywords": ["empleados", "contratados", "despues"],
        "sql_template": """
            SELECT nombre, apellido, fecha_contratacion
            FROM empleados
            WHERE fecha_contratacion > '{fecha}';
        """
    },
    "todos_los_empleados_cargo": {
    	"keywords": ["empleados", "todos", "cargo"],
    	"sql": """
            SELECT e.nombre, e.apellido, c.nombre AS cargo
            FROM empleados e
            JOIN cargos c ON e.cargo_id = c.id;
    	"""
    },
    "todos_los_empleados": {
        "keywords": ["empleados", "todos"],
        "sql": """
            SELECT nombre, apellido
            FROM empleados;
        """
    },
    "empleado_salario_max2": {
        "keywords": ["empleado", "sueldo", "mayor",],
        "sql": """
            SELECT e.nombre, e.apellido, c.salario_base
            FROM empleados e
            JOIN cargos c ON e.cargo_id = c.id
            ORDER BY c.salario_base DESC
            LIMIT 1;
        """
	 },
    "empleado_salario_max3": {
        "keywords": ["empleado", "mejor", "pagado",],
        "sql": """
            SELECT e.nombre, e.apellido, c.salario_base
            FROM empleados e
            JOIN cargos c ON e.cargo_id = c.id
            ORDER BY c.salario_base DESC
            LIMIT 1;
        """
         },

    "departamentos_mas_empleados": {
        "keywords": ["departamento", "mas", "empleados"],
        "sql": """
            SELECT d.nombre AS departamento, COUNT(e.id) AS cantidad_empleados
            FROM departamentos d
            JOIN empleados e ON d.id = e.departamento_id
            GROUP BY d.nombre
            ORDER BY cantidad_empleados DESC
            LIMIT 1;
        """
    },

    "empleados_entre_fechas": {
        "keywords": ["empleados", "contratados", "entre"],
        "sql_template": """
            SELECT nombre, apellido, fecha_contratacion
            FROM empleados
            WHERE fecha_contratacion BETWEEN '{fecha_inicio}' AND '{fecha_fin}';
        """
    },

    "cargo_por_salario": {
        "keywords": ["cargo", "sueldo", "base"],
        "sql_template": """
            SELECT nombre
            FROM cargos
            WHERE salario_base = {salario};
        """
    },

    "numero_empleados_por_cargo": {
        "keywords": ["empleados", "cargo", "cuantos"],
        "sql": """
            SELECT c.nombre AS cargo, COUNT(e.id) AS total_empleados
            FROM cargos c
            LEFT JOIN empleados e ON e.cargo_id = c.id
            GROUP BY c.nombre;
        """
    },

    "empleados_y_departamentos": {
        "keywords": ["empleados", "departamentos", "lista", "pertenecen"],
        "sql": """
            SELECT e.nombre, e.apellido, d.nombre AS departamento
            FROM empleados e
            JOIN departamentos d ON e.departamento_id = d.id;
        """
    },

    "proyectos_finalizados_este_mes": {
        "keywords": ["proyectos", "finalizados", "este mes", "terminados"],
        "sql": """
            SELECT nombre, fecha_fin
            FROM proyectos
            WHERE EXTRACT(MONTH FROM fecha_fin) = EXTRACT(MONTH FROM CURRENT_DATE)
              AND EXTRACT(YEAR FROM fecha_fin) = EXTRACT(YEAR FROM CURRENT_DATE);
        """
    },

    "numero_proyectos_por_departamento": {
        "keywords": ["proyectos", "por", "departamento", "cuantos"],
        "sql": """
            SELECT d.nombre AS departamento, COUNT(p.id) AS total_proyectos
            FROM departamentos d
            LEFT JOIN proyectos p ON d.id = p.departamento_id
            GROUP BY d.nombre;
        """
    },

    "proyectos_finalizados": {
        "keywords": ["proyectos", "completados"],
        "sql": """
            SELECT nombre, fecha_fin
            FROM proyectos
            WHERE fecha_fin IS NOT NULL;
        """
    },

    "empleados_por_departamento": {
        "keywords": ["empleados", "por", "departamento", "pertenecen"],
        "sql_template": """
            SELECT e.nombre, e.apellido
            FROM empleados e
            JOIN departamentos d ON e.departamento_id = d.id
            WHERE LOWER(d.nombre) LIKE LOWER('%departamento%');
        """
    },

    "cargos_salario_superior": {
        "keywords": ["cargos", "salario", "mayor", "superior"],
        "sql_template": """
            SELECT nombre, salario_base
            FROM cargos
            WHERE salario_base > {salario};
        """
    },

    "proyectos_por_empleado": {
        "keywords": ["proyectos", "empleado", "participa", "trabaja"],
        "sql_template": """
            SELECT p.nombre, p.descripcion
            FROM proyectos p
            JOIN asignaciones_proyectos ap ON p.id = ap.proyecto_id
            JOIN empleados e ON ap.empleado_id = e.id
            WHERE LOWER(e.nombre) LIKE LOWER('%nombre%');
        """
    },

    "listar_cargos": {
        "keywords": ["cargos", "lista"],
        "sql": """
            SELECT nombre, salario_base
            FROM cargos;
        """
    },

    "listar_departamentos": {
        "keywords": ["departamentos", "lista"],
        "sql": """
            SELECT nombre
            FROM departamentos;
        """
    },

    "proyectos_por_fecha_inicio": {
        "keywords": ["proyectos", "empiezan", "inicio", "comienzan"],
        "sql_template": """
            SELECT nombre, descripcion, fecha_inicio
            FROM proyectos
            WHERE fecha_inicio = '{fecha}';
        """
    },

    "empleados_antes_fecha": {
        "keywords": ["empleados", "contratados", "antes"],
        "sql_template": """
            SELECT nombre, apellido, fecha_contratacion
            FROM empleados
            WHERE fecha_contratacion < '{fecha}';
        """
    },

    "duracion_proyectos": {
        "keywords": ["duracion", "proyectos"],
        "sql": """
            SELECT nombre, fecha_inicio, fecha_fin,
                   fecha_fin - fecha_inicio AS duracion
            FROM proyectos
            WHERE fecha_fin IS NOT NULL;
        """
    },

    "empleados_email_corporativo": {
        "keywords": ["empleados", "correo", "corporativo"],
        "sql": """
            SELECT nombre, apellido, email
            FROM empleados
            WHERE LOWER(email) LIKE LOWER('%@%');
        """
    },

    "proyectos_activos": {
        "keywords": ["proyectos", "activos"],
        "sql": """
            SELECT nombre, descripcion, fecha_inicio
            FROM proyectos
            WHERE fecha_fin IS NULL;
        """
    },

    "empleado_salario_min": {
        "keywords": ["empleado", "salario", "mas bajo"],
        "sql": """
            SELECT e.nombre, e.apellido, c.salario_base
            FROM empleados e
            JOIN cargos c ON e.cargo_id = c.id
            ORDER BY c.salario_base ASC
            LIMIT 1;
        """
    },

    "empleados_por_cargo_cantidad": {
        "keywords": ["cuántos", "empleados", "por cargo"],
        "sql": """
            SELECT c.nombre AS cargo, COUNT(e.id) AS total_empleados
            FROM cargos c
            LEFT JOIN empleados e ON e.cargo_id = c.id
            GROUP BY c.nombre;
        """
    },

    "empleados_por_departamento_cantidad": {
        "keywords": ["cuántos", "empleados", "por departamento"],
        "sql": """
            SELECT d.nombre AS departamento, COUNT(e.id) AS total_empleados
            FROM departamentos d
            LEFT JOIN empleados e ON e.departamento_id = d.id
            GROUP BY d.nombre;
        """
    },

    "empleados_orden_fecha": {
        "keywords": ["empleados", "orden", "fecha", "contratación"],
        "sql": """
            SELECT nombre, apellido, fecha_contratacion
            FROM empleados
            ORDER BY fecha_contratacion ASC;
        """
    },

    "ultimo_empleado_contratado": {
        "keywords": ["ultimo", "empleado", "contratado", "más reciente"],
        "sql": """
            SELECT nombre, apellido, fecha_contratacion
            FROM empleados
            ORDER BY fecha_contratacion DESC
            LIMIT 1;
        """
    },

    "empleados_departamento": {
        "keywords": ["empleados", "departamento", "pertenecen"],
        "sql": """
            SELECT e.nombre, e.apellido, d.nombre AS departamento
            FROM empleados e
            JOIN departamentos d ON e.departamento_id = d.id;
        """
    },

    "contar_empleados": {
        "keywords": ["cuantos", "empleados", "hay", "total"],
        "sql": """
            SELECT COUNT(*) AS total_empleados FROM empleados;
        """
    },

    "empleados_por_departamento": {
        "keywords": ["empleados", "departamento", "trabajan"],
        "sql_template": """
            SELECT e.nombre, e.apellido
            FROM empleados e
            JOIN departamentos d ON e.departamento_id = d.id
            WHERE LOWER(d.nombre) LIKE LOWER('%{departamento}%');
        """
    },

    "proyectos_por_empleado": {
        "keywords": ["proyectos", "asignados", "empleado"],
        "sql_template": """
            SELECT p.nombre, p.descripcion
            FROM proyectos p
            JOIN asignaciones_proyectos ap ON p.id = ap.proyecto_id
            JOIN empleados e ON ap.empleado_id = e.id
            WHERE LOWER(e.nombre) LIKE LOWER('%nombre%') AND LOWER(e.apellido) LIKE LOWER('%{apellido}%');
        """
    },

    "media_salario_por_cargo": {
        "keywords": ["media", "salario", "cargo"],
        "sql": """
            SELECT nombre, AVG(salario_base) AS salario_promedio
            FROM cargos
            GROUP BY nombre;
        """
    },

    "lista_cargos": {
        "keywords": ["lista", "cargos"],
        "sql": """
            SELECT nombre AS cargo, salario_base FROM cargos;
        """
    },


    "numero_proyectos_departamento": {
        "keywords": ["proyectos", "departamento", "cuántos"],
        "sql": """
            SELECT d.nombre AS departamento, COUNT(p.id) AS total_proyectos
            FROM departamentos d
            LEFT JOIN proyectos p ON d.id = p.departamento_id
            GROUP BY d.nombre;
        """
    },

    "empleados_sin_proyectos": {
        "keywords": ["empleados", "sin", "proyectos"],
        "sql": """
            SELECT e.nombre, e.apellido
            FROM empleados e
            LEFT JOIN asignaciones_proyectos ap ON e.id = ap.empleado_id
            WHERE ap.proyecto_id IS NULL;
        """
    },

    "proyectos_en_fecha": {
        "keywords": ["proyectos", "fecha", "iniciados"],
        "sql_template": """
            SELECT nombre, descripcion
            FROM proyectos
            WHERE fecha_inicio = '{fecha}';
        """
    },

     "empleados_con_cargo": {
    "keywords": ["empleados", "cargo", "de"],
    "variables": ["cargo"],
    "sql_template": """
        SELECT e.nombre, e.apellido
        FROM empleados e
        JOIN cargos c ON e.cargo_id = c.id
        WHERE LOWER(c.nombre) LIKE LOWER('%{cargo}%');
    """
},

}

