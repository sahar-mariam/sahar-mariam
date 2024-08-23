import nltk
import streamlit as st
from nltk.corpus import wordnet #lexical database
from nltk.tokenize import word_tokenize #create tokens

#downloading required NLTK resources
nltk.download('wordnet')
nltk.download('punkt')

#generate meanings
def get_word_meanings(word):
    synsets = wordnet.synsets(word)
    meanings = [syn.definition() for syn in synsets]
    return meanings if meanings else ["No meanings found."]

def get_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)[:10] if synonyms else ["No synonyms found."]

#streamlit app
st.title("NLP Project: Word Meanings and Synonyms")

#taking input from the user
word = st.text_input("Enter a word:")

#user choices
option = st.selectbox("What would you like to do?", 
                      ("Select an option", "Get Meanings", "Get Synonyms"))

#response for choices
if word and option != "Select an option":
    if option == "Get Meanings":
        meanings = get_word_meanings(word)
        st.write(f"Meanings of '{word}':")
        for meaning in meanings:
            st.write(meaning)
    
    elif option == "Get Synonyms":
        synonyms = get_synonyms(word)
        st.write(f"Synonyms of '{word}':")
        st.write(", ".join(synonyms))


