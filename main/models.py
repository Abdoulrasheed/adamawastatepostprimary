from django.db import models


class Applicant(models.Model):

	post = models.CharField(max_length=100)
	dept = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	dob = models.CharField(max_length=100)
	lga = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	nationality = models.CharField(max_length=100)
	lang = models.CharField(max_length=100)
	nok_address = models.CharField(max_length=100)
	nok_phone = models.CharField(max_length=100)
	mstatus = models.CharField(max_length=100)

	passport = models.ImageField(upload_to="passports/")
	sig = models.ImageField(upload_to="sigs/")

	class Meta:
		verbose_name = "Applicant"
		verbose_name_plural = "Applicants"


	def __str__(self):
		return self.name
