import streamlit as st
import info
import pandas as pd
from PIL import Image, ImageOps
import Home_Page
import PhaseII

st.set_page_config(layout="wide", page_title="Elan McClain Portfolio")

def nav():
    st.sidebar.title("Navigation")
    
    home = st.sidebar.button("Home", use_container_width=True)
    about = st.sidebar.button("About Me", use_container_width=True)
    quiz = st.sidebar.button("Motorcycle Quiz", use_container_width=True)
    
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    
    if home:
        st.session_state.page = "Home"
    elif about:
        st.session_state.page = "About Me"
    elif quiz:
        st.session_state.page = "Motorcycle Quiz"
    
    return st.session_state.page

def sidebar():
    st.sidebar.markdown("---")
    try:
        st.sidebar.image(info.pic, width=150)
    except:
        st.sidebar.write("Profile picture not available")
    
    st.sidebar.title("Connect with Me")
    
    link = f'<a href="{info.linkurl}" target="_blank"><img src="{info.linkedin}" alt="LinkedIn" width="30" height="30"></a>'
    st.sidebar.markdown("Connect with me on LinkedIn", unsafe_allow_html=True)
    st.sidebar.markdown(link, unsafe_allow_html=True)
    
    st.sidebar.markdown("Or email me!", unsafe_allow_html=True)
    email = f'<a href="mailto:{info.email}"><img src="{info.emailimg}" alt="Email" width="30" height="30"></a>'
    st.sidebar.markdown(email, unsafe_allow_html=True)

def about():
    st.header("About Me")
    
    try:
        st.image("Images/FullSelfie.jpg", width=400)
    except:
        st.write("Full picture not found")
    
    st.write(info.about)
    st.write("**What I'm passionate about:**")
    st.write("• Problem solving and innovative technology solutions")
    st.write("• Leading teams and making positive impacts") 
    st.write("• Continuous learning and growth")
    st.write("• Having Fun!")
    st.write("---")

def education():
    st.header("Education")
    for e in info.edu:
        st.subheader(f"**{e['Institution']}**")
        st.write(f"**Degree:** {e['Degree']}")
        st.write(f"**Graduation Date:** {e['Graduation Date']}")
        st.write(f"**Location:** {e['Location']}")
        if "Photo" in e and e["Photo"]:
            try:
                img = Image.open(e["Photo"])
                img = ImageOps.exif_transpose(img)
                st.image(img, width=250)
            except:
                st.write("Image not found")
    
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(info.courses)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names", 
        "semester": "Semester Taken",
        "skills": "What I Learned"
    }, hide_index=True, use_container_width=True)
    st.write("---")

def experience():
    st.header("Professional Experience")
    for job, (desc, imgs) in info.exp.items():
        with st.expander(f"{job}"):
            if imgs:
                if isinstance(imgs, list):
                    for img in imgs:
                        try:
                            st.image(img, width=250)
                        except:
                            st.write("Image not found")
                else:
                    try:
                        st.image(imgs, width=250)
                    except:
                        st.write("Image not found")
            for bullet in desc:
                st.write(bullet)
    st.write("---")

def projects():
    st.header("Projects")
    for name, pinfo in info.projects.items():
        with st.expander(f"{name}"):
            if isinstance(pinfo, tuple):
                text = pinfo[0]
                img = pinfo[1] if len(pinfo) > 1 else None
                link = pinfo[2] if len(pinfo) > 2 else None
                
                st.write(text)
                
                if img:
                    try:
                        st.image(img, width=300)
                    except:
                        st.write("Image not found")
                
                if link:
                    st.markdown(f"[**Play the Game!**]({link})")
            else:
                st.write(pinfo)
    st.write("---")

def skills():
    st.header("Skills")
    
    st.subheader("Programming Languages")
    for skill, level in info.langs.items():
        icon = info.icons.get(skill, "")
        st.write(f"{skill} {icon}")
        st.progress(level / 10)
    
    st.subheader("Other Languages")
    for lang, prof in info.spoken.items():
        icon = info.others.get(lang, "")
        st.write(f"{lang} {icon}: {prof}")
    st.write("---")

def activities():
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    
    with tab1:
        st.subheader("Leadership")
        for title, (details, img) in info.lead.items():
            with st.expander(f"{title}"):
                if img:
                    try:
                        pimg = Image.open(img)
                        pimg = ImageOps.exif_transpose(pimg)
                        st.image(pimg, width=250)
                    except:
                        st.write("Image not found")
                for bullet in details:
                    st.write(bullet)
    
    with tab2:
        st.subheader("Community Service")
        for title, details in info.activities.items():
            with st.expander(f"{title}"):
                if isinstance(details, list):
                    for bullet in details:
                        st.write(bullet)
                else:
                    st.write(details)
    st.write("---")

def hobbies():
    st.header("Hobbies & Interests")
    
    st.subheader("Cars")
    st.write(info.hobbies["Cars"])

    st.write("**My Car Timeline**")
    for car in info.cars:
        with st.expander(f"{car['date']} - {car['action']} {car['car']}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if car['action'] == 'Bought':
                    st.markdown("🟢 **Purchased**")
                elif car['action'] == 'Sold':
                    st.markdown("🔴 **Sold**")
                elif car['action'] == 'Wrecked':
                    st.markdown("💥 **Wrecked**")
                st.write(car['details'])
            
            with col2:
                if car.get('image'):
                    try:
                        st.image(car['image'], width=150)
                    except:
                        st.write("Image not found")

    st.subheader("Firearms")
    st.write(info.hobbies["Firearms"])

    with st.expander("Shooting with Friends"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("One of my favorite parts of guns is the social aspect. Whether it's the friendly old guys at the gun shop who like to tell stories every time I go in to buy ammo or my best friends coming over to my house for some competitive target shooting, everyone I have interacted with in this hobby has been extremely kind and helpful. I love how firearms brings together such a great community of people accross lines that would typically divide people.")
        with col2:
            try:
                st.image("Images/3Migos-min.jpg", width=200)
            except:
                st.write("Image not found")

    with st.expander("Building & Customizing Firearms"):
        col1, col2 = st.columns([1, 2])
        with col1:
            try:
                st.image("Images/buildingaglock-min.jpg", width=200)
            except:
                st.write("Image not found")
        with col2:
            st.write("The technical side of firearms fascinates me - understanding how each of the components work together just scratches the mechanical itch in my brain. I loved playing with Legos as a kid, and I think that building firearms is the adult version of that pasttime. Fitting springs and pins, sanding components, and assembling parts is one of my favorite parts of the hobby of firearms.")

    st.subheader("Motorcycles")
    st.write(info.hobbies["Motorcycles"])

    st.write("**My Georgia Mountain Riding Journey**")
    st.write("Here are some of my favorite riding spots in North Georgia:")

    for i, loc in enumerate(info.rides):
        with st.expander(f"Stop {i+1}: {loc['name']} - {loc['date']}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(loc["description"])
            with col2:
                try:
                    st.image(loc["image"], width=250)
                except:
                    st.write("Image not found")

    st.write("---")

# Main execution
page = nav()
sidebar()

if page == "Home":
    Home_Page.show_home_page()
elif page == "About Me":
    st.title("Elan McClain - Portfolio")
    st.write("**Welcome to my portfolio!** Explore my journey as a Computer Science student at Georgia Tech.")
    st.write("---")
    
    about()
    education()
    experience()
    projects()
    skills()
    activities()
    hobbies()
    
elif page == "Motorcycle Quiz":
    PhaseII.show_quiz()
