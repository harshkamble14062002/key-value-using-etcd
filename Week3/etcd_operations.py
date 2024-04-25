import etcd3
# Connect to etcd
etcd = etcd3.client(host='localhost', port=2379)

# Function to list all keys
def list_keys():
    return list(etcd.get_all())

def get_keys_and_values():
    # Use get_all() to retrieve all key-value pairs
	response_iter = etcd.get_all()+++
    # Extract key and value from response objects
	all_values = [("Key", "Value")]  # Initialize with headers
	for k, v in response_iter:
		# Decode key
		key = k.decode('utf-8')
		# Check for the presence of 'value' attribute
		if hasattr(v, 'value'):
			value = v.value.decode('utf-8')
		else:
			# Access value from key for newer versions
			value = v.key.decode('utf-8')
		all_values.append((value, key))

	return all_values

# Function to get the value for a specific key
def get_value(key):
    try:
        value, _ = etcd.get(key)
        if value is not None:
            return value.decode()  # Decode bytes to string
        else:
            return None  # Return None if key not found
    except Exception as e:
        return f"Error: {str(e)}"

# Function to delete a key-value pair from etcd
def delete_key(key):
    try:
        etcd.delete(key)
        return "Key deleted successfully."
    except etcd3.exceptions.KeyNotFoundError:
        return "Key not found"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to put a key-value pair into etcd
def put_key_value(key, value):
    try:
        etcd.put(key, value)
        return "Key-value pair added successfully."
    except Exception as e:
        return f"Error: {str(e)}"


'''
user interface in terminal
# Function to display options
def display_options():
    print("Options:")
    print("1. Get value for a key")
    print("2. Put key-value pair")
    print("3. Delete key-value pair")
    print("4. List all keys")
    print("5. Exit")

# Function to handle option 1: Get value for a key
def option_get_value():
    print("---------------------------------------")
    key = input("Enter the key: ")
    value = get_value(key)
    if value is not None:
        print("Value for key", key, ":", value)
    else:
        print("Key not found")
    print("---------------------------------------")

# Function to handle option 2: Put key-value pair
def option_put_key_value():
    print("---------------------------------------")
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    print(put_key_value(key, value))
    print("---------------------------------------")

# Function to handle option 3: Delete key-value pair
def option_delete_key():
    print("---------------------------------------")
    key = input("Enter the key to delete: ")
    print(delete_key(key))
    print("---------------------------------------")

# Function to handle option 4: List all keys
def option_list_keys():
    print("---------------------------------------")
    print("Listing all keys:")
    keys = list_keys()
    for key, _ in keys:
        print(key.decode())
    print("---------------------------------------")

# Function to handle option 5: Exit
def option_exit():
    print("---------------------------------------")
    print("Exiting...")
    global exit_flag
    exit_flag = True
    print("---------------------------------------")

# Dictionary mapping options to their respective functions
options = {
    '1': option_get_value,
    '2': option_put_key_value,
    '3': option_delete_key,
    '4': option_list_keys,
    '5': option_exit
}

# Main function
def main():
    global exit_flag
    exit_flag = False
    while not exit_flag:
        display_options()
        choice = input("Enter your choice: ")
        if choice in options:
            options[choice]()  # Call the corresponding function for the chosen option
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
'''
