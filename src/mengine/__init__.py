from  implementations import server_manager
from implementations import connectionmanager

def main():
    # Initialize and run your class
    con_mg = connectionmanager.ConnectionManager()
    instance = server_manager.ServerManager(con_mg)
    instance.start_up_conn()

# Check if the script is being run directly
if __name__ == "__main__":
    main()