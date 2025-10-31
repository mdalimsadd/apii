from http.server import BaseHTTPRequestHandler
import requests
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the current date (you can adjust timezone if needed)
        today = datetime.utcnow().strftime("%Y-%m-%d")
        start_time = f"{today} 00:00:00"
        end_time = f"{today} 23:59:59"

        # Target URL
        url = "http://109.236.84.81/ints/agent/res/data_smscdr.php"

        # Query parameters (auto updates daily)
        params = {
            "fdate1": start_time,
            "fdate2": end_time,
            "frange": "",
            "fclient": "",
            "fnum": "",
            "fcli": "",
            "fgdate": "",
            "fgmonth": "",
            "fgrange": "",
            "fgclient": "",
            "fgnumber": "",
            "fgcli": "",
            "fg": "0",
            "sEcho": "1",
            "iColumns": "9",
            "sColumns": ",,,,,,,,",
            "iDisplayStart": "0",
            "iDisplayLength": "25",
            "mDataProp_0": "0",
            "bSortable_0": "true",
            "mDataProp_1": "1",
            "bSortable_1": "true",
            "mDataProp_2": "2",
            "bSortable_2": "true",
            "mDataProp_3": "3",
            "bSortable_3": "true",
            "mDataProp_4": "4",
            "bSortable_4": "true",
            "mDataProp_5": "5",
            "bSortable_5": "true",
            "mDataProp_6": "6",
            "bSortable_6": "true",
            "mDataProp_7": "7",
            "bSortable_7": "true",
            "mDataProp_8": "8",
            "bSortable_8": "false",
            "iSortCol_0": "0",
            "sSortDir_0": "desc",
            "iSortingCols": "1",
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://109.236.84.81/ints/agent/SMSCDRReports",
        }

        try:
            # Perform request
            res = requests.get(url, params=params, headers=headers, timeout=15)

            # Return success
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            result = {
                "date_used": today,
                "status": res.status_code,
                "request_url": res.url,
                "data": res.text,
            }

            self.wfile.write(json.dumps(result, indent=2).encode())

        except Exception as e:
            # Return error
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_msg = {"error": str(e)}
            self.wfile.write(json.dumps(error_msg).encode())
