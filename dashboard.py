import streamlit as st
from app.database.repository import Repository
st.set_page_config(
    page_title="Mridul AI News",
    page_icon="AI",
    layout="wide"
)
st.title("Mridul AI News")
st.subheader("Personalized AI News Dashboard")
st.write(
    "AI news collected, summarized, and stored automatically."
)
repo = Repository()
articles = repo.get_recent_digests(hours=24)
st.success(f"{len(articles)} AI news articles available")
st.divider()
st.header("Latest AI News")
search = st.text_input(
    "Search AI News",
    placeholder="Search by title or summary..."
)
filtered_articles = [
    article for article in articles
    if search.lower() in (
        article["title"] + " " + article["summary"]
    ).lower()
]
for index, article in enumerate(filtered_articles, start=1):
    st.subheader(f"{index}. {article['title']}")
    st.write(article["summary"])
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Source: {article['article_type']}")
    with col2:
        st.markdown(
            f"[Read original article]({article['url']})"
        )
    st.divider()
