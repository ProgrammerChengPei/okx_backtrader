from typing import Optional, Union
import json5
import yaml
import logging.config

import json
import asyncio
from okx.websocket.WsPrivateAsync import WsPrivateAsync

from dataclasses import dataclass


with open("./cfg/logging.yaml", "r", encoding="utf-8") as y:
    cfg = yaml.safe_load(y)
    logging.config.dictConfig(cfg)


class Subscriber(object):
    # class Request(object):
    #     def __init__(
    #         self,
    #         name: str,
    #         instType: Optional[Union[str, InstType]] = None,
    #         uly: Optional[str] = None,
    #         instId: Optional[str] = None,
    #     ) -> None:
    #         self.name = name
    #         self.instType = enum_to_str(instType)
    #         self.uly = uly
    #         self.instId = instId

    #     def to_dict(self) -> Dict[str, str]:
    #         ret = {
    #             "channel": self.name,
    #         }
    #         if self.instType is not None:
    #             ret["instType"] = self.instType
    #         if self.uly is not None:
    #             ret["uly"] = self.uly
    #         if self.instId is not None:
    #             ret["instId"] = self.instId
    #         return ret

    # class Response(object):
    #     pass

    #     def from_dict(self):
    #         pass

    def on_response(self):
        pass


def on_subscribe():
    """
    ex.
    {
        "event": "subscribe",
        "arg": {
            "channel": "positions",
            "instType": "FUTURES",
            "instFamily": "BTC-USD",
            "instId": "BTC-USD-200329"
        },
        "connId": "a4d3ae55"
    }
    """
    # for k, v in j.items():
    #     if k
    pass


def privateCallback(message):
    # print("privateCallback", message)
    j = json.loads(message)
    print(type(msg))
    # for k, v in j.items():
    #     if k
    print(msg)


async def main():
    # url error: APIKey does not match current environment.
    # url should be without '?brokerId=9999'
    # url = "wss://ws.okx.com:8443/ws/v5/business?brokerId=9999"

    with open("./cfg/okx.json", "r", encoding="utf-8") as j:
        cfg = json5.load(j)

    ws = WsPrivateAsync(
        # apiKey="your apiKey",
        # passphrase="your passphrase",
        # secretKey="your secretKey",
        url=cfg["url"]["模拟盘"]["WebSocket私有频道"],
        useServerTime=False,
        **cfg["login"]["sim"]
    )
    await ws.start()  # connect, then consume by None function
    print(
        "-----------------------------------------subscribe--------------------------------------------"
    )
    args = []
    arg1 = {"channel": "account", "ccy": "BTC"}
    arg2 = {"channel": "orders", "instType": "ANY"}
    arg3 = {"channel": "balance_and_position"}
    args.append(arg1)
    args.append(arg2)
    args.append(arg3)

    # callback is used for websocket, not only for subscript
    await ws.subscribe(args, callback=privateCallback)
    await asyncio.sleep(0.3)
    print(
        "-----------------------------------------unsubscribe--------------------------------------------"
    )
    args2 = [arg2]
    await ws.unsubscribe(args2, callback=privateCallback)
    await asyncio.sleep(0.3)
    print(
        "-----------------------------------------unsubscribe all--------------------------------------------"
    )
    args3 = [arg1, arg3]
    await ws.unsubscribe(args3, callback=privateCallback)


if __name__ == "__main__":
    asyncio.run(main())
