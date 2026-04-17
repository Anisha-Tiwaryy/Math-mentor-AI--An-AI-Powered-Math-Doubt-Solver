# 🧮 MathMentor AI — An AI-Powered Math Doubt Solver

![MathMentor AI Banner](mm.png)

> *Step-by-step math help for K-12 students — because understanding the 'why' matters more than just the answer.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://math-mentor-ai--an-ai-powered-math-doubt-solver-be2jnbgo7rymqf.streamlit.app/)

---

## 🚀 Live Demo

🔗 **[Try MathMentor AI Live](https://math-mentor-ai--an-ai-powered-math-doubt-solver-be2jnbgo7rymqf.streamlit.app/)**

---

## 📌 About The Project

**MathMentor AI** is an intelligent math tutoring web app built for students from Grade 1 to Grade 12. Powered by **Google Gemini AI**, it provides instant, clear, and step-by-step solutions to any math doubt — just like having a personal tutor available 24/7.

Built as part of an application for **Cuemath's AI Builder - Product Team**, this project reflects Cuemath's vision of making math learning meaningful and accessible for every student.

---

## ✨ Features

- 🤖 **AI-Powered Solutions** — Uses Google Gemini 1.5 Flash for fast, accurate answers
- 📚 **Grade-wise Support** — Tailored explanations from Grade 1 to Grade 12
- 🖼️ **Image Upload** — Upload a photo of your textbook problem and get it solved
- 🔢 **Step-by-Step Explanations** — Every solution is broken down clearly
- 💡 **Tips & Shortcuts** — Includes helpful tricks for faster solving
- 🕓 **Chat History** — Review all your previous doubts in one place
- 📱 **Fully Responsive** — Works on desktop and mobile

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web app framework |
| Google Gemini API | AI model for solving math |
| Pillow (PIL) | Image processing |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure
Math-mentor-AI/
│
├── app.py               # Main Streamlit application
├── gemini_helper.py     # Gemini API integration
├── requirements.txt     # Project dependencies
├── mm.png               # App logo
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
---

## ⚙️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Anisha-Tiwaryy/Math-mentor-AI--An-AI-Powered-Math-Doubt-Solver.git
cd Math-mentor-AI--An-AI-Powered-Math-Doubt-Solver
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Create a `.env` file in the project folder:
Get your free API key from [Google AI Studio](https://aistudio.google.com)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API key |

> ⚠️ Never share your API key or push your `.env` file to GitHub!

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud**.

🔗 [https://math-mentor-ai--an-ai-powered-math-doubt-solver-be2jnbgo7rymqf.streamlit.app/](https://math-mentor-ai--an-ai-powered-math-doubt-solver-be2jnbgo7rymqf.streamlit.app/)

---

## 👩‍💻 Author

**Anisha Tiwary**
- GitHub: [@Anisha-Tiwaryy](https://github.com/Anisha-Tiwaryy)
- Email: anishadgp04@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ using Streamlit & Google Gemini API | Made by Anisha</p>
