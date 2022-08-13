from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import Sinalizar


@receiver(post_save, sender=Sinalizar)
def sobrevivente_infectado(sender, instance, **kwargs):
    if(Sinalizar.objects.filter(
            sobrevivente_infectado=instance.sobrevivente_infectado
    ).count() >= 3):
        instance.sobrevivente_infectado.infectado = True
        instance.sobrevivente_infectado.save()
