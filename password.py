import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="Password Checker by Farida",
    page_icon="🔒",
    layout="centered"
)
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput>div>div>input {
        width: 250px !important; 
        margin: auto;
        transition: border 0.3s ease !important;
    }
    .stTextInput>div>div>input:hover {
        border: 2px solid #4CAF50 !important;
    }
    .stButton button {
        background-color: #4CAF50 !important;
        color: white !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover {
        background-color: #45a049 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .feedback-box {
        padding: 15px;
        margin-top: 15px;
        border-radius: 10px;
        background-color: #f8f9fa;
    }
    .feedback-item {
        padding: 12px;
        margin: 10px 0;
        background-color: #ffebee;
        color: #d32f2f;
        border-radius: 8px;
        transition: all 0.3s ease;
        border-left: 4px solid #d32f2f;
    }
    .feedback-item:hover {
        background-color: #ffcdd2;
        transform: translateX(10px);
    }
    .st-expander {
        border: 2px solid #e0e0e0 !important;
        border-radius: 12px !important;
        transition: border-color 0.3s ease !important;
    }
    .st-expander:hover {
        border-color: #4CAF50 !important;
    }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level.")

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Must contain both uppercase and lowercase letters")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Should include at least one number (0-9)")

    # Special character check
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("❌ Should include at least one special character")

    # Display results
    if score == 4:
        st.success("""
        🎉 **Strong Password!**
        Your password is secure and meets all requirements!
        """)
    elif score == 3:
        st.warning("""
        ⚠️ **Moderate Password**
        Consider adding more complexity for better security
        """)
    else:
        st.error("""
        🔥 **Weak Password**
        Please follow the suggestions below to improve
        """)

    # Show feedback
    if feedback:
        with st.expander("💡 Password Improvement Suggestions", expanded=True):
            st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
            for item in feedback:
                st.markdown(f'<div class="feedback-item">{item}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# User input
password = st.text_input(
    "Enter your password:",
    type="password",
    placeholder="Type your password here...",
    help="A strong password should contain uppercase, lowercase, numbers, and special characters"
)

# Check button
if st.button("🔍 Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")