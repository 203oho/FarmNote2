import random
import string
from app.models import SessionModel

def get_a_session_token():
    """
    Generate a session token.
    """
    characters = string.ascii_letters + string.digits
    valid_token = ''.join(random.choice(characters)for _ in range(6))

    return valid_token