import streamlit as st 

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")
st.title("🔒 Simple Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

def check_strength(pwd):
    if len(pwd) == 0:
        st.warning("Please enter a password.")
    elif len(pwd) < 6:
        st.error("❌ Weak Password: Too short, minimum 6 characters needed.")
    elif pwd.isdigit() or pwd.isalpha():
        st.info("⚡ Medium Password: Add both letters and numbers.")
    else:
        st.success("✅ Strong Password: Good job!")

if st.button("Check Password"):
    check_strength(password)
