import streamlit as st
import resend
import os
from dotenv import load_dotenv
# Set your Resend API key
load_dotenv()
resend.api_key =os.getenv('resend_api')

def send_email(to_email, html_content):
    try:
        response = resend.Emails.send({
            "from": "Ollie AI Support <support@ollie.health>",
            "to": to_email,
            "subject": "Test Email from Streamlit App",
            "html": html_content
        })
        return True, "Email sent successfully!"
    except Exception as e:
        return False, str(e)

st.title("Email Sender App")

# Input fields
to_email = st.text_input("Recipient's Email Address")
html_content = st.text_area("HTML Content for Email", height=200)

# Send button
if st.button("Send Email"):
    if to_email and html_content:
        success, message = send_email(to_email, html_content)
        if success:
            st.success(message)
        else:
            st.error(f"Error sending email: {message}")
    else:
        st.warning("Please fill in both email address and HTML content.")

st.markdown("---")
st.write("Note: Make sure to replace 'YOUR_RESEND_API_KEY' with your actual Resend API key.")
st.write("Also, update 'your_verified_email@example.com' with a verified sender email address in your Resend account.")