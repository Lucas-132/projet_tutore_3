from logSystem import *

if __name__ == "__main__":
    try:
        network = LogSystem("config.json")
        network.log()
        network.launch()
        network.database("database.db")
        
    except Exception as e:
        print("\t", str(e))