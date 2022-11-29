from django.db import models
import datetime

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=50, unique=True)
    descripcion = models.CharField(null=False, max_length=100)
    precio = models.IntegerField(null=False, max_length=10)
    stock = models.IntegerField(max_length=5)

class Cliente(models.Model):

    id = models.IntegerField(max_length= 6, primary_key=True)
    nombre  = models.CharField(null=False, max_length=50)
    email = models.CharField(null=False, max_length=70)
    telefono = models.IntegerField(null=False, max_length=12)
    direccion = models.CharField(null=False, max_length= 100)
    registrado = models.BooleanField(default=False)


class Inventario(models.Model):

    cantidad_productos = models.IntegerField(max_length=6)
    total_stock  = models.IntegerField(max_length=5)

class Pedido(models.Model):

    id = models.CharField(primary_key=True)
    fecha_creacion  = models.DateField(default=datetime.date.today)
    detalle = models.CharField(null=False, max_length=100)
    id_cliente = models.IntegerField(null=False, max_length= 60)
    medio_pago = models.CharField(null=False, max_length= 60)
    total = models.IntegerField(null=False, max_length= 2)

class Detalle_producto(models.Model):

    id_detalle = models.CharField(primary_key=True)
    producto  = models.CharField(null=False, max_length=40)
    descripcion = models.CharField(null=False, max_length=100)
    precio = models.IntegerField(null=False, max_length= 10)
    stock = models.CharField(max_length= 5)

class Servicio(models.Model):

    id_servicio = models.CharField(primary_key=True)
    servicio = models.CharField(null=False, max_length=20)
    valor= models.IntegerField(null=False, max_length=10)
   
class Entrega(models.Model):

    id_entrega = models.IntegerField(primary_key=True)
    direccion  = models.CharField(null=False, max_length=60)
    tipo_entrega = models.CharField(null=False, max_length=60)
   
class Categoria(models.Model):

    id_categoria = models.IntegerField(primary_key=True)
    Categoria  = models.CharField(null=False, max_length=40)
   
class Carrito(models.Model):

    cantidad_items = models.IntegerField(max_length= 10)
    subtotal = models.IntegerField(null=False, max_length=40)
   

class Vendedor(models.Model):

    id_vendedor = models.IntegerField(max_length= 25, primary_key=True)
    nombre  = models.CharField(null=False, max_length=40)
