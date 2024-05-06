import requests

url = "https://live.euronext.com/pd_es/data/stocks/download?mics=XOSL%2CMERK%2CXOAS"
url2 = "https://live.euronext.com/en/pd_es/data/stocks?mics=XOSL%2CMERK%2CXOAS"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}
body=b"iDisplayLength=100&iDisplayStart=0&args%5BinitialLetter%5D=&args%5Bfe_type%5D=csv&args%5Bfe_decimal_separator%5D=.&args%5Bfe_date_format%5D=d%2Fm%2FY"
data = requests.post(url, headers=headers, data=body)

body2={
    "iDisplaylength":100,
    "iDisplayStart":0,
    "args[initialLetter]":"",
    "args[fe_type]":"csv",
    "args[fe_decimal_separator]":".",
    "args[fe_date_format]": "d/m/Y",
}

req = requests.Request(
    method="post",
    url=url,
    data=body,
    # cookies={"Cookie:", "visid_incap_2784297=qdClnIiQT9C+077gnv+JS5Y2tmUAAAAAQUIPAAAAAACeEE/P7tnBiv5KuWCR9Gr8; incap_ses_723_2784297=4KwmZe92u1wnLlC7150ICpY2tmUAAAAAUbgpblHN1vmyBDU4pjnYhw==; OptanonAlertBoxClosed=2024-01-28T11:13:17.716Z; eupubconsent-v2=CP5F21gP5F21gAcABBENAlEgAAAAAAAAAChQAAAAAAAA.YAAAAAAAAAAA; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jan+28+2024+12%3A13%3A17+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=H59%3A0%2CH2%3A0%2CH4%3A0%2CH54%3A0&consentId=3e9d7858-03e2-4b37-9956-b3b8070d3bed&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A0%2CC0003%3A0%2CC0001%3A1%2CC0004%3A0%2CV2STACK42%3A0&genVendors=V4%3A0%2CV19%3A0%2CV24%3A0%2CV10%3A0%2CV21%3A0%2CV3%3A0%2CV2%3A0%2CV20%3A0%2C"}
)

resp = requests.post(
    url=url,
    data=body,
)

resp.content

req_prep = req.prepare()


resp = requests.get("https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&published=1&vertical=realestate")
resp.json()