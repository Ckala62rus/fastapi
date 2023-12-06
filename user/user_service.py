from passlib.hash import pbkdf2_sha256


def make_hash_password(password: str) -> str:
    """
    Convert string to hash.
    Example:
        input: toomanysecrets
        output: $pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk

    :param password:
    :return: hash
    """
    return pbkdf2_sha256.hash(password)


def compare_hash_password(input_password: str, password_form_database: str) -> bool:
    """
    Compare input user password(hash) with passwordstore in database,
    and return True or False

    :param input_password:
    :param password_form_database:
    :return:
    """
    return pbkdf2_sha256.verify(input_password, password_form_database)
