# UK COVID stats Benford's law

![Chart showing UK COVID statistics follow Benford's law](output.png)

Data from [coronavirus.data.gov.uk](https://coronavirus.data.gov.uk/)

## Setup

Install curl, Python and matplotlib

```
curl -o data.json https://c19downloads.azureedge.net/downloads/json/coronavirus-cases_latest.json
```

## Running

```
python analysis.py
```