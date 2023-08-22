import json

data = {
    "us-gaap": {
      "AcceleratedShareRepurchaseProgramAdjustment": {
        "label": "Accelerated Share Repurchase Program, Adjustment",
        "description": "The amount needed to adjust previously recorded stockholders' equity balances to the actual aggregate amounts paid, whether in cash or other consideration, to acquire all of the shares purchased under an Accelerated Share Repurchase arrangement.",
        "units": {
          "USD": [
            {
              "start": "2016-05-02",
              "end": "2016-07-31",
              "val": 9000000,
              "accn": "0001045810-16-000300",
              "fy": 2016,
              "fp": "Q2",
              "form": "10-Q",
              "filed": "2016-08-23",
              "frame": "CY2016Q2"
            },
            {
              "start": "2016-02-01",
              "end": "2016-10-30",
              "val": 9000000,
              "accn": "0001045810-16-000353",
              "fy": 2016,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2016-11-22"
            }
          ]
        }
      },
      "AcceleratedShareRepurchasesFinalPricePaidPerShare": {
        "label": "Accelerated Share Repurchases, Final Price Paid Per Share",
        "description": "Final price paid per share for the purchase of the targeted number of shares, determined by an average market price over a fixed period of time.",
        "units": {
          "USD/shares": [
            {
              "start": "2015-01-26",
              "end": "2015-10-25",
              "val": 21.63,
              "accn": "0001045810-15-000173",
              "fy": 2015,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2015-11-18"
            },
            {
              "start": "2016-02-01",
              "end": "2016-07-31",
              "val": 42.06,
              "accn": "0001045810-16-000300",
              "fy": 2016,
              "fp": "Q2",
              "form": "10-Q",
              "filed": "2016-08-23"
            },
            {
              "start": "2016-02-01",
              "end": "2016-10-30",
              "val": 42.06,
              "accn": "0001045810-16-000353",
              "fy": 2016,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2016-11-22"
            }
          ]
        }
      },
      "AcceleratedShareRepurchasesSettlementPaymentOrReceipt": {
        "label": "Accelerated Share Repurchases, Settlement (Payment) or Receipt",
        "description": "Amount of cash receipt from (payment to) bank; or stock received from (issuance to) bank in the settlement of the accelerated share repurchase agreement.",
        "units": {
          "USD": [
            {
              "end": "2013-07-28",
              "val": 750000000,
              "accn": "0001045810-13-000075",
              "fy": 2013,
              "fp": "Q2",
              "form": "10-Q",
              "filed": "2013-08-21",
              "frame": "CY2013Q2I"
            },
            {
              "end": "2013-07-28",
              "val": 750000000,
              "accn": "0001045810-13-000054",
              "fy": 2013,
              "fp": "Q1",
              "form": "10-Q",
              "filed": "2013-05-22"
            },
            {
              "end": "2013-10-27",
              "val": 750000000,
              "accn": "0001045810-13-000109",
              "fy": 2013,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2013-11-19",
              "frame": "CY2013Q3I"
            },
            {
              "end": "2015-10-25",
              "val": 400000000,
              "accn": "0001045810-15-000173",
              "fy": 2015,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2015-11-18",
              "frame": "CY2015Q3I"
            },
            {
              "end": "2016-01-31",
              "val": 587000000,
              "accn": "0001045810-16-000205",
              "fy": 2015,
              "fp": "FY",
              "form": "10-K",
              "filed": "2016-03-17",
              "frame": "CY2015Q4I"
            },
            {
              "end": "2016-05-01",
              "val": 500000000,
              "accn": "0001045810-16-000353",
              "fy": 2016,
              "fp": "Q3",
              "form": "10-Q",
              "filed": "2016-11-22",
              "frame": "CY2016Q1I"
            },
            {
              "end": "2016-05-01",
              "val": 500000000,
              "accn": "0001045810-16-000300",
              "fy": 2016,
              "fp": "Q2",
              "form": "10-Q",
              "filed": "2016-08-23"
            },
            {
              "end": "2016-05-01",
              "val": 500000000,
              "accn": "0001045810-16-000275",
              "fy": 2016,
              "fp": "Q1",
              "form": "10-Q",
              "filed": "2016-05-25"
            }
          ]
        }
      }
    }
}

# facts = [
#     {"name": metric, "value": value} for metric, value in data["us-gaap"].items()
# ]

facts = []

for metric, metric_data in data["us-gaap"].items():
    for unit, entry_data in metric_data["units"].items():
        for entry in entry_data:
            if entry["form"] == "10-Q":
                data_attributes = {
                    "name": metric,
                    "value": entry["val"],
                    "fy": entry["fy"],
                    "fp": entry["fp"],
                }
                facts.append(data_attributes)
        print()
        # for entry, entry_data in metric_data["data"].items():
            
for d in facts:
    print(d)
    
# if (e["form"] == "10-Q" for e in d["units"]["usd"].items()): new_dir["a"]
# print(facts)

# for f in facts:
    # print(f)
    # print()
