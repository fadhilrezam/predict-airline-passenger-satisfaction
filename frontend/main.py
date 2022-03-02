import streamlit as st
import eda, pred
# from SessionState import _get_state


# state = _get_state()

st.set_page_config(
    page_title = ' Phase 1 Milestone 2 - Fadhil Reza Maulana',
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state = 'expanded'
)

st.markdown("![Alt Text](https://giffiles.alphacoders.com/107/107600.gif)")
PAGES = {
    'Hal 1 - Exploratory Data Analysis Page' : eda,
    'Hal 2 - Prediction Page' : pred
}

st.sidebar.title('Menu')
selection = st.sidebar.selectbox('Pilih Halaman', list(PAGES.keys()))
page = PAGES [selection]
page.app()