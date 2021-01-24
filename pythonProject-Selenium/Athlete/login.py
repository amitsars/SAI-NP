
class login:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = login()
        return cls.instance

    def __init__(self):
        pass

    def valid_user_login(self):
        print("valid user login function called.")

    def invalid_user_login(self):
        print("invalid user login function called.")


login = login.get_instance()