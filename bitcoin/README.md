Bitcoin module
==============

The module needs to implement the following two functions:

- signrawtransaction(rawtx, txinputs, privatekeys)
- sendrawtransaction(rawtx)

We are experimenting with using bitcoinj, for SPV support, and we hope to soon add some tips and tricks here, but at the moment we are running with bitcoind.

The module runs it automatically on startup, with the configuration file setting the RPC user and password and making sure you are running on testnet (we do not want to accidentally run this with a mainnet wallet - it is not safe) and also implements the close function that shuts it down.

Protip: using [freewil](https://github.com/freewil)'s easy mining fork on an internal net can come very handy when testing.
