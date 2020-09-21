import ta
import numpy as np


def cyclical_encoding(df):
    df['datetime'] = df.index.to_timestamp()
    min_min = np.min(df.datetime.dt.minute)
    df['min_sin'] = np.sin(2 * np.pi * (df.datetime.dt.minute - min_min) / np.max(df.datetime.dt.minute - min_min))
    df['min_cos'] = np.cos(2 * np.pi * (df.datetime.dt.minute - min_min) / np.max(df.datetime.dt.minute - min_min))
    hour_min = np.min(df.datetime.dt.hour)
    df['hour_sin'] = np.sin(2 * np.pi * (df.datetime.dt.hour - hour_min) / np.max(df.datetime.dt.hour - hour_min))
    df['hour_cos'] = np.cos(2 * np.pi * (df.datetime.dt.hour - hour_min) / np.max(df.datetime.dt.hour - hour_min))
    day_min = np.min(df.datetime.dt.day)
    df['day_sin'] = np.sin(2 * np.pi * (df.datetime.dt.day - day_min) / np.max(df.datetime.dt.day - day_min))
    df['day_cos'] = np.cos(2 * np.pi * (df.datetime.dt.day - day_min) / np.max(df.datetime.dt.day - day_min))
    # month_min = np.max(df.datetime.dt.month) df['month_sin'] = np.sin(2 * np.pi * (df.datetime.dt.month -
    # month_min) / np.max(df.datetime.dt.month - month_min)) df['month_cos'] = np.cos(2 * np.pi * (
    # df.datetime.dt.month - month_min) / np.max(df.datetime.dt.month - month_min))
    return df


def price_direction(df, horizon=10):
    df[f'label_{horizon}'] = df.close.shift(-horizon) - df.close
    df[f'label_{horizon}'] = df[f'label_{horizon}'].apply(lambda x: 0 if x <= 0 else 1)
    return df


def momentum_indicators(df):
    df['roc'] = ta.momentum.roc(close=df.close)  # Rate of Change (ROC)
    df['rsi'] = ta.momentum.rsi(close=df.close)  # Relative Strength Index (RSI)
    df['tsi'] = ta.momentum.tsi(close=df.close)  # True strength index (TSI)
    return df


def volume_indicators(df):
    df['obv'] = ta.volume.on_balance_volume(close=df.close, volume=df.volume)  # On Balance Volume (OBV)
    df['vpt'] = ta.volume.volume_price_trend(close=df.close, volume=df.volume)  # Volume-price trend (VPT)
    df['fi'] = ta.volume.force_index(close=df.close, volume=df.volume)  # Force Index (FI)
    df['nvi'] = ta.volume.negative_volume_index(close=df.close, volume=df.volume)  # Negative Volume Index (NVI)
    return df


def volatility_indicators(df):
    bb_indicator = ta.volatility.BollingerBands(close=df.close)
    df['bb_bbhi'] = bb_indicator.bollinger_hband_indicator()  # Bollinger Band high indicator
    df['bb_bbli'] = bb_indicator.bollinger_lband_indicator()  # Bollinger Band low indicator
    return df


def trend_indicators(df):
    aroon_indicator = ta.trend.AroonIndicator(close=df.close)
    macd_indicator = ta.trend.MACD(close=df.close)
    kst_indicator = ta.trend.KSTIndicator(close=df.close)
    df['aroon_down'] = aroon_indicator.aroon_down()  # Aroon Down Channel
    df['aroon'] = aroon_indicator.aroon_indicator()  # Aroon Indicator
    df['aroon_up'] = aroon_indicator.aroon_up()  # Aroon Up Channel
    df['macd_line'] = macd_indicator.macd()  # MACD Line
    df['macd_hist'] = macd_indicator.macd_diff()  # MACD Histogram
    df['macd_signal'] = macd_indicator.macd_signal()  # MACD Signal Line
    df['kst'] = kst_indicator.kst()  # Know Sure Thing (KST)
    df['kst_diff'] = kst_indicator.kst_diff()  # Diff Know Sure Thing (KST)
    df['kst_signal'] = kst_indicator.kst_sig()  # Signal Line Know Sure Thing (KST)
    df['dpo'] = ta.trend.dpo(close=df.close)  # De-trended Price Oscillator (DPO)
    df['trix'] = ta.trend.trix(close=df.close)  # Trix (TRIX)
    df['sma_10'] = ta.trend.sma_indicator(close=df.close, n=10)  # SMA n=10
    df['sma_20'] = ta.trend.sma_indicator(close=df.close, n=20)  # SMA n=20
    df['sma_30'] = ta.trend.sma_indicator(close=df.close, n=30)  # SMA n=30
    df['sma_60'] = ta.trend.sma_indicator(close=df.close, n=60)  # SMA n=60
    df['ema_10'] = ta.trend.sma_indicator(close=df.close, n=10)  # EMA n=10
    df['ema_20'] = ta.trend.sma_indicator(close=df.close, n=20)  # EMA n=20
    df['ema_30'] = ta.trend.sma_indicator(close=df.close, n=30)  # EMA n=30
    df['ema_60'] = ta.trend.sma_indicator(close=df.close, n=60)  # EMA n=60
    return df
