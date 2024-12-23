import streamlit as st
import requests

from textblob import TextBlob

# text_input() : strings
# number_input() : int

st.title('News Fetcher App with built in sentimental analyzer:')
st.write('Enter the topic you want to search for:')

topic = st.text_input("Enter a topic:", value='Python')

# spinner ---> loading icon

if st.button('Fetch News...'):
    with st.spinner("Fetching news....."):
        url = 'https://newsapi.org/v2/everything'

        params = {
            'q': topic,
            'apiKey': 'daa4b61565614f039bd9c2826c7ba18d',
            'pageSize': 10

        }

        response = requests.get(url, params=params)
        articles = response.json()['articles']

        if not articles:
            st.warning('No articles related to this topic is found.....')

        else:

            for i, article in enumerate(articles, start=1):
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')

                analysis = TextBlob(description)
                sentiment = analysis.sentiment.polarity

                if sentiment > 0.2:
                    sentiment_label = 'Positive 😊'
                    bg_color = 'lightgreen'

                elif sentiment < 0.2:
                    sentiment_label = 'Negative 😞'
                    bg_color = 'lightcoral'

                else:
                    sentiment_label = 'Neutral 😑'
                    bg_color = 'lightyellow'

                # st.write(description)
                # st.write(sentiment_label)
                html = f"""
                <div class ="box" style= "background-color:{bg_color}">
                <h4>{i}.{title}</h4>
                <p><b> Description:</b>{description}</p>
                <p> <b> Sentiment:</b> {sentiment_label}</p>
                <a href= "{url}" target="_blank"> Link to the article </a>

                </div>
                """
                css = """
                <style>
                .box{
                  padding : 10px;
                  border-radius : 5px;
                  border : 2px solid black;
                  margin-bottom : 10px;
                }
                </style>
                """

                st.markdown(html, unsafe_allow_html=True)

                st.markdown(css, unsafe_allow_html=True)

# name = 'adhavan'
# sub = 'python'
# print(f"My name is {name}.I am learning {sub}")
#
# # formatted string
