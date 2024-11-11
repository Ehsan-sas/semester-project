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

st.image('./clickbait_journalism.webp', caption='cyberhoot.com')

# Introduction and Background
st.header('1111111111Introduction and Background')
st.write('In the digital age, where content is monetized based on views and clicks, content creators often use clickbait—misleading or exaggerated titles to attract attention. This practice frustrates users and spreads misinformation. Detecting and mitigating clickbait is crucial to enhance content quality and user experience. Current models struggle to generalize across various types of media, such as news articles and video titles. To detect clickbait, various proposals have been tested, including simpler supervised classifiers (i.e. Random Forest [1]), and more advanced deep learning methods (e.g. Convolutional Neural Networks [2]). Publically available clickbait datasets also vary, with differing feature sets and lower sample sizes, from social media ranging from YouTube [3] to news sites [4].')
st.write('This project aims to build a more robust AI model to detect clickbait across different media platforms by analyzing common features of deceptive headlines. By combining data preprocessing and machine learning, the goal is to develop a versatile solution applicable to a wide range of online content [5].')

# Problem Definition
st.header('Problem Definition')
st.write('Monetization of online media has created a massive market for consumer attention, pushing creators to make their content as clickable as possible. Users decide which media to consume based on short titles, leading to the rise of clickbait, where titles are exaggerated or misleading to attract users. The aim of this project is to create an AI model that detects clickbait, which could potentially block such content. Previous efforts have focused on detecting clickbait in specific media forms [2], but this project seeks to uncover general insights into clickbait techniques and apply them across different platforms. The model will be trained on large datasets of clickbait articles and tested on a smaller YouTube title dataset to evaluate its efficacy.')




# Methods
st.header('Methods')
st.write('To tackle clickbait detection, the project will employ a combination of preprocessing techniques and machine learning algorithms, ensuring the model can generalize across different media types. The preprocessing phase will involve data cleaning, such as removing irrelevant information and stop words. Feature engineering will follow, creating new features like title length and punctuation use, which are often linked to clickbait. The raw text will be transformed into numerical representations, such as word importance, to facilitate model training [6].')
st.write('Both unsupervised and supervised machine learning methods will be explored. K-means clustering, an unsupervised method, will help identify patterns in titles and group similar ones, revealing common clickbait strategies. For supervised learning, logistic regression will be employed for binary classification, determining whether a title is clickbait. Random forest, a more complex algorithm that combines decision trees, will also be used to improve prediction accuracy and handle large datasets.')

# Potential Results and Discussion
st.header('Potential Results and Discussion')
st.write('Model performance can be measured using accuracy [7], the fraction of correct predictions on the test set. As this is a binary classification task, additional analysis can be conducted using true or false positives and negatives. For instance, a false negative occurs when a clickbait title is misclassified as non-clickbait. Metrics such as precision, recall, and F1 score will provide a clearer understanding of the model’s strengths and weaknesses. A confusion matrix can be used to visualize the model performance [8].')

st.write('The project expects the final model to successfully identify clickbait titles across various media. If successful, the model could be deployed to help users make more informed content decisions and reduce the spread of deceptive practices online.')


# References
st.header('References')
st.write('[1] M. Potthast, S. Köpsel, B. Stein, and M. Hagen, ‘Clickbait Detection’, in Advances in Information Retrieval, 2016, pp. 810–817.')
st.write('[2] A. Agrawal, "Clickbait detection using deep learning," 2016 2nd International Conference on Next Generation Computing Technologies (NGCT), Dehradun, India, 2016, pp. 268-272, doi: 10.1109/NGCT.2016.7877426.')
st.write('[3] A. Zavalny, “Youtube Clickbait Classification,” Kaggle, 2021. https://www.kaggle.com/datasets/thelazyaz/youtube-clickbait-classification (accessed Oct. 04, 2024).')
st.write('[4] Y. Kashnitsky, ‘Clickbait news detection’. Kaggle, 2019.')
st.write('[5] R. Raj, C. Sharma, R. Uttara and C. R. Animon, "A Literature Review on Clickbait Detection Techniques for Social Media," 2024 11th International Conference on Reliability, Infocom Technologies and Optimization (Trends and Future Directions) (ICRITO), Noida, India, 2024, pp. 1-5, doi: 10.1109/ICRITO61523.2024.10522359.')
st.write('[6] P. Klairith and S. Tanachutiwat, "Thai Clickbait Detection Algorithms Using Natural Language Processing with Machine Learning Techniques," 2018 International Conference on Engineering, Applied Sciences, and Technology (ICEAST), Phuket, Thailand, 2018, pp. 1-4, doi: 10.1109/ICEAST.2018.8434447.')
st.write('[7] Ferri, Cèsar & Hernandez-Orallo, Jose & Modroiu, R. (2009). An Experimental Comparison of Performance Measures for Classification. Pattern Recognition Letters. 30. 27-38.')
st.write('[8] Bella, Ferri, Hernández-Orallo, and Ramírez-Quintana “Calibration of Machine Learning Models” in Khosrow-Pour, M. “Machine learning: concepts, methodologies, tools and applications.” Hershey, PA: Information Science Reference (2012).')


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










