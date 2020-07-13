# Stock Market Prediction

```python
python ./download_data.py --help
```

```
usage: download_data.py [-h] --tickers TICKERS --year YEAR --token TOKEN
                        [--path PATH] [--freq FREQ]

Download & save stock price data

optional arguments:
  -h, --help         show this help message and exit
  --tickers TICKERS  Tickers (comma separated values). Eg. AAPL,MSFT,WMT,GS
  --year YEAR        Year (to download data)
  --token TOKEN      API token
  --path PATH        Path to store data
  --freq FREQ        Frequency ([min], [hour]) in which you want data
                     resampled. Eg. 1min 5min 1hour
```

```python
python ./download_data.py --tickers=MSFT,WMT,GS --year=2019 --token=$API_TOKEN --path=./data --freq=1min
```
