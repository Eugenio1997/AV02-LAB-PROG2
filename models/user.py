class User:
    def __init__(self, name: str, email: str, phone_number: str, password: str):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__password = password

    def to_dict(self):
        return dict(name=self.name, email=self.email, phone_number=self.phone_number, password=self.password)

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def password(self):
        return self.__password
