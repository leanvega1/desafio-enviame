import requests
import json

url = "https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries"

payload = json.dumps({
  "shipping_order": {
    "n_packages": 1,
    "content_description": "ORDEN 255826267",
    "imported_id": "255826267",
    "order_price": 24509.0,
    "weight": "0.98",
    "volume": "1.0",
    "type": "delivery"
  },
  "shipping_origin": {
    "warehouse_code": "401"
  },
  "shipping_destination": {
    "customer": {
      "name": "Bernardita Tapia Riquelme",
      "email": "b.tapia@outlook.com",
      "phone": "977623070"
    },
    "delivery_address": {
      "home_address": {
        "place": "Puente Alto",
        "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto",
        "information": ""
      }
    }
  },
  "carrier": {
    "carrier_code": "BLX",
    "tracking_number": ""
  }
})
headers = {
  'Accept': 'application/json',
  'api-key': 'ea670047974b650bbcba5dd759baf1ed',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

file = open("myOutFile.txt", "w")
file.write(response.text)
file.write("\n")
file.close()
