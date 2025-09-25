import streamlit as st

def show_home_page():
    # Title of App
    st.title("Web Dev Lab01")
    # Assignment Data 
    # TODO: Fill out your team number, section, and team members
    st.header("CS 1301 - Section X")
    st.subheader("Web Development")
    st.subheader("Elan McClain")
    # Introduction
    # TODO: Write a quick description for all of your pages in this lab below, in the form:
    #       1. **Page Name**: Description
    #       2. **Page Name**: Description
    #       3. **Page Name**: Description
    #       4. **Page Name**: Description
    st.write("""
    Welcome to my Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:
    1. **Home Page**: Landing page
    2. **Portfolio**: This page tells all about me, from my professional achievements to my hobbies!
    3. **Motorcycle Quiz**: A quiz to help you determine what motorcycle is a good choice for you!
    """)
    
