from programs import logSystem

if __name__ == "__main__":
    try:
        network = logSystem.LogSystem("config.json")
        network.log()
        network.launchView()
        network.launchDatabase()
        
    except Exception as e:
        print("\t", str(e))