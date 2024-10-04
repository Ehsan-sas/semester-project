import streamlit as st
import pandas as pd

# Title
st.title('Clickbait Detector Project Proposal')

# Introduction and Background
st.header('Introduction and Background')
st.subheader('Topic')
st.write('The advent of monetization for online media created a massive market for consumer attention. Everyone who posts content on the internet is incentivized to garner as many clicks as possible and maximize the amount of time consumers spend watching.')
st.write('Users decide what piece of media to consume based on short titles, headlines, or thumbnails. This has led to the prevalent problem of clickbait, where creators make misleading or greatly exaggerated titles to “bait” users into looking at the content.')

# Problem Definition
st.header('Problem Definition')
st.write('We aim to create an AI model that will detect whether or not a given title is clickbait, which could be used to block clickbait content. Prior work has created models that detect clickbait in specific forms of media. We aim to create a model that generalizes across different types of media, training it on larger datasets for clickbait articles and testing its efficacy on YouTube title datasets.')

# Methods
st.header('Methods')
st.write('We plan to use the following preprocessing methods and machine learning algorithms for our project:')
st.write('- **Preprocessing methods**: (3+ preprocessing techniques)')
st.write('- **Machine learning algorithms**: (3+ unsupervised and supervised algorithms)')

# Potential Results and Discussion
st.header('Potential Results and Discussion')
st.write('We will use accuracy as a metric to evaluate the model. Additionally, we will use precision, recall, and F1 score to analyze false positives and negatives. A confusion matrix will also be used to visualize the performance of our model.')

# Gantt Chart
st.header('Gantt Chart')
st.write('You can view our Gantt chart in the provided Excel file for a timeline of our project phases:')
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

# References
st.header('References')
st.write('- IEEE format references will be included here.')

# Run the app
if __name__ == '__main__':
    st.run()
