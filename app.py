import streamlit as st
import google.generativeai as genai
import os
from prompts import get_solution_prompt, get_practice_prompt

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(page_title="MathMentor AI", page_icon="🧮", layout="centered")

st.title("🧮 MathMentor AI")
st.markdown("*Step-by-step math help for K-12 students — because understanding the 'why' matters more than just the answer.*")

# Grade selector
grade = st.selectbox("Select your grade:", 
    ["Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])

# Problem input
problem = st.text_area("Enter your math problem:", 
    placeholder="e.g. Find the roots of 2x² + 5x - 3 = 0",
    height=100)

if st.button("🔍 Solve & Explain", use_container_width=True):
    if problem.strip():
        with st.spinner("Thinking step by step..."):
            # Get solution
            solution_prompt = get_solution_prompt(problem, grade)
            solution = model.generate_content(solution_prompt).text
            
            st.markdown("### 📝 Step-by-Step Solution")
            st.markdown(solution)
            
            # Get practice question
            practice_prompt = get_practice_prompt(problem, grade)
            practice = model.generate_content(practice_prompt).text
            
            st.divider()
            st.markdown("### 🎯 Try This Practice Problem")
            st.info(practice)
    else:
        st.warning("Please enter a math problem first!")

st.markdown("---")
st.caption("Built for Cuemath's vision of teaching math the right way. | Made by Anisha")
