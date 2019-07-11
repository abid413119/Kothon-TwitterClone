from django.core.exceptions import ValidationError

### Validation outside the model

def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Content can't be blank")
    return value