import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def load_options(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        options = [line.strip() for line in file.readlines()]
    return options

genre_options = load_options("genre_options.txt")
reading_habits_options = load_options("reading_habits_options.txt")

# Kitap öneri fonksiyonu
def recommend_books(genre, recent_books, reading_habits, favorite_author):
    prompt = f"""
    Bir kitap eleştirmeni gibi davran ve aşağıdaki bilgilere göre kitap önerisi yap:
    - Tür: {genre}
    - En son okunan kitaplar: {recent_books}
    - Okuma alışkanlıkları: {reading_habits}
    - Favori yazar: {favorite_author}

    Lütfen 3 kitap öner ve her bir kitap için şu formatta yanıt ver:
    Kitap Adı: [Kitap adı]
    Açıklama: [Kısa açıklama]
    """
    response = model.generate_content(prompt)
    return response.text

# Kitap önerilerini ayrıştırma
def parse_recommendations(response_text):
    recommendations = []
    books = response_text.split("\n\n")
    for book in books:
        lines = book.split("\n")
        book_data = {}
        for line in lines:
            if line.startswith("Kitap Adı:"):
                book_data["name"] = line.replace("Kitap Adı:", "").strip()
            elif line.startswith("Açıklama:"):
                book_data["summary"] = line.replace("Açıklama:", "").strip()
        if book_data:
            recommendations.append(book_data)
    return recommendations

# Streamlit Arayüzü
st.title("📚 Akıllı Kitap Öneri Sistemi")

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

if st.session_state.step == 1:
    st.subheader("1. Hangi türde kitaplar okumayı seversiniz?")
    genre = st.selectbox("Tür seçin", genre_options)
    if st.button("Devam"):
        st.session_state.answers["genre"] = genre
        st.session_state.step += 1

elif st.session_state.step == 2:
    st.subheader("2. En son okuduğunuz kitaplar hangileri?")
    recent_books = st.text_input("Son okuduğunuz kitapları yazın")
    if st.button("Devam"):
        st.session_state.answers["recent_books"] = recent_books
        st.session_state.step += 1

elif st.session_state.step == 3:
    st.subheader("3. Günde ne kadar süre kitap okuyorsunuz?")
    # Change the input to a selectbox (dropdown menu)
    reading_habits = st.selectbox(
        "Günde ne kadar süre kitap okuyorsunuz?", reading_habits_options
    )

    if st.button("Devam"):
        st.session_state.answers["reading_habits"] = reading_habits
        st.session_state.step += 1


elif st.session_state.step == 4:
    st.subheader("4. Favori yazarınız kim?")
    favorite_author = st.text_input("Favori yazarınızı yazın")
    if st.button("Kitap Önerisi Al"):
        st.session_state.answers["favorite_author"] = favorite_author
        st.session_state.step += 1

elif st.session_state.step == 5:
    with st.spinner("Kitap önerileriniz hazırlanıyor..."):
        answers = st.session_state.answers
        response_text = recommend_books(
            answers["genre"],
            answers["recent_books"],
            answers["reading_habits"],
            answers["favorite_author"],
        )
        recommendations = parse_recommendations(response_text)

        for idx, book in enumerate(recommendations, start=1):
            st.markdown(f"### 📖 Kitap {idx}: {book['name']}")
            st.markdown(f"**Açıklama:** {book['summary']}")
            st.markdown("---")
