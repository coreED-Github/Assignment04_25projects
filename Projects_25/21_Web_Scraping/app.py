import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_github_profile(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        username = url.strip().split("github.com/")[-1].strip("/")
        full_url = f"https://github.com/{username}"
        response = requests.get(full_url, headers=headers)

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        name_tag = soup.find('span', {'class': 'p-name'})
        name = name_tag.get_text(strip=True) if name_tag else "Name not found"

        bio_tag = soup.find('div', {'class': 'p-note'})
        bio = bio_tag.get_text(strip=True) if bio_tag else "No bio available"

        follower_tag = soup.find('a', href=f"/{username}?tab=followers")
        followers = follower_tag.find('span').text.strip() if follower_tag else "0"

        img_tag = soup.find('img', {'alt': 'Avatar'})
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

        return {
            "name": name,
            "bio": bio,
            "followers": followers,
            "image_url": img_url,
            "profile_link": full_url
        }

    except Exception as e:
        return None

st.set_page_config(page_title="GitHub Profile Scraper", layout="centered")
st.title("GitHub Profile Scraper")
st.write("Enter any public GitHub profile URL to view basic info:")

user_input = st.text_input("Enter GitHub Profile URL")

if st.button("Scrape Profile"):
    if user_input and "github.com" in user_input:
        data = scrape_github_profile(user_input)

        if data:
            if data["image_url"]:
                st.image(data["image_url"], width=150)
            else:
                st.warning("Profile image not found.")

            st.markdown(f"### 🧑 Name: {data['name']}")
            st.markdown(f"### 📄 Bio: {data['bio']}")
            st.markdown(f"### 👥 Followers: {data['followers']}")
            st.markdown(f"[Visit GitHub Profile]({data['profile_link']})", unsafe_allow_html=True)
        else:
            st.error("Could not fetch profile. Please check the URL or try again.")
    else:
        st.warning("Please enter a valid GitHub profile URL.")