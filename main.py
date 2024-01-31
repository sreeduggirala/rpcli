import typer

# @notice: Fetches RPC URLs for the specified chain
# @params: Chain name
def url_by_name(name: str):
    print(name)


# @notice: Fetches RPC URLs for the specified chain
# @params: Chain ID
def url_by_id(id: int):
    print(id)


# @notice: Outputs chain IDs for all EVM-compatible mainnets and testnets
def all_ids():
    print("all ids")

url_by_id(1)
