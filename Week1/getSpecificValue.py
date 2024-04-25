import etcd3

def get_value_for_key(client, key):
    value = client.get(key)  # Get the value of the specified key
    
    return value[0].decode() # returning value

def main():
    client = etcd3.client(host = "localhost" , port = 2379) # Connect to etcd server
  
    key = input("Enter the key: ") #specific key from user

    value = get_value_for_key(client, key) # Get value for the specified key

    print(f"The value of key '{key}' is: {value}") # Print the value of the key

if __name__ == "__main__":
    main()
