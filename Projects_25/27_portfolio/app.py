from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "file_" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "saira.jpg"

st.set_page_config(page_title="Digital CV | Saira", page_icon=":wave:")

NAME = "Saira"
DESCRIPTION = "School Principal | Math Teacher | E-Commerce Developer | Programmer | Freelancer"
EMAIL = "sairanasir853@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/saira-nasir-935bb1230",
    "GitHub": "https://github.com/coreED-Github",
    "Facebook": "https://www.facebook.com/share/1ALRVFEn2n/"
}
PROJECTS = {
    "🏆 E-Commerce Marketplace with Sanity CMS & Next.js": "https://marketplace-home-store-ecommerce-website.vercel.app/",
    "🏆 E-Commerce website with Sanity CMS & Next.js": "https://e-commerce-website-practise.vercel.app/",
    "🏆 E-Commerce website with Next.js & Tailwind CSS": "https://chocolate-cake-shop.vercel.app/",
    "🏆 My Portfolio with Tailwind CSS & Next.js": "https://my-portolio-project.vercel.app/",
    "🏆 API Integration country info Website with Next.js and APIs": "https://classassignment-15-country.vercel.app",
    "🏆 Resume builder using HTML and CSS": "https://resume-builder-005.vercel.app/",
}

# Sidebar
st.sidebar.title("Saira Nasir Portfolio")
nav_selection = st.sidebar.radio("Go to", ["Home", "Education", "Skills", "Experience", "Projects", "Contact"])



with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

if nav_selection == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button("📄 Download Resume", data=PDFbyte, file_name=resume_file.name, mime="application/octet-stream")
        st.write("📫", EMAIL)

    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].markdown(f"[{platform}]({link})")

elif nav_selection == "Education":
    st.subheader("Education")
    st.write("---")
    st.markdown("""
- 🎓 Bachelor of Commerce - Karachi University  
- 📍 Location: Karachi, Pakistan  
- 🗓 Duration: 2021 - 2024
    """)

elif nav_selection == "Skills":
    st.subheader("Technical Skills")
    st.write("---")
    st.markdown("""
- 👩‍💻 Programming: Python, SQL, JavaScript, TypeScript, Next.js, React, HTML, CSS  
- 📊 Data Science: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- ☁ CMS & APIs: Sanity CMS, EasyPost, Shippo, AliExpress APIs  
- 🎨 Frontend: TailwindCSS, Responsive Design  
- 🧪 Testing: Cypress, UAT, Lighthouse Audits  
    """)

elif nav_selection == "Experience":
    st.subheader("Experience")
    st.write("---")
    st.markdown("""
*🚧 School Principal | Math Teacher*  
2018 - Present  
- Teaching Data Science & mentoring students in real-world projects.

*🚧 Freelance Developer | E-Commerce Projects*  
2024 - Present  
- Built and deployed marketplace platforms using Next.js & Sanity CMS.  
- Integrated dynamic shipment tracking APIs and performed UAT for clients.
    """)

elif nav_selection == "Projects":
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.markdown(f"[{project}]({link})")

elif nav_selection == "Contact":
    st.subheader("Get in Touch")
    st.write("---")
    st.write(f"📫 Email: {EMAIL}")
    st.write("📱 Phone: 03492908035")
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].markdown(f"[{platform}]({link})")
    st.info("Feel free to reach out for collaborations, mentorship, or freelance work!")

# Footer
st.markdown("""
<hr style='border:1px solid #ccc'/>
<div style='text-align:center; color:gray; font-size: small;'>
    Built with ❤ by Saira | © 2025
</div>
""", unsafe_allow_html=True)