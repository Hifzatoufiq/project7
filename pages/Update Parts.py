import streamlit as st
import pandas as pd

st.set_page_config(
  
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        body {
            background-color: #080707;
            color: #f4fbfb;
            font-family: serif;
            primaryColor=#7b2828;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.subheader("Update Parts Master list")
# Create a DataFrame with the given data
data1 = {
   
    'Part discription<br>(father)': ['PICKUP FRAME', 'PICKUP FRAME', 'PICKUP FRAME','V6 TAIL GATE<br> <br>V6 TAIL GATE','HD TAIL GATE','HD TAIL GATE'],
    'item name(childern)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790', 'item 1<br><br>item 2','item 1','item 2'],
    'QUANTITY per order': ['1', '1', '1','1','1','1'],
   # 'program ': ['Welding part 1', 'welding part 2', 'welding part3','','',''],
     #'Detail': ['Diameter:12<br>lenght:120', 'Diameter:19<br>lenght:130', 'Diameter:15<br>lenght:170','','',''],
}
df1 = pd.DataFrame(data1)

styled_df = df1.style.hide(axis="index").set_table_styles([
    {'selector': '', 'props': [('background-color', '#262730'), ('color', 'white')]},
    {'selector': 'th', 'props': [('background-color', '#262730'), ('color', 'white')]}
])

st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)