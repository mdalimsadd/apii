import fetch from "node-fetch";

export default async function handler(req, res) {
  try {
    // Get current date (UTC)
    const now = new Date();
    const yyyy = now.getUTCFullYear();
    const mm = String(now.getUTCMonth() + 1).padStart(2, "0");
    const dd = String(now.getUTCDate()).padStart(2, "0");
    const today = `${yyyy}-${mm}-${dd}`;

    const fdate1 = `${today} 00:00:00`;
    const fdate2 = `${today} 23:59:59`;

    const url = new URL("http://109.236.84.81/ints/agent/res/data_smscdr.php");
    const params = {
      fdate1,
      fdate2,
      frange: "",
      fclient: "",
      fnum: "",
      fcli: "",
      fgdate: "",
      fgmonth: "",
      fgrange: "",
      fgclient: "",
      fgnumber: "",
      fgcli: "",
      fg: "0",
      sEcho: "1",
      iColumns: "9",
      sColumns: ",,,,,,,,",
      iDisplayStart: "0",
      iDisplayLength: "25",
      mDataProp_0: "0",
      bSortable_0: "true",
      mDataProp_1: "1",
      bSortable_1: "true",
      mDataProp_2: "2",
      bSortable_2: "true",
      mDataProp_3: "3",
      bSortable_3: "true",
      mDataProp_4: "4",
      bSortable_4: "true",
      mDataProp_5: "5",
      bSortable_5: "true",
      mDataProp_6: "6",
      bSortable_6: "true",
      mDataProp_7: "7",
      bSortable_7: "true",
      mDataProp_8: "8",
      bSortable_8: "false",
      iSortCol_0: "0",
      sSortDir_0: "desc",
      iSortingCols: "1",
    };
    Object.entries(params).forEach(([key, val]) => url.searchParams.append(key, val));

    const headers = {
      "Accept": "application/json, text/javascript, */*; q=0.01",
      "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) Chrome/141.0.0.0 Mobile Safari/537.36",
      "X-Requested-With": "XMLHttpRequest",
      "Referer": "http://109.236.84.81/ints/agent/SMSCDRReports",
    };

    const response = await fetch(url, { headers });
    const data = await response.text();

    res.status(200).json({
      date_used: today,
      status: response.status,
      request_url: url.toString(),
      data,
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
