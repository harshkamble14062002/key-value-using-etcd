import etcd3

client =   etcd3.client(host = 'localhost' , port = 2379)  # connecting to server

def get_all_KeyValue(): #creating a function to return all the key values in the etcd node
  for key , value in client.get_all(): 
    print(f"Key : {key.decode()} , Value : {value.decode()}") #printing all the Keys and Values

get_all_KeyValue() 
