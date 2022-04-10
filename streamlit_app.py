import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Tankwars Statistic Tool",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

    
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



# disclaimer
st.info("For our american friends: this tool was created for educational purposes only, not financial advice.")
