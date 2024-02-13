# BTCagent

# Bitcoin Transaction History Viewer

This Python script allows you to view the transaction history associated with a specific Bitcoin address. It connects to a Bitcoin node via RPC and retrieves transaction details.

## Prerequisites

- Python 3
- Bitcoin Core running with RPC enabled

## Installation

1. Clone this repository:


git clone https://github.com/sacriphanius/BTCagent.git


2. Install dependencies:

pip install -r requirements.txt


## Usage

1. Make sure Bitcoin Core is running with RPC enabled.

2. Run the script:

python3 BTCagent.py

3. Enter the Bitcoin address when prompted.

4. View the transaction history associated with the provided Bitcoin address.



How can you connect to a BTC node?


1. **Downloading and Installing Bitcoin Core**: Bitcoin Core is the original and official implementation of the Bitcoin network. Firstly, download Bitcoin Core from the official website and install it on your computer. Download and installation instructions are available for most operating systems.

2. **Starting and Synchronizing Bitcoin Core**: Launch Bitcoin Core, and initially synchronizing the blockchain may take some time. This process involves downloading and verifying all blocks.

3. **Setting up RPC Connection Parameters**: Bitcoin Core allows interaction with other programs via RPC (Remote Procedure Call). This requires setting up RPC connection parameters and credentials in the Bitcoin Core configuration file, `bitcoin.conf`, or directly through the Bitcoin Core console.

4. **Connecting to the Bitcoin Core Console**: You can interact with the Bitcoin Core console by opening the Bitcoin Core application and accessing the console, or by connecting via RPC through another program.

5. **Installing Python and the bitcoinrpc Library**: To interact with Bitcoin Core, you can use the `bitcoinrpc` library for Python. Install this library using the command `pip install python-bitcoinrpc`.

6. **Interacting with Bitcoin Core Using Python Scripts**: Now you can connect to Bitcoin Core and perform various operations using Python scripts. This could include querying transaction histories for Bitcoin addresses, creating new transactions, or executing other Bitcoin network functions.

By following these steps, you can connect to a Bitcoin node and interact with Bitcoin Core. However, before using Bitcoin Core, ensure that your system has sufficient storage space and an internet connection. Additionally, remember to take security measures and keep your private credentials secure.
