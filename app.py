import streamlit as st
import joblib
import os

st.set_page_config(page_title="Email Spam Detection", page_icon="📧", layout="centered")

MODEL_PATH = "email_spam_detection_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

st.title("📧 Email Spam Detection System")
st.write("Enter an email message below. The machine-learning model will classify it as SPAM or NOT SPAM.")

model = load_model()
if model is None:
    st.error("Model file not found. Upload email_spam_detection_model.pkl beside app.py.")
    st.stop()

email_text = st.text_area(
    "Paste the email subject and message:",
    height=200,
    placeholder="Example: Congratulations! You have won a free prize..."
)

if st.button("Check Email", type="primary", use_container_width=True):
    if not email_text.strip():
        st.warning("Please enter an email message first.")
    else:
        prediction = model.predict([email_text])[0]
        probabilities = model.predict_proba([email_text])[0]
        classes = list(model.named_steps["classifier"].classes_)
        confidence = float(probabilities[classes.index(prediction)]) * 100

        st.subheader("Prediction")
        if prediction == "spam":
            st.error("🚨 SPAM EMAIL")
        else:
            st.success("✅ NOT SPAM")

        st.write(f"Model confidence for predicted class: **{confidence:.2f}%**")
        st.progress(min(max(confidence / 100, 0.0), 1.0))

st.divider()
st.caption(
    "Academic demonstration only. This classifier can make mistakes. "
    "A NOT SPAM prediction does not prove an email or its links are safe. "
    "Do not paste private or confidential information."
)
