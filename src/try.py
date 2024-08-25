import json5
import okx.Funding as Funding

with open("./cfg/okx.json", "r", encoding="utf-8") as j:
    cfg = json5.load(j)
    sim = cfg["login"]["sim"]

flag = "1"  # live trading: 0, demo trading: 1

fundingAPI = Funding.FundingAPI(
    api_key=sim["apiKey"],
    api_secret_key=sim["secretKey"],
    passphrase=sim["passphrase"],
    use_server_time=False,
    flag=flag,
)

result = fundingAPI.get_currencies()
print(result)
