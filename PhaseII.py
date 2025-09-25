import streamlit as st
import time

def show_quiz():
    st.title("Which motorcycle is right for me?")
    st.write("Answer these questions to find out which motorcycle best fits your needs!")
    
    if 'started' not in st.session_state:
        st.session_state.started = False
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'current' not in st.session_state:
        st.session_state.current = 0
    
    qs = [
        {
            "question": "What's your ideal riding style?",
            "type": "radio",
            "options": ["Cruising leisurely", "High-speed adrenaline", "Off-road adventures", "Daily commuting"],
            "key": "style"
        },
        {
            "question": "What motorcycle features do you prioratize most? (Select all that apply)",
            "type": "multiselect",
            "options": ["comfort", "performance and speed", "reliability", "Fuel efficiency", "Storage capacity", "Off-roading ability"],
            "key": "features"
        },
        {
            "question": "What's the perfect length of a ride for you?",
            "type": "number",
            "min": 1,
            "max": 500,
            "default": 50,
            "key": "distance",
            "help": "Enter the average distance in miles for your typical motorcycle rides"
        },
        {
            "question": "Which riding environment appeals to you most?",
            "type": "radio",
            "options": ["Highway touring", "City streets", "Twisty mountain backroads", "Mixed terrain (on/off road)"],
            "key": "environment"
        },
        {
            "question": "Your riding experience level:",
            "type": "radio",
            "options": ["Beginner (0-1 years)", "Intermediate (2-5 years)", "Advanced (6+ years)", "Expert (10+ years)"],
            "key": "experience"
        }
    ]
    
    results = {
        "cruiser": {
            "name": "Harley-Davidson Street Glide",
            "description": "You want a machine that is focused on the journey, not the destination. The Harley Davidson Street Glide is just the bike for you! With 117 cubic inches of American iron, you can cruise the highways to your heart's content, and do so in maximum comfort and style. ",
            "image": "Images/HDstreetglide.jpg"
        },
        "sport": {
            "name": "Kawasaki Ninja ZX6R",
            "description": "For you, speed and performance is the name of the game. If you want a bike that will put most 6 figure supercars to shame, look no further than the Kawasaki ZX6R! With a 15,000 RPM redline you'll be carving canyons and chasing laptimes like a pro.",
            "image": "Images/ZX6R.jpg"
        },
        "adventure": {
            "name": "BMW GS Adventure",
            "description": "You're an explorer at heart who wants a bike that can go anywhere from city streets to mountain trails. The BMW GS is a balance between a long distance cuiser and an OHV Trail killer, and is exactly what you need for your next adventure.",
            "image": "Images/bmwgs.jpg"
        },
        "standard": {
            "name": "Royal Enfield Hunter 350",
            "description": "Practical, easy to learn, and fun! Do you want reliability, timeless styling, and practicality, all while keeping the fun-to-ride nature of a sports bike? Look no further than the Royal Enfield Hunter 350! Perfect for daily riding to the office, or weekend fun on the backroads.",
            "image": "Images/REhunter350.jpg"
        }
    }
    
    if not st.session_state.started:
        show_intro()
    elif len(st.session_state.answers) < len(qs):
        show_question(qs)
    else:
        show_results(results)

def show_intro():
    st.markdown("""
    ### How it works:
    - Answer 5 questions about your riding preferences
    - Get matched with the perfect motorcycle for the way you want to ride
    
    Are you ready to find out what bike is the perfect fit for you?
    """)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start Quiz", use_container_width=True):
            st.session_state.started = True
            st.rerun()

