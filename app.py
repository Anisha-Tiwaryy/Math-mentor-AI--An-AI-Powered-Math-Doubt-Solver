import streamlit as st
from gemini_helper import solve_math_doubt
from PIL import Image
import os

# ─── Page Configuration ───────────────────────────────────────
st.set_page_config(
    page_title="MathMentor AI",
    page_icon="🧮",
    layout="centered"
)

# ─── Custom CSS Styling ───────────────────────────────────────
st.markdown("""
    <style>
        .main {
            background-color: #f8f9ff;
        }
        .stButton>button {
            background-color: #4A90D9;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #357ABD;
            color: white;
        }
        .answer-box {
            background-color: #ffffff;
            border-left: 5px solid #4A90D9;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .title-text {
            font-size: 42px;
            font-weight: 800;
            color: #1a1a2e;
            text-align: center;
        }
        .subtitle-text {
            font-size: 18px;
            color: #555;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ─── Load Banner Image ────────────────────────────────────────
# This gets the folder where app.py is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to mm.png
banner_path = os.path.join(BASE_DIR, "mm.png")

# Check if file exists and show it
if os.path.exists(banner_path):
    banner = Image.open(banner_path)
    st.image(banner, use_container_width=True)
else:
    st.warning(f"⚠️ Banner image not found at: {banner_path}")

st.markdown('<p class="title-text">🧮 MathMentor AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Your personal AI-powered math tutor — type a doubt or upload a problem photo!</p>', unsafe_allow_html=True)

st.divider()

# ─── Session State for Chat History ───────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ─── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    logo_path = os.path.join(BASE_DIR, "mm.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)
    st.title("📚 MathMentor AI")
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. 📝 Type your math doubt")
    st.markdown("2. 📸 OR upload a photo of your problem")
    st.markdown("3. 🔍 Click **Solve My Doubt**")
    st.markdown("4. ✅ Get step-by-step solution!")
    st.markdown("---")
    st.markdown("### Topics I can help with:")
    st.markdown("- Algebra & Equations")
    st.markdown("- Calculus & Integration")
    st.markdown("- Geometry & Trigonometry")
    st.markdown("- Statistics & Probability")
    st.markdown("- Number Theory")
    st.markdown("---")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat cleared!")

# ─── Main Input Section ───────────────────────────────────────
st.markdown("### 📝 Type Your Doubt")
question = st.text_area(
    label="",
    placeholder="e.g. How do I solve quadratic equations?\nOr: What is integration by parts?",
    height=150,
    key="question_input"
)

st.markdown("### 📸 Upload a Photo of Your Problem (Optional)")
uploaded_file = st.file_uploader(
    label="",
    type=["png", "jpg", "jpeg"],
    help="Take a photo of your textbook problem and upload it here!"
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="📌 Your uploaded problem", use_container_width=True)
# ─── Solve Button ─────────────────────────────────────────────
solve_clicked = st.button("🔍 Solve My Doubt", type="primary")

if solve_clicked:

    if not question.strip() and uploaded_file is None:
        st.warning("⚠️ Please type a math question OR upload an image of your problem!")

    else:
        pil_image = None
        if uploaded_file is not None:
            pil_image = Image.open(uploaded_file)

        final_question = question.strip()
        if not final_question and pil_image is not None:
            final_question = "Please solve the math problem shown in this image step by step."

        with st.spinner("🤔 MathMentor AI is solving your doubt..."):
            answer = solve_math_doubt(final_question, pil_image)

        st.markdown("### ✅ Solution")
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

        st.session_state.chat_history.append({
            "question": final_question,
            "answer": answer,
            "had_image": uploaded_file is not None
        })

# ─── Chat History Section ─────────────────────────────────────
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### 🕓 Previous Doubts")

    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        with st.expander(f"Q{len(st.session_state.chat_history) - i}: {chat['question'][:60]}..."):
            st.markdown("**Your question:**")
            st.write(chat["question"])
            if chat["had_image"]:
                st.info("📸 This question included an uploaded image")
            st.markdown("**MathMentor's Answer:**")
            st.markdown(chat["answer"])

# ─── Footer ───────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit & Google Gemini API | MathMentor AI</p>",
    unsafe_allow_html=True
)
