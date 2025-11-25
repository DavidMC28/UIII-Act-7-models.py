from django.db import models

class PadreMadre(models.Model):
    id_padre_madre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono_principal = models.CharField(max_length=20)
    telefono_alternativo = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    relacion_con_nino = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class GrupoNinos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=50)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    num_ninos_actual = models.IntegerField(default=0)
    capacidad_maxima = models.IntegerField()
    descripcion_actividades = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_grupo

class PersonalGuarderia(models.Model):
    id_personal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20)
    certificaciones = models.TextField(blank=True, null=True)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

class Nino(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    id_nino = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    id_padre_madre_principal = models.ForeignKey(PadreMadre, on_delete=models.CASCADE)
    alergias = models.TextField(blank=True, null=True)
    necesidades_especiales = models.TextField(blank=True, null=True)
    grupo_asignado = models.ForeignKey(GrupoNinos, on_delete=models.SET_NULL, null=True)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ActividadGuarderia(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    id_grupo = models.ForeignKey(GrupoNinos, on_delete=models.CASCADE)
    material_requerido = models.TextField(blank=True, null=True)
    es_obligatoria = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_actividad

class AsistenciaNino(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)
    estuvo_enfermo = models.BooleanField(default=False)
    notas_dia = models.TextField(blank=True, null=True)
    id_personal_registro = models.ForeignKey(PersonalGuarderia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asistencia {self.id_nino} - {self.fecha_asistencia}"

class PagoMensualidad(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('VENCIDO', 'Vencido'),
    ]
    
    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]
    
    id_pago = models.AutoField(primary_key=True)
    id_nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_CHOICES)
    mes_correspondiente = models.DateField()
    estado_pago = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Pago {self.id_nino} - {self.mes_correspondiente}"
