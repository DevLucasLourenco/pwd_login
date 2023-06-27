from getpass import getpass

class input_login():
    def __init__(self, database) -> None:
        self.database = database
        self.user = input('User:')
        self.pwd = self.pwd_run()
        
        if not (self.user in self.database) and (self.pwd in self.database):
            raise ValueError("Incoerência em assimilação de dados.")
        else:
            pass
    
    def pwd_run():
        return int(getpass(prompt='Password:'))
        
    
