[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Stock Market Prediction

## Install packages

```shell
> pip install -r requirements.txt
```

## Download data

```python
> export API_TOKEN=[Your Tiingo API token here]
> python ./script/download_data.py --help
```

```
usage: download_data.py [-h] [--tickers TICKERS] [--year YEAR] --token TOKEN
                        [--path PATH] [--freq FREQ]

Download & save stock price data

optional arguments:
  -h, --help         show this help message and exit
  --tickers TICKERS  Tickers (comma separated values). Eg. AAPL,MSFT,WMT,GS.
                     Default S&P500 (Will download all stock data)
  --year YEAR        Year (to download data). Default: 2019
  --token TOKEN      API token
  --path PATH        Path to store data. Default: ./data
  --freq FREQ        Frequency ([min], [hour]) in which you want data
                     resampled. Eg. 1min 5min 1hour. Default: 1min
```

Example:

```python
> python ./script/download_data.py \
    --tickers=AAPL,MSFT,WMT,AMZN,GOOG,BLK,JPM,GS,NFLX,KO \
    --year=2019 \
    --token=$API_TOKEN \
    --path=./data \
    --freq=1min
```

# References
- Arévalo, A., Niño, J., Hernández, G. and Sandoval, J., 2020. High-Frequency Trading Strategy Based On Deep Neural Networks.

- Zhou, X., Pan, Z., Hu, G., Tang, S. and Zhao, C., 2018. Stock Market Prediction on High-Frequency Data Using Generative Adversarial Nets. Mathematical Problems in Engineering, 2018, pp.1-11.
