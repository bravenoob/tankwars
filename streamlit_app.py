import pandas as pd
import requests
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode


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
           
"""
)

st.info(
    "To support more community tools like this, consider delegating to the [Future FTM Delegator]()."
)


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

#load data
for offset in range(0, total_record, 100):
    url = "https://marketplace-api.tankwars.zone/api/v1/items?limit=50&offset=" + str(offset) + "&order_by=NEWEST&status=Selling"             
    response = requests.get(url=url, headers=headers, params=querystring).json()        
    all_items.append(response)       
    print(offset)


# disclaimer
st.info("For our american friends: this tool was created for educational purposes only, not financial advice.")
