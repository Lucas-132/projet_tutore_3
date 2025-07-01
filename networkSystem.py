import random
import re

class Server:
    def __init__ (self, name:str, price:int= 5000):
        self.name = name
        self.price = price
        self.client : list[object] = []
        
    def bind(self, others : list[object]):
        for machine in others:
            self.client.append(machine)
            machine.binded_server = self
        
    
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
        self.binded_server = None

    def __str__(self):
        return f"PC name : {self.name}, PC price : {self.price}"
    
class Printer(Server):
    def __init__(self, ip:str, price = 1000):
        super().__init__(price)
        self.ip = ip
        self.price = price

    def __str__(self):
        return f"Printer IP : {self.ip}, Printer price : {self.price}"
        
class Network:
    
    def __init__(self, name:str):
        self.port_input = [0 for x in range(3)]
        self.port_output = [0 for x in range(16)]
        self.name = name

    
    def add_server(self, other: Server):
        # Inputs
        free_space_input = []
        for port in range(len(self.port_input)) :
            if self.port_input[port] == 0:
                free_space_input.append(port)
        self.port_input[random.choice(free_space_input)] = other
        
        # Outputs
        free_space_output = []
        temp_free_space_selected = 0
        for port in range(len(self.port_output)) :
            if self.port_output[port] == 0:
                free_space_output.append(port) 
        for client in range (len(other.client)):
            temp_free_space_selected = random.choice(free_space_output)
            self.port_output[temp_free_space_selected] = other.client[client]
            free_space_output.remove(temp_free_space_selected)
                
    
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
            if server != 0:
                sum += server.global_server_cost()
        return sum
    
    def __str__(self):
        # Initialising str message
        message = f"Network: {self.name}"

        # Counting the ammount of servers connected to this network
        for input_port_number in range (len(self.port_input)):
            if self.port_input[input_port_number] != 0:
                # Adding Input port infos to str message
                message += f"\n\t{self.port_input[input_port_number].name} Server Cost: {self.port_input[input_port_number].price} Port: {input_port_number + 1} Server global Cost: {self.port_input[input_port_number].global_server_cost()}"
                # Adding binded machines (clients) infos
                for client in self.port_input[input_port_number].client:
                    message += f"\n\t\t{client.name} {client.price}"
                    # Checking which output port the client is connected to and adding this port to str message
                    for output_port_number in range(len(self.port_output)):
                        if client == self.port_output[output_port_number]:
                            message += f" Port: {output_port_number + 1}"
        
        # Adding outputs ports recap to str message
        port_output_names = [] # (this array is used to display the distribution of the clients inside the network)
        for output_port_number in range(len(self.port_output)):
            if self.port_output[output_port_number] != 0:
                port_output_names.append(self.port_output[output_port_number].binded_server.name)
            else :
                port_output_names.append(0)
        message += f"\n\nPorts OUT: {port_output_names}"

        # Adding network global cost to str message
        message += f"\nNetwork Global Cost: {self.global_cost()}"
        return message
