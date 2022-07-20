from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


def remove_user_token(user):
    # Remove old token
    Token.objects.filter(user=user).delete()


def get_user_token(user):

    try:
        Token.objects.get(user=user)
        remove_user_token(user)
        token = Token.objects.create(user=user)

    except ObjectDoesNotExist:
        token = Token.objects.create(user=user)

    return token.key
