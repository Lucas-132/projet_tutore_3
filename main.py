from networkSystem import *
from networkView import *
from networkDB import create_database
import os
import json
from logSystem import *

if __name__ == "__main__":
    try:
        network = LogSystem("config.json")
        network.log()
        network.launch()

        """db_path = "NetworkDB1.db"
        if os.path.exists(db_path):
            os.remove(db_path)
        create_database(network)"""
        
    except Exception as e:
        print("\t", str(e))