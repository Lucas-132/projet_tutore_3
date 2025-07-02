from networkSystem import *
import matplotlib.pyplot as plt
import numpy as np

class networkView:
  def __init__(self, networks: list[Network]):
    self.networks = networks

  def add_network(self, networks: list[Network]):
    self.networks.append(networks)
  
  def delete_network(self, networks : list[Network]):
    for network in networks:
            self.networks.remove(network)

  def graph(self):
    for network_number in range(len(self.networks)):
      servers = []
      servers_prices = []
      colors = ['tab:red', 'tab:blue', 'tab:green']
      for server in self.networks[network_number].port_input:
        if server != 0:
            servers.append(server.name)
            servers_prices.append(server.price)
      plt.bar(servers,servers_prices,color=colors)
      plt.title(f"{self.networks[network_number].name} server prices")
      plt.xlabel('servers')
      plt.ylabel('prices')
      plt.show()

  def __str__(self):
    message = ""
    for view in self.networks:
       message += f"{view}\n\n"
    return message
       