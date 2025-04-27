import streamlit as st
from streamlit_option_menu import option_menu

# 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
#     st.write("asdssda")
#     
# selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
#     icons=['house', 'cloud-upload', "list-task", 'gear'],
#     on_change=on_change, key='menu_5', orientation="horizontal")
# selected5

# sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        menu_icon="cast", icons=['house', 'gear'], default_index=1)
    selected

# 2. horizontal menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    default_index=0, orientation="horizontal") # menu_icon="cast"

selected2
