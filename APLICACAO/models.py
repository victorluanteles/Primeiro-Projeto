from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    def __str__(self):
        return self.nome

class Habilidade(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=200, verbose_name="Descrição/Sobre")
    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    altura = models.FloatField()
    fk_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    fk_habilidades = models.ManyToManyField(Habilidade)
    ponto_saude = models.PositiveIntegerField()
    ataque = models.PositiveIntegerField()
    defesa = models.PositiveIntegerField()
    habilidades = models.CharField(max_length=50)
    movimentos = models.CharField(max_length=50)
    velocidade = models.PositiveIntegerField()
    experiencia = models.PositiveIntegerField()
    peso = models.FloatField()


    def __str__(self):
        return self.nome