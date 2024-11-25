from django.core.exceptions import ValidationError

class SpecialCharacterValidator:
    """
    Validador que asegura que las contraseñas contengan al menos un carácter especial.
    """
    def validate(self, password, user=None):
        if not any(char in "!@#$%^&*()_+" for char in password):
            raise ValidationError(
                "La contraseña debe contener al menos un carácter especial: !@#$%^&*()_+.",
                code='password_no_special',
            )

    def get_help_text(self):
        return "La contraseña debe contener al menos un carácter especial: !@#$%^&*()_+."
