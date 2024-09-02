
# Binomial Sentiment Classification Model for eGov Mobile App

## Overview
This project focuses on classifying user comments on the eGov mobile app into positive or negative sentiments. We utilize a Naive Bayes classifier due to its effectiveness in handling text classification tasks. This model helps in understanding user sentiment which can be crucial for continuous improvement of the app.

![eGov Mobile App](./images/egov_app.png)  <!-- Replace 'image_link_here' with the actual link to the image -->

## Dataset
The model is trained using a labeled dataset consisting of user comments categorized into two types:
- `positive_reviews.csv` - Contains comments expressing positive sentiments.
- `negative_reviews.csv` - Contains comments expressing negative sentiments.

## Model Details
- **Algorithm**: Naive Bayes Classifier
- The choice of a Naive Bayes Classifier is motivated by its proficiency in dealing with natural language texts, especially for binary classification problems like sentiment analysis. It is simple, efficient and appropriate for mixed-language data which is often present in Kazakstan market. 

## File Descriptions
- `nlp_model_for_mgov_reviews.py` - Contains the script for preprocesssing data and training the sentiment classification model.
- `positive_reviews.csv` - Sample dataset of positive user comments.
- `negative_reviews.csv` - Sample dataset of negative user comments.

## Results

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.90      | 0.99   | 0.94     | 2075    |
| 1     | 0.97      | 0.65   | 0.78     | 662     |

- **Accuracy**: 91%
- **Macro Avg**: Precision: 0.93, Recall: 0.82, F1-Score: 0.86
- **Weighted Avg**: Precision: 0.92, F1-Score: 0.90, Support: 2737