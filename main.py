import typer


app = typer.Typer()


# @notice: Fetches RPC URLs for the specified chain
# @params: Chain name
@app.command()
def get_url_name(name: str):
    print(name)


# @notice: Fetches RPC URLs for the specified chain
# @params: Chain ID
@app.command()
def get_url_id(id: int):
    print(id)


# @notice: Outputs chain IDs for all EVM-compatible mainnets and testnets
@app.command()
def id():
    print("all ids")


if __name__ == "__main__":
    app()
