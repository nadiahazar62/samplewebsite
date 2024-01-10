import streamlit as st

def main():
    st.set_page_config(page_title="My Company Website", layout="wide")

    st.title("My Company Website")

    page = st.experimental_get_query_params().get("page", ["Home"])[0]
    navigation_bar(page)

    if page == "Home":
        show_home()
    elif page == "About Us":
        show_about_us()
    elif page == "Careers":
        show_careers()

def navigation_bar(current_page):
    st.write(
        """
        <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            background-color: #f0f0f0;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .navbar a {
            margin-right: 1rem;
            text-decoration: none;
            color: black;
            font-weight: bold;
            font-size: 18px;
        }
        </style>
        <div class="navbar">
            <a href="?page=Home">Home</a>
            <a href="?page=About Us">About Us</a>
            <a href="?page=Careers">Careers</a>
        </div>
        """
    , unsafe_allow_html=True)

def show_home():
    st.header("Welcome to our Main Page!")
    st.write("This is the main page content.")

def show_about_us():
    st.header("About Us")
    st.write("We are an awesome company doing amazing things.")
    st.image("your_about_us_image.jpg", caption="Company Image", use_column_width=True)

def show_careers():
    st.header("Careers")
    st.write("Join our talented team! Check out our open positions.")
    st.button("View Open Positions")

if __name__ == "__main__":
    main()
