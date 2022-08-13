from django.db import models


class Itens(models.Model):
    nome = models.CharField("Nome", max_length=50)
    pontos = models.IntegerField("Pontos", blank=True, null=True)

    def __str__(self):
        return self.nome


class Sobrevivente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    # idade = models.IntegerField("Idade", blank=True, null=True)
    idade = models.IntegerField("Idade")
    sexo = models.CharField("Sexo", max_length=15)
    latitude = models.CharField("Latitude", max_length=50)
    longitude = models.CharField("Longitude", max_length=50)
    infectado = models.BooleanField("Infectado", default=False)
    inventario = models.ManyToManyField(
        Itens,
        related_name="sobrevivente_itens",
        through="SobreviventeInventario"

    )

    def __str__(self):
        return self.nome


class SobreviventeInventario(models.Model):
    item = models.ForeignKey(
        Itens, verbose_name="Item", related_name="inventario_itens",
        on_delete=models.CASCADE)
    sobrevivente = models.ForeignKey(
        Sobrevivente,
        verbose_name="Sobrevivente",
        related_name="inventario_sobreviventes",
        on_delete=models.CASCADE)
    quantidade = models.IntegerField("Quantidade")


class Sinalizar(models.Model):
    sobrevivente = models.ForeignKey(
        Sobrevivente, verbose_name="Sobrevivente", related_name="sobrevivente",
        on_delete=models.CASCADE)
    sobrevivente_infectado = models.ForeignKey(
        Sobrevivente, verbose_name="Sobrevivente Infectado", related_name="sobrevivente_infectado",
        on_delete=models.CASCADE)

    class Meta:
        unique_together = [['sobrevivente', 'sobrevivente_infectado']]


class Negociar(models.Model):
    sobrevivente1 = models.ForeignKey(
        Sobrevivente,
        verbose_name="Sobrevivente1",
        related_name="sobrevivente1",
        on_delete=models.CASCADE)
    sobrevivente2 = models.ForeignKey(
        Sobrevivente,
        verbose_name="Sobrevivente2",
        related_name="sobrevivente2",
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.sobrevivente_trocar.nome


TROCAR_RECEBER = (
    ("1", "Trocar"),
    ("2", "Receber"),)


class TrocarReceber(models.Model):
    negociar = models.ForeignKey(
        Negociar,
        verbose_name="Negoicar",
        related_name="negociar",
        on_delete=models.CASCADE)
    itens = models.ManyToManyField(
        Itens,
        related_name="itens"
    )
    quantidade = models.IntegerField("Quantidade")
    item_troca = models.CharField("Item Troca",
                                  max_length=50,
                                  choices=TROCAR_RECEBER, default=1)

    def display_itens_nome(self):
        return ', '.join(itens.nome for itens in self.itens.all())
    display_itens_nome.short_description = 'Nome'
