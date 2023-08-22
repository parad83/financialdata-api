<h1>Webscrapping API for Trading View </h1>
Made with Flask as the framework for the get and post requests and Beautiful Soup and Requests libraries for scrapping the data.
<hr>

**Content**
- Assets,Current_Assets,Cash,Accounts_Receivable,Inventory,Fixed_Assets,Total_Liabilities,Current_Liabilities,Long_Term_Debt,Equity from *balance sheets*,
- Operating_Cash_Flow,Capital_Expenditure,Financing_Cash_Flow,Net_Cash_Flow from *cash flow statements*,
- Revenue,COGS,Operating_Expenses,Interest_Expense,Taxes from *income statements*.

<hr>

**Updates**

*v1* data from Trading View web app

*v2* data from SEC EDGAR database


    EDGAR API:

    Access all information given CIK:
        https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
        
    Access specific metric of a given company given its CIK and name of the metric
        https://data.sec.gov/api/xbrl/companyconcept/CIK##########./us-gaap/<NAME>.json

    Access specific metric in a given period in all companies
        https://data.sec.gov/api/xbrl/frames/us-gaap/</NAME>/USD/CY####.json
    
    The period format is:
    - CY#### for annual data (duration 365 days +/- 30 days), 
    - CY####Q# for quarterly data (duration 91 days +/- 30 days), 
    - CY####Q#I for instantaneous data.
