from django.db import models

class baloon(models.Model):
	def __unicode__(self):
		return self.header
	header = models.CharField(max_length = 1023)
	text = models.TextField()
	footer = models.TextField()
	hint = models.TextField()
	coord1 = models.FloatField()
	coord2 = models.FloatField()
	
