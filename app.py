# SentimentResponder: Streamlit Reactive Agent
%%writefile app.py
import streamlit as st
from textblob import TextBlob

# App Title
st.title("💬 Emotional Sentiment Responder")
st.write("Type anything and the agent will respond based on your emotions!")

# Input Box
user_input = st.text_input("🗣️ Say something:")

# Enhanced Emotion Detection
def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lowered = text.lower()

    # Keyword-based overrides
    if any(word in lowered for word in ["angry", "furious", "mad", "annoyed", "rage"]):
        return "😠 Whoa, sounds like you’re angry. Want to talk about it?"
    elif any(word in lowered for word in ["lonely", "alone", "isolated", "abandoned"]):
        return "😔 Feeling lonely is tough. I'm here for you."
    elif any(word in lowered for word in ["confident", "unstoppable", "strong", "brave"]):
        return "💪 I love that confidence! Keep pushing forward!"

    # Polarity-based fallback
    if polarity > 0.75:
        return "🤩 You're radiating joy!"
    elif polarity > 0.5:
        return "😁 That sounds fantastic!"
    elif polarity > 0.2:
        return "😊 That’s awesome! Keep going!"
    elif polarity > 0.05:
        return "🙂 Sounds positive!"
    elif polarity > -0.05:
        return "😐 Feeling neutral? That’s totally fine."
    elif polarity > -0.2:
        return "😕 Hmm, something seems off."
    elif polarity > -0.5:
        return "😟 Oh no, I’m here if you need a friend."
    elif polarity > -0.75:
        return "😢 That sounds sad. Sending virtual hugs."
    else:
        return "😭 I'm really sorry you're feeling this way."

# Output
if user_input:
    response = detect_emotion(user_input)
    st.markdown(f"**Agent says:** {response}")
