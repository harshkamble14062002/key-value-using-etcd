import etcd3

def insert_to_etcd():
    etcd = etcd3.client(host='127.0.0.1', port=2379)
    
    while True:
        try:
            key = input("Enter key (or 'exit' to stop): ")
            if key.lower() == 'exit':
                break
            
            value = input("Enter value: ")
            etcd.put(key, value)
            print(f"Inserted: {key} => {value}")
        except Exception as e:
            print(f"An error occurred: {e}")

if _name_ == "_main_":
    insert_to_etcd()
