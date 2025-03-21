import streamlit as st
import time
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import pandas as pd
import folium
from streamlit_folium import folium_static


# Set page config FIRST
st.set_page_config(page_title="Viva Palestine", layout="centered")

# Custom CSS for mobile-friendly navigation
st.markdown(
    """
    <style>
    /* Make sidebar wider */
    section[data-testid="stSidebar"] {
        width: 250px !important;
    }
    /* Increase button size and padding */
    .stButton button {
        width: 100%;
        padding: 15px 0;
        font-size: 18px;
    }
    /* Responsive font size for mobile */
    @media (max-width: 600px) {
        .stButton button {
            font-size: 20px;
            padding: 20px 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define pages
PAGES = {
    "Home": "home",
    "Palestinian Culture": "culture",
    "Palestinian Trivia": "trivia",
    "Palestinian Heritage": "heritage",
    "Palestinian Music & Poetry": "music_poetry",
    "Virtual Tour of Palestine": "virtual_tour",
    "Palestinian Art & Calligraphy": "art_calligraphy",
    "Support Palestine": "support",
    "User Contribution Wall": "contribution_wall"
}

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Navigation buttons
def navigate_to(page):
    st.session_state.current_page = page

# Sidebar for navigation
st.sidebar.title("Navigation")
for page_name, page_key in PAGES.items():
    if st.sidebar.button(page_name, key=page_key):
        navigate_to(page_key)


# Home Page
if st.session_state.current_page == "home":
    st.markdown(
        """
        <h1 style='text-align: center; color: green; animation: fadeIn 2s;'>
             Free Palestine App 
        </h1>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write("### Welcome, Freedom Fighter! ✊")
    placeholder = st.empty()
    message = "This is not just an app; it's a digital resistance! Here, you can explore, learn, and stand in solidarity with Palestine. Let's go!"
    for i in range(len(message) + 1):
        placeholder.markdown(f"#### {message[:i]}")
        time.sleep(0.05)



# Palestinian Culture Page
elif st.session_state.current_page == "culture":
    st.write("## Palestinian Culture 🎥")
    st.video("https://youtu.be/iuSN7Bl8OXE?si=s_1dVIpdRfJUqf26")

# Palestinian Trivia Page
elif st.session_state.current_page == "trivia":
    st.write("## Palestinian Trivia 🎉")
    st.write("Test your knowledge about Palestine!")

    questions = [
        ("What is the capital of Palestine?", ["Tel Aviv", "Jerusalem", "Ramallah", "Nablus"], "Jerusalem"),
        ("Which Palestinian city is famous for its ancient olive trees?", ["Jericho", "Nablus", "Hebron", "Jenin"], "Nablus"),
        ("What is the largest city in Palestine?", ["Ramallah", "Gaza", "Nablus", "Bethlehem"], "Gaza"),
        ("Which Palestinian dish is well known worldwide?", ["Falafel", "Mansaf", "Musakhan", "Hummus"], "Musakhan"),
        ("What is the name of the famous Palestinian scarf?", ["Hijab", "Shemagh", "Keffiyeh", "Ghutra"], "Keffiyeh"),
        ("Which sea borders Palestine?", ["Red Sea", "Mediterranean Sea", "Dead Sea", "Caspian Sea"], "Mediterranean Sea"),
        ("What is the name of the Palestinian resistance symbol?", ["Olive branch", "Dome of the Rock", "Handala", "Eagle"], "Handala"),
        ("Which Palestinian city is famous for its religious significance to Christians?", ["Nazareth", "Bethlehem", "Jerusalem", "Ramallah"], "Bethlehem"),
        ("What is the historic Palestinian marketplace called?", ["Bazaar", "Souq", "Medina", "Khan"], "Souq")
    ]

    for i, (question, options, correct_answer) in enumerate(questions):
        response = st.radio(question, options, index=None, key=f"q{i}")
        if response:
            if response == correct_answer:
                st.success("✅ Correct! ")
                st.balloons()
            else:
                st.error(f"❌ Nope! The right answer is {correct_answer}. Keep learning!")

# Palestinian Heritage Page
elif st.session_state.current_page == "heritage":
    st.write("## Palestinian Heritage 📸")

    rows = [
        ["C://Users//Lapcom Store//.streamlit//MVIMG_20190611_202033.jpg", "Al-Aqsa Mosque, one of Islam's holiest sites, located in the heart of Jerusalem. A symbol of faith, resilience, and Palestinian heritage."],
        ["C://Users//Lapcom Store//.streamlit//download.jpg", "Traditional Palestinian Women's Clothing – A beautiful display of embroidered dresses (thobes), a symbol of heritage, identity, and resilience."],
        ["C://Users//Lapcom Store//.streamlit//download (1).jpg", "Dome of the Rock – An iconic Islamic landmark in Jerusalem, known for its stunning golden dome and deep religious and historical significance."],
        ["C://Users//Lapcom Store//.streamlit//download (2).jpg", "Ancient Palestinian Olive Trees – A symbol of resilience and deep-rooted Palestinian heritage, these olive trees have stood for centuries, witnessing history and nurturing generations with their precious oil."],
        ["C://Users//Lapcom Store//.streamlit//download (3).jpg", "Buraq Wall – A sacred site in Jerusalem, known in Islamic tradition as the place where Prophet Muhammad tied his Buraq during the Night Journey (Isra and Mi'raj). It holds deep historical and religious significance for Muslims worldwide."],
        ["C://Users//Lapcom Store//.streamlit//download (4).jpg", "Jerusalem Walls – These historic walls surround the Old City of Jerusalem, standing as a witness to centuries of history, culture, and resilience. Built by the Ottomans in the 16th century, they protect some of the most sacred sites in the world, including Al-Aqsa Mosque and the Dome of the Rock."],
        ["C://Users//Lapcom Store//.streamlit//download (5).jpg", "Church of the Nativity - One of the holiest sites in Christianity, located in Bethlehem. It is believed to be the birthplace of Jesus Christ."],
        ["C://Users//Lapcom Store//.streamlit//4.jpg", "Church of the Holy Sepulchre – A sacred Christian site in Jerusalem, believed to be the location of Jesus Christ's crucifixion, burial, and resurrection."],
        ["C://Users//Lapcom Store//.streamlit//12.jpg", "Khan al-Umdan – A historic caravanserai in Acre, Palestine, built during the Ottoman era. It was a key center for trade and commerce, known for its grand columns and stunning architecture."],
        ["C://Users//Lapcom Store//.streamlit//14.jpg", "The Shrine of the Báb and the Bahá'í Gardens – A UNESCO World Heritage Site in Haifa, featuring breathtaking terraced gardens and the golden-domed shrine, a sacred site in the Bahá'í faith."]
    ]

    for i in range(0, len(rows), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.image(rows[i][0], caption=rows[i][1], use_container_width=True)
        if i+1 < len(rows):
            with col2:
                st.image(rows[i+1][0], caption=rows[i+1][1], use_container_width=True)

# Palestinian Music & Poetry Page
elif st.session_state.current_page == "music_poetry":
    st.write("## Palestinian Music & Poetry 🎶📖")
    st.audio("C://Users//Lapcom Store//.streamlit//9wymWT3oql0.mp3")
    st.write("**Poem by Mahmoud Darwish**")
    st.markdown("""
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .fade-in {
                animation: fadeIn 3s;
            }
        </style>
        <p class='fade-in'>\"We have on this land that which makes life worth living...\"</p>
        """, unsafe_allow_html=True)

# Virtual Tour of Palestine Page
elif st.session_state.current_page == "virtual_tour":
    st.write("## Virtual Tour of Palestine 🗺️")

    # Define a folium map centered on Palestine
    m = folium.Map(location=[31.9522, 35.2332], zoom_start=8, max_bounds=True, tiles="CartoDB dark_matter")

    # Add markers for major Palestinian cities
    locations = {
        "Jerusalem": [31.7683, 35.2137],
        "Ramallah": [31.8996, 35.2042],
        "Nablus": [32.2211, 35.2544],
        "Gaza": [31.5375, 34.4889],
        "Hebron": [31.5326, 35.0998],
        "Bethlehem": [31.7054, 35.2024],
        "Jenin": [32.4634, 35.2958]
    }

    for city, coords in locations.items():
        folium.Marker(coords, popup=city, icon=folium.Icon(color="green")).add_to(m)

    # Set map boundaries to restrict zooming out
    m.fit_bounds([[31.2, 34.2], [32.6, 35.7]])

    # Display the map
    folium_static(m)

    st.write("Explore Palestine with 360-degree views: [Google Maps](https://www.google.com/maps/place/Palestine)")

# Palestinian Art & Calligraphy Page
elif st.session_state.current_page == "art_calligraphy":
    st.write("## Palestinian Art & Calligraphy 🎨")
    st.image("C://Users//Lapcom Store//.streamlit//download19.jpg", caption="Arabic Calligraphy")

# Support Palestine Page
elif st.session_state.current_page == "support":
    st.write("## Support Palestine 💚")
    st.write("Sign petitions: [Click Here](https://www.change.org/search?q=palestine)")
    st.write("Recommended Books & Movies:")
    st.write("- **Book:** \"Mornings in Jenin\" by Susan Abulhawa")
    st.write("- **Movie:** \"Gaza Fights for Freedom\" (2019)")

# User Contribution Wall Page
elif st.session_state.current_page == "contribution_wall":
    st.write("## User Contribution Wall 📜")
    user_message = st.text_area("Leave a message of support:")
    if st.button("Submit Message"):
        st.write("Thank you for your support! Your message has been added.")

# Footer
st.write("---")
st.markdown("""
    <h2 style='text-align: center; color: red;'> Remember... </h2>
    <p style='text-align: center; font-size:20px; color: green;'>
        ✊ Palestine will always be free! <br>
        🌍 The land belongs to its people! <br>
        ❤️ Keep supporting, keep resisting!  
    </p>
""", unsafe_allow_html=True)

# Palestinian Flag Animation at the End
if st.button("Wave the Flag! ", key="wave_flag_end"):
    with st.spinner("Raising the flag..."):
        time.sleep(2)
    st.success("The Palestinian flag is waving high! ")
    st.image("C://Users//Lapcom Store//.streamlit//images.jpg", caption="Palestine will always be free! ✊", use_container_width=True)
