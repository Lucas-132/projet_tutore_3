class Server:
    def __init__ (self, nom:str, prix:int= 5000):
        self.nom = nom
        self.prix = prix
        
    def bind(self, other : object):
        pass
    
    def unbind(self, other : object):
        pass
    
class Client(Server):
    
    def __init__(self, nom : str, prix:int):
        super().__init__(nom, prix=1000)    
        
class Network:
    
    def __init__(self):
        pass
    
    def add_server(self, other: object):
        pass
    
    def delete_server(self, other: object):
        pass
    