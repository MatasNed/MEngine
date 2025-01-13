from implementations import server_manager
from implementations import connectionmanager
from implementations import process_manager

def main():
    # Initialize and run your class
    proc_mg = process_manager.ConcreteProcessManager()
    con_mg = connectionmanager.ConnectionManager(proc_mg)
    instance = server_manager.ServerManager(con_mg)
    instance.start_up_conn()

# Check if the script is being run directly
if __name__ == "__main__":
    main()