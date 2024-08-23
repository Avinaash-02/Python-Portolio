from pathlib import Path
import streamlit as st
from PIL import Image
#---------Path-------------
current_dir=Path(__file__).parent if "__file__"in locals() else Path.cwd()
#current working directory
css_file=current_dir/"styles"/"style.css"
resume_file=current_dir/"Assests"/"Avinaash Venkat Resume (3).pdf"
profile_pic=current_dir/"Assests"/"imageavi.png"
PAGE_TITLE="Digital CV |🧪Avinaash Venkat🧪"
PAGE_ICON=":👾"
NAME="⚡Avinaash   Venkat⚡"
DESCRIPTION="""
A final year Student with a passion to achieve my dreams and goals.
Currenlty Desired to learn DSA and other tech stack !!!!
"""
EMAIL="bass.avinaashvenkat@gmail.com"
SOCIAL_MEDIA={
    "Instagram":"https://www.instagram.com/zacky_naash/",
    "LinkedIn":"https://www.linkedin.com/in/avinaash-venkat-b-852671222?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "Youtube":"https://www.youtube.com/@Zits786",
    "Twitter":"https://x.com/home",
    "Github":"https://www.github.com/Avinaash-02",

}

#Configuration
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
# st.title("Hello there !")

#------LOAD CSS , PDF and PROFILE PIC------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb")as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)


#------Hero Section----------
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Avinaash Venkat Resume (3).pdf",
        mime="application/octect-stream",
    )
st.write("🩻",EMAIL)

#Social Links

st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for i,(platform,link)in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f"[{platform}]({link})")#formatting
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
-⚡Interned as a Content Developer in TriHusLab and worked as a Web designer and Devloper

-⚡Having Knowledge in working with Python and its Modules

-⚡Actively learning DSA and Practising in Leetcode,GFG,Skillrack etc.

-⚡Having a good Speaking skills and Leadership skills, Ready to lead a team
"""

)
#Skills
st.write("#")
st.subheader("Tech Stack(aka)Hard Skills")
st.write(
    """
🤖Programming: Python(Numpy, Pandas),Java ,SQL

📥Data Visualization: Power-BI

🗂️Database:SQL

🖥️Web Development: HTML,Javascript, CSS

⚗️Design: UI/UX Design - FIGMA


    """

)
#Work History
st.write("#")
st.subheader("Work History and Experience")
st.write("-------------")
#JOB1
st.write("Content Developer || TriHusLab")
st.write("Oct-Nov(2023)")
st.write(
    """
➤ Worked on Marketing and strategical Position to enhance the feasibility especially on scaling their business by convincing
their  product.

➤ Utilized the design software such as FIGMA, Adobe XD for prototype Design and developed the Website

➤ Developed integration requirements for their  Website

➤ Built an no code WIX Website for the brand.

➤ Acquired knowledge of Agile development processes, learned how to effectively collaborate with a team, and
expanded technical proficiency with various tech stacks.

➤ Tech Stack: HTML, CSS, JavaScript , React , Figma

"""
)
#JOB-2
st.write("#")
st.subheader("Projects")
st.write("-----------------")
st.subheader("Armour-Evault | React JS,CSS,Metamask,Pinata Storage")
st.write(
"""
➤ Developed a user-friendly Digital storage using Blockchain Technology on  stack upon with React JS, which includes Payment
Gateway for a seamless and Secured experience.

➤ Integrated MetaMask so  that users can securely log in and register, keeping their information safe.

➤ Utilized Pinata for handling Storage , providing a secure and trustworthy platform for Data transactions.

➤ Created a module with Chat application with Judicial Members can chat an transfer the Transaction Data Key Privately
among them.


"""
)
st.write("#")
st.write("-----------------")
st.subheader("Fake Manipulation Detection| Python, Flask, Alan AI ,News API  ")
st.write(
"""
➤ Developed an user friendly interface for the public

➤ Implemented authentication and authorization functionalities for both users and administrators.

➤ Users and Administrators have the capability to report incidents.

➤ Administrators have additional features, including viewing all incident reports and managing user status, and also have the
ability to view, edit, filter, and delete user data.


"""
)
#Certifications
st.write("#")
st.subheader("Certifications")
st.write("-----------------")
st.subheader("")
st.write(
"""

• NPTEL-Big Data Analytics-2023 || Score 91% .

• NPTEL-Introduction to DBMS-2023 || Score 54%.

• NPTEL-Cloud Computing-2024 || Score 80%.

• UDEMY-Javascript QR Code Generator.

• UDEMY - Web Development Course by Angela Yu


"""
)
with st.container():
    st.write("--------")
    st.write("Get in Touch With Me")
    st.write("##")
contact_form="""
<form action="https://formsubmit.co/bass.avinaashvenkat@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name and Query" required>
     <input type="hidden" name="_captcha" value="false">
     <input type="email" name="email"placeholder="Your E-mail" required>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column :
    st.empty()
