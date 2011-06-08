from django.db import models
import datetime
# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_state = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question

	def was_published_today(self):
		return self.pub_state.date() == datetime.date.today()
	was_published_today.short_description = 'Published today?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()

	def __unicode__(self):
		return self.choice
