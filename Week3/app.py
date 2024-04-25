import streamlit as st
import etcd_operations

# Title
st.title("etcd Operations")

# Sidebar menu
option = st.sidebar.selectbox("Select Operation", ["Get Value", "Put Key-Value Pair", "Delete Key-Value Pair", "List Values" , "List Keys and Values"])

# Function to get value for a key
def get_value():
    st.subheader("Get Value")
    key = st.text_input("Enter the key:")
    if st.button("Get Value"):
        value = etcd_operations.get_value(key)
        if value is not None:
            st.success(f"Value for key '{key}': {value}")
        else:
            st.error(f"Key '{key}' not found")

# Function to put key-value pair
def put_key_value():
    st.subheader("Put Key-Value Pair")
    key = st.text_input("Enter the key:")
    value = st.text_input("Enter the value:")
    if st.button("Put Key-Value Pair"):
        result = etcd_operations.put_key_value(key, value)
        st.success(result)

# Function to delete key-value pair
def delete_key():
    st.subheader("Delete Key-Value Pair")
    key = st.text_input("Enter the key to delete:")
    if st.button("Delete Key-Value Pair"):
        result = etcd_operations.delete_key(key)
        st.success(result)

# Function to list all keys
def list_keys():
    st.subheader("List Values")
    keys = etcd_operations.list_keys()
    if keys:
        st.write("Values in etcd:")
        for key, _ in keys:
            st.write(key.decode())
    else:
        st.info("No keys found in etcd.")
 
def list_key_value():
    st.subheader("List of Keys and Values")
    keys_and_values = etcd_operations.get_keys_and_values()
    if len(keys_and_values) > 1:  
        st.table(keys_and_values)
    else:
        st.info("No keys found in etcd.")

# Main function
def main():
    if option == "Get Value":
        get_value()
    elif option == "Put Key-Value Pair":
        put_key_value()
    elif option == "Delete Key-Value Pair":
        delete_key()
    elif option == "List Values":
        list_keys()
    elif option == "List Keys and Values":
    	list_key_value()

if __name__ == "__main__":
    main()
