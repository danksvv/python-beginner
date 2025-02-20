import time 

def connect() -> None:
    print("Connecting to the database...")
    time.sleep(2)
    print("Connected!")

    # This is a dummy function that simulates a connection to a database.
    # this if __name__ == "__main__": block is used to test the function 
if __name__ == "__main__":
    connect()
