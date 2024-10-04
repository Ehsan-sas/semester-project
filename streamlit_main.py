import streamlit as st
import pandas as pd
import os


# Inject custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFF;
    }
    .css-18ni7ap.e8zbici2 {
        background-color: #FFFFF;
    }
    h1, h2, h3 {
        color: #4169E1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write(
    """
    <style>
    .dataframe {
        direction: ltr;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)







    






# Title
st.title('Clickbait Detector Project Proposal')

# Introduction and Background
st.header('Introduction and Background')
st.write('Topic')
st.write('Literature')
st.write('Datasets')

# Problem Definition
st.header('Problem Definition')
st.write('The advent of monetization for online media created a massive market for consumer attention. Everyone who posts content on the internet is incentivised to garner as many clicks as possible and maximize the amount of time consumers spend watching. Users decide what piece of media to consume based on short titles, headlines, or thumbnails so all creators must optimize these short snippets of information to be as clickable as possible. This has led to the prevalent problem of clickbait, where creators will make misleading or greatly exaggerated titles in order to “bait” users into looking at the content.')
         
st.write('In an effort to solve this problem, we aim to create an AI model that will detect whether or not a given title is clickbait, which could later be used to automatically block clickbait content. There has been prior work to create models that detect clickbait in specific forms of media, but we hope to create a model that will find more general insights into common clickbait techniques and work across different types of media. To that end we will explore methods such as training the model on the larger datasets we found for clickbait articles, then testing its efficacy in accurately predicting the smaller YouTube title dataset.')




# Methods
st.header('Methods')
st.write('To effectively address the problem of clickbait detection, we will implement a combination of preprocessing methods and machine learning algorithms, ensuring the model generalizes well across different types of media. Preprocessing will play a crucial role in cleaning and structuring the data before training. We will begin with data cleaning,which includes removing irrelevant or redundant information, such as special characters, stop words, and noisy data that do not contribute meaningfully to the classification task. Then, feature engineering will be applied, where we will create new features like the length of the title, or the use of punctuation marks, all of which are commonly associated with clickbait. Finally, we will use data transformation techniques to transform raw textual data into numerical representations that reflect word importance across the dataset.')
st.write('For machine learning, we will explore both unsupervised and supervised techniques. First, K-means clustering, an unsupervised learning method, will help in identifying patterns in titles and grouping similar types of titles, which can provide insights into common clickbait strategies. For supervised methods, we will use logistic regression, a simple but effective binary classification method, to detect whether a title is clickbait or not based on labeled training data. We will also implement random forest, a more complex and robust algorithm that combines decision trees to improve prediction accuracy and handle large datasets.')

# Potential Results and Discussion
st.header('Potential Results and Discussion')
st.write('One of the metrics that we could use to measure the performance of our models is accuracy, which is simply the fraction of correct predictions on the test set. As our task is a binary classification task, we can perform more detailed analysis by categorizing the model predictions as true or false positives and negatives. For example, if an article is clickbait but our model predicts that it is not clickbait, the prediction would be a false negative. Commonly-used metrics that are based on this categorization include precision, recall, and F1 score. Using these metrics would help us determine what exactly our model excels and struggles at. We could also visualize this information using a confusion matrix.')

st.write('If all goes well, we expect that our final model will be able to successfully identify clickbait titles across various media. This could then be deployed in the real world, allowing users to make informed decisions about the content they engage with and discouraging the spread of deceptive and harmful practices on the internet.')


# References
st.header('References')
st.write('- IEEE format')

# Gantt Chart
st.header('Gantt Chart')
with st.expander('Access the Chart'):
    # Media
    st.image('./GANTT.png', use_column_width=True)
    




# Contributions
st.header('Contributions')
contributions = {
    'Name': ['Aristei Zachary','Stephan Tserovski', 'Narges Moeini', 'Jay Cha', 'Ehsan Asadollahi'],
    'Contributions': ['Introduction','Problem Definition and Gantt Chart','Methods','Potential Results and Discussion','Streamlit and Video']
}

df = pd.DataFrame(contributions)

with st.expander("Contributions Table"):
    st.write(df.to_html(index=False), unsafe_allow_html=True)  # Display the table when the button is clicked










