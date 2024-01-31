import typer
import json

allChains = json.load(open("./chains.json"))
# for i in allChains["chains"]:
#     print(i)

app = typer.Typer()


# @notice: Fetches RPC URLs for the specified chain
# @params: Chain name
@app.command()
def get_url_name(name: str):
    for i in allChains["chains"]:
        if allChains["chains"][i]["name"] == name:
            returnVal = [entry["url"] for entry in allChains["chains"][i]["rpc"]]
            print(returnVal)
            return returnVal
    print("chain not found")
    raise Exception("Chain not found")

    


# @notice: Fetches RPC URLs for the specified chain
# @params: Chain ID
@app.command()
def get_url_id(id: int):
    for i in allChains["chains"]:
        if allChains["chains"][i]["chainId"] == id:
            # print(allChains["chains"][i]["rpc"])
            returnVal = [entry["url"] for entry in allChains["chains"][i]["rpc"]]
            print(returnVal)
            return returnVal
    print("chain not found")
    raise "Chain not found"

# @notice: Outputs chain IDs for all EVM-compatible mainnets and testnets
@app.command()
def id():
    complete = {"Chain Name": "Chain ID"}
    for i in allChains["chains"]:
        complete[allChains["chains"][i]["name"]] = allChains["chains"][i]["chainId"]
    print(json.dumps(complete, indent=2))
    return complete


if __name__ == "__main__":
    app()
