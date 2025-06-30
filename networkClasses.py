class Server:
    def __init__ (self, nom:str, prix:int= 5000):
        self.nom = nom
        self.prix = prix
        self.client : list[object] = []
        
    def bind(self, others : list[object]):
        for machine in others:
            self.client.append(machine)
    
    def unbind(self, others : list[object]):
        for machine in others:
            self.client.remove(machine)

    def global_server_cost(self) -> int:
        sum = 0
        for machine in self.client:
            sum += machine.prix
        return sum + self.prix
    
    def __str__(self):
        clients_lists = ""
        for client in self.client:
            clients_lists += client.nom + ", "
        return f"Nom du server : {self.nom}\nPrix du serveur :{self.prix}\nClients connecté au serveur : {clients_lists}"
    
class Client(Server):
    
    def __init__(self, nom : str, prix:int=1000):
        super().__init__(nom, prix)
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Nom du PC : {self.nom}, Prix du PC :{self.prix}"
        
class Network:
    
    def __init__(self):
        self.port_entree = [0 for x in range(3)]
        self.port_sortie = [0 for x in range(16)]

    
    def add_server(self, other: Server):
        # Entrées
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == 0:
                self.port_entree[port] = other
                break
        # Sorties
        for client in range (len(other.client)):
            for port in range(len(self.port_sortie)) :
                if self.port_sortie[port] == 0:
                    self.port_sortie[port] = other.client[client]
                    break
                
    
    def delete_server(self, other:Server):
        # Entrées
        for port in range(len(self.port_entree)) :
            if self.port_entree[port] == other:
                self.port_entree[port] = 0
                break
        # Sorties
        for client in other.client:
            for port in range(len(self.port_sortie)) :
                if self.port_sortie[port] == client:
                    self.port_sortie[port] = 0
                    break
                
    def global_cost(self):
        sum = 0
        for server in self.port_entree:
            sum += server.prix
        return sum