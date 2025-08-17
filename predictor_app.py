import streamlit as st

def predict_approval(age, severity, work_history, adaptable, diagnosis_years):
    score = 0
    if age > 50:
        score += 2
    elif age > 45:
        score += 1
    score += severity
    if work_history == "no":
        score += 1
    if adaptable == "no":
        score += 2
    if diagnosis_years >= 3:
        score += 1

    if score >= 9:
        return "Likely"
    elif score >= 6:
        return "Possible"
    else:
        return "Unlikely"


# Streamlit UI
st.set_page_config(page_title="Disability Approval Predictor", layout="centered")

st.title("🧠 Disability Approval Predictor")
st.markdown("""
This tool estimates your likelihood of being approved for Social Security Disability Insurance (SSDI).
If your chances are low, it provides **AI-powered income alternatives** to support you in Smart America.
""")

# User Inputs
age = st.number_input("What is your age?", min_value=0, max_value=120, value=30)
severity = st.slider("How severe is your condition? (1 = mild, 5 = extreme)", 1, 5, 3)
work_history = st.selectbox("Can you return to your past work?", ["yes", "no"])
adaptable = st.selectbox("Can you do a different type of work?", ["yes", "no"])
diagnosis_years = st.number_input("How many years ago were you diagnosed?", min_value=0, max_value=50, value=1)

# Submit Button
if st.button("Check My Chances"):
    result = predict_approval(age, severity, work_history, adaptable, diagnosis_years)
    st.subheader(f"Estimated SSDI Approval: **{result}**")

    if result == "Unlikely":
        st.warning("⚠️ Based on your inputs, your SSDI approval is unlikely.")
        st.markdown("### 💡 Smart America: AI-Based Income Ideas")
        st.markdown("""
        - **AI Blog or YouTube Channel**  
          Use ChatGPT to script content, Canva/CapCut to create visuals, and monetize with ads or affiliate links.  

        - **Sell Digital Products**  
          Let AI help you create eBooks, journals, or guides. Sell on Gumroad or Stan Store.  

        - **Virtual Assistant or Prompt Writer**  
          Use AI tools to offer services on Fiverr or Upwork.  

        - **Voice-to-Text Content Creation**  
          If typing is difficult, use tools like Descript or Whisper to write by speaking.  

        - **Teach AI Locally or Online**  
          Many people don’t understand ChatGPT, Notion, or Canva. Offer beginner lessons—even if you’re still learning.  

        👉 Visit [YouGood.site](https://yougood.site) for more tools and support.
        """)
    else:
        st.success("✅ You may have a chance! Talk to a disability advocate or attorney. Meanwhile, explore income options as backup.")
# Sidebar Donation
st.sidebar.markdown("---")
st.sidebar.markdown("### 💖 Support This Project")
st.sidebar.markdown(
    """
    If you find this tool helpful, consider supporting us with a small donation.  
    👉 [Click here to Donate](https://buymeacoffee.com/dppsquad)  
    """
)

# Donation Section at the bottom
st.markdown("---")
st.markdown("### 💖 Support This Project")
st.markdown(
    """
    If you find this tool helpful, consider supporting us with a small donation.  
    👉 [Click here to Donate](https://buymeacoffee.com/dppsquad)  
    """
)
