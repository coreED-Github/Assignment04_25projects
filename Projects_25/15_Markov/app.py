import streamlit as st
import pdfplumber
import os
import random
from collections import defaultdict

st.set_page_config(page_title="📄 PDF & TXT Viewer + AI Generator", layout="wide")
st.title("📄 Full File Viewer + ✨ Markov Chain AI Generator")

uploaded_file = st.file_uploader("📂 Upload any full .pdf or .txt file from your computer", type=["pdf", "txt"])
extracted_text = ""

if uploaded_file is not None:
    st.success(f"✅ File '{uploaded_file.name}' uploaded!")

    temp_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    if uploaded_file.name.endswith(".pdf"):
        try:
            with pdfplumber.open(temp_path) as pdf:
                all_text = []
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        all_text.append(text)
                extracted_text = "\n\n".join(all_text)
        except Exception as e:
            st.error(f"❌ PDF read failed: {e}")

    elif uploaded_file.name.endswith(".txt"):
        try:
            with open(temp_path, "r", encoding="utf-8") as f:
                extracted_text = f.read()
        except Exception as e:
            st.error(f"❌ TXT read failed: {e}")

    os.remove(temp_path)

    if extracted_text.strip():
        st.markdown("### 📃 Full File Content:")
        st.markdown(
            f"""<div style='white-space: pre-wrap; background-color: #fdfdfd; padding: 1em; border-radius: 10px; font-family: "Courier New", monospace;'>{extracted_text}</div>""",
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ No readable text found in the uploaded file.")

    if extracted_text.strip():
        if st.button("✨ Generate AI Text using Markov Chain"):
            def build_markov_model(text, n=2):
                model = defaultdict(list)
                words = text.split()
                for i in range(len(words) - n):
                    key = tuple(words[i:i + n])
                    model[key].append(words[i + n])
                return model

            def generate_markov_text(model, n=2, max_words=150):
                if not model:
                    return "❌ Not enough text to generate output."
                start = random.choice(list(model.keys()))
                output = list(start)
                for _ in range(max_words):
                    state = tuple(output[-n:])
                    next_word = random.choice(model[state]) if state in model else None
                    if next_word:
                        output.append(next_word)
                    else:
                        break
                return ' '.join(output)

            model = build_markov_model(extracted_text)
            generated_text = generate_markov_text(model)

            st.markdown("### 🤖 AI Generated Text (Markov Chain Style):")
            st.markdown(
                f"""<div style='white-space: pre-wrap; background-color: #e7faff; padding: 1em; border-radius: 10px; font-family: "Courier New", monospace;'>{generated_text}</div>""",
                unsafe_allow_html=True,
            )
