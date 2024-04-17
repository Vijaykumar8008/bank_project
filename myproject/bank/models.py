from django.db import models

# Create your models here.
class BankDetails(models.Model):
	id = models.AutoField(primary_key = True , help_text='ID')
	bank_nm = models.CharField(max_length=20,help_text = 'Bank Name')
	account_nm = models.CharField(max_length=20,help_text = 'Account Number')
	ifsc_code = models.CharField(max_length=20,help_text = 'IFSC Number')
	branch =models.CharField(max_length=20,help_text = 'Branch')

	class Meta:
		db_table = 'bank_details'