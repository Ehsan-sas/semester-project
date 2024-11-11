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
st.title('Clickbait Detector - Midterm')

st.image('./clickbait_journalism.webp', caption='cyberhoot.com')

# Introduction and Background
st.header('Introduction and Background')
st.write('In the digital age, where content is monetized based on views and clicks, content creators often use clickbait—misleading or exaggerated titles to attract attention. This practice frustrates users and spreads misinformation. Detecting and mitigating clickbait is crucial to enhance content quality and user experience. Current models struggle to generalize across various types of media, such as news articles and video titles. To detect clickbait, various proposals have been tested, including simpler supervised classifiers (i.e. Random Forest [1]), and more advanced deep learning methods (e.g. Convolutional Neural Networks [2]). Publically available clickbait datasets also vary, with differing feature sets and lower sample sizes, from social media ranging from YouTube [3] to news sites [4].')
st.write('This project aims to build a more robust AI model to detect clickbait across different media platforms by analyzing common features of deceptive headlines. By combining data preprocessing and machine learning, the goal is to develop a versatile solution applicable to a wide range of online content [5].')

# Problem Definition
st.header('Problem Definition')
st.write('Monetization of online media has created a massive market for consumer attention, pushing creators to make their content as clickable as possible. Users decide which media to consume based on short titles, leading to the rise of clickbait, where titles are exaggerated or misleading to attract users. The aim of this project is to create an AI model that detects clickbait, which could potentially block such content. Previous efforts have focused on detecting clickbait in specific media forms [2], but this project seeks to uncover general insights into clickbait techniques and apply them across different platforms. The model will be trained on large datasets of clickbait articles and tested on a smaller YouTube title dataset to evaluate its efficacy.')

# Methods
st.header('Methods')
st.write('In this project, data cleaning and feature engineering steps have been implemented to prepare text data for a clickbait detection dataset. Data cleaning has started by filtering out entries with fewer than 20 characters through the is_text_not_too_short function, ensuring that only substantial text samples are retained for further processing. This function verifies the length of each entry, discarding short and potentially irrelevant samples. Additionally, the clean_text function has been applied to standardize the text format by removing any leading and trailing whitespace, promoting consistency across the dataset.')
st.write('For feature engineering, the add_word_and_character_features function has been developed to construct text-based features that may enhance model performance. Key features such as character_count and word_count have been included to capture the length and verbosity of each text entry, while average_word_length has been introduced to provide insights into word complexity. Ratios for stylistic elements, such as uppercase_ratio, numeral_ratio, and punctuation_ratio, have been calculated to reflect structural aspects often seen in clickbait. Additionally, linguistic analysis has been performed by including ratios of various parts of speech—adjective_ratio, adverb_ratio, interjection_ratio, noun_ratio, pronoun_ratio, proper_noun_ratio, and verb_ratio—which capture language patterns that may characterize clickbait content.')
st.write('Together, these features have been designed to provide a comprehensive representation of the text, enhancing the model’s ability to distinguish between clickbait and non-clickbait text based on structural, stylistic, and linguistic attributes.')
st.write('Now that the data has been preprocessed, model implementation and training can proceed. A combination of one supervised and one unsupervised learning approach has been selected to explore different aspects of the dataset and achieve a comprehensive analysis. The supervised model has been implemented using a Random Forest algorithm, chosen for its robustness and capability to handle high-dimensional data while capturing complex feature interactions—critical considerations given the diverse set of linguistic and structural features. Additionally, Random Forest’s resilience to overfitting has made it well-suited for accurately distinguishing between clickbait and non-clickbait across varied text samples.')
st.write('For the unsupervised model, Principal Component Analysis (PCA) has been applied to reduce the dimensionality of the feature set, allowing for an exploration of the underlying structure without relying on labeled data. PCA has been selected to identify key patterns and correlations within the features, assisting in feature selection and reducing redundancy.')
st.write('By employing these two approaches, both interpretability and predictive accuracy have been targeted to improve the model’s ability to identify clickbait content effectively.')

# Results and Discussion
st.header('Results and Discussion')
st.subheader('RandomForest Results:')
st.write('Our RandomForest implementation scored a 99% training accuracy, a 99% validation accuracy, and a 90% test accuracy. This tells us that the model is very good at predicting whether or not a given video title is attempting to clickbait users. These results also potentially indicate slight overfitting since the training accuracy is nearly perfect while the test accuracy is a bit lower, but the predictions are still very accurate nevertheless.')
st.image('./Picture 1.png', caption='RandomForest Results')
st.write('The confusion matrix for our RandomForest implementation shows us that the model predicts slightly more false negatives than false positives. The difference isn’t big enough to indicate a clear and distinct trend, especially considering how good the accuracy is overall. Thus, we do not believe there to be any distinct bias in the model from this data.')
st.subheader('PCA Results:')
st.write('On the left of this visualization are the pca features ordered from the one which explains the most variance (pca0) to the one which explains the least variance (pca13). At the top are the features of our data, and the matrix shows which feature in our data the given pca feature represents. For example, since pca0 is mapped to character_count with a value of 1.0, we understand that pca0 is essentially representing the character count. Therefore, this visualization of our PCA results shows us that it considers character count to be the most important feature. It would follow that word count, label, and average word length are also very important, but we would like to do further analysis after factoring out the character count before coming to any conclusions.')
st.image('./Picture 2.png', caption='PCA Results')
# Next Steps
st.header('Next Steps')
st.write('We will want to do further analysis of our models including a more complete breakdown of the most important features of our dataset. We also plan to implement another supervised model to end up with 3 models total by the final report.')

# References
st.header('References')
st.write('[1] M. Potthast, S. Köpsel, B. Stein, and M. Hagen, ‘Clickbait Detection’, in Advances in Information Retrieval, 2016, pp. 810–817.')
st.write('[2] A. Agrawal, "Clickbait detection using deep learning," 2016 2nd International Conference on Next Generation Computing Technologies (NGCT), Dehradun, India, 2016, pp. 268-272, doi: 10.1109/NGCT.2016.7877426.')
st.write('[3] A. Zavalny, “Youtube Clickbait Classification,” Kaggle, 2021.')
st.write('[4] Y. Kashnitsky, ‘Clickbait news detection’. Kaggle, 2019.')
st.write('[5] R. Raj, C. Sharma, R. Uttara and C. R. Animon, "A Literature Review on Clickbait Detection Techniques for Social Media," 2024.')

# Contributions Table
st.header('Contributions')
contributions = {
    'Name': ['Stephan Tserovski', 'Jay Cha', 'Zachary Aristei', 'Narges Moeini', 'Ehsan Asadollahi'],
    'Proposal Contributions': ['Results Discussion and Gantt Chart', 'Data Preprocessing', 'Model and Visualization Coding', 'Model Discussion', 'Streamlit']
}

df = pd.DataFrame(contributions)

with st.expander("Contributions Table"):
    st.write(df.to_html(index=False), unsafe_allow_html=True)
