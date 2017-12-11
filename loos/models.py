from django.db import models


class Prize(models.Model):
    prize_text = models.TextField()
    prize_description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.prize_text


class Ticket(models.Model):
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)

    @property
    def ticket_num(self):
        return self.id

    def __str__(self):
        return f"Loos nr {self.id}, auhind {self.prize.prize_text}"
