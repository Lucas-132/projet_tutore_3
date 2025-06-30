class Server:
    def __init__ (self, nom:str, prix:int= 5000):
        self.nom = nom
        self.prix = prix
        self.client : object = None
        
    def bind(self, other : object):
        self.client = other
    
    def unbind(self):
        self.client = None
    
<<<<<<< HEAD
=======
    def __str__(self):
        return f"Nom du server : {self.nom}\n Prix du serveur :{self.prix}\n Client connecté au serveur :{self.client}\n "
    
>>>>>>> develop
class Client(Server):
    
    def __init__(self, nom : str, prix:int=1000):
        super().__init__(nom, prix)
        self.nom = nom
        self.prix = prix
<<<<<<< HEAD
=======
    
    def __str__(self):
        return f"Nom du PC : {self.nom}\n Prix du PC :{self.prix}\n"
>>>>>>> develop
        
class Network:
    
    def __init__(self):
<<<<<<< HEAD
        pass
    
    def add_server(self, other: object):
        pass
    
    def delete_server(self, other: object):
        pass
=======
        self.port_entree = [0 for x in range(3)]
        self.port_sortie = [0 for x in range(16)]

    
    def add_server(self, other: object):
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == 0:
                self.port_entree.insert(port, other.nom)
    
    def delete_server(self, other: object):
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == other.nom:
                self.port_entree.insert(port, 0)
>>>>>>> develop
    