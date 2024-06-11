from module1 import ServerManager
def main():
    # Initialize and run your class
    instance = ServerManager()
    instance.listen()

# Check if the script is being run directly
if __name__ == "__main__":
    main()