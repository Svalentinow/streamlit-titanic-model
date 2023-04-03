import streamlit as st
from pages.home import homes
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")


selected = option_menu(None, ["Result", "Predict"],
                       icons=['cloud-upload', "bi-file-person"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal",
                       styles={
    "container": {"padding": "1!important", "background-color": "#fafafa"}, })


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
        f"""
            <style>
            .stApp {{
                background: url("https://i.imgur.com/akdsDra.jpg");
                background-size: cover
            }}
            </style>
            """,
        unsafe_allow_html=True
    )


def set_prompt_input_color():
    st.markdown(
        f"""
        <style>
        .css-1n76uvr{{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg_hack_url()
set_prompt_input_color()

dict = {
    '0': 'Country',
    '1': "Pop",
    '2': "R&B",
    '3': 'Rap',
    '4': 'Rock',

}

st.write("Did they survive?: ", st.session_state['survived'])
st.write(" ")


if selected == "Predict":
    switch_page("app")

