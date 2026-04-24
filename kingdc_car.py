import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Car Simulator", page_icon="🚗", layout="wide")
st.title("🚗 KINGDC CAR SHOWROOM SIMULATOR")

# --- CAR DATABASE (STABLE IMAGE LINKS) ---
CARS = {
    "Toyota Supra": {
        "speed": 70,
        "handling": 60,
        "price": 500,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3e/2019_Toyota_Supra_%28A90%29_IMG_3733.jpg"
    },
    "BMW M3": {
        "speed": 75,
        "handling": 70,
        "price": 800,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/44/2018_BMW_M3_Competition_Automatic_3.0.jpg"
    },
    "Tesla Model S": {
        "speed": 85,
        "handling": 80,
        "price": 1200,
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_Model_S_Plaid_front_view.jpg"
    },
    "Lamborghini Huracan": {
        "speed": 95,
        "handling": 85,
        "price": 2000,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/2019_Lamborghini_Huracan_Evo_Front.jpg"
    }
}

# --- SESSION STATE ---
if "money" not in st.session_state:
    st.session_state.money = 1500

if "garage" not in st.session_state:
    st.session_state.garage = ["Toyota Supra"]

if "current_car" not in st.session_state:
    st.session_state.current_car = "Toyota Supra"

# --- SIDEBAR ---
st.sidebar.header("👤 Player Stats")
st.sidebar.write("💰 Money:", st.session_state.money)

car_choice = st.sidebar.selectbox("Select Car", st.session_state.garage)
st.session_state.current_car = car_choice

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🚗 Garage", "🛒 Dealership", "🏁 Race"])

# ================= GARAGE =================
with tab1:
    st.subheader("Your Garage")

    for car in st.session_state.garage:
        stats = CARS[car]

        st.markdown(f"### 🚗 {car}")

        try:
            st.image(stats["image"], use_container_width=True)
        except:
            st.warning("Image failed to load")

        st.write(f"⚙️ Speed: {stats['speed']} | Handling: {stats['handling']}")
        st.divider()

# ================= DEALERSHIP =================
with tab2:
    st.subheader("Car Dealership")

    for car, stats in CARS.items():

        st.markdown(f"### 🚗 {car}")

        try:
            st.image(stats["image"], use_container_width=True)
        except:
            st.warning("Image not available")

        st.write(f"💰 Price: {stats['price']}")

        if st.button(f"Buy {car}"):
            if st.session_state.money >= stats["price"]:
                st.session_state.money -= stats["price"]

                if car not in st.session_state.garage:
                    st.session_state.garage.append(car)

                st.success(f"You bought {car}!")
                st.rerun()
            else:
                st.error("Not enough money!")

        st.divider()

# ================= RACE =================
with tab3:
    st.subheader("🏁 Race Mode")