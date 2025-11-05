from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("TuyaControl")

@mcp.tool()
def turn_on(device_id: str):
    """Bật thiết bị Tuya"""
    url = f"https://openapi.tuyaus.com/v1.0/devices/{device_id}/commands"
    payload = {"commands": [{"code": "switch_1", "value": True}]}
    headers = {"Authorization": "Bearer <YOUR_TUYA_TOKEN>"}
    return requests.post(url, json=payload, headers=headers).json()

if __name__ == "__main__":
    mcp.run()
