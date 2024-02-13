from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def get_transaction_history(bitcoin_address):
    rpc_user = 'your_rpc_username'  # Bitcoin node RPC username
    rpc_password = 'your_rpc_password'  # Bitcoin node RPC password
    rpc_port = 8332  # Bitcoin node RPC port

    # Establishing connection to Bitcoin node RPC
    rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}")

    # Retrieving transaction history for the Bitcoin address
    try:
        transactions = rpc_connection.listtransactions("*", 1000)
        for tx in transactions:
            if tx['address'] == bitcoin_address:
                print("Transaction ID:", tx['txid'])
                print("Amount:", tx['amount'])
                print("Confirmations:", tx['confirmations'])
                print("---------------------------------")
    except JSONRPCException as e:
        print(f"Error: {e}")

# Getting Bitcoin address from the user
bitcoin_address = input("Please enter your Bitcoin address: ")

# Displaying transaction history
get_transaction_history(bitcoin_address)
