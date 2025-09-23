import streamlit as st
import info
import pandas as pd
from PIL import Image, ImageOps
import Home_Page
import PhaseII

# Set page config
st.set_page_config(layout="wide", page_title="Elan McClain Portfolio")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌟 Navigation")

# Page selection
page = st.sidebar.selectbox("Choose a page:", 
                           ["🏠 Home", "👨‍💻 About Me", "🏍️ Motorcycle Quiz"])

# Contact info in sidebar
st.sidebar.markdown("---")
st.sidebar.image(info.profile_picture, width=150)
st.sidebar.title("Connect with Me")

st.sidebar.write("🔗 [LinkedIn](%s)" % info.my_linkedin_url)
st.sidebar.write("✉️ [Email](mailto:%s)" % info.my_email_address)

st.sidebar.write("---")
st.sidebar.write("**Quick Stats:**")
st.sidebar.write(f"📊 Programming Languages: {len(info.programming_languages)}")
st.sidebar.write(f"👑 Leadership Roles: {len(info.leadership_data)}")

# --- PAGE CONTENT ---
if page == "🏠 Home":
    # Load Home Page content
    Home_Page.show_home_page()

elif page == "👨‍💻 About Me":
    # ABOUT ME PAGE CONTENT
    st.title("🌟 Elan McClain - Portfolio")
    st.write("**Welcome to my portfolio!** Explore my journey as a Computer Science student at Georgia Tech.")
    st.write("---")

    # Create tabs for sections
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📌 About Me", 
        "💼 Career", 
        "🎓 Education", 
        "🗣️ Languages", 
        "📂 Projects",
        "🏅 Leadership",
        "🤝 Community Service",
        "🎯 Hobbies & Interests"
    ])

    # --- ABOUT ---
    with tab1:
        st.subheader("Who I Am")
        st.write(info.about_me)
        st.write("**What I'm passionate about:**")
        st.write("• Problem solving and innovative technology solutions")
        st.write("• Leading teams and making positive impacts") 
        st.write("• Continuous learning and growth")

    # --- CAREER ---
    with tab2:
        st.subheader("Career")
        for role, (details, images) in info.experience_data.items():
            st.subheader(role)
            for d in details:
                st.write(d)
            if images:
                if isinstance(images, list):
                    for img in images:
                        try:
                            st.image(img, width=200)
                        except:
                            st.write("Image not found")
                else:
                    try:
                        st.image(images, width=200)
                    except:
                        st.write("Image not found")

    # --- EDUCATION ---
    with tab3:
        st.subheader("Education")
        for edu in info.education_data:
            st.subheader(edu["🎓 Degree"])
            st.write(f"**Institution:** {edu['🏫 Institution']}")
            st.write(f"**Location:** {edu['📍 Location']}")
            st.write(f"**Graduation Date:** {edu['📅 Graduation Date']}")
            if "Photo" in edu and edu["Photo"]:
                try:
                    img = Image.open(edu["Photo"])
                    img = ImageOps.exif_transpose(img)
                    st.image(img, width=200)
                except:
                    st.write("Image not found")
        
        # Add courses section here
        st.subheader("Courses")
        for code, name, semester, skill in zip(
            info.course_data["code"],
            info.course_data["names"],
            info.course_data["semester_taken"],
            info.course_data["skills"]
        ):
            with st.expander(f"{code} - {name} ({semester})"):
                st.write(skill)

    # --- LANGUAGES ---
    with tab4:
        st.subheader("Programming Languages")
        st.bar_chart(info.programming_languages)
        st.subheader("Other Languages")
        for lang, level in info.other_languages.items():
            icon = info.other_icons.get(lang, "")
            st.write(f"{icon} {lang}: {level}")

    # --- PROJECTS ---
    # --- PROJECTS ---
    with tab5:
        st.subheader("Projects")
        for project, description in info.projects_data.items():
            with st.expander(project):
                if isinstance(description, tuple):
                    # Handle tuple with text, image, and optional link
                    text_description = description[0]
                    image_path = description[1] if len(description) > 1 else None
                    project_link = description[2] if len(description) > 2 else None
                    
                    st.write(text_description)
                    
                    if image_path:
                        try:
                            st.image(image_path, width=300)
                        except:
                            st.write("Image not found")
                    
                    if project_link:
                        st.markdown(f"🎮 [**Play the Game!**]({project_link})")
                else:
                    st.write(description)

    # --- LEADERSHIP ---
    with tab6:
        st.subheader("Leadership")
        for role, (details, img) in info.leadership_data.items():
            with st.expander(role):
                for bullet in details:
                    st.write(bullet)
                if img:
                    try:
                        pil_img = Image.open(img)
                        pil_img = ImageOps.exif_transpose(pil_img)
                        st.image(pil_img, width=150)
                    except:
                        st.write("Image not found")

    # --- COMMUNITY SERVICE ---
    with tab7:
        st.subheader("Community Service")
        for activity, details in info.activity_data.items():
            with st.expander(activity):
                if isinstance(details, list):
                    for bullet in details:
                        st.write(bullet)
                else:
                    st.write(details)

    # --- HOBBIES & INTERESTS ---
    with tab8:
        st.subheader("🎯 Hobbies & Interests")
        st.markdown("### 🚗 Cars")
        st.write(info.hobbies_data["🚗 Cars"])

# Car Timeline
        st.markdown("#### My Car Timeline")

        for car_entry in info.car_timeline_data:  # ← This should be info.car_timeline_data
            # Create columns for text and image
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if car_entry['action'] == 'Bought':
                    st.markdown(f"🟢 **{car_entry['date']} - Bought {car_entry['car']}**")
                elif car_entry['action'] == 'Sold':
                    st.markdown(f"🔴 **{car_entry['date']} - Sold {car_entry['car']}**")
                elif car_entry['action'] == 'Wrecked':
                    st.markdown(f"💥 **{car_entry['date']} - Wrecked {car_entry['car']}**")
                st.write(f"   {car_entry['details']}")
            
            with col2:
                if car_entry.get('image'):
                    try:
                        st.image(car_entry['image'], width=150, caption=car_entry['car'])
                    except:
                        st.write("📷 Image not found")
            
            st.markdown("---")  # Divider between entries
                # --- FIREARMS ---
        st.markdown("### 🔫 Firearms")
        st.write(info.hobbies_data["🔫 Firearms"])

        # Create expandable card sections
        with st.expander("🎯 Shooting with Friends"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write("One of my favorite parts of guns is the social aspect. Whether it's the friendly old guys at the gun shop who like to tell stories every time I go in to buy ammo or my best friends coming over to my house for some competitive target shooting, everyone I have interacted with in this hobby has been extremely kind and helpful. I love how firearms brings together such a great community of people accross lines that would typically divide people.")
            with col2:
                try:
                    st.image("Images/3Migos-min.jpg", width=200, caption="Doing some casual shooting with the boys")
                except:
                    st.write("📷 Image not found")

        with st.expander("🔧 Building & Customizing Firearms"):
            col1, col2 = st.columns([1, 2])
            with col1:
                try:
                    st.image("Images/buildingaglock-min.jpg", width=200, caption="Assembling a gen3 parts kit in a new 3D printed frame after I warped the first one.")
                except:
                    st.write("📷 Image not found")
            with col2:
                st.write("""
                The technical side of firearms fascinates me - understanding how each of the components work together just scratches the mechanical itch in my brain.
                I loved playing with Legos as a kid, and I think that building firearms is the adult version of that pasttime. Fitting springsand pins, sanding components, and assembling parts is one of my favorite parts of the hobby of firearms.""")

        # --- MOTORCYCLES ---
        st.markdown("### 🏍️ Motorcycles")
        st.write(info.hobbies_data["🏍️ Motorcycles"])

        st.markdown("###  My Georgia Mountain Riding Journey")
        st.write("Here are some of my favorite riding spots in North Georgia:")

        # Create progress timeline
        for i, location in enumerate(info.motorcycle_locations):
            progress = (i + 1) / len(info.motorcycle_locations)
            
            # Show progress bar
            st.progress(progress, text=f"Riding Adventure {i+1} of {len(info.motorcycle_locations)}")
            
            # Create columns for content
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"**🏔️ Stop {i+1}: {location['name']}**")
                st.markdown(f"*📅 {location['date']}*")
                
                try:
                    st.image(location["image"], width=400, caption=f"Riding at {location['name']}")
                except:
                    st.info(f"📷 Photo from {location['name']} - Image not found")
                
                st.write(location["description"])
                st.markdown("---")

        st.success("Hopefully many more riding adventures to come!")
