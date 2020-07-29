from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def generate_verification_token(email):
    node=URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    result = node.dumps(email,salt=current_app.config['SECURITY_PASSWORD_SALT'])
    return result


def confirm_verification_token(token, expiration=21600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token,salt=current_app.config['SECURITY_PASSWORD_SALT'],max_age=expiration)
        return email
    except Exception as e :
        return e
