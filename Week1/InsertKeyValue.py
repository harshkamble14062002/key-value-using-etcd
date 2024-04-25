import etcd3

def insert_to_etcd():
    etcd = etcd3.client(host='127.0.0.1', port=2379)
    
    while True:
        key = input("Enter key (or 'exit' to stop): ")
        if key.lower() == 'exit':
            break
        
        value = input("Enter value: ")
        etcd.put(key, value)
        print(f"Inserted: {key} => {value}")

if __name__ == "__main__":
    insert_to_etcd()
