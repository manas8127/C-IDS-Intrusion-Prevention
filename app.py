import app1
import app2
import app3
import app4
import cyber_mads
import streamlit as st
import streamlit.components.v1 as components
PAGES = {
    "Dashboard": app1,
    "Reports": app2,
    "Timeline": app3,
    "Upload": app4
}
st.title("Cyber MADS")
st.sidebar.title('C-IDS')
# st.sidebar.button("Dashboard", list(PAGES.keys())
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()