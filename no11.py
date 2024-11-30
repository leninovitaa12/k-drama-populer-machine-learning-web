import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Top Korean Drama List",
    page_icon=":heart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load data from CSV file (using correct separator and header)
drama_data = pd.read_csv("top_kdrama.csv", sep=",", header=None)  # Use the correct separator

# Assign column names (based on the CSV file)
drama_data.columns = ["Name", "Year of release", "Aired Date", "Aired On", "Episode", "Network", "Duration", "Content Rating", "Cast", "Genre", "Tags", "Rank", "Rating"]

# Sidebar navigation (dropdown)
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Data", "Complete Drama Data", "Visualization", "Contact"])

# Home Page
if page == "Home":
    st.title("Korean Drama List :heart:")
    st.image("rumah.jpg", caption="Korean Drama", use_container_width=True)
    st.markdown("Welcome to the Korean Drama List app! Explore and discover your favorite Korean dramas.")

    # Display poster images (replace with your actual poster URLs)
    st.header("Popular Korean Dramas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("drama1.jpeg", caption="Drama 1")
    with col2:
        st.image("drama2.jpeg", caption="Drama 2")
    with col3:
        st.image("drama3.jpeg", caption="Drama 3")
        
# Data Page
elif page == "Data":
    st.title("Drama Data")
    st.header("Drama List")
    st.dataframe(drama_data)

    st.header("Descriptive Statistics")
    st.write(drama_data.describe())

# Complete Drama Data Page
elif page == "Complete Drama Data":
    st.title("Complete Drama Data")
    st.header("Drama List")
    st.dataframe(drama_data)

    st.header("Highest Rated Drama")
    # Get the drama with the highest rank (Rank #1)
    highest_rated_drama = drama_data[drama_data['Rank'] == 'Rank #1']
    st.dataframe(highest_rated_drama)

    # Highway-mpg Chart
    st.header("Duration vs Rating (Highest Rated Drama)")
    fig, ax = plt.subplots()
    ax.scatter(highest_rated_drama["Duration"], highest_rated_drama["Rating"])
    ax.set_xlabel("Duration")
    ax.set_ylabel("Rating")
    ax.set_title("Duration vs Rating")
    st.pyplot(fig)

    # Horsepower Chart
    st.header("Episode vs Rating (Highest Rated Drama)")
    fig, ax = plt.subplots()
    ax.scatter(highest_rated_drama["Episode"], highest_rated_drama["Rating"])
    ax.set_xlabel("Episode")
    ax.set_ylabel("Rating")
    ax.set_title("Episode vs Rating")
    st.pyplot(fig)

# Visualization Page
elif page == "Visualization":
    st.title("Data Visualization")
    x_axis = st.selectbox("Select X-axis", drama_data.columns)
    y_axis = st.selectbox("Select Y-axis", drama_data.columns)

    fig, ax = plt.subplots()
    ax.scatter(drama_data[x_axis], drama_data[y_axis])
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title("Data Visualization")
    st.pyplot(fig)

# Contact Page
elif page == "Contact":
    st.title("Contact and About")
    st.header("About Me")
    st.write("This app was created by [Your Name].")
    st.write("I am a passionate data enthusiast with a keen interest in Korean dramas.")

    st.header("Contact Information")
    st.write("Email: [Your Email]")
    st.write("GitHub: [Your GitHub Profile URL]")
    st.write("Instagram: [Your Instagram Profile URL]")
    st.write("WhatsApp: [Your WhatsApp Number]")