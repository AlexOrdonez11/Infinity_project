from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200, null=True)
	correo = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Propiedad(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null = True)
	nombre = models.CharField(max_length=200)
	precio = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	imagen = models.ImageField(null=True, blank=True)
	habitaciones = models.IntegerField()
	garaje = models.IntegerField()
	banos = models.IntegerField()

	def __str__(self):
		return self.nombre

	@property
	def URLimagen(self):
		try:
			url = self.imagen.url
		except:
			url = ''
		return url

class Filter(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	fecha = models.DateTimeField(auto_now_add=True)
	completada = models.BooleanField(default=False)
	trans_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.trans_id)

	@property
	def get_total_filters(self):
		filteritems = self.itemorden_set.all()
		total = sum([item.get_total for item in filteritems])
		return total 

	@property
	def get_filter_items(self):
		filteritems = self.itemfilter_set.all()
		total = sum([item.cantidad for item in filteritems])
		return total

	@property
	def MinMax(self):
		MinMax = False
		items = self.itemfilter_set.all()
		for i in items:
			if i.propiedad.digital == False:
				MinMax = True
		return shipping

class ItemFIlter(models.Model):
	propiedad = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	filter = models.ForeignKey(Filter, on_delete=models.SET_NULL, null=True)
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	fecha = models.DateTimeField(auto_now_add=True)
	@property
	def get_total(self):
		total = self.propiedad.precio * self.cantidad
		return total

class Shipping(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	dpto = models.CharField(max_length=200, null=False)
	cod_postal = models.CharField(max_length=200, null=False)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.direccion

