import requests

DEFAULT_EDGAR_METRIC = [
    "AccountsReceivableNetCurrent",
    "Assets",
    "AssetsCurrent",
    "CashAndCashEquivalentsAtCarryingValue",
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect",
    "CostOfRevenue",
    "IncomeTaxExpenseBenefit",
    "InterestExpense",
    "InventoryNet",
    "Liabilities",
    "LiabilitiesCurrent",
    "LongTermDebtNoncurrent",
    "NetCashProvidedByUsedInFinancingActivities",
    "NetCashProvidedByUsedInOperatingActivities",
    "OperatingExpenses",
    "PrepaidExpenseAndOtherAssetsCurrent",
    "PurchasesOfPropertyAndEquipmentAndIntangibleAsset",
    "Revenues",
    "StockholdersEquity"
]

def get_cik(string):
    matches = []
    with open("cik-lookup-data.txt", 'r') as file:
        for line in file:
            if string.lower() in line.strip().lower():             
                name = ' '.join(line.split(' ')[:-1])
                code = line.split(' ')[-1].split(':')[-2]               
                matches.append({name: code})
    return matches


# 0001045810 <-- nvidia

def get_edgar(CIK, metrics, start, end, form):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept-Encoding": "gzip, deflate",
        "Host": "data.sec.gov"
    }

    response = requests.get(
        url=url,
        headers=headers
    )
    
    facts = {}
    if response.status_code == 200:
        data = response.json()
        for metric, metric_data in data["facts"]["us-gaap"].items():
            if not(metric in metrics):
                continue
            facts[metric] = {
                "label": metric_data["label"],
                "description": metric_data["description"],
                "values": {}
            }
            for unit, entry_data in metric_data["units"].items():
                for entry in entry_data:
                    if entry["form"] == str(form) and int(entry["fy"]) >= int(start) and int(entry["fy"]) <= int(end):
                        # year = entry["fy"]
                        # attrs = {
                        #     "fp": entry["fp"],
                        #     "val": entry["val"],
                        # }
                        # if year not in facts[metric]["values"]:
                        #     facts[metric]["values"][year] = []
                        # facts[metric]["values"][year].append(attrs)
                        year = entry["fy"]
                        if year not in facts[metric]["values"]:
                            facts[metric]["values"][year] = {}
                        facts[metric]["values"][year][entry["fp"]] = entry["val"]
        return(
            {"content": facts, 
             "status_code": 200}
        )
    else:
        return(
            {"content": "Error", 
            "status_code": response.status_code}
        )