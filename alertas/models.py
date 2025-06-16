from django.db import models


class Temperatura(models.Model):
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.valor}°C em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"


class Alerta(models.Model):
    temperatura = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Alerta {self.temperatura}°C em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"


class LogAlerta(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)  # Ex: "Máxima", "Mínima"
    temperatura = models.FloatField()
    mensagem = models.TextField()

    def __str__(self):
        return f"[{self.data.strftime('%d/%m/%Y %H:%M:%S')}] {self.tipo}: {self.temperatura}°C"
