from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int):
        return text_type(
            text_type(user.pk) + text_type(timestamp)
        )
        
generate_token = TokenGenerator()