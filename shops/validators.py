from django.core.exceptions import ValidationError

def validate_phone_number(value):
	if len(value) != 10:
		raise ValidationError("Please check the entered phone number")
