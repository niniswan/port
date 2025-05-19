import streamlit as st

st.set_page_config(page_title="Student Portfolio", layout="centered")

# Title and Subtitle
st.title("🎓 John Doe")
st.subheader("BS Computer Science Student")
st.write("Welcome to my online portfolio!")

# About Me Section
st.header("📌 About Me")
st.write("""
I'm a computer science student passionate about learning and building projects.
I enjoy solving problems using Python and exploring new tech.
""")

# Projects Section
st.header("🧠 Projects")
st.markdown("- **Grade Calculator** – Computes grades based on input scores.")
st.markdown("- **Attendance Tracker** – CLI app to track class attendance.")
st.markdown("- **Budget App** – Helps manage student expenses.")

# Skills Section
st.header("⚙️ Skills")
skills = ["Python", "HTML & CSS", "Git & GitHub", "Problem Solving"]
st.write(", ".join(skills))

# Contact Section
st.header("📬 Contact")
st.write("📧 Email: john.doe@example.com")
st.write("🔗 GitHub: [github.com/johndoe](https://github.com/johndoe)")
st.write("💼 LinkedIn: [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)")
