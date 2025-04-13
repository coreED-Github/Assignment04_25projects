import streamlit as st
import random
import re
import time
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="Markov Chain AI Text Composer", layout="wide")
st.markdown("""
    <style>
    .typing-text {
        font-family: 'Courier New', monospace;
        font-size: 18px;
        white-space: pre-wrap;
        border-left: 3px solid #00FFAA;
        padding-left: 10px;
        animation: blink 1s steps(2, start) infinite;
    }
    @keyframes blink {
        to { border-color: transparent }
    }
    </style>
""", unsafe_allow_html=True)

def build_markov_chain(text, retain_punctuation=False):
    if not retain_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    chain = {}
    for current_word, next_word in zip(words, words[1:]):
        chain.setdefault(current_word, []).append(next_word)
    return chain

def generate_text(chain, start_word, length=50, seed=None):
    if seed is not None:
        random.seed(seed)
    word = start_word.lower()
    result = [word]
    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
    return ' '.join(result)

def draw_graph(chain):
    G = nx.DiGraph()
    for word, next_words in chain.items():
        for next_word in next_words:
            G.add_edge(word, next_word)
    fig, ax = plt.subplots(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=10, ax=ax)
    st.pyplot(fig)


def display_typing(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"<div class='typing-text'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(0.03)

st.title("✨ Markov Chain AI Text Composer")
st.write("Generate creative text with AI using a Markov Chain model!")

col1, col2 = st.columns([2, 1])

with col1:
    upload_file = st.file_uploader("Upload a .txt file (optional)", type=['txt'])
    if upload_file is not None:
        stringio = StringIO(upload_file.getvalue().decode("utf-8"))
        user_input = stringio.read()
    else:
        user_input = st.text_area("Or type/paste your text here", height=200)

    start_word = st.text_input("Enter starting word")
    length = st.slider("How many words to generate?", 10, 200, 50, 10)
    seed = st.text_input("Random seed (optional)")
    retain_punct = st.checkbox("Keep punctuation?", False)

    generate = st.button("Generate Text")

with col2:
    st.subheader("Settings & Theme")
    st.toggle("Dark Mode (System default applies)")
    st.info("Your input will create an AI-powered text with Markov logic.")

if generate and user_input and start_word:
    try:
        seed_val = int(seed) if seed else None
    except ValueError:
        seed_val = None

    chain = build_markov_chain(user_input, retain_punctuation=retain_punct)
    output_text = generate_text(chain, start_word, length, seed=seed_val)

    st.markdown("### Generated Output:")
    display_typing(output_text)

    st.download_button("Download Text", output_text, file_name="generated_text.txt")
    st.code(output_text, language='text')
    st.success("Text generated successfully!")

    st.markdown("""
    <button onclick="copyText()" style="padding:10px 20px; font-size:16px; background:#4CAF50; color:white; border:none; border-radius:5px; cursor:pointer;">Copy Generated Text</button>

    <script>
    function copyText() {
        const text = document.querySelector('code').innerText;
        navigator.clipboard.writeText(text).then(function() {
            alert("Copied to clipboard!");
        }, function(err) {
            alert("Failed to copy text!");
        });
    }
    </script>
    """, unsafe_allow_html=True)
    with st.expander("Show Word Transition Graph"):
        draw_graph(chain)

elif generate:
    st.warning("Please enter both input text and a starting word.")