import streamlit as st
import pandas as pd


# Inject custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5f5;
    }
    .css-18ni7ap.e8zbici2 {
        background-color: #31333F;
    }
    h1 {
        color: #E694FF;
    }
    h2, h3 {
        color: #1f77b4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# Sidebar
with st.sidebar:
    st.title("Sidebar Menu")
    st.button("Click Me")

# Main content
st.title("Main Section")
st.write("Here is the main content of the app.")

# Custom containers for structured layouts
with st.container():
    st.header("Section 1")
    st.write("Content for section 1")

with st.container():
    st.header("Section 2")
    st.write("Content for section 2")



# Title
st.title('Clickbait Detector Project Proposal')

# Introduction and Background
st.header('Introduction and Background')
st.subheader('Topic')
st.subheader('Literature')
st.subheader('Datasets')

# Problem Definition
st.header('Problem Definition')
st.write('The advent of monetization for online media created a massive market for consumer attention. Everyone who posts content on the internet is incentivised to garner as many clicks as possible and maximize the amount of time consumers spend watching. Users decide what piece of media to consume based on short titles, headlines, or thumbnails so all creators must optimize these short snippets of information to be as clickable as possible. This has led to the prevalent problem of clickbait, where creators will make misleading or greatly exaggerated titles in order to “bait” users into looking at the content.')
         
st.write('In an effort to solve this problem, we aim to create an AI model that will detect whether or not a given title is clickbait, which could later be used to automatically block clickbait content. There has been prior work to create models that detect clickbait in specific forms of media, but we hope to create a model that will find more general insights into common clickbait techniques and work across different types of media. To that end we will explore methods such as training the model on the larger datasets we found for clickbait articles, then testing its efficacy in accurately predicting the smaller YouTube title dataset.')



# Methods
st.header('Methods')
st.write('- **Preprocessing methods**: (3+ preprocessing techniques)')
st.write('- **Machine learning algorithms**: (3+ unsupervised and supervised algorithms)')

# Potential Results and Discussion
st.header('Potential Results and Discussion')
st.write('One of the metrics that we could use to measure the performance of our models is accuracy, which is simply the fraction of correct predictions on the test set. As our task is a binary classification task, we can perform more detailed analysis by categorizing the model predictions as true or false positives and negatives. For example, if an article is clickbait but our model predicts that it is not clickbait, the prediction would be a false negative. Commonly-used metrics that are based on this categorization include precision, recall, and F1 score. Using these metrics would help us determine what exactly our model excels and struggles at. We could also visualize this information using a confusion matrix.')

st.write('If all goes well, we expect that our final model will be able to successfully identify clickbait titles across various media. This could then be deployed in the real world, allowing users to make informed decisions about the content they engage with and discouraging the spread of deceptive and harmful practices on the internet.')


# References
st.header('References')
st.write('- IEEE format')

# Gantt Chart
st.header('Gantt Chart')
st.markdown('[Click here to view Gantt Chart](Gantt Chart.xlsx)')

# Contribution Table
st.header('Contribution Table')
st.write('Here are the contributions of each group member to the proposal:')
contributions = {
    "Stephan Tserovski": "Problem Definition and Gantt Chart",
    "Jay Cha": "Potential Results and Discussion",
    "Narges Moeini": "Methods"
}
st.table(contributions)

