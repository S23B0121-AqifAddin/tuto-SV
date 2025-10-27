import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Accident Motorbike in Bangladesh",
    page_icon=":material/school:",
)

# --- Define pages ---
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
visualise = st.Page("home1.py", title="Pencapaian Akademik Pelajar", icon=":material/school:")
page_1 = st.Page("page1.py", title="Page 1", icon=":material/description:")
page_2 = st.Page("page2.py", title="Page 2", icon=":material/bar_chart:")
page_3 = st.Page("page3.py", title="Page 3", icon=":material/settings:")

# --- Navigation menu ---
pg = st.navigation({
    "Main Menu": [home, visualise, page_1, page_2, page_3]
})

# --- Run selected page ---
pg.run()
