"""
AI Trip Planner for India
Run:
    pip install streamlit
    streamlit run app.py

This starter app uses sample cost estimates, not live prices.
"""

import streamlit as st
import random

st.set_page_config(page_title="AI Trip Planner India", page_icon="🇮🇳", layout="centered")

DESTINATIONS = {
    "Goa": {
        "daily_hotel": 1800, "daily_food": 700, "daily_local": 400,
        "travel_from_mumbai": 1800,
        "places": ["Baga Beach", "Fort Aguada", "Fontainhas", "Dudhsagar Falls"]
    },
    "Jaipur": {
        "daily_hotel": 1500, "daily_food": 600, "daily_local": 350,
        "travel_from_mumbai": 2200,
        "places": ["Hawa Mahal", "Amber Fort", "City Palace", "Jantar Mantar"]
    },
    "Manali": {
        "daily_hotel": 2000, "daily_food": 700, "daily_local": 600,
        "travel_from_mumbai": 3500,
        "places": ["Hadimba Temple", "Old Manali", "Solang Valley", "Mall Road"]
    },
    "Kerala": {
        "daily_hotel": 2200, "daily_food": 800, "daily_local": 600,
        "travel_from_mumbai": 3000,
        "places": ["Alleppey backwaters", "Fort Kochi", "Munnar tea gardens", "Kovalam Beach"]
    },
    "Mumbai": {
        "daily_hotel": 2200, "daily_food": 800, "daily_local": 500,
        "travel_from_mumbai": 300,
        "places": ["Gateway of India", "Marine Drive", "Elephanta Caves", "Siddhivinayak Temple"]
    },
    "Rishikesh": {
        "daily_hotel": 1400, "daily_food": 600, "daily_local": 350,
        "travel_from_mumbai": 2800,
        "places": ["Laxman Jhula area", "Triveni Ghat", "Beatles Ashram", "Neer Garh Waterfall"]
    },
    "Udaipur": {
        "daily_hotel": 1700, "daily_food": 650, "daily_local": 400,
        "travel_from_mumbai": 2300,
        "places": ["City Palace", "Lake Pichola", "Jagdish Temple", "Saheliyon-ki-Bari"]
    },
    "Delhi": {
        "daily_hotel": 1800, "daily_food": 700, "daily_local": 450,
        "travel_from_mumbai": 2500,
        "places": ["Red Fort", "India Gate", "Humayun's Tomb", "Qutub Minar"]
    },
}

def rupees(amount):
    return f"₹{amount:,.0f}"

st.title("🇮🇳 AI Trip Planner India")
st.write("Plan a trip, explore places, and keep an eye on your budget.")

with st.form("trip_form"):
    col1, col2 = st.columns(2)
    with col1:
        start_city = st.selectbox("Starting city", ["Mumbai", "Pune", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata"])
        destination = st.selectbox("Destination", list(DESTINATIONS.keys()))
        days = st.slider("Trip duration (days)", 1, 14, 3)
    with col2:
        people = st.number_input("Number of travellers", min_value=1, max_value=20, value=2)
        budget = st.number_input("Total budget (₹)", min_value=1000, max_value=1000000, value=10000, step=500)
        travel_style = st.selectbox("Travel style", ["Budget", "Balanced", "Comfort"])
    interests = st.multiselect(
        "What do you enjoy?",
        ["Beaches", "Nature", "History", "Food", "Adventure", "Shopping", "Culture"],
        default=["Nature", "Food"]
    )
    submitted = st.form_submit_button("Create my trip plan")

if submitted:
    place = DESTINATIONS[destination]
    style_factor = {"Budget": 0.75, "Balanced": 1.0, "Comfort": 1.5}[travel_style]
    hotel = place["daily_hotel"] * style_factor * days * people
    food = place["daily_food"] * style_factor * days * people
    local = place["daily_local"] * days * people
    # A rough travel estimate per person, adjusted slightly for starting city.
    travel = place["travel_from_mumbai"] * people
    if start_city == destination:
        travel = 0
    elif start_city == "Pune":
        travel *= 0.85
    elif start_city in ["Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata"]:
        travel *= 1.25
    travel = round(travel)
    sightseeing = round(250 * days * people)
    emergency = round((hotel + food + local + travel + sightseeing) * 0.10)
    total = round(hotel + food + local + travel + sightseeing + emergency)
    per_person = total / people

    st.subheader(f"Your {days}-day plan for {destination}")
    st.write(f"**Starting from:** {start_city}  ·  **Travellers:** {people}  ·  **Style:** {travel_style}")
    st.write(f"**Estimated total:** {rupees(total)}")
    st.write(f"**Estimated per person:** {rupees(per_person)}")

    if total <= budget:
        st.success(f"Great! The estimated trip is within your budget by {rupees(budget - total)}.")
    else:
        st.warning(f"This plan is over budget by {rupees(total - budget)}. Try Budget style, fewer days, or a lower-cost destination.")

    st.subheader("Budget breakdown")
    breakdown = {
        "Travel to destination": travel,
        "Hotel / stay": round(hotel),
        "Food": round(food),
        "Local transport": round(local),
        "Sightseeing / activities": sightseeing,
        "Emergency buffer (10%)": emergency,
    }
    st.bar_chart(breakdown)
    for category, amount in breakdown.items():
        st.write(f"- **{category}:** {rupees(amount)}")

    st.subheader("Day-wise itinerary")
    places = place["places"][:]
    random.shuffle(places)
    for day in range(days):
        first = places[(day * 2) % len(places)]
        second = places[(day * 2 + 1) % len(places)]
        st.markdown(f"**Day {day + 1}**")
        st.write(f"Morning: {first}")
        st.write(f"Afternoon: {second}")
        st.write("Evening: Explore a nearby market, try local food, and rest.")

    if interests:
        st.subheader("Personalised suggestions")
        st.write(f"Your interests: {', '.join(interests)}.")
        if "Food" in interests:
            st.write("Try local dishes and check restaurant prices before ordering.")
        if "Nature" in interests:
            st.write("Keep time for a park, viewpoint, beach, or nature walk.")
        if "History" in interests or "Culture" in interests:
            st.write("Check monument opening times and ticket prices before visiting.")
        if "Adventure" in interests:
            st.write("Book adventure activities with verified operators and check safety requirements.")

    st.caption("Important: These are illustrative estimates. Actual transport fares, hotel prices, opening times, and ticket costs change by date and season. Check current prices before booking.")
