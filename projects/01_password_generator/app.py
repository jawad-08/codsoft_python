import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


import streamlit as st
from password_generator.generator import generate_password
from password_generator.strength import estimate_entropy, strength_label
import streamlit.components.v1 as components
import html

st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔒 Password & Passphrase Generator")
st.write("Generate secure passwords or passphrases and see a quick strength estimate.")

with st.sidebar:
    st.header("Options")
    use_passphrase = st.checkbox("Use passphrase (words)", value=False)
    if use_passphrase:
        words = st.slider("Number of words", 3, 8, 4)
        separator = st.selectbox("Separator", ["-", " ", "_"])
    else:
        length = st.slider("Length", 6, 64, 12)
        use_upper = st.checkbox("Include uppercase (A-Z)", value=True)
        use_lower = st.checkbox("Include lowercase (a-z)", value=True)
        use_digits = st.checkbox("Include digits (0-9)", value=True)
        use_special = st.checkbox("Include symbols", value=True)
        exclude_ambiguous = st.checkbox("Exclude ambiguous chars (l 1 I O 0 o)", value=False)

if st.button("Generate"):
    try:
        if use_passphrase:
            pwd = generate_password(use_passphrase=True, words=words, separator=separator)
        else:
            pwd = generate_password(length=length,
                                    use_upper=use_upper,
                                    use_lower=use_lower,
                                    use_digits=use_digits,
                                    use_special=use_special,
                                    exclude_ambiguous=exclude_ambiguous)
        entropy = estimate_entropy(pwd)
        label, score = strength_label(entropy)

        st.subheader("Generated")
        st.text_input("Password / Passphrase", value=pwd, key="generated_pwd")

        st.write("**Strength:**", label)
        st.progress(int(score))

        # safe-escape password for JS snippet
        safe_pwd = html.escape(pwd).replace("'", "\\'")
        components.html(f"""
            <button onclick="navigator.clipboard.writeText('{safe_pwd}')">Copy to clipboard</button>
        """, height=40)

    except Exception as e:
        st.error(str(e))

st.write("---")
st.write("Tip: use passphrases (multiple words) for memorability with good entropy.")
