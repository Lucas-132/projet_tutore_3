class Server:
    def __init__ (self, nom:str, prix:int= 5000):
        self.nom = nom
        self.prix = prix
        self.client : object = None
        
    def bind(self, other : object):
        self.client = other
    
    def unbind(self):
        self.client = None
    
    def __str__(self):
        return f"Nom du server : {self.nom}\n Prix du serveur :{self.prix}\n Client connecté au serveur :{self.client}\n "
    
class Client(Server):
    
    def __init__(self, nom : str, prix:int=1000):
        super().__init__(nom, prix)
        self.nom = nom
        self.prix = prix
        
class Network:
    
    def __init__(self):
        pass
    
    def add_server(self, other: object):
        pass
    
    def delete_server(self, other: object):
        pass
    