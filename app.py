import random
import streamlit as st

# Word pairs
word_pairs = [
    ("coffee", "der Kaffee"),
    ("milk", "die Milch"),
    ("tea", "der Tee"),
    ("water", "das Wasser"),
    ("bread", "das Brot"),
    ("wine", "der Wein"),
    ("beer", "das Bier"),
    ("bye", "tschüss"),
    ("father", "der Vater"),
    ("mother", "die Mutter"),
    ("sister", "die Schwester"),
    ("brother", "der Bruder"),
    ("man", "der Mann"),
    ("husband", "der Mann"),
    ("you", "du"),
    ("daughter", "die Tochter"),
    ("son", "der Sohn"),
    ("woman", "die Frau"),
    ("wife", "die Frau"),
    ("nice", "nett"),
    ("big", "groß"),
    ("very", "sehr"),
    ("smart", "klug"),
    ("great", "super"),
    ("how are you?", "wie geht's"),
    ("good", "gut"),
    ("good day!", "guten Tag"),
    ("I am fine", "es geht"),
    ("good morning", "guten Morgen"),
    ("see you soon", "bis bald"),
    ("cheers", "prost"),
    ("good bye", "auf Wiedersehen"),
    ("I am sorry", "es tut mir leid"),
    ("see you later", "bis später"),
    ("no problem", "kein Problem"),
    ("good evening", "guten Abend"),
    ("of course", "natürlich"),
    ("boy", "der Junge"),
    ("young", "jung"),
    ("beautiful", "schön"),
    ("dog", "der Hund"),
    ("cat", "die Katze"),
    ("elephant", "der Elefant"),
    ("mouse", "die Maus"),
    ("bear", "der Bär"),
    ("owl", "die Eule"),
    ("where", "wo"),
    ("pizza", "die Pizza"),
    ("cheese", "der Käse"),
    ("salad", "der Salat"),
    ("delicious", "lecker"),
    ("with", "mit"),
    ("hot", "heiß"),
    ("sandwich", "das Sandwich"),
    ("egg", "das Ei"),
    ("here", "hier"),
    ("excuse me", "Entschuldigung"),
    ("cold", "kalt"),
    ("waiter", "der Kellner"),
    ("menu", "die Speisekarte"),
    ("salt", "das Salz"),
    ("restaurant", "das Restaurant"),
    ("sausage", "die Wurst"),
    ("bill", "die Rechnung"),
    ("food", "das Essen"),
    ("to", "zu"),
    ("schnitzel", "das Schnitzel"),
    ("USA", "Amerika"),
    ("Germany", "Deutschland"),
    ("small", "klein"),
    ("Canada", "Kanada"),
    ("wonderful", "wunderbar"),
    ("to come", "kommen"),
    ("Vienna", "Wien"),
    ("Austria", "Österreich"),
    ("big", "groß"),
    ("Munich", "München"),
    ("city", "die Stadt"),
    ("France", "Frankreich"),
    ("also", "auch"),
    ("how is it", "wie ist es"),
    ("loud", "laut"),
    ("expensive", "teuer"),
    ("exciting", "aufregend"),
    ("waitress", "die Kellnerin"),
    ("actor", "der Schauspieler"),
    ("actress", "die Schauspielerin"),
    ("he", "er"),
    ("she", "sie"),
    ("job or occupation", "der Beruf"),
    ("what", "was"),
    ("your (sing male, sing neutral)", "dein"),
    ("your (female or plural)", "deine"),
    ("doctor (female)", "die Ärztin"),
    ("doctor (male)", "der Arzt"),
    ("friend or girlfriend (female)", "die Freundin"),
    ("stressful", "stressig"),
    ("but", "aber"),
    ("interesting", "interessant"),
    ("teacher (male)", "der Lehrer"),
    ("teacher (female)", "die Lehrerin"),
    ("work", "die Arbeit"),
    ("never", "nie"),
    ("sometimes", "manchmal"),
    ("to swim", "schwimmen"),
    ("to paint", "malen"),
    ("to cook", "kochen"),
    ("good", "gut"),
    ("very", "sehr"),
    ("always", "immer"),
    ("often", "oft"),
    ("to play", "spielen"),
    ("chess", "das Schach"),
    ("piano", "das Klavier"),
    ("park", "der Park"),
    ("taxi stand", "der Taxistand"),
    ("train station", "der Bahnhof"),
    ("market", "der Markt"),
    ("over there", "da drüben"),
    ("church", "die Kirche"),
    ("pharmacy", "die Apotheke"),
    ("library", "die Bibliothek"),
    ("old", "alt"),
    ("close", "in der Nähe"),
    ("elegant", "elegant"),
    ("hotel", "das Hotel"),
    ("coffee shop", "das Café"),
    ("museum", "das Museum"),
    ("cheap", "billig"),
    ("bakery", "die Bäckerei"),
    ("supermarket", "der Supermarkt"),
    ("cinema", "das Kino"),
    ("right", "rechts"),
    ("left", "links"),
    ("far away", "weit weg"),
    ("ATM", "der Geldautomat"),
    ("subway station", "die U-Bahnstation"),
    ("university", "die Universität"),
    ("new", "neu")
]


# Initialize session state
if 'question' not in st.session_state:
    st.session_state.question = None
if 'answer' not in st.session_state:
    st.session_state.answer = None
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ''
if 'result' not in st.session_state:
    st.session_state.result = ''

# Function to get a new question
def next_question():
    english, german = random.choice(word_pairs)
    if random.choice([True, False]):
        st.session_state.question = f"What is the German word for <span style='color:blue; font-weight:bold; font-size:24px;'>{english}</span>?"
        st.session_state.answer = german
    else:
        st.session_state.question = f"What is the English word for <span style='color:blue; font-weight:bold; font-size:24px;'>{german}</span>?"
        st.session_state.answer = english
    st.session_state.user_answer = ''
    st.session_state.result = ''

# Function to check the answer
def check_answer():
    if st.session_state.user_answer.lower() == st.session_state.answer.lower():
        st.session_state.result = "Correct!"
    else:
        st.session_state.result = f"Wrong. The correct answer was '{st.session_state.answer}'."

# UI layout
st.title("English-German Quiz")

if st.session_state.question:
    st.markdown(st.session_state.question, unsafe_allow_html=True)

    st.text_input("Your answer:", key="user_answer", on_change=check_answer)
    st.write(st.session_state.result)

st.button("Next", on_click=next_question)
