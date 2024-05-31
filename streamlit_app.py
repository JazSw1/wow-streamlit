import streamlit as st

# Initialize session state to store the list of phrases
if 'phrases' not in st.session_state:
    st.session_state.phrases = ["Enter your phrases here", "Example phrase 1", "Example phrase 2"]

def add_phrase():
    st.session_state.phrases.append(st.session_state.new_phrase)
    st.session_state.new_phrase = ""

def sort_phrases():
    st.session_state.phrases.sort()

def remove_phrase(index):
    st.session_state.phrases.pop(index)

st.title("Phrase Editor and Sorter")

# Text input to add new phrases
new_phrase = st.text_input("Add a new phrase", key="new_phrase")
st.button("Add Phrase", on_click=add_phrase)

# Display the list of phrases with a remove button
st.write("## Your Phrases")
for i, phrase in enumerate(st.session_state.phrases):
    cols = st.columns([10, 1])
    cols[0].write(phrase)
    if cols[1].button("Remove", key=f"remove_{i}"):
        remove_phrase(i)

# Button to sort phrases
if st.button("Sort Phrases"):
    sort_phrases()

# Display sorted phrases
st.write("## Sorted Phrases")
st.write(st.session_state.phrases)
