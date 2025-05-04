import streamlit as st
import requests

def get_github_user_data(username):

    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()

        name = user_data.get('name', 'No name found')
        bio = user_data.get('bio', 'No bio found')
        avatar_url = user_data.get('avatar_url', '')
        repos_url = user_data.get('repos_url', '')
        followers = user_data.get('followers', 0)
        following = user_data.get('following', 0)
        public_repos = user_data.get('public_repos', 0)
        company = user_data.get('company', 'Not available')
        location = user_data.get('location', 'Not available')
        blog = user_data.get('blog', 'Not available')

        repos_response = requests.get(repos_url)
        if repos_response.status_code == 200:
            repos_data = repos_response.json()
            repos_list = [(repo['name'], repo['html_url']) for repo in repos_data]
        else:
            repos_list = []
        
        return {
            'name': name,
            'bio': bio,
            'avatar_url': avatar_url,
            'repos': repos_list,
            'followers': followers,
            'following': following,
            'public_repos': public_repos,
            'company': company,
            'location': location,
            'blog': blog
        }
    else:
        return None

st.title("GitHub Profile Information")
username = st.text_input("Enter GitHub username:")

if username:
    user_data = get_github_user_data(username)
    if user_data:
        st.subheader(f"Name: {user_data['name']}")
        st.write(f"Bio: {user_data['bio']}")
        st.image(user_data['avatar_url'], caption='Profile Image', width=150)

        st.subheader("User Details:")
        st.write(f"Followers: {user_data['followers']}")
        st.write(f"Following: {user_data['following']}")
        st.write(f"Public Repositories: {user_data['public_repos']}")
        st.write(f"Company: {user_data['company']}")
        st.write(f"Location: {user_data['location']}")
        st.write(f"Blog: {user_data['blog']}")

        st.subheader("Repositories:")
        if user_data['repos']:
            for repo_name, repo_url in user_data['repos']:
                st.markdown(f"- [{repo_name}]({repo_url})")
        else:
            st.write("No repositories found.")
    else:
        st.error("User not found. Please check the username and try again.")
