from django.db import models


class Acessorio(models.Model):
    descircao = models.CharField(max_length=100)

    def __str__(self):
        return self.descircao

    class Meta:
        verbose_name = "acessório"
        verbose_name_plural = "acessórios"


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "cores"


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nome.upper()}-{self.nacionalidade.upper()}"


class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return f"{self.marca}-{self.modelo}-{self.ano}-{self.cor}"

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
