from django.core.exceptions import ValidationError


COUNTRY = ['Brasil', 'Argentina', 'Peru']
def validate_country(value):
	cat = value.capitalize()
	if not value in COUNTRY and not cat in COUNTRY:
		raise ValidationError('Not a valid category')

