from collections import defaultdict
import requests
import json

'''
Access all information given CIK:
    https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
    
Access specific metric of a given company given its CIK and name of the metric
    https://data.sec.gov/api/xbrl/companyconcept/CIK##########./us-gaap/<NAME>.json
    
Access specific metric in a given period in all companies
    https://data.sec.gov/api/xbrl/frames/us-gaap/<NAME>/USD/CY####.json
    
    The period format is:
    - CY#### for annual data (duration 365 days +/- 30 days), 
    - CY####Q# for quarterly data (duration 91 days +/- 30 days), 
    - CY####Q#I for instantaneous data.

'''

url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept-Encoding": "gzip, deflate",
    "Host": "data.sec.gov"
}

response = requests.get(
    url=url,
    headers=headers
)

metrics = [
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
                if entry["form"] == "10-Q" and int(entry["fy"]) >= 2021:
                    year = entry["fy"]
                    if year not in facts[metric]["values"]:
                        facts[metric]["values"][year] = {}
                    facts[metric]["values"][year][entry["fp"]] = entry["val"]
    print(json.dumps(facts, indent=2))
else:
    print(response.status_code)
