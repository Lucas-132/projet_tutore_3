class Server:
    def __init__ (self, name:str, price:int= 5000):
        self.name = name
        self.price = price
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
            sum += machine.price
        return sum + self.price
    
    def __str__(self):
        clients_lists = ""
        for client in self.client:
            clients_lists += client.name + ", "
        return f"Server name : {self.name}\nServer price :{self.price}\nClients connected to server : {clients_lists}"
    
class Client(Server):
    
    def __init__(self, name : str, price:int=1000):
        super().__init__(name, price)
        self.name = name
        self.price = price

    def __str__(self):
        return f"PC name : {self.name}, PC price :{self.price}"
        
class Network:
    
    def __init__(self):
        self.port_input = [0 for x in range(3)]
        self.port_output = [0 for x in range(16)]

    
    def add_server(self, other: Server):
        # Inputs
        for port in range(len(self.port_input)) :
            if self.port_input[port] == 0:
                self.port_input[port] = other
                break
        # Outputs
        for client in range (len(other.client)):
            for port in range(len(self.port_output)) :
                if self.port_output[port] == 0:
                    self.port_output[port] = other.client[client]
                    break
                
    
    def delete_server(self, other:Server):
        # Inputs
        for port in range(len(self.port_input)) :
            if self.port_input[port] == other:
                self.port_input[port] = 0
                break
        # Outputs
        for client in other.client:
            for port in range(len(self.port_output)) :
                if self.port_output[port] == client:
                    self.port_output[port] = 0
                    break
                
    def global_cost(self):
        sum = 0
        for server in self.port_input:
            sum += server.price
        return sum