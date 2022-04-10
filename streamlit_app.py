import os
import random
import requests
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from replit.database import Database

# main body
st.header("Tankwars Statistic Tool | #tankwars_stats")

# description
st.sidebar.write(
    """
    Made by [@bravenoob21](https://twitter.com/bravenoob21).

    Accompanying YouTube video [tbd](link).
    """
)

st.markdown(
    """
            
            #### Instructions
            Open the menu bar to input projected $ASTRO price, dual incentive staking rewards, user LP positions, and user lockup durations.

"""
)

st.info(
    "To support more community tools like this, consider delegating to the [Future FTM Delegator]()."
)

st.markdown(
    """### Terraswap Liquidity

Current pair liquidity on Terraswap, $ASTRO token to liquidity ratio, and current LP incentives.

"""
)

# sidebar
st.sidebar.markdown(
    f"""
    # Assumptions
    """
)

# astro price prediction
astro_price = st.sidebar.number_input(
    "$ASTRO Price", min_value=0.01, value=2.5, help="Price of $ASTRO"
)

# requests headers
headers = {
    "authority": "api.coinhall.org",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "accept": "*/*",
    "sec-gpc": "1",
    "origin": "https://coinhall.org",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://coinhall.org/",
    "accept-language": "en-US,en;q=0.9",
}

# coinhall api
response = requests.get(
    "https://api.coinhall.org/api/v1/charts/terra/pairs", headers=headers
).json()

# convert to dataframe
df = (
    pd.DataFrame.from_dict(response, orient="index")
    .reset_index(drop=False)
    .rename(columns={"index": "address"})
    .drop(labels=["timestamp", "unofficial", "startAt", "endAt"], axis=1)
)


# replit database
#db = Database(
#    "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2Mzk5NzQzNDMsImlhdCI6MTYzOTg2Mjc0MywiZGF0YWJhc2VfaWQiOiI2MTA3MDMxZC00ZTY0LTQzNTAtOWM5NS00NmQ0MWNkNDJkYmUifQ.jlsw5c7Lg4afcejjTNBcqYRvo6-fMHWAS9ICWjFj9nUvK-jsxM5IbFwayZ3e6dAQSn2m2pNVKV6C7VRsZ3ZIBQ"
#)


# disclaimer
st.info("For our american friends: this tool was created for educational purposes only, not financial advice.")
