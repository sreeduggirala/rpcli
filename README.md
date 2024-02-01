# rpcli

rpcli is an open-source CLI that fetches EVM-compatible RPC URLs from [ChainList](https://chainlist.org)

This code is free and publicly available under the Apache 2.0 open-source license!

## Installation

We recommend installing rpcli in a virtual environment from PyPi.

[PyPi](https://pypi.org/project/rpcli) -- NOT YET ACTIVE

`pip install rpcli` -- NOT YET ACTIVE

## Features

`rpcli fetch-rpc --chain-name <chain-name>` outputs the specified chain's RPC URLs into a text file

`rpcli fetch-rpc --chain-id <chainID>` outputs the specified chain's RPC URLs into a text file

`rpcli id` outputs all EVM-compatible chains' IDs into a text file

## Features

- Fetches RPC URLs of EVM-compatible mainnets by name or chainID
- Presents EVM-compatible mainnet and testnet chainIDs

## Limitations

- ``rpcli fetch id`` currently has no filtration (outputs all supported chainIDs)
- No integration with Solidity development environments (i.e., Foundry, ApeWorX)
- No automatic RPC URL parsing based on latency
- Inefficient/clunky name-based fetching
- Non-EVM RPC URLs unavailable

## Extension

In the near future, we plan to support non-EVM networks and automatic RPC URL parsing (based on latency and maximum height of chain).

Furthermore, we plan to establish an ApeWorX plugin for our beloved Solidity + Python devs.

Any contributions on these issues are greatly appreciated!

## Contributing

rpcli is a tool for devs by devs. We welcome any contributions: improvement suggestions, bug reports, and code enhancements.

Please report bugs and request features by opening GitHub issues.

You may contribute to the project via forking/cloning the repository and submitting a pull request with your changes.

## Credits

[Aditya Rai](https://github.com/adityarai10101), [Sree Duggirala](https://github.com/sreeduggirala)
