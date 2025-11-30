framework django : convierte lo siguiente a models.py , unicamnete quiero el modelo  Entidad	Atributos	Tipo de Campo
Nino	id_nino, nombre, apellido, fecha_nacimiento, genero, id_padre_madre_principal, alergias, necesidades_especiales, grupo_asignado, fecha_inscripcion	INT, VARCHAR(100), VARCHAR(100), DATE, CHAR(1), INT, TEXT, TEXT, VARCHAR(50), DATE
Padre_Madre	id_padre_madre, nombre, apellido, email, telefono_principal, telefono_alternativo, direccion, dni, relacion_con_nino, profesion	INT, VARCHAR(100), VARCHAR(100), VARCHAR(100), VARCHAR(20), VARCHAR(20), VARCHAR(255), VARCHAR(20), VARCHAR(50), VARCHAR(100)
Personal_Guarderia	id_personal, nombre, apellido, cargo, email, telefono, fecha_contratacion, salario, dni, certificaciones, turno	INT, VARCHAR(100), VARCHAR(100), VARCHAR(50), VARCHAR(100), VARCHAR(20), DATE, DECIMAL(10,2), VARCHAR(20), TEXT, VARCHAR(50)
Grupo_Ninos	id_grupo, nombre_grupo, edad_minima, edad_maxima, id_personal_cargo, num_ninos_actual, capacidad_maxima, descripcion_actividades	INT, VARCHAR(50), INT, INT, INT, INT, INT, TEXT
Actividad_Guarderia	id_actividad, nombre_actividad, descripcion, horario, duracion_minutos, id_grupo, material_requerido, es_obligatoria	INT, VARCHAR(100), TEXT, VARCHAR(100), INT, INT, TEXT, BOOLEAN
Asistencia_Nino	id_asistencia, id_nino, fecha_asistencia, hora_entrada, hora_salida, estuvo_enfermo, notas_dia, id_personal_registro	INT, INT, DATE, TIME, TIME, BOOLEAN, TEXT, INT
Pago_Mensualidad	id_pago, id_nino, fecha_pago, monto_pagado, concepto, metodo_pago, mes_correspondiente, estado_pago, fecha_vencimiento	INT, INT, DATETIME, DECIMAL(10,2), VARCHAR(100), VARCHAR(50), DATE, VARCHAR(50), DATE
Relaciones:

Nino (id_padre_madre_principal) -> Padre_Madre (id_padre_madre) (Muchos a Uno)
Nino (grupo_asignado) -> Grupo_Ninos (nombre_grupo) (Muchos a Uno) - (considerando nombre como clave)
Grupo_Ninos (id_personal_cargo) -> Personal_Guarderia (id_personal) (Muchos a Uno)
Actividad_Guarderia (id_grupo) -> Grupo_Ninos (id_grupo) (Muchos a Uno)
Asistencia_Nino (id_nino) -> Nino (id_nino) (Muchos a Uno)
Asistencia_Nino (id_personal_registro) -> Personal_Guarderia (id_personal) (Muchos a Uno)
Pago_Mensualidad (id_nino) -> Nino (id_nino) (Muchos a Uno)
