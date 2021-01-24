from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao
        return self.valor
        return self.categoria
        return self.observacoes


    class Meta:
        verbose_name_plural = 'Transações'
