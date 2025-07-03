import json
from programs.networkSystem import *
from programs.networkView import *
from networkDB import create_database
import os


class LogSystem:
  def __init__(self, configjson: str):
    self.configjson = configjson
  
  def log(self):
    # Chargement du JSON
    with open(self.configjson, "r") as f:
        config = json.load(f)
    # Création du réseau
    global network
    network = Network(config["name"])

    for server_data in config["servers"]:
        server = Server(server_data["name"], server_data.get("cost", 0))
        
        # Ajout de l'imprimante
        p = server_data.get("printer")
        if p:
            printer = Printer(p["name"], p["ip"], p["cost"])
            server.bind([printer])
        
        # Ajout des clients
        for c in server_data.get("clients", []):
            client = Client(c["name"], c.get("cost", 0))
            server.bind([client])
        
        network.add_server(server)
    
  def launchView(self):
    view = networkView([network])
    print(view)
    view.graph()

  def launchDatabase(self, file_name = "NetworkDB.db"):
    if os.path.exists(file_name):
      os.remove(file_name)
    create_database(network)