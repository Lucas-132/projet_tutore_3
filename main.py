from logSystem import *

if __name__ == "__main__":
    try:
        network = LogSystem("config.json")
        network.log()
        network.launchView()
        network.launchDatabase()
        
    except Exception as e:
        print("\t", str(e))