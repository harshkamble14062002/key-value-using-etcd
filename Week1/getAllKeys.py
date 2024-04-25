import etcd3

def get_all_keys():
    # Connect to etcd server
    etcd = etcd3.client()

    # Fetch all keys
    keys = etcd.get_all()

    # Extract keys only
    key_list = [key.decode('utf-8') for key, _ in keys]

    # Print all keys
    for key in key_list:
        print(f"Key: {key}")

if __name__ == "__main__":
    get_all_keys()

