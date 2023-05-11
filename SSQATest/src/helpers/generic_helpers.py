import random
import string
import logging as logger

def generate_random_email_and_password(domain=None, email_prefix=None):

    if not domain:
        domain = ("supersqa.com")
    if not email_prefix:
        email_prefix = ("testuser")

    email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase , k=email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain
    logger.info(f"Generated Random Email is {email}")
    return email

    # password_length = 20
    # random_password = ''.join(random.choices(string.ascii_letters, k=password_length))
    #
    # logger.info(f"Generated Random Password is{random_password}")

    # random_info = {"email" : email , "password" : random_password }
    # return random_info