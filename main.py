class UserAccount:
    def __init__(self, username):
        self.username = username
        self.__password = None   

    def set_password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Parol kamida 8 ta belgi bo'lishi kerak.")
        self.__password = new_password


    def _check_password(self, password):
        return self.__password == password


class AuthenticationSystem:
    @staticmethod
    def login(user_account, password):
        if user_account._check_password(password):
            return "Tizimga muvaffaqiyatli kirdingiz!"
        else:
            return "Parol noto‘g‘ri!"

user = UserAccount("ali")

user.set_password("superparol123")  

auth = AuthenticationSystem()

print(auth.login(user, "superparol123"))
print(auth.login(user, "xato123")) 
