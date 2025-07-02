from networkSystem import *
from networkView import *
from networkDB import create_database
import os
import json

if __name__ == "__main__":
    try:
        # Chargement du JSON
        with open("config.json", "r") as f:
            config = json.load(f)

        # Création du réseau
        network1 = Network(config["name"])

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
            
            network1.add_server(server)

        db_path = "NetworkDB1.db"
        if os.path.exists(db_path):
            os.remove(db_path)
        create_database(network1)
        
        view = networkView([network1])
        print(view)
        view.graph()
        
    except Exception as e:
        print("\t", str(e))