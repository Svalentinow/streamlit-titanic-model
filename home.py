def homes():
    import streamlit as st
    import numpy as np
    from streamlit_option_menu import option_menu
    from streamlit_extras.switch_page_button import switch_page
    import pickle
    

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
                background: url("https://cdn.pixabay.com/photo/2015/12/27/05/48/turntable-1109588_1280.jpg");
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
            .css-184tjsw.e16nr0p34 > p {{
                color: white !important;
                font-weight: 900;
                font-size: 23px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack_url()
    set_prompt_input_color()
    st.markdown(
        "<h1 style='text-align: center; color: black; background-color: white; opacity: .95'> Welcome to titanic </1>", unsafe_allow_html=True)

    

    txt1 = st.text_area('Fare price:',
                       placeholder="...", key = 1, height=50)
    txt2 = st.text_area('sex:',
                       placeholder="0 for female 1 for male",key = 2, height=50)
    txt3 = st.text_area('age:',
                       placeholder="...",key = 3, height=50)


    # save variables in the current session
    if "survived" not in st.session_state:
        st.session_state["survived"] = ""
    model = pickle.load(open('model.pkl', 'rb'))
    if(st.button('Submit')):
        list = [txt1,txt2,txt3]
        l = [int(x) for x in list]
        f = [np.array(l)]
        survived = model.predict(f)
        output = "yes"
        if survived == 0:
            output = "no"
        st.session_state["survived"] = output


        switch_page("result")

    else:
        st.write('')
