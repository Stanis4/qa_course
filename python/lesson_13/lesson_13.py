"""Написати Singleton (на вибір за допомогою мета класу або декоратора) """


def singleton(cls):
    _instances = {}

    def instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return instance


@singleton
class Server:

    def __init__(self, name: str, pwd: str):
        self.server = f'{name}:{pwd}'


server1 = Server('username', 'pwd')
server2 = Server('username_2', 'pwd_2')

if server1 is server2:
    print("Server1 and server2 instances are the same")
else:
    print("Variables contain different instances.")
