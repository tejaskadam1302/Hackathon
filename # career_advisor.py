# career_advisor.py

import streamlit as st
import google.generativeai as genai

# 1. Initialize Gemini client
genai.configure(api_key="AIzaSyBatYOCOJqgyp8haIH13Jvv_oOxD1gYXwA")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Streamlit App Title
st.set_page_config(page_title="AI Career & Skills Advisor", layout="centered")
st.title("🎓 AI-Powered Career & Skills Advisor")
st.write("Get personalized career suggestions, skill roadmaps, and learning resources powered by AI.")

# 3. User Inputs
education = st.text_input("📘 Current Education (e.g., B.Tech Electronics, MBA, 12th Science)")
skills = st.text_area("🛠 Current Skills (comma separated, e.g., Python, Excel, Communication)")
interests = st.text_area("💡 Interests (e.g., AI, Marketing, Design, Finance)")

if st.button("Get Career Suggestions"):
    with st.spinner("Analyzing your profile..."):
        # 4. AI Prompt
        prompt = f"""
        You are a career advisor.
        The user has the following profile:
        Education: {education}
        Skills: {skills}
        Interests: {interests}

        Suggest 3 suitable career paths. 
        For each career path, provide:
        1. Short description of the role.
        2. Required skills in learning order (beginner → advanced).
        3. Free and paid learning resources.
        4. Possible entry-level job titles.
        5. Future growth opportunities.

        Format output with clear headings and bullet points.
        """

        # 5. Gemini API Call
        response = model.generate_content(prompt)
        
        # 6. Show Result
        st.success("Here are your personalized career suggestions:")
        st.markdown(response.text)

