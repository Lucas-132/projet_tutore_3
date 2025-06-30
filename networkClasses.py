class Server:
    def __init__ (self, nom:str, prix:int= 5000):
        self.nom = nom
        self.prix = prix
        self.client : list[object] = []
        
    def bind(self, other : object):
        self.client.append(other.nom)
    
    def unbind(self, other : object):
        self.client.remove(other.nom)
    
    def __str__(self):
        return f"Nom du server : {self.nom}\nPrix du serveur :{self.prix}\nClient connecté au serveur :{self.client.nom}\n "
    
class Client(Server):
    
    def __init__(self, nom : str, prix:int=1000):
        super().__init__(nom, prix)
        self.nom = nom
        self.prix = prix
    
    def __str__(self):
        return f"Nom du PC : {self.nom}, Prix du PC :{self.prix}\n"
        
class Network:
    
    def __init__(self):
        self.port_entree = [0 for x in range(3)]
        self.port_sortie = [0 for x in range(16)]

    
    def add_server(self, other: object):
        # Entrées
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == 0:
                self.port_entree[port] = other.nom
                break
        # Sorties
        client = 1
        while client <= (len(other.client)):
            for port in range(len(self.port_sortie)) :
                if self.port_sortie[port] == 0:
                    self.port_sortie[port] = other.client[client-1]
                    client += 1
                    break
                
    
    def delete_server(self, other: object):
        # Entrées
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == other.nom:
                self.port_entree[port] = 0
                break
        # Sorties
        for client in other.client:
            for port in range(len(self.port_sortie)) :
                if self.port_sortie[port] == client:
                    self.port_sortie[port] = 0
                    break
                