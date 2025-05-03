import streamlit as st

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("➡️ Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("➡️ Add lowercase letters (a–z).")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("➡️ Add uppercase letters (A–Z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("➡️ Add numbers (0–9).")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        suggestions.append("➡️ Add special characters (!@#$%^&*).")

    return score, suggestions

def get_strength_label(score):
    if score <= 2:
        return "❌ Weak"
    elif score <= 4:
        return "⚠️ Moderate"
    else:
        return "✅ Strong"

# Streamlit App
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    strength = get_strength_label(score)

    st.markdown(f"**Strength:** {strength} (Score: {score}/5)")

    if score < 5:
        st.markdown("### 🔧 Suggestions to improve your password:")
        for tip in feedback:
            st.write(tip)
    else:
        st.success("🎉 Your password is strong!")
