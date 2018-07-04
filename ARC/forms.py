from django import forms
from .models import Inventory

class InventoryForm(forms.Form):
	
	class Meta:
		itemname = forms.CharField()
		description = forms.CharField()
		item_type = forms.CharField()
		quantity = forms.IntegerField()
		uid = forms.IntegerField()
		
class LaboratoryForm(forms.Form):
	
	class Meta:
		labname = forms.CharField()
		roomnum = forms.CharField()
		cap = forms.IntegerField()
		
class TermForm(forms.Form):
	
	class Meta:
		termname = forms.CharField()
		startdate = forms.DateField()
		enddate = forms.DateField()