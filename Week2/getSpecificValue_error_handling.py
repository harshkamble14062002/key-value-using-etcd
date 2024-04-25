import etcd3

def get_value_for_key(client, key):
    try:
        value = client.get(key)  # Get the value of the specified key
        if value:
            return value[0].decode() # returning value
        else:
            return None
    except Exception as e:
        print(f"Error occurred while getting value for key '{key}': {e}")
        return None

def main():
    try:
        client = etcd3.client(host="localhost", port=2379) # Connect to etcd server
        
        key = input("Enter the key: ") #specific key from user

        value = get_value_for_key(client, key) # Get value for the specified key

        if value is not None:
            print(f"The value of key '{key}' is: {value}") # Print the value of the key
        else:
            print(f"No value found for key '{key}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    main()