def show_question(qs):
    current = st.session_state.current
    q = qs[current]
    progress = (current + 1) / len(qs)
    st.progress(progress, text=f"Question {current + 1} of {len(qs)}")
    
    st.markdown(f"### {q['question']}")
    answer = None
    
    if q['type'] == 'radio':
        answer = st.radio(
            "Choose your answer:",
            q['options'],
            key=f"q_{current}"
        )
    elif q['type'] == 'multiselect':
        answer = st.multiselect(   #NEW
            "Select all that apply:",
            q['options'],
            key=f"q_{current}"
        ) 
    elif q['type'] == 'number':
        answer = st.number_input( #NEW
            q.get('help', 'Enter a number:'),
            min_value=q['min'],
            max_value=q['max'],
            value=q['default'],
            key=f"q_{current}"
        )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if current > 0:
            if st.button("Previous"):
                st.session_state.current -= 1
                st.rerun()
    
    with col3:
        canproceed = False
        if q['type'] == 'radio' and answer:
            canproceed = True
        elif q['type'] == 'multiselect' and len(answer) > 0:
            canproceed = True
        elif q['type'] == 'number' and answer is not None:
            canproceed = True
        
        if canproceed:
            if st.button("Next"):
                st.session_state.answers[q['key']] = answer
                st.toast("Answer saved!", icon="✅") #NEW

                if current < len(qs) - 1:
                    st.session_state.current += 1
                st.rerun() #NEW
        else:
            st.button("Next", disabled=True, help="Please provide an answer to continue")

def show_results(results):
    with st.spinner("Analyzing your answers..."): #NEW
        time.sleep(1)
    st.balloons() #NEW
    
    resulttype = calc_result(st.session_state.answers)
    result = results[resulttype]
    
    st.markdown("## Your Perfect Motorcycle Match!")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"### {result['name']}")
        st.write(result['description'])
        
        with st.expander("Your Answers Summary"):
            for key, value in st.session_state.answers.items():
                if isinstance(value, list):
                    formatted = ", ".join(value)
                else:
                    formatted = str(value)
                st.write(f"**{key.replace('_', ' ').title()}:** {formatted}")
    
    with col2:
        try:
            st.image(result['image'], caption=result['name'], width=300)
        except:
            st.info(f"Image of {result['name']}")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Take Quiz Again"):
            st.session_state.started = False
            st.session_state.answers = {}
            st.session_state.current = 0
            st.rerun()

def calc_result(answers):
    scores = {
        "cruiser": 0,
        "sport": 0, 
        "adventure": 0,
        "standard": 0
    }
    
    style = answers.get('style')
    if style == 'Cruising leisurely':
        scores['cruiser'] += 3
    elif style == 'High-speed adrenaline':
        scores['sport'] += 3
    elif style == 'Off-road adventures':
        scores['adventure'] += 3
    elif style == 'Daily commuting':
        scores['standard'] += 2
        scores['sport'] += 1
    
    features = answers.get('features', [])
    for f in features:
        if f == 'Comfort':
            scores['cruiser'] += 2
            scores['adventure'] += 1
        elif f == 'performance and speed':
            scores['sport'] += 3
        elif f == 'reliability':
            scores['adventure'] += 2
            scores['standard'] += 2
        elif f == 'Fuel efficiency':
            scores['standard'] += 2
            scores['cruiser'] += 1
        elif f == 'Storage capacity':
            scores['adventure'] += 2
            scores['cruiser'] += 1
        elif f == 'Off-roading ability':
            scores['adventure'] += 3
    
    distance = answers.get('distance', 50)
    if distance <= 25:
        scores['standard'] += 2
        scores['sport'] += 1
    elif distance <= 100:
        scores['standard'] += 1
        scores['sport'] += 1
        scores['adventure'] += 1
    elif distance <= 200:
        scores['adventure'] += 2
        scores['cruiser'] += 2
    else:
        scores['cruiser'] += 3
        scores['adventure'] += 2
    
    env = answers.get('environment')
    if env == 'Highway touring':
        scores['cruiser'] += 3
        scores['adventure'] += 1
    elif env == 'City streets':
        scores['standard'] += 3
        scores['sport'] += 1
    elif env == 'Twisty mountain backroads':
        scores['sport'] += 3
        scores['standard'] += 1
    elif env == 'Mixed terrain (on/off road)':
        scores['adventure'] += 3
    
    exp = answers.get('experience')
    if 'Beginner' in exp:
        scores['standard'] += 2
        scores['cruiser'] += 1
    elif 'Intermediate' in exp:
        scores['standard'] += 1
        scores['sport'] += 1
        scores['adventure'] += 1
        scores['cruiser'] += 1
    elif 'Advanced' in exp:
        scores['sport'] += 2
        scores['adventure'] += 2
    elif 'Expert' in exp:
        scores['sport'] += 3
        scores['adventure'] += 1
    
    return max(scores, key=scores.get)
