from networkSystem import *

class networkView:
  def __init__(self, networks: list[Network]):
    self.networks = networks

  def add_network(self, networks: list[Network]):
    self.networks.append(networks)
  
  def delete_network(self, networks : list[Network]):
    for network in networks:
            self.networks.remove(network)

  def __str__(self):
    message = ""
    for view in self.networks:
       message += f"{view}\n\n"
    return message
       