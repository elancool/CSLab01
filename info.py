
#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/profile.jpg"
header_description = "Welcome to my portfolio! Here you'll find my journey as a Computer Science student, showcasing my projects, experiences, and passion for technology!"
about_me = "Hi! I'm Elan Mcclain, a freshman student at GT majoring in CS. I enjoy tinkering of all kinds, on both mechanical and digital projects. "
location = "📍I currently live in Atlanta, Georgia, but am from Armuchee Georgia."

#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "http://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=elan-mcclain-3aa69b349"
my_email_address = "emcclain8@gatech.edu"


education_data = [
    {
        '🎓 Degree': 'High School Diploma',
        '🏫 Institution': 'Armuchee High School',
        '📍 Location': 'Armuchee, GA',
        '📅 Graduation Date': 'May, 2025',
        'Photo': 'Images/Graduation.jpg'
    },
    {
        '🎓 Degree': 'Bachelor of Science in Computer Science',
        '🏫 Institution': 'Georgia Institute of Technology',
        '📍 Location': 'Atlanta, GA',
        '📅 Graduation Date': '2029',
        'Photo': 'Images/Me_n_Buzz.jpg'
    }
]
course_data = {
    "code":["CS 1301"], 
    "names":["Intro to CS"], 
    "semester_taken":["1st"],
    "skills":["Started with limited coding experience & learned how to write code and build projects!"],
    }
experience_data = {
    "Team Leader at Chick-Fil-A": (
        ["September 2022 - August 2025",
         "- Maintained satisfactory guest interface",
         "- Successful resolution of team member conflicts",
         "- Provided 2nd mile service to guests"],
        ["Images/Professional.jpg", "Images/Me_n_Twin.jpg"]
    ),
    "Team Member at Mcdonalds": (
    ["June 2022 - August 2022",
     "- Consistently provided above and beyond service to guests"],
    None
),
}

projects_data = {
    "Custom Industrial Part Manufacturing": ("My dad is an arborist and works with heavy equipment, and he was having trouble sourcing a part for some machinery, so using CAD software, I designed a replacement part for him and created it using additive manufacturing technology","Images/PartForDad.png", None),
    "Web App building": ("Using Python and Streamlit, I created this interactive web app to share information about who I am with others!", None, None),
    "Scratch Game Design": ("My mom works for a Christian Missions agency and several years ago she asked me to build her a simple platform game that she could use to help train churches on outreach, so I built her this game!", None, "https://scratch.mit.edu/projects/370260307/"),
}

programming_languages = {
    "Python": 7,
    "Scratch": 5
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Scratch": "🐱‍",
    "Python": "🐍",
}
other_icons = {"English": "🇬🇧",
    "Spanish":"🇲🇽"
}

#CHANGE BELOW
other_languages = {
    "English": "Fluent",
    "Spanish": "Conversational",
}
leadership_data = {
    "Team Leader at Chick-Fil-A": (["- Provided 3 years of leadership and guidance to our team"],"Images/Me_n_Trevor.jpg"),
    "Team Captain of Floyd County 4H Lifesmarts Team": (["- Led our team to 3 national competitions, securing 4th and 3rd place finishes"],"Images/Lifesmarts.jpg"),
}
activity_data = {
    "Key Club member 2022-2025": "- Participated in group community service projects"
}

car_timeline_data = [
    {
        'date': 'July 2021',
        'action': 'Bought',
        'car': '1990 Chevrolet Corvette',
        'details': 'My first car, absolutely gorgeous! Mint condition and cherry red. When I got it, the car only had 16 thousand miles and had been meticulously cared for.',  # ← Added comma
        'image': 'Images/Vette.jpg'
    },
    {
        'date': 'December 2022',
        'action': 'Wrecked',
        'car': '1990 Chevrolet Corvette',
        'details': 'Learned a lesson about driving the hard way. Put my first car into a ditch less than a mile from home.',  # ← Added comma
        'image': 'Images/Vettewreck.jpg'
    },
    {
        'date': 'October 2023',
        'action': 'Bought',
        'car': '1996 Camaro Z28',
        'details': 'Saved up some money and bought a hooptie muscle car! Not in the best shape but I was determined to fix it up. I learned how to work on cars with this car, and I did a number of jobs from changing spark plugs and brakes to touching up the paint.',  # ← Added comma
        'image': 'Images/Camaro.jpg'
    },
    {
        'date': 'August 2024',
        'action': 'Bought',
        'car': '2007 Mercedes Benz E550',
        'details': 'Decided to buy a responsible adult car for commuting back and forth to school.',  # ← Added comma
        'image': 'Images/Mercedes.jpg'
    },
    {
        'date': 'March 2025',
        'action': 'Sold',
        'car': '1996 Camaro Z28',
        'details': 'Sold the camaro to get funds to put toward buying a motorcycle.'
    },
    {
        'date': 'May 2025',
        'action': 'Sold',
        'car': '2007 Mercedes Benz E550',
        'details': 'Sold the Mercedes bacause reliability wasn\'t a strong suit for old German cars.'
    },
    {
        'date': 'June 2025',
        'action': 'Bought',
        'car': '1999 Pontiac Firebird Formula',
        'details': 'My current vehicle, and one I have wanted for a long time. Also my first manual car!',  # ← Added comma
        'image': 'Images/Firebird.jpg'
    }
]
hobbies_data = {
    "🚗 Cars": "Since I was just a child watching Top Gear on TV, I have always had a fascination with cars. In my 4 years of car ownership, I have enjoyed all aspects of cars, whether it be driving, doing maintenance, or chatting with other people at car shows. The only thing I don't enjoy doing with a car is sitting in traffic!",
    
    "🔫 Firearms": "I have been around firearms since I was a small boy shooting my dad's .22 rifle in the backyard, but it was my best friend who really drove my intrest in the hobby of firearms. From building to traget shooting to hunting, I enjoy all aspects of gun ownership and usage, especially when practiced with both fun and safety in mind.",
    
    "🏍️ Motorcycles": "Motorcycles combine my love for the mechanical with the thrill of riding. Though it may bring my parents some undue stress, I find nothing more enjoyable than a twisty backroad, nice weather, and the sound of my 2023 Kawasaki Z400.",
}

motorcycle_locations = [
        {
        "name": "The Pocket",
        "date": "April 2025",
        "image": "Images/pocket_ride.jpg", 
        "description": "A very pretty ride through the Chattahoochee National Forrest, the Pocket is reccomended as a road to ride by numerous online outlets and I am forutnate to have grown up less than 10 minutes away from this stretch of road."
    },
    {
        "name": "John's Mountain",
        "date": "May 2025",
        "image": "Images/Johnsmountain.jpg",
        "description": "A gorgeous ride through Calhoun Gap over John's Mountain. This road has a ton of twists and curves and, while fun, is also somewhat dangerous. The view from the top is worht it, however."
    },
    {
        "name": "Blood Mountain",
        "date": "September 2025", 
        "image": "Images/bloodmountain.jpg",
        "description": "A Beautiful ride in North Georgia, this was my first ever group ride with the GT Motorcycle Club, and hopefully the first of many!"
    },
]
