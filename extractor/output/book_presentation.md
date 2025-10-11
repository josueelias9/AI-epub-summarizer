---
marp: true
theme: default
paginate: true
footer: 'Eng. Josué Huamán'
style: |
  section {
    background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg');
    background-size: 250px;
    background-position: 95% 5%;
    background-repeat: no-repeat;
    opacity: 1;
  }

---

<style>
section.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-size: 16px;
}
</style>

---

![bg](https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg)

---
<!-- _class: lead -->
<!-- _paginate: false -->

# Book Summary Presentation

### AI-Generated Book Summary

---# 2. Official Google Cloud CertifiedProfessional Machine Learning EngineerStudy Guide

---

# 7. Chapter 1Framing ML Problems

---

## 7.1. Translating Business Use Cases

* **Identify Use Case**: Understand impact, success criteria, and data available for a specific problem.
  * _Stakeholders_: Identify key people related to the use case, including executives, CFOs, managers, and data managers.
  * Impact: Determine the purpose of the ML project, such as increasing profit or improving quality of life.

* **Match with Machine Learning**: Choose an algorithm and metric that fit the identified use case.
  * _Outcomes_: Understand what would happen if the solution is implemented, including potential counterproductive reactions from users.

---

  * Problem Feasibility: Determine if the problem can be solved using machine learning, considering existing technology, available data, and budget.

* **Select Machine Learning Approach**: Identify a suitable ML approach that aligns with the use case and stakeholder needs.

---
## 7.2. Machine Learning Approaches

* **Overview**: Machine learning has a vast range of approaches and methods for solving problems.
    * _Multiple solutions exist for some problems and not all ML frameworks fit every use case._
    * _There are hundreds of ways to apply machine learning techniques, making it essential to have a broad knowledge base._
    * _Understanding the landscape of ML approaches is crucial for selecting the right method for a given problem._

---

### 7.2.1. Supervised, Unsupervised, and Semi‐supervised Learning

* **Machine Learning Classification by Data Type**:
	+ Supervised: uses labeled data, e.g., image classification, sentiment analysis
	+ Unsupervised: uses unlabeled data, e.g., clustering, topic modeling
* **Unsupervised Learning Methods**:
	+ Clustering algorithms (e.g., k-means)
	+ Autoencoders (dimensionality reduction)
	+ Topic modeling (document clustering)
* **Semi-Supervised Learning**: combines labeled and unlabeled data to address uncertainty in unsupervised learning

---

*Supervised, Unsupervised, and Semi‐supervised Learning*
Name | Data Type | Supervised/Unsupervised
---|---|---
Regression – Tables | Tabular | Supervised
Classification – Tables | Tabular | Supervised
Forecasting | Series | Supervised
Image classification | Image | Supervised
Image segmentation | Image | Supervised
Object detection | Image | Supervised
Video classification | Video | Supervised
Video object tracking | Video | Supervised
Video action recognition | Video | Supervised
Sentiment analysis | Text | Supervised
Entity extraction | Text | Supervised
Translation | Text | Supervised
K‐means clustering | Tabular | Unsupervised
Principal component analysis | Tabular | Unsupervised
Topic modeling | Text | Unsupervised
Collaborative filtering/recommendations | Mixed | Supervised/Unsupervised

<!-- _class: centered -->

---

### 7.2.2. Classification, Regression, Forecasting, and Clustering

* **Classification**: predicting labels or categories for input data (e.g., dog vs cat), with variations including binary and multiclass classification.
    * Can be applied to thousands of classes, like object detection in images
* _Regression_: predicting a numerical value based on input features (e.g., house price or rainfall amount)
    * Uses different algorithms than classification
* **Forecasting**: predicting future values from time-series data, often using techniques that convert to regression problems
* _Clustering_: grouping data points into clusters based on similarities and differences, with applications such as grouping cities by location.

---

*Classification, Regression, Forecasting, and Clustering*
Student ID | Age | Exam Scores (Out of 100)
---|---|---
1 | 34 | 75
2 | 23 | 59
3 | 36 | 92
4 | 31 | 67

<!-- _class: centered -->

---

*Classification, Regression, Forecasting, and Clustering*
****|  Temperature
---|---
Series 1 | 29, 30, 40, 39, 23, 20
Series 2 | 10, 11, 13, 23, 43, 34
Series 2 | 19, 18, 19, 20, 38, 20
Series 4 | 14, 17, 34, 34, 12, 43

<!-- _class: centered -->

---

## 7.3. ML Success Metrics

* _Confusion Matrix_: A table showing true positives, true negatives, false positives, and false negatives.
    * **Metrics**: 
        + Precision: 5/(5+3) = 0.625
        + Recall: 5/(5+2) = 0.714
        + F1 Score: 2 x (0.625 x 0.714)/(0.625 + 0.714) = 0.666

---

*ML Success Metrics*
****|  Predicted
---|---
**Actual** |  | **Positive Prediction** | **Negative Prediction**
**Positive Class** | 5 | 2
**Negative Class** | 3 | 990

<!-- _class: centered -->

---

*ML Success Metrics*
****|  Scenario | Formula
---|---|---
Precision | Lower false positive |
Recall | Lower false negative |
F1 | Lower false positive and false negative together |

<!-- _class: centered -->

---

### 7.3.1. Area Under the Curve Receiver Operating Characteristic (AUC ROC)

**ROC Curve:**

* **Definition:** Graphical plot summarizing binary classification model performance
* **Plot points:** False positive rate (x-axis) vs. True positive rate (y-axis)
* _Ideal point:_ Top-left corner with 100% true positives and 0% false positives

---

### 7.3.2. The Area Under the Precision‐Recall (AUC PR) Curve

* **AUC PR Curve**: measures relationship between precision and recall
    * **Precision-Recall Plot**: x-axis: recall, y-axis: precision
        + Best score: horizontal line across top with 100% precision and recall (ideal but not achievable)
        + Preferred for imbalanced datasets to mitigate skewing

---

### 7.3.3. Regression

* **Regression Metrics**: 
    * **MAE** Measures average absolute difference
    * **RMSE** Penalizes large errors, ranges 0-∞
    * **RMSLE** Asymmetric metric, penalizes under-prediction
* 
* Alternative metrics:
    * **MAPE** Measures proportional difference
    * **R2**: Evaluates model fit, ranges 0-1

---

## 7.4. Responsible AI Practices

**Key Considerations for AI and Machine Learning**

* **Fairness**: Consider biases in datasets and models using statistical methods to measure bias.
* **Interpretability**: Use model explanations to understand complex models like neural networks, but choose algorithms that support model explanations when necessary.
* **Privacy**: Minimize data leakage by using techniques to detect and prevent sensitive data exposure.

    * _**Security**_: Identify potential threats, stay ahead of the curve by learning new approaches, and develop strategies to combat cyber threats throughout the ML development process._

---

## 7.5. Summary

* Understanding the Business Use Case: Taking a high-level view of a company's needs and goals
* Framing Machine Learning Problems: Defining key aspects of a problem to guide the development of a solution

---

## 7.6. Exam Essentials

* **Machine Learning for Business**
Translate business challenges into machine learning to solve problems like regression, classification, and forecasting. 
* **Key Considerations**
* * **Problem Types**: Regression (continous), Classification (binary/ multi-class), Forecasting (time-series)
* * **Metrics**: Precision, Recall, F1, AUC ROC, RMSE, MAPE
* * _Responsible AI Practices_: Fairness, Interpretability, Privacy, Security

---

# 8. Chapter 2Exploring Data and Building Data Pipelines

---

## 8.1. Visualization

* _Data Visualization_: Exploratory technique to find trends and outliers in data.
    * **Methods**: Univariate Analysis (box plots, distribution plots) and Bivariate Analysis (line plots, bar plots, scatterplots)
        * *_Visualizes data to identify_*: imbalances, features influencing models

---

### 8.1.1. Box Plot

* A **box plot** displays data as 25th, 50th, and 75th quartiles, with outliers outside the whiskers.
* The body of the plot represents the interquartile range, where most observations are present.
* Whiskers show maximum and minimum values.

---

### 8.1.2. Line Plot

* A line plot shows the relationship between two variables, analyzing data trend changes over time.
* It displays data points connected by straight lines.
* Used to visualize and analyze trends in data over time.

---

### 8.1.3. Bar Plot

* A bar plot compares categorical data over time, displaying trends and patterns in data such as sales, visitors, or revenue.
* Used for analyzing data and identifying differences between categories.
* Example: Comparing weekly sales figures, website visitor numbers, or monthly product revenue.

---

### 8.1.4. Scatterplot

* **What is a Scatterplot**: A type of plot that visualizes clusters in a dataset and shows relationships between two variables.
    * Used to identify patterns and correlations
    * Most common plot in data science

---

## 8.2. Statistics Fundamentals

* **Central Tendency Measures**: 
    * Mean
    * Median
    * Mode

---

### 8.2.1. Mean

Mean is the accurate measure to describe the data when we do not have any outliers present.

---

### 8.2.2. Median

* **Median**: calculated by finding middle value(s) in sorted dataset
    * *Even numbers:** average of two middle values
    * *Odd numbers:** single middle value

---

### 8.2.3. Mode

* **Mode**: the value(s) that appear most often in a dataset

---

### 8.2.4. Outlier Detection

* **Effect of Outliers on Statistics**: The mean is sensitive to outliers, which can significantly alter its value.
    * **Variance Measurement**: Variance is the average of squared differences from the mean.
        * _Example_: Adding an outlier (210) changes the mean and median but not the mode.

---

*Outlier Detection*
With Outlier | Without Outlier
---|---
Mean: 12.72 | Mean: 29.16
Median: 13 | Median: 14
Mode: 15 | Mode: 15

<!-- _class: centered -->

---

### 8.2.5. Standard Deviation

**Summary**

* **Standard Deviation**: square root of variance, identifies outliers (data points > 1 std dev from mean)
* **Covariance**: measures variation between two random variables

---

### 8.2.6. Correlation

* **Correlation Coefficient**: A normalized form of covariance, ranging from -1 to +1.
    * _Positive Correlation_: Increase in one variable results in increase in another.
    * _Negative Correlation_: Increase in one variable results in decrease in another.
    * _Zero Correlation_: No substantial impact between variables.

---

## 8.3. Data Quality and Reliability

* **Data Quality** is crucial for model reliability.
    * Reliable data has no missing values, duplicates, or incorrect features.
    * Data should be checked for errors and inconsistencies, including label errors and noise in features.

---

### 8.3.1. Data Skew

* **Data Skew**: occurs when the normal distribution curve is not symmetric
* _Causes_: outliers or uneven data distribution
    * **Types of Skew**:
        * Right-skewed: typically found in income data, leading to extreme outliers
            * Example: income data, with most people having average income and few having very high incomes (e.g., billionaires)

---

### 8.3.2. Data Cleaning

* **Normalization**: transforms features to similar scales, improving model performance and stability.
    * _Goal_: reduce variance in feature values
    * _Benefit_: stable training and better model performance

---

### 8.3.3. Scaling

* **Scaling in Feature Values**
  * Converts floating-point feature values to standard ranges (e.g. 0-1) for better convergence and accuracy
  * Benefits include avoiding "NaN traps" and reducing feature importance
* **When to Use Scaling**
  * Uniformly distributed data with no skew or outliers
  * Examples: age, uniform distributions

---

### 8.3.4. Log Scaling

* **Log Scaling**: used when data is not in a comparable range
*   *Example*: large values like 10,000 are converted to smaller values like 10 for comparison.
*   *Effect*: scales data to a standard range (e.g., 0-100) for analysis.

---

### 8.3.5. Z‐score

* **Scaling Method**: Calculating z-score as standard deviations away from the mean
    * _Formula:_ (value - mean) / stddev
    * Example: (130 - 100) / 20 = 1.5, which falls within the acceptable range of ±3

---

### 8.3.6. Clipping

* _Feature Clipping_: Capping extreme outlier values in features using a fixed threshold to prevent distortion during normalization.

---

### 8.3.7. Handling Outliers

* An _outlier_ is a data point that is significantly different from the rest due to human error or skew.
    * Techniques for detecting outliers include box plots, Z-score, clipping, and IQR analysis
    * Outliers can be removed or imputed with new values such as mean, median, mode, or boundary values.

---

## 8.4. Establishing Data Constraints

* **Data Schema**: defines metadata for ML pipeline
    * **Advantages**:
        * Enables metadata-driven preprocessing
        * Validates new data, catches anomalies like skews and outliers
            * Facilitates reproducibility and consistency

---

### 8.4.1. Exploration and Validation at Big‐Data Scale

* _TensorFlow Data Validation (TFDV)_ is used for detecting data anomalies and schema anomalies in large datasets.
    * **TFDV uses** _TensorFlow Extended (TFX)_ libraries: `TensorFlow Data Validation`, `TensorFlow Transform`, `TensorFlow Model Analysis`, and `TensorFlow Serving`.
    * **Key use cases:** Exploratory Data Analysis Phase, Production Pipeline Phase

---

## 8.5. Running TFDV on Google Cloud Platform

* **TFDV APIs**: Built on Apache Beam for batch and streaming pipelines
*   **Integration**: Natively integrated with:
    *   BigQuery
    *   Google Cloud Storage
    *   Vertex AI Pipelines

---

## 8.6. Organizing and Optimizing Training Datasets

* **Dataset Split**: Data is divided into three main datasets: Training, Validation, and Test.
    * _**Training Dataset***_: Used to train the model and learn from the data.
    * _**Validation Dataset***_: Used for hyperparameter tuning and evaluating model behavior after training.
    * _**Test Dataset***_: Used to evaluate the performance of the trained model.

---

### 8.6.1. Imbalanced Data

* **Imbalanced Data**: Unequal classes in a dataset, affecting model performance.
    * _Example_: Credit card transactions with 1,000 non-fraud and 5 fraud examples, leading to biased training on non-fraud scenarios.
* **Handling Imbalance**: Downsample majority class, upweight minority class for more balanced data.
    * _Advantage_: Faster model convergence due to increased minority class examples.

---

### 8.6.2. Data Splitting

* **Data Splitting Challenges**: Random splitting can cause skew because it doesn't account for temporal relationships between data points.
* **Solution 1: Temporal Data Splitting**: Split data based on publication date to avoid same-story overlaps in training and testing sets.
* **Solution 2: Time-Stamped Evaluation**: Use a specific time period for evaluation, like the second week of May, to prevent overlap with training set.

---

### 8.6.3. Data Splitting Strategy for Online Systems

* **Data Splitting for Online Systems**: 
  * Split training and validation data by time to mirror the lag between training and prediction
* **Time-Based Splits**:
  * Recommended for large datasets (millions of examples)
* **Considerations**: 
  * Use domain knowledge to determine when a random split is suitable

---

## 8.7. Handling Missing Data

* **Handling Missing Data**: There are several ways to handle missing data in a dataset, including deleting rows/columns with missing values, replacing missing values with mean/median/modal values, imputing missing values with most frequent category, and using machine learning algorithms.
    * _Methods for Handling Missing Data_ 
      * Deleting or replacing columns/rows
      * Replacing missing values with mean/median/modal
      * Imputing missing values with most frequent category
* **Advantages of Each Method**:
  * Deleting/columns: information loss, poor model performance
  * Replacing/Imputing: prevents data loss, suitable for small datasets
* _Machine Learning Algorithms_ 

---

  * Ignore missing values (k-NN, Naive Bayes)
  * Predict missing values using correlation with other variables

---
## 8.8. Data Leakage

* **Data Leakage**: Exposing model to test data during training, causing overfitting
    * Occurs when target variable is used as feature or features are not separated properly
        * Causes model to memorize actual data rather than generalize well
    * Can be prevented by:
        * Selecting uncorrelated features and splitting data correctly
            * Using separate normalization for training and test data
                * Handling time-series data with cutoff values and cross-validation

---

## 8.9. Summary

* **Data Visualization**: Visualizing data using box plots, line plots, scatterplots, and checking data correlation
* **Data Cleaning**: Using log scaling, scaling, clipping, and z-score to improve data quality and validate data schema
    * _Establishing Data Constraints_ 
    * Dealing with missing data and data leakage 
        * Splitting data into training, validation, and testing sets

---

## 8.10. Exam Essentials

* **Understanding Data Visualization**: Visualize data using box plots, line plots, and scatterplots to understand trends and patterns.
  * Understand statistical terms: mean, median, mode, standard deviation, and data correlation.
  * Check for outliers and data quality using statistical terms and data cleaning techniques.
  * Establish data constraints by defining a schema and validating data through Total Data Validation Framework (TFDV).
  * Organize and optimize training data by splitting into training, test, and validation sets, and applying sampling strategies.

---

# 9. Chapter 3Feature Engineering

---

## 9.1. Consistent Data Preprocessing

* **Pretraining Data Transformation**: Apply transformations before model training, separate code lives outside machine learning model.
    * Advantages: computation performed once, look at entire dataset for transformation.
    * Disadvantages: same transformation needs to be reproduced at prediction time, may lead to skew with data changes.
* **Inside Model Data Transformation**: Transform data within model during training, decoupling from data is possible.
    * Advantage: easy to change transformation technique without affecting data.
    * Disadvantage: computation heavy transformations increase model latency.

---

## 9.2. Encoding Structured Data Types

* A good feature should relate to business objectives, be numeric with magnitude, and have enough examples
    * **Feature Engineering Types**
        * *_Categorical Data_*: defines categories with limited values (e.g., yes/no, male/female)
        * *_Numeric Data_*: represents scalar or continuous values (e.g., observations, recordings)

---

### 9.2.1. Why Transform Categorical Data?

**Categorical Data in Machine Learning**
* Most ML algorithms require numeric input and output variables
* Categorical data must be converted to numeric data for processing
* Conversion may need to be reversed during predictions if it's an output variable.

---

### 9.2.2. Mapping Numeric Values

* _Data types (int, float) require no special encoding due to multiplication by weights_
* _Two common transformations for numeric data: normalization and bucketing_

---

#### 9.2.2.1. Normalizing

* **Normalization Techniques**: Scaling, log scaling, z score, and clipping are used to normalize numeric data.
    * **Reasons for Normalization**:
        * Prevents slow model convergence due to varying data ranges
        * Prevents NaN errors in wide datasets

---

#### 9.2.2.2. Bucketing

### Bucketing Summary
* _Transform numeric data to categorical data_
* Two common methods:
  * **Equal-spaced boundaries**: Divide into ranges with varying amounts of data points
  * **Quantile boundaries**: Divided into equal-sized buckets, no fixed span
* Use equal-spaced for many distributions, quantile for skewed data

---

### 9.2.3. Mapping Categorical Values

* **Data Conversion**: Methods exist to transform categorical data into numerical data for machine learning models

---

#### 9.2.3.1. Label Encoding or Integer Encoding

* *_Label Encoding_*: assigning unique integers to distinct categories based on a vocabulary.
* *_Usage:_*
  * When number of categories is small
  * Categories represent limited ranges or ordinal values
  * Examples: dog breeds, days of week, ratings (1-3)

---

#### 9.2.3.2. One‐Hot Encoding

* **One-Hot Encoding**: creates dummy variables for categorical features where order does not matter.
    * Example: convert categorical values into binary representation
        * Red → 00
        * Blue → 01
    * Used when no ordinal relationship exists and integer encoding is insufficient.

---

*One‐Hot Encoding*
Categorical Value | Integer Encoding or Creating a Vocabulary Mapping | One‐Hot Encoding
---|---|---
Red | 0 | 00
Blue | 1 | 01

<!-- _class: centered -->

---

#### 9.2.3.3. Out of Vocab (OOV)

* **Handling Outliers**: Create a single "_out of vocabulary_" category to group rare outliers together, avoiding unnecessary training on individual outliers.
* This approach saves computational resources and simplifies model development.
* Training data categories are reduced by aggregating rare anomalies into a single category.

---

#### 9.2.3.4. Feature Hashing

* **Hashing**: applies a hash function to categorical features using their hash values as indices
    * **Advantages**:
        * No need to update vocabulary when feature distribution changes
    * **Disadvantage**:
        * Often causes collisions

---

#### 9.2.3.5. Hybrid of Hashing and Vocabulary

* **Approach**: Replace standard vocabulary categories with hashed ones to represent out-of-box data categories
* 
* **Advantage**: Model learns to recognize and categorize out-of-box data despite lack of predefined vocabulary
* 
* **Benefits**: Hashing approach allows for more flexibility in handling unseen data

---

#### 9.2.3.6. Embedding

* **What is Embedding?**: A categorical feature represented as a continuous-valued feature
* **How used in DL**: Converted from indices to an embedding for text classification and document classification tasks
    * Typically used with "bag-of-words" representations of documents

---

### 9.2.4. Feature Selection

* **Feature Selection**: Selecting a subset of useful input variables to predict a target variable
    * **Dimensionality Reduction**: Reducing the number of features to:
        * Reduce noise and overfitting problems
        * Decrease training time and computational resources

---

## 9.3. Class Imbalance

* **Classification Model False Negatives**: In a classification model, a false negative occurs when a patient is predicted to be healthy but actually has the disease.
    * This misclassification can lead to incorrect diagnoses and treatment decisions.
    * Minimizing false negatives is crucial for accurate outcomes in classification models.

---

### 9.3.1. Classification Threshold with Precision and Recall

**Classification Threshold**
classification threshold is a value that determines when to classify as positive or negative
usually set by human and assumed to be 0.5

* **Choosing Threshold**: affects false positives and false negatives
    * Raising threshold reduces false positives, increases precision
    * Lowering threshold reduces false negatives, increases recall
* **Precision vs Recall**:
    * Precision: true positives / total positive predictions
    * Recall (TPR): true positives / total samples of interest

---

### 9.3.2. Area under the Curve (AUC)

* **Classification Problem Types**
  * _AUC ROC_: balanced dataset with equal examples for both classes
  * _AUC PR_: imbalanced dataset with unequal examples for both classes

---

#### 9.3.2.1. AUC ROC

* **ROC Curve**: a graph showing classification model performance at all thresholds
* * _AUC (Area Under Curve)_*: measures 2D area under ROC curve, representing binary classification model's class separation ability
    * AUC closer to 1.0 = better class separation, up to 1.0

---

#### 9.3.2.2. AUC PR

* **Precision-Recall Curve**: a graph measuring Precision values on y-axis and Recall values on x-axis, useful for imbalanced binary classification models.
* **AUC PR**: the area under the precision-recall curve, giving more attention to the minority class, especially in highly skewed domains.

---

## 9.4. Feature Crosses

* **Feature Cross**: A synthetic feature created by multiplying two or more features, often used to add nonlinearity to linear models.
* **Use of Feature Crosses**:
  * To increase predictive ability when a single feature has limited value on its own
  * To represent nonlinearity in complex models by creating new interactions between features

---

## 9.5. TensorFlow Transform

* **Efficient Input Pipeline for TensorFlow Models**: 
  * Utilizing the TF Data API
  * Leveraging TensorFlow Transform for optimization

---

### 9.5.1. TensorFlow Data API (tf.data)

* **Improve Model Execution Speed**: Reduce device idle time with efficient data input pipeline best practices
* *_tf.data_* API provides transformations for:
  * _Prefetching_ transformation to overlap preprocessing and model execution
    * `_tf.data.Dataset.prefetch()_`
  * _Interleaving_ transformation to parallelize data reading
    * `_tf.data.Dataset.interleave()`_
* Use *_cache_* transformation to store data in memory during the first epoch
  * `_tf.data.Dataset.cache()`_
* Reduce memory usage with transformations and minimize overhead

---

### 9.5.2. TensorFlow Transform

* **TensorFlow Transform**: Allows transformations prior to training, reducing training-serving skew, using TFX with Cloud Dataflow.
    * _Key steps_:
        - Analyze and transform training data
        - Read and transform evaluation data
    * Utilizes Cloud Dataflow for pipeline execution

---

*TensorFlow Transform*
Step | TFX library | GCP service
---|---|---
Data extraction & validation | TensorFlow Data Validation | Cloud Dataflow
Data transformation | TensorFlow Transform | Cloud Dataflow
Model training & tuning | TensorFlow (tf.Estimators and tf.Keras) | Vertex AI Training
Model evaluation & validation | TensorFlow Model Analysis | Cloud Dataflow
Model serving for prediction | TensorFlow Serving | Vertex AI Prediction

<!-- _class: centered -->

---

## 9.6. GCP Data and ETL Tools

* **Data Transformation Tools in Google Cloud**
  * _Cloud Data Fusion_: a code-free ETL service for building and managing data pipelines from various sources.
  * _Dataprep by Trifacta_: a serverless, intelligent tool for exploring, cleaning, and preparing structured and unstructured data.

---

## 9.7. Summary

* **Feature Engineering Summary**
  * Transforming features is crucial for model training and serving
  * Techniques include bucketing, normalization, linear encoding, one-hot encoding, hashing, and embedding for numerical and categorical features
  * Selecting features and using dimensionality reduction techniques like PCA are important

---

## 9.8. Exam Essentials

* **Data Preprocessing Fundamentals**
  * Understand when to apply transformations (before or during training) and techniques such as:
    * Encoding structured data types (bucketing, normalization, hashing, one-hot encoding)
  * Feature selection: dimensionality reduction for improving model performance
  * Addressing class imbalance with metrics like accuracy, AUC, precision, and recall

---

# 10. Chapter 4Choosing the Right ML Infrastructure

---

## 10.1. Pretrained vs. AutoML vs. Custom Models

* **Pretrained Models**: Easy-to-use pre-trained models by Google, deployed via APIs, with a serverless approach and a free tier.
    *  Can be used without ML expertise
    *  Fast incorporation of ML into applications
* **AutoML (Vertex AI)**: Build your own model using your data, choosing the best algorithm. Requires cloud resources for training and deployment.
    *  Provides flexibility beyond AutoML options
    *  Requires team of ML experts or significant expertise
* **Custom Models**: Most flexible option, allowing choice of algorithm, hardware provisioning, and data types. Fewer customers have access to custom models due to high expertise requirements.

---

## 10.2. Pretrained Models

* **Pretrained Models**: Machine learning models trained on large datasets, performing well in benchmark tests, supported by large teams.
* **Using Pretrained Models**: Customers can start using these models immediately through web console or SDKs.
    * **Available Google Cloud Pretrained Models**:
        * Vision AI
        * Video AI
        * Natural Language AI
        * Translation AI
        * Speech-to-Text and Text-to-Speech

---

### 10.2.1. Vision AI

* **Vision AI** provides convenient access to machine learning algorithms for image processing, including object detection, face detection, and handwriting analysis.
    * Can be used from a browser at `https://cloud.google.com/vision` or in production by uploading an image or URL.
        * Predictions include:
            * Objects detected
            * Image labels (e.g. Table, Furniture)
            * Dominant colors
            * "Safe Search" classification (Adult, Spoof, Medical, Violence, Racy)

---

### 10.2.2. Video AI

* **Video AI**: recognizes objects, places, and actions in videos with pre-trained machine learning models.
    * Can process stored or streaming videos, returning results in real-time.
    * Supports over 20,000 different object, place, and action labels.
        * Enhances metadata for video search, tagging, and analysis.

---

### 10.2.3. Natural Language AI

* **Overview**: The Natural Language AI provides insights from unstructured text using pretrained machine learning models for entity extraction, sentiment analysis, syntax analysis, and categorization.
    * _Entity Extraction_: identifies entities with additional information like Wikipedia links
    * _Sentiment Analysis_: provides positive/negative/neutral scores with magnitude for sentences and entities
* **Use Cases**:
  * Measure customer sentiment toward products using entity analysis and sentiment analysis
  * Use Healthcare Natural Language API to extract medical insights from clinical notes and research documents

---

### 10.2.4. Translation AI

* **Translation Service**: uses Google Neural Machine Translation technology to support over 100 languages, translating between any pairs
    * Offers two levels: Basic and Advanced, with the latter allowing for document translation and glossary usage
        * **Advanced Level Features**:
            * Supports audio translations in real-time via Media Translation API

---

### 10.2.5. Speech‐to‐Text

* _Speech-to-Text Service_: converts recorded or streaming audio to text
* Used for creating subtitles for video recordings and streaming videos
* Often combined with a translate service for multilingual subtitles

---

### 10.2.6. Text‐to‐Speech

* The Text‐to‐Speech service uses DeepMind's speech synthesis expertise to provide humanlike speech.
    * Supports 220+ voices in 40+ languages and variants
        *_Unique voices available for brand representation_

---

## 10.3. AutoML

* **AutoML Definition**: Automated process of automating model training tasks, allowing users to bring in data and configure settings with minimal input.
    * **Supported Problems**: Image classification, text classification, translation, and others using well-understood ML problems
    * **Data Types and Use Cases**:
        * Structured data
        * Images/video
        * Natural language
        * Recommendations AI/Retail AI

---

### 10.3.1. AutoML for Tables or Structured Data

* **Overview of AutoML Tables**: Vertex AI provides two methods for training ML models: BigQuery ML and Vertex AI Tables, which can be triggered using Python, Java, or Node.js.
    * **Vertex AI Tables**:
        * Can deploy model on an endpoint and serve predictions through a REST API
        * Available AutoML algorithms:
            * Table (Classification): AUC ROC, Logloss, Precision at Recall, Recall at Precision
            * Table (Regression): RMSE, RMSLE, MAE
            * Time-series data: Forecasting, RMSE, RMSLE, MAPE, Quantile loss

* **Configuring AutoML Jobs**: 
    * Set "budget" to limit training time and enable early stopping to avoid unnecessary costs.

---

        * Minimum budget values vary by model type (e.g. 20 hours for Object Detection AutoML)
        * Node hour prices differ by model type due to varying hardware usage

---
*AutoML for Tables or Structured Data*
Data Type | ML Problem | Metrics
---|---|---
Table (IID) | Classification | AUC ROC, AUC ROC, Logloss, Precision at Recall, Recall at Precision
Table (IID) | Regression | RMSE, RMSLE, MAE
Time‐series data | Forecasting | RMSE, RMSLE, MAPE, Quantile loss

<!-- _class: centered -->

---

### 10.3.2. AutoML for Images and Video

* **Vertex AI AutoML for Image and Video Data**: automates building models for image classification, multiclass classification, object detection, and segmentation, as well as video classification, action recognition, and object tracking.
    * Supported devices: iPhones, Android phones (including Google Pixel and Samsung Galaxy), and Edge TPU devices
* **AutoML Edge Models**: optimized for edge devices with low memory and latency requirements

---

*AutoML for Images and Video*
Data Type | ML Problem | AutoML Details
---|---|---
Image | Image classification (single) | Predict one correct label from a list of labels provided by user during training.
Image | Multiclass classification | Predict all the correct labels that you want assigned to an image.
Image | Object detection | Predict all the locations of objects that you're interested in.
Image | Image segmentation | Predict per‐pixel areas of an image with a label.
Video | Classification | Get label predictions for entire videos, shots, and frames.
Video | Action recognition | Identify the action moments in video.
Video | Object tracking | Get labels, tracks, and time stamps for objects you want to track in a video.

<!-- _class: centered -->

---

### 10.3.3. AutoML for Text

* **AutoML Text Problems**: 
  * _Text Classification_: predict one label for a document
  * Multi-Label Classification: predict all labels for a document
  * Entity Extraction: identify entities in text items
  * Text-to-Text Translation: convert source to target language

---

*AutoML for Text*
Data Type | ML Problem | AutoML Details
---|---|---
Text | Text classification | Predict the one correct label that you want assigned to a document.
Text | Multi‐label classification | Predict all the correct labels that you want assigned to a document.
Text | Entity extraction | Identify entities within your text items.
Text to text | Translation | Convert text from source language to target language.

<!-- _class: centered -->

---

### 10.3.4. Recommendations AI/Retail AI

* GCP's AutoML solution for retail includes Retail Search, Vision API Product Search, and Recommendations AI.
    * **Retail Search**: Google-quality search that can be customized and built upon user intent and context
    * **Vision API Product Search**: Trained on reference images of products to enable image-based searches
    * **Recommendations AI**: Analyzes customer behavior and context to drive engagement through relevant recommendations

---

*Recommendations AI/Retail AI*
Recommendation Type | What Does It Predict? | Usage | Data Used | Optimization Objective
---|---|---|---|---
Others you may like | The next product the user is likely to buy | Product page | Customer behavior and product relevance | Click‐through rate
Frequently bought together (shopping cart expansion) | Items frequently bought together for a specific product within the same shopping session | Checkout page | User behavior in shopping cart | Revenue per order
Recommended for you | The next product the user likely will buy | Home page | User viewing history and context | Click‐through rate
Similar items | Other products with similar attributes | Product page | Product catalog | Click‐through rate

<!-- _class: centered -->

---

### 10.3.5. Document AI

* **Overview**: Document AI extracts details from various document types, including forms, government documents, and scanned images.
    * **Document Types**: Forms (with handwritten text), passports, driver's licenses, tax filings.
        * **Variability**: Text structure, handwritten ink, errors.
* **Document AI Platform**: 
    * Detects document quality
    * Extracts text, layout, key/value pairs, entities

---

### 10.3.6. Dialogflow and Contact Center AI

* _Dialogflow_ is a conversational AI offered by Google Cloud for building chatbots and voicebots.
    * It integrates with various services, including telephony and contact center solutions.
        * Provides a comprehensive CCAI (Contact Center Artificial Intelligence) solution.

---

#### 10.3.6.1. Virtual Agent (Dialogflow)

**Advanced Virtual Agent Solution**
* _Rapid development for enterprise use_
* _Handles topic switching, supplemental questions, and multichannel support 24/7_
* _Complex cases forwarded to human agents_

---

#### 10.3.6.2. Agent Assist

* **Agent Assist**: provides real-time support by:
  * Identifying intent
  * Offering pre-crafted responses
  * Accessing a centralized knowledge base

---

#### 10.3.6.3. Insights

* *_Service Purpose_*: Measures sentiment of driver calls to help leadership improve call center operations.
* **Method**: Uses natural language processing technology
* *_Goal_*: Inform leadership on areas for improvement

---

#### 10.3.6.4. CCAI

* Contact Center AI platform supports multichannel customer communication.
* Dialogflow and CCAI use advanced machine learning for natural language processing.
* Detailed understanding of CCAI not required for this exam.

---

## 10.4. Custom Training

* **GPU Training**: Custom training with GPUs accelerates deep learning model training, reducing computation time by an order of magnitude.
* *Compute-intensive operations*: GPU massively parallel architectures speed up matrix multiplications and other compute-intensive tasks.
* *_CPU vs. GPU_*: Training on a single CPU can take days or months, while GPU acceleration reduces training time to hours.

---

### 10.4.1. How a CPU Works

* A **CPU** is a processor that can handle various types of workloads and supports multiple operations.
* It loads data from memory, performs an operation, and stores the result back into memory for each calculation.
* This serial processing is inefficient for complex tasks like training ML models on large datasets.

---

### 10.4.2. GPU

* **GPUs in Vertex AI**: 
  * A GPU is a specialized chip for rapidly processing data to create images.
  * It works with the CPU, but can improve speed by an order of magnitude.

* **Specifying GPUs**:
  * Use `machineSpec.acceleratorType` and `machineSpec.acceleratorCount` to specify GPU type and number per VM.
  * Ensure virtual CPUs and memory match machine type requirements.

* **GPU Restrictions**: 
  * Available in specific regions, with a list of locations: `cloud.google.com/vertex-ai/docs/general/locations`.
  * Limitations on the number of GPUs per instance, subject to change as more instance types are introduced.

---

### 10.4.3. TPU

* **TPUs vs GPUs**: TPUs were designed specifically for machine learning workloads and provide better performance
    * _Matrix Processing_: TPU's primary task is matrix processing, utilizing multiple matrix multiply units (MXUs) with high multiplication-accumulate operations.
    * _Advantage_: Thousands of directly connected multiply-accumulators form a large physical matrix, enabling huge operations on huge matrices.

---

#### 10.4.3.1. How to Use TPUs

**Cloud TPU Configurations**

* **TPU Device**: Single device
* *_TPU Pod_*: Group of devices connected by high-speed interconnects
	+ Scalable, low-code changes required
* **TPU Slice**: Subdivision of a TPU Pod
* **TPU VM**: Virtual machine with TPU resources

---

#### 10.4.3.2. Advantages of TPUs

* **Comparing Computational Speed**
  * **GPU vs TPU**: TPUs accelerate computational speed by an order of magnitude compared to GPUs.
  * **Training Time Comparison**:
    * CPUs: months
    * GPUs: days
    * TPUs: hours

---

#### 10.4.3.3. When to Use CPUs, GPUs, and TPUs

**Hardware Selection Guidelines**

* **CPUs**
	+ Rapid prototyping, small models, custom C++ ops
	+ Limited I/O or network bandwidth on host
* **GPUs**
	+ Existing source code not available for change
	+ Large models with medium batch size
	+ Missing TensorFlow ops on TPUs
* **TPUs**
	+ Matrix computations, no custom ops, large effective batch sizes

**Cloud TPU Limitations**

* *Frequent branching or algebraic operations*
* *Sparse data and high precision*
* *Deep neural networks with custom C++ ops*

---

#### 10.4.3.4. Cloud TPU Programming Model

* **TPU Bottleneck**: Data transfer between Cloud TPU and host memory is a significant bottleneck due to slow PCIe bus.
* **Optimization Strategy**: Execute most or all of the training loop on the TPU for optimal performance.
* *_Ideal Programming Model_*: Leverage TPU's high bandwidth for efficient computation.

---

## 10.5. Provisioning for Predictions

* **Prediction Phase**: Focuses on generating output without requiring input data
    * **Online Prediction**: Real-time querying, stored data used to reduce response time
    * **Batch Prediction**: Uses pre-existing input data for cost-effective prediction

---

### 10.5.1. Scaling Behavior

* **Autoscaling in Vertex AI**: Autoscales prediction nodes when CPU usage is high
    * _Requires monitoring of multiple resources_ 
        - CPU usage
        - Memory usage
        - GPU usage

---

### 10.5.2. Finding the Ideal Machine Type

* To determine the ideal machine type for a custom prediction container, benchmark the instance by calling prediction calls until it hits 90+ percent CPU utilization.
    * Consider single-threaded web server limitations and resource effective utilization (CPU, memory, GPU).
    * Include model type, serving wrapper code, latency and throughput requirements, and price in the decision-making process.
* Using GPUs can accelerate predictions, but there are restrictions:
    * Limited to TensorFlow SavedModel or custom container with GPU support
    * Not available in all regions
    * Limitations on the number of GPUs per machine type

---

### 10.5.3. Edge TPU

**Edge Inference**
Edge devices collect and process data on device itself due to limited bandwidth.

* **Key Benefits of Edge TPU:**
	+ Accelerates ML inference with 4 trillion operations per second (4 TOPS)
	+ Consumes only 2 watts of power
* **Edge TPU Availability:**
	+ Available for prototyping and production devices in various form factors

---

### 10.5.4. Deploy to Android or iOS Device

* **ML Kit**: Google's machine learning package for mobile apps
    * **Key Benefits**: Optimized for device performance, allows offline predictions, and reduces bandwidth usage
        * **Deployment Options**: Train model on Google Cloud, use AutoML or custom model

---

## 10.6. Summary

* **Overview**: learned about pretrained models on Google Cloud, AutoML applicability, and hardware options for training and prediction workloads
* _Key Hardware Options_:
  * GPUs (General Purpose Computing)
  * TPUs (Accelerated Matrix Multiplication)
* **Edge Deployment**: deploying to edge devices beyond cloud infrastructure

---

## 10.7. Exam Essentials

* **Choosing the Right Machine Learning (ML) Approach**
  * Choose between pretrained models, AutoML, or custom models based on solution readiness, flexibility, and approach.
  
* **Provisioning Hardware for Training and Prediction**
  * Train with GPU or TPU hardware, using instance types that support specialized hardware. For prediction, use cloud-based CPUs and GPUs for scalability and deployment.
  
* **Serverless ML Solutions**
  * Use pretrained models and domain-specific solutions to solve problems without provisioning hardware.

---

# 11. Chapter 5Architecting ML Solutions

---

## 11.1. Designing Reliable, Scalable, and Highly Available ML Solutions

* **ML Pipeline**: data collection, transformation, model training, tuning, deployment, and monitoring
  * Automate pipeline steps using Google Cloud Storage, Dataflow, Google Cloud Vertex AI Training, and Vertex AI Pipelines
  * Use scalable infrastructure for distributed training and hyperparameter tuning with Vertex AI AutoML and Experiments
* **Deployment and Monitoring**: deploy models to production using Vertex AI Prediction and monitor model performance with Vertex AI Model Monitoring

---

*Designing Reliable, Scalable, and Highly Available ML Solutions*
ML Workflow | Google Cloud Service
---|---
Data collection | Google Cloud storage, Pub/Sub (streaming data), BigQuery
Data transformation | Dataflow
Model training | Custom models (Vertex AI Training and Vertex AutoML)
Tuning and experiment tracking | Vertex AI hyperparameter tuning and Vertex AI Experiments
Deployment and monitoring | Vertex AI Prediction and Vertex AI Model Monitoring
Orchestration and CI/CD | Vertex AI Pipelines
Explanations and responsible AI | Vertex Explainable AI, model cards

<!-- _class: centered -->

---

## 11.2. Choosing an Appropriate ML Service

**Google Cloud ML Services**

* **Top Layer**: AI solutions (Document AI, Contact Center AI, Enterprise Translation Hub) - managed SaaS offerings with no code implementation.
	+ Built on top of Vertex AI services
* **Middle Layer**: Vertex AI - includes pretrained APIs, AutoML, and Workbench for data science workflow management.
	+ AutoML: enriches use cases with custom business models
	+ Workbench: development environment for custom model building
* **Bottom Layer**: Infrastructure (compute instance, containers, TPUs, GPUs, storage) - requires manual management for scalability and reliability.

---

*Choosing an Appropriate ML Service*
GCP Service | When to Use
---|---
BigQuery ML | You have structured data stored in a BigQuery data warehouse because BigQuery ML requires a tabular dataset. You are comfortable with SQL and the models available in BigQuery ML match the problem you are trying to solve. We are going to cover all the models in Chapter 14.
AutoML (in the context of Vertex AI) | Your problem fits into one of the types that AutoML supports, such as classification, object detection, sentiment analysis, and translation.

<!-- _class: centered -->

---

## 11.3. Data Collection and Data Management

* **Data Stores in Google Cloud**
  * *Google Cloud Storage*: general-purpose object storage for large amounts of unstructured data.
  * *BigQuery*: fully-managed enterprise data warehouse service for structured data analysis.
  * *Vertex AI's datasets*: dataset management for machine learning model training and annotation.
  * *Vertex AI Feature Store*: feature store for managing and serving features to machine learning models.

---

### 11.3.1. Google Cloud Storage (GCS)

* **Google Cloud Storage**: service for storing objects in Google Cloud
    * Supports various data types (images, videos, audio, unstructured data)
    * Can store large files (at least 100 MB) and split into shards for improved throughput
        * Shards: combine individual data types into large files of size at least 100 MB

---

### 11.3.2. BigQuery

* **BigQuery Data Storage**: Store tabular data in BigQuery for better speed, use tables instead of views for training data.
* **Accessing BigQuery**: Use Google Cloud console, `bq` command-line tool, REST API, or Vertex AI Jupyter Notebooks with BigQuery Magic/Python client.
* **Google Cloud Tools for BigQuery**:
  * TensorFlow/Keras: `tf.data.dataset reader for BigQuery`
  * TFX: `BigQuery client`
  * Dataflow: `BigQuery I/O connector`

---

*BigQuery*
Framework | Google Cloud tool to read data from BigQuery
---|---
TensorFlow or Keras | `tf.data.dataset reader for BigQuery` and tfio.BigQuery.BigQueryClient()

<!-- _class: centered -->

---

### 11.3.3. Vertex AI Managed Datasets

* **Use Managed Datasets**: Train custom models using Vertex AI managed datasets instead of ingesting data directly from storage.
* * *
* **Benefits**:
  * Centralized dataset management
  * Integrated data labeling for unstructured data
  * Easy lineage tracking and model governance
  * Easy comparison between AutoML and custom models
* 
* **Alternatives**: More control over data splitting in training code, or not requiring lineage between data and model.

---

### 11.3.4. Vertex AI Feature Store

* **Vertex AI Feature Store**: A fully managed repository for organizing, storing, and serving ML features.
    * **Features**:
        * Can be fetched to train custom or AutoML models
        * Users can ingest feature values from various data sources
    * **Benefits**:
        * No need to compute and save feature values in separate locations
        * Detects drifts and mitigates data skew by creating features centrally

---

### 11.3.5. NoSQL Data Store

* **Static Reference Features** 
    * Stored in optimized NoSQL database
    * Engineered for singleton lookup operations
    * Used for submillisecond latency applications

* **NoSQL Data Store Options**
  * Memorystore: _managed in-memory database_ with submillisecond read access
  * Datastore: fully managed, scalable document database with millisecond latency
  * Bigtable: massively scalable key-value map with millisecond latency and linear scalability

---

*NoSQL Data Store*
****|  Memorystore | Datastore | Bigtable
---|---|---|---
Description | Memorystore is a managed in‐memory database. When you use its Redis offering, you can store intermediate data for submillisecond read access. Keys are binary‐safe strings, and values can be of different data structures. | Datastore is a fully managed, scalable NoSQL document database built for automatic scaling, high performance, and ease of application development. Data objects in Datastore are known as entities. An entity has one or more named properties in which you store the feature values required by your model or models. | Bigtable is a massively scalable NoSQL database service engineered for high throughput and for low‐latency workloads. It can handle petabytes of data, with millions of reads and writes per second at a latency that's on the order of milliseconds. The data is structured as a sorted key‐value map. Bigtable scales linearly with the number of nodes.
Retrieval | Submillisecond retrieval latency on a limited amount of quickly changing data, retrieved by a few thousand clients. | Millisecond retrieval latency on slowly changing data where storage scales automatically. | Millisecond retrieval latency on dynamically changing data, using a store that can scale linearly with heavy reads and writes.
Use cases | User‐feature lookup in real‐time bidding that requires submillisecond retrieval time.

<!-- _class: centered -->

---

## 11.4. Automation and Orchestration

* **Machine Learning Workflows**: Data collection, preprocessing, model training, evaluation, and deployment
* _**Key Components of an ML Pipeline**:_
    * Orchestration of steps in the pipeline
    * Automation for continuous model training
* **Tools for Managing Pipelines**: 
    * Kubeflow Pipelines (Kubernetes-based)
    * Vertex AI Pipelines (serverless)

---

### 11.4.1. Use Vertex AI Pipelines to Orchestrate the ML Workflow

**Vertex AI Pipelines Summary**
* A managed service for automating, monitoring, and governing ML systems in a serverless manner
* Stores workflow artifacts in Vertex ML Metadata for lineage analysis
* Supports TensorFlow Extended (v0.30.0+) or Kubeflow Pipelines SDK (v1.8.9+)
* Enables experiments tracking for GA now

---

### 11.4.2. Use Kubeflow Pipelines for Flexible Pipeline Construction

* **Overview of Kubeflow**: An open source Kubernetes framework for developing and running portable ML workloads
    * Includes Kubeflow Pipelines for composing, orchestrating, and automating ML systems
    * Supports local, on-premises, or cloud deployments (e.g., Google Cloud)
* **Kubeflow Pipelines Features**:
    * Provides a flexible way to construct pipelines with simple code
    * Integrates Vertex AI functionality like AutoML through Pipeline Components

---

### 11.4.3. Use TensorFlow Extended SDK to Leverage Pre‐built Components for Common Steps

* **TensorFlow and Vertex AI**: prebuilt components for data ingestion, validation, and training
* **TFX**: frameworks for defining, launching, and monitoring machine learning models in production
* *_Recommended over TensorFlow Extended SDK_*: existing use of TensorFlow, working with structured and textual data, or handling large datasets

---

### 11.4.4. When to Use Which Pipeline

* **Vertex AI Pipelines**: Can run Kubeflow Pipelines v1.8.9+ or TensorFlow Extended v0.30.0+
    * Uses Apache Beam under the hood
    * Supports distributed processing backends like Spark, Dataflow, and Flink
* **Recommending use cases**:
    * TFX for large-scale ML workflows with terabytes of data
    * Kubeflow Pipelines for smaller or more complex pipelines

---

## 11.5. Serving

* **Prediction Methods**: 
  * _Offline Prediction_: Making predictions on data that has been pre-processed and stored
  * Online Prediction: Receiving and processing new, real-time data to make predictions

---

### 11.5.1. Offline or Batch Prediction

* **Offline Batch Prediction**: Perform predictions on large batches of data using a trained model, suitable for use cases like recommendations, demand forecasting, and text classification.
* **Vertex AI Batch Prediction**: Run batch prediction jobs on data stored in BigQuery or Google Cloud Storage.
* **Use Cases**: Recommendations, demand forecasting, segment analysis, and classifying large batches of text.

---

### 11.5.2. Online Prediction

**Near Real-Time Predictions**

* **Deployment**: Deploy model endpoints using HTTPS, microservices architecture, and services like Vertex AI, App Engine, or GKE.
* 
  * **Synchronous**: Caller waits for prediction before proceeding.
    * _Example Use Cases_: Real-time bidding, real-time sentiment analysis of Twitter feeds.
  * 
    * **Asynchronous**: End user polls feature store or data store for predictions in real time.
      * _Methods_:
        + Push: Model generates predictions and notifies end user.
        + Poll: Model stores predictions in low-latency database; end user periodically checks database.

**Minimizing Latency**

* **Model Level**:

---

  - Minimize model latency by building smaller models with fewer layers.
    * _Example_: Using Cloud GPU or TPU for acceleration.
* 
  - **Serving Level**:
    + Store input features in low-latency data store.
    + Precompute predictions using offline batch-scoring job.
    + Cache predictions.

---
## 11.6. Summary

* **Key Topics**: 
    * Designing reliable ML solutions on GCP
    * Choosing the right services for each layer of the GCP AI/ML stack
    * Data collection and management with Vertex AI and BigQuery
* **Automation and Orchestration**: 
    * Using Vertex AI Pipelines, Kubeflow Pipelines, and TFX pipelines for automation
* **Model Serving**: 
    * Serving models in batch mode and real-time using Vertex AI Prediction

---

## 11.7. Exam Essentials

* Design reliable, scalable, and highly available ML solutions using Google Cloud AI/ML services.
    * Choose an appropriate ML service from GCP's AI/ML stack based on the use case and expertise.
    * Implement data management, automation, and orchestration to optimize pipeline efficiency.
    * Deploy models with best practices for serving data, including batch vs. real-time prediction and latency management.

---

# 12. Chapter 6Building Secure ML Pipelines

---

## 12.1. Building Secure ML Systems

* **Data Security**: Google Cloud provides built-in security measures for enterprise users' data
* _**Encryption Measures**_: 
    * Data at Rest: Encrypting stored data to protect it from unauthorized access
    * Data in Transit: Encrypting data while it is being transmitted over the internet

---

### 12.1.1. Encryption at Rest

* **Encryption in Google Cloud**: 
    * Data is encrypted at rest by default with customer-managed or Google-managed keys.
    * AEAD encryption can be used for individual table values in BigQuery.

* **Hash Integrity Checking**:
    * Google Cloud Storage supports CRC32C and MD5 hashes to check data integrity.

* **Encryption Types**:
    * Server-side encryption occurs after data is received, before disk storage.
    * Client-side encryption occurs before data is sent, with encrypted data arriving at Cloud Storage.

---

*Encryption at Rest*
Server‐Side Encryption | Client‐Side Encryption
---|---
Encryption that occurs after the cloud storage receives your data, but before the data is written to disk and stored. | Encryption that occurs before data is sent to Cloud Storage and BigQuery. Such data arrives at Cloud Storage and BigQuery already encrypted but also undergoes server‐side encryption.
You can create and manage your encryption keys using a Google Cloud Key Management Service. |  You are responsible for the client‐side keys and cryptographic operations.

<!-- _class: centered -->

---

### 12.1.2. Encryption in Transit

* *Transport Layer Security (TLS) is used by Google Cloud to secure data transmission.* 
    * *Protects data from eavesdropping and tampering while in transit.*

---

### 12.1.3. Encryption in Use

* **Encryption in Use**: Encrypts data in memory to protect against compromise or data exfiltration
    * **Confidential Computing**: A service that encrypts data in use using Confidential VMs and Confidential GKE Nodes
        * Provides an additional layer of protection for sensitive data

---

## 12.2. Identity and Access Management

* _Identity and Access Management (IAM) in Google Cloud_ 
    * Manage access to data and resources at project or resource level
    * Project-level roles: assign roles to principals for project-wide access
    * Resource-level roles: set IAM policies on specific resources for granular access control

---

### 12.2.1. IAM Permissions for Vertex AI Workbench

* **Vertex AI Workbench**: A data science service offered by Google Cloud Platform (GCP) that leverages JupyterLab to explore and access data.
    * _Uses Virtual Private Cloud, providing encryption at rest and in transit._
    
* **Types of Notebooks**:
  * _User-Managed Notebook_: Highly customizable but requires more setup and management.
  * _Managed Notebook_: Less customizable but integrates with Cloud Storage and BigQuery, and has automatic shutdown.

* **Access Modes**: 
  * _Single User Only_: Grants access only to a specified user.
  * _Service Account_: Grants access to a service account, which can be used by multiple users.

---

### 12.2.2. Securing a Network with Vertex AI

* **Security in Google Cloud**: The cloud provider monitors security threats, while end users are responsible for protecting data and assets.
*   **Shared Responsibility Model**: Cloud provider is responsible, but user must secure their own data and resources.
*   **Shared Fate Model**: An ongoing partnership to improve security through various components: 
    *   _Help getting started_: Secure blueprints with IaC and security recommendations
    *   _Risk Protection Program_
    *   _Assured Workloads and Governance_

---

#### 12.2.2.1. Securing Vertex AI Workbench

* **Secure Your Workbench**
  * Use a private IP address to reduce attack surface and expose sensitive data.
  * Connect your instance to a VPC network in the same project using private services access.

* **Configure Shared VPC Network**
  * Specify a shared VPC network or a VPC network within your project, enabling internal IP addresses and controlling service access with VPC Service Controls.

---

#### 12.2.2.2. Securing Vertex AI Endpoints

**Hosting Models with Vertex AI**

Vertex AI provides options for hosting models:
* **Public Endpoints**: publicly accessible to the Internet
* **Private Endpoints**: secure, low-latency connection to endpoint without public data traversal

To set up a private endpoint, follow these steps:

* Go to Endpoint > Create Endpoint and select Private
* Configure VPC Network Peering for high scalability and security

---

#### 12.2.2.3. Securing Vertex AI Training Jobs

* **Using private IP addresses** 
  * Connects training jobs to your network for more security and lower latency
  * Uses VPC to peer with custom Vertex AI training jobs
* **VPC Service Controls**
  * Provides defense in depth using IAM
  * Prevents service operations from accessing public buckets or tables
* **Recommended defense strategy** 
  * Use both VPC Service Controls and IAM for security

---

#### 12.2.2.4. Federated Learning

* **Federated Learning**: enables mobile phones and devices to collaboratively learn a shared prediction model without sharing training data
    * _Benefits_:
        * Smarter models
        * Lower latency
        * Less power consumption
    * _Key characteristic_: all training data remains on the device, ensuring privacy while allowing for collaborative learning

---

#### 12.2.2.5. Differential Privacy

**Differential Privacy**: 
* Protects sensitive information about individuals by sharing patterns within groups
* Allows quantifying degree of privacy protection provided by an algorithm
* Enables responsible training of machine learning models on private data

**Application to Machine Learning**
* Prevents memorization of individual patient medical histories in diagnosis models
* Allows secure training of models with PII data from distributed silos

---

#### 12.2.2.6. Format‐Preserving Encryption and Tokenization

* **Format-Preserving Encryption (FPE)**: Encrypts data in its original format, preserving structure.
* _Use cases_:
    * **Payment Card Verification**: Exposes required payment card info to employees while protecting sensitive details.
    * **Legacy Databases**: Allows encrypted data storage without changing database structure.

---

## 12.3. Privacy Implications of Data Usage and Collection

* **Data Sensitive Areas**: Google Cloud focuses on handling _personally identifiable information (PII)_ and _protected health information (PHI)_, particularly in sensitive areas.
    * **Key Information Types**: This includes name, address, Social Security number, date of birth, financial info, passport numbers, telephone numbers, and email addresses.
        * **HIPAA Privacy Rule**: Federal protection for PHI held by covered entities, giving patients rights while permitting disclosure for patient care.

---

### 12.3.1. Google Cloud Data Loss Prevention

* **Google Cloud Data Loss Prevention (DLP) API**: removes identifying information from text content, including tables, to prevent sensitive data disclosure.
    * **De-identification techniques**: masking, tokenization, encryption, and bucketing
* **Key concepts**:
  * **Data profiles**: identifies high-risk data across the organization for protection
  * **Risk analysis**: determines effective de-identification strategy or monitors changes after de-identification
  * **Inspection (jobs and triggers)**: automates DLP scans on Google Cloud Storage repositories

---

### 12.3.2. Google Cloud Healthcare API for PHI Identification

* The Google Cloud Healthcare API provides a de-identification operation to remove sensitive information from healthcare data.
    * This process can be highly configured and applies to various data types, including text, images, FHIR, and DICOM data.
        * The HIPAA Privacy Rule standard identifies 18 identifiers that must be handled with special care when de-identified

---

### 12.3.3. Best Practices for Removing Sensitive Data

* **Strategies for handling sensitive data**
  * Use views, Cloud DLP, and NLP APIs to identify and mask sensitive data in unstructured content.
  * Apply dimension-reducing techniques like PCA to combine features and protect data with multiple columns.
  * Utilize coarsening techniques such as:
    * Zeroing out IP addresses
    * Binning numeric quantities (e.g., age, birthdays)
    * Coarsening zip codes to first three digits
    * Using location identifiers or obfuscating unique characteristics

---

*Best Practices for Removing Sensitive Data*
Type of Data | Strategy Used
---|---
Data is restricted to specific columns in structured datasets. | You can create a view that doesn't provide access to the columns in question. The data engineers cannot view the data, but at the same time the data is live and doesn't require human intervention to de‐identify it for continuous training.
Sensitive data is part of unstructured content, but it's identifiable using known patterns or regex. | You can use Cloud DLP to address this type of data.
Sensitive data exists within images, videos, audio, or unstructured free‐form data. | Use NLP API, Cloud Speech API, and Vision AI and Video Intelligence API to identify the sensitive data such as email and location out of box and then mask or remove it.

<!-- _class: centered -->

---

*Best Practices for Removing Sensitive Data*
Field | Description
---|---
IP addresses | Zero out the last octet of IPv4 addresses (the last 80 bits if using IPv6).
Numeric quantities | Numbers can be binned to make them less likely to identify an individual; for example, age and birthdays can be changed into ranges.
Zip codes | Can be coarsened to include just the first three digits.
Location | Use location identifiers such as city, state, or zip code, or use a large range to obfuscate the unique characteristics of one row.

<!-- _class: centered -->

---

## 12.4. Summary

* **Data Security in Machine Learning**: 
  * Encryption at rest and transit
  * IAM for secure access to Vertex AI Workbench
* **Secure ML Development**:
  * Federated learning
  * Differential privacy
* **PII Data Management**:
  * Cloud DLP for identification and de-identification

---

## 12.5. Exam Essentials

* **Build Secure ML Systems**
  * Understand encryption at rest and in transit for ML data storage
  * Set up IAM roles and network security for Vertex AI Workbench
  * Learn about differential privacy, federated learning, and tokenization

* **Data Privacy Implications**
  * Identify and mask PII type data using Google Cloud DLP API
  * Identify and mask PHI type data using Google Cloud Healthcare API
  * Follow best practices for removing sensitive data

---

# 13. Chapter 7Model Building

---

## 13.1. Choice of Framework and Model Parallelism

* **Scaling Deep Learning**: Modern deep learning models require larger datasets and increased computational resources due to growing parameter sizes.
* **Distributed Training**: To train large models efficiently, multinode training with data parallelism and/or model parallelism is necessary.

---

### 13.1.1. Data Parallelism

* **Data Parallelism**: Splitting dataset into parts and assigning them to parallel machines or GPUs, using same parameters for forward propagation on each
* _Synchronous_ vs _Asynchronous_ strategies in distributed training: 
  * Synchronous: all nodes wait for gradient computation before proceeding
  * Asynchronous: nodes compute gradients independently and send back to main node

---

#### 13.1.1.1. Synchronous Training

* **Synchronous Training**: Model sends parts of data to each accelerator/GPU, with each GPU training solely on its part of the data. 
    * All GPUs compute outputs and gradients in parallel.
    * An all-reduce algorithm collects trainable parameters from each worker/accelerator.

---

#### 13.1.1.2. Asynchronous Training

* **Asynchronous Training**: allows workers to train independently, reducing downtime and idle periods.
    * _Reduces waiting time during maintenance_
    * Enables data parallelism across all workers.
* **All-Reduce Sync Strategy**: suitable for TPU and multi-GPUs.

---

### 13.1.2. Model Parallelism

* **Model Parallelism**: Breaks down a single model into smaller parts, each running on a separate GPU.
    * Benefits: Overcomes memory limitations when training large deep learning models.
    * Example: Train a ResNet50 model across 10 GPUs.
* **Distributed Training Strategies in TensorFlow**:
    * MirroredStrategy: Synchronous distributed training on multiple GPUs on one machine.
    * ParameterServerStrategy: Designates some machines as workers and others as parameter servers.

---

*Model Parallelism*
Strategy | Description
---|---
MirroredStrategy | Synchronous distributed training on multiple GPUs on one machine.
CentralStorageStrategy | Synchronous training but no mirroring.
MultiWorkerMirroredStrategy | Synchronous distributed training across multiple workers, each with potentially multiple GPUs or multiple machines.
TPUStrategy | Synchronous distributed training on multiple TPU cores.
ParameterServerStrategy | Some machines are designated as workers and some as parameter servers.

<!-- _class: centered -->

---

## 13.2. Modeling Techniques

Let's go over some basic terminology in neural networks that you might see in exam questions.

---

### 13.2.1. Artificial Neural Network

* **Artificial Neural Networks (ANNs)**: simplest type of neural network with one hidden layer.
* **Feedforward Neural Networks**: classic example of ANNs used for supervised learning, primarily with numerical and structured data, such as regression problems.

---

### 13.2.2. Deep Neural Network (DNN)

* **Deep Neural Networks (DNNs)**: ANNs with multiple hidden layers between input and output layers.
* **Definition**: A neural network with at least two hidden layers is considered a DNN, also known as a _deep net_.
* **Example**: Figure 7.5 illustrates the structure of a deep neural network.

---

### 13.2.3. Convolutional Neural Network

* **Overview of CNNs**: Convolutional neural networks (CNNs) are DNNs specialized for image input and image classification tasks.

---

### 13.2.4. Recurrent Neural Network

* **Recurrent Neural Networks (RNNs)**: designed for sequences of data, effective for natural language processing and time-series forecasting.
    * Popularized by LSTMs, which can learn long-term dependencies in sequential data.
    * Used for tasks like class labeling and predicting numerical values.

* **Training Neural Networks**:
    * Uses stochastic gradient descent with a chosen loss function.
    * Goal is to find weights and biases that minimize average loss across examples.

---

### 13.2.5. What Loss Function to Use

**Neural Network Loss Functions**
* The choice of loss function depends on the activation function used in the output layer.
* Table 7.2 summarizes loss functions based on ML problems:
	+ Regression: Mean Squared Error (MSE)
	+ Binary classification: Binary cross-entropy, categorical hinge loss, and squared hinge loss
	+ Multiclass classification: Categorical cross-entropy or sparse categorical cross-entropy

---

*What Loss Function to Use*
****|  Output | Output Layer Configuration or Activation Function | Loss Functions
---|---|---|---
Regression problem | Numerical output | One node with a linear activation unit | Mean squared error (MSE)
Binary classification problem | Binary outcome | Sigmoid activation unit | Binary cross‐entropy, categorical hinge loss, and squared hinge loss (Keras)
Multiclass classification problem | Single label multiclass | Softmax activation function | Categorical cross‐entropy (on one‐hot encoded data) and sparse categorical cross‐entropy (apply on integers)

<!-- _class: centered -->

---

### 13.2.6. Gradient Descent

* **Gradient Descent**: calculates the gradient of the loss curve at the starting point
    * _Direction_: always points in the steepest increase in the loss function
    * **Update Rule**: takes a step in the direction of the negative gradient to minimize loss

---

### 13.2.7. Learning Rate

* **Gradient Descent Algorithm**: updates point by multiplying gradient by a scalar (learning rate) to determine direction of next step
    * **Learning Rate** (_step size_): controls magnitude of update, values closer to 1 result in larger steps
        * affects convergence speed and accuracy of optimization

---

### 13.2.8. Batch

* _Gradient Descent Batch_: The total number of examples used to calculate the gradient in a single iteration.
* **Batch Size**: A large batch can increase computation time per iteration.
* **Small Batch vs Large Batch**: Small batches improve iteration speed, while large batches may slow down training.

---

### 13.2.9. Batch Size

* **Batch Size**: The number of examples in a batch
    * Typically fixed during training and inference
        * Can be dynamically adjusted using TensorFlow

---

### 13.2.10. Epoch

* **Epoch**: Training process that iterates through all training data exactly once
    * Typically consists of multiple passes (forward and backward)
    * Made up of one or more batches

---

### 13.2.11. Hyperparameters

* **Hyperparameters in ML Training**
    * Learning rate: affects training speed and accuracy
        + Too small: slow learning, but faster computation
        + Too large: fast learning, but potential loss of accuracy

---

#### 13.2.11.1. Tuning Batch Size

* **Batch Size Tuning**: 
  * Smaller batch sizes lead to higher accuracy and faster training time.
  * Batch size too small causes instability, too large causes long training time.
  * Smaller batches improve gradient updates and generalization.
* **Large Batch Sizes**:
  * Can cause out of memory errors during training.

---

#### 13.2.11.2. Tuning Learning Rate

* **Achieving a desirable learning rate is crucial** because:
  * It prevents wasted time and resources
  * Affects cloud GPU costs
  * Ensures accurate model predictions
  * Prevents over- or under-training

---

## 13.3. Transfer Learning

* _Transfer learning_ is the process of applying knowledge gained from one task to another related task in machine learning (ML).
    * It saves time and improves performance by reusing pre-trained models or layers.
        * Using available pretrained models as a starting point for training your own model
        * Enabling the development of models with limited data

---

## 13.4. Semi‐supervised Learning

* **Semi-Supervised Learning**: Machine learning approach combining small labeled data with large unlabeled data
* **Definition**: Combines a few labeled examples with many unlabeled examples during training
* **Positioning**: Falls between _unsupervised_ and _supervised_ machine learning

---

### 13.4.1. When You Need Semi‐supervised Learning

* **Semi-Supervised Learning**: Use unlabeled data to augment training data when labeled data is insufficient.
* **Benefits**:
	+ Increase training data size without additional resources
	+ Improve model accuracy
* **Limitations**:
	+ No guarantee of 100% accurate labels

---

### 13.4.2. Limitations of SSL

* **Semi-Supervised Learning**: Uses minimal labeled and large amounts of unlabeled data for classification tasks
* _Not Applicable to All Tasks_: Requires representative labeled data for success
* **Limited Representation Risk**: Labeled data can lead to biased models if it doesn't represent the entire distribution

---

## 13.5. Data Augmentation

* **Data Augmentation**: Increasing the size of a neural network's training dataset through minor alterations (flips, translations, rotations) to synthetically generate more data.
* **Types of Data Augmentation**:
  * *_Offline Augmentation_*: Applying data augmentation before training data is collected
  * *_Online Augmentation_*: Applying data augmentation during the training process

---

### 13.5.1. Offline Augmentation

* **Offline Augmentation**: Increases dataset size before training
    * Reduces need for large datasets during training
    * Preferred for smaller datasets due to increased storage and computation requirements.

---

### 13.5.2. Online Augmentation

* **Online Augmentation**: Perform data augmentation on a mini-batch before feeding it to a machine learning model.
* **Data Augmentation Techniques for Images**:
  * Flip
  * Rotate
  * Crop
  * Scale
  * Gaussian noise
  * Translate

---

## 13.6. Model Generalization and Strategies to Handle Overfitting and Underfitting

* **Key Concepts:** 
  * _Bias_: error rate of the training data; high bias means oversimplification
  * _Variance_: error rate of testing data; high variance results in poor generalization
    * Deep neural networks require finding optimal balance between capacity and complexity to generalize well

---

### 13.6.1. Bias Variance Trade‐Off

* _Balance between bias and variance is crucial in machine learning_
  * Overfitting (high variance, low bias) with simple models
  * Underfitting (low variance, high bias) with complex models
* Increasing capacity addresses underfitting, while specialized techniques are needed for overfitting.

---

### 13.6.2. Underfitting

* **Underfit Model**: Performs poorly on training and test datasets, with high bias and low variance.
    * Causes due to: *_Poorly cleaned data_*, *_High bias in model_*.
    * Solutions: *_Increase complexity_*, *_Remove noise from data_*, *_More epochs/training time_*

---

### 13.6.3. Overfitting

* **Overfitting**: Model performs well on training data, but poorly on new data or with added noise.
    * Causes low bias and high variance in model performance.
    * Can be addressed by increasing training examples, changing network complexity, or using regularization techniques.

---

### 13.6.4. Regularization

* **Regularization**: Shrinks learned estimates toward 0, tuning the loss function by adding a penalty term to prevent excessive fluctuation of coefficients.
    * _L1 regularization_ (lasso): Combats overfitting by shrinking parameters toward 0, making features obsolete. 
    * _L2 regularization_ (ridge): Combats overfitting by forcing weights to be small but not exactly 0.

* **Common issues with backpropagation**:
  * Exploding gradients: prevented by batch normalization and lower learning rate
  * Dead ReLU units: prevented by lowering the learning rate
  * Vanishing gradients: prevented or alleviated by using ReLU instead of sigmoid, increasing the depth and width of layers

---

*Regularization*
L1 Regularization | L2 Regularization
---|---
L1 regularization, also known as L1 norm or lasso (in regression problems), combats overfitting by shrinking the parameters toward 0. This makes some features obsolete. So, this works well for feature selection in case you have a huge number of features. | L2 regularization, or the L2 norm or ridge (in regression problems), combats overfitting by forcing weights to be small but not making them exactly 0.
L1 regularization penalizes the sum of absolute values of the weights. | L2 regularization penalizes the sum of squares of the weights.
L1 regularization has built‐in feature selection. | L2 regularization doesn't perform feature selection.
L1 regularization is robust to outliers. | L2 regularization is not robust to outliers.
L1 regularization helps with feature selection and reducing model size or leading to smaller models. | L2 regularization always improves generalization in linear models.

<!-- _class: centered -->

---

## 13.7. Summary

* **Model Parallelism & Data Parallelism**: Training neural networks with both approaches
    * _Key Strategies_: Model parallelism for large-scale models, data parallelism for large datasets
* *_Hyperparameters_*: Importance of learning rate, batch size, epoch, and hyperparameters in training neural networks
    * _Consequences_:
        + Decreasing learning rate slows down training
        + Increasing epoch may not improve performance
* *_Transfer Learning_*: Using pre-trained models to adapt to new tasks with advantages of improved accuracy
* *_Data Augmentation_*: Techniques for increasing dataset size, including online and offline methods (e.g. rotation, flipping)
    * _Use Cases_:

---

        + Online augmentation for large datasets
        + Offline augmentation for small datasets

---
## 13.8. Exam Essentials

* **Parallelism in Deep Learning**: Understand framework or model parallelism for large neural networks, including data parallel and distributed training with TensorFlow.
    * _Data Parallelism_: Use multiple GPUs to train a single model.
    * _Model Parallelism_: Split the model into smaller parts and train each part separately.
    * Distributed Training: Train models across multiple machines using TensorFlow.

---

# 14. Chapter 8Model Training and Hyperparameter Tuning

---

## 14.1. Ingestion of Various File Types into Training

* **Data Types**: structured (e.g., databases), semi-structured (e.g., PDFs), unstructured (e.g., images, videos)
* **Data Sources**: batch, real-time streaming, IoT sensors
* **Data Volume**: small (MB) to petabyte scale

---

### 14.1.1. Collect

* **Google Cloud Data Ingestion Services**: 
  * Use Pub/Sub for real-time streaming and analytics
  * Utilize Datastream for change data capture and replication of databases to Google Cloud storage
  * Leverage BigQuery Data Transfer Service to load data from external sources into BigQuery

---

### 14.1.2. Process

* *_Data Preprocessing Tools_* 
    * **Handling missing values**
    * **Data normalization**
    * **Feature scaling**

---

#### 14.1.2.1. Cloud Dataflow

* **Cloud Dataflow**: serverless, fully managed service for processing streaming and batch data
    * Built on Apache Beam with exact-once streaming semantics for simplified business logic
    * Processing pipelines perform actions, allowing pipeline monitoring and data transformation/analysis
    * Aims to improve performance of MapReduce workloads and makes Hadoop workloads more maintainable

---

#### 14.1.2.2. Cloud Data Fusion

* **Cloud Data Fusion**: A user-friendly ETL (Extract, Transform, Load) tool that eliminates code implementation.

---

#### 14.1.2.3. Cloud Dataproc

* **Dataproc Overview**: Fully managed service for running Apache Spark, Flink, Presto, and 30+ open-source tools and frameworks.
    * **Key Features**:
        + Automates cluster creation and management
        + Integrates with other Google Cloud Platform services (BigQuery, Storage, Bigtable, etc.)
        + Supports batch processing, querying, streaming, and machine learning

* **Integration with Other Services**: 
    * _Cloud Data Ingestion_: Easily ETL terabytes of raw log data into BigQuery for business reporting
    * _Data Storage_: Uses HDFS for storage, with automatic installation of Cloud Storage connector

* **Connectors and APIs**

---

    * Supports 7+ connectors for various services (BigQuery, Cloud Storage, Pub/Sub Lite, etc.)
        + Enables seamless integration between Dataproc and other Google Cloud Platform services

---
*Cloud Dataproc*
Connector | Description
---|---
Cloud Storage connector | This is by default available on Dataproc and this connector helps run Apache Hadoop or Apache Spark jobs directly on data in Cloud Storage. Store your data in Cloud Storage and access it directly with Cloud Storage connector. You do not need to transfer it into HDFS first.
BigQuery connector | You can use BigQuery connector to enable programmatic read/write access to BigQuery. This is an ideal way to process data that is stored in BigQuery as command‐line access is not exposed. The BigQuery connector is a library that enables Spark and Hadoop applications to process data from BigQuery and write data to BigQuery. BigQuery Spark connector is used for Spark and BigQuery Hadoop connector is used for Hadoop.
BigQuery Spark connector | Apache Spark SQL connector for Google BigQuery. The connector supports reading Google BigQuery tables into Spark's DataFrames, and writing DataFrames back into BigQuery. This is done by using the Spark SQL Data Source API to communicate with BigQuery.
Cloud Bigtable with Dataproc | Bigtable is an excellent option for any Apache Spark or Hadoop uses that require Apache HBase. Bigtable supports the Apache HBase APIs so it is easy to use Bigtable with Dataproc.
Pub/Sub Lite Spark connector | The Pub/Sub Lite Spark connector supports Pub/Sub Lite as an input source to Apache Spark Structured Streaming in the default micro‐batch processing and experimental continuous processing modes.

<!-- _class: centered -->

---

#### 14.1.2.4. Cloud Composer

* *_Cloud Composer_*: A managed data workflow orchestration service that allows you to author, schedule, and monitor pipelines using Python DAGs.
    * Supports hybrid and multicloud architecture for on-premises, cloud, or mixed environments.
    * Provides end-to-end integration with Google Cloud products for pipeline orchestration.

---

#### 14.1.2.5. Cloud Dataprep

* **Cloud Dataprep**: UI-based ETL tool for visual exploration, cleaning, and preparing structured and unstructured data for analytics.

---

#### 14.1.2.6. Summary of Processing Tools

* *_GCP Processing Tools_*:
	+ Cloud Storage
	+ Cloud Datastore
	+ Cloud Functions
	+ Cloud Run
	+ BigQuery
	+ Cloud Pub/Sub

---

### 14.1.3. Store and Analyze

* **Data Storage for Machine Learning**
  * Google Cloud Storage: suitable for image, video, audio, and unstructured data
  * BigQuery: for tabular data and structured data with Vertex AI Feature Store
  * Vertex Data Labeling: for unstructured data
    * Store large files (100-10,000 MB) for improved read and write throughput
    * Use Avro files or TFRecord files in Google Cloud Storage

---

*Store and Analyze*
Type of Data | Product
---|---
Tabular data | BigQuery, BigQuery ML
Image, video, audio, and unstructured data | Google Cloud Storage
Unstructured data | Vertex Data Labeling
Structured data |  Vertex AI Feature Store
For AutoML image, video, text | Vertex AI Managed Datasets

<!-- _class: centered -->

---

## 14.2. Developing Models in Vertex AI Workbench by Using Common Frameworks

* **Vertex AI Workbench Overview**
  * A Jupyter Notebook-based development environment for data science workflows
  * Interacts with Vertex AI and other Google Cloud services from within a Jupyter Notebook instance

* **Managed Notebooks vs User-Managed Notebooks**
  * Key differences:
    * + **Automated shutdown**: Managed notebooks automatically shut down when idle, while user-managed notebooks require manual shutdown.
    * - No UI integration with Cloud Storage and BigQuery
    * + **Scheduled runs**: Managed notebooks can run on a recurring schedule without instance shutdown.
    * - Custom containers and Dataproc or Serverless Spark integration not supported

---

*Developing Models in Vertex AI Workbench by Using Common Frameworks*
Managed notebook | User‐managed notebook
---|---
**Automated shutdown for idle instances:** Choosing a managed notebook will shut down your Jupyter Notebooks when not in use. This feature helps save costs because the instances will shut down when not in use automatically. | **Automated shutdown for idle instances:** This feature is not supported out of the box. However, you can create a monitor to see when instances are idle using Cloud Monitoring and Cloud Functions and shut them down when not in use.
**UI integration with Cloud Storage and BigQuery:** From within JupyterLab's navigation menu on a managed notebooks instance, you can use the Cloud Storage and BigQuery integration to browse data and other files that you have access to and load data into your notebook. | **UI integration with Cloud Storage and BigQuery:** There is no UI integration. However, you can use the BigQuery connector to connect to BigQuery data using code or you can also use the BigQuery magic (`%%`) command to run BigQuery SQLl commands on a Jupyter Notebook.

<!-- _class: centered -->

---

### 14.2.1. Creating a Managed Notebook

### Creating Managed Notebooks in Vertex AI

To create a managed notebook:

* Enable all APIs in Vertex AI
* Click Workbench and New Notebook
* Create the notebook with default settings

A monthly billing estimate will appear. 

After creation, wait for the notebook to become available.

* You can upgrade the notebook instance by:
	+ Checking for upgrades from the notebook interface
	+ Upgrading manually to preserve data on the data disk

---

### 14.2.2. Exploring Managed JupyterLab Features

* **Getting Started**: After clicking Open JupyterLab, frameworks like Serverless Spark and PySpark are available for use.
* **Existing Resources**: Tutorials and notebooks in the `tutorials` folder help get started with building models.
* **Terminal Option**: A terminal is available to run terminal commands within the notebook.

---

### 14.2.3. Data Integration

* **Load Data from Cloud Storage**: Click the Browse GCS icon to load data from cloud storage folders.
    * Select the desired folder and file to upload.
    * Load the data into the managed notebook for analysis or processing.

---

### 14.2.4. BigQuery Integration

* Click on the BigQuery icon in the left sidebar to access your BigQuery tables
* Alternatively, use the Open SQL editor option to query tables directly from JupyterLab without leaving the interface

---

### 14.2.5. Ability to Scale the Compute Up or Down

* _Modify Jupyter Environment Hardware_ 
* Click "n1-standard-4" and select the hardware modifications
* Attach a GPU to the instance within the Jupyter environment

---

### 14.2.6. Git Integration for Team Collaboration

* To access project collaboration settings, click the left navigation branch icon
* Alternatively, run `git clone <your‐repository name>` in the terminal to clone your repository

---

### 14.2.7. Schedule or Execute a Notebook Code

* **Executing Code in Jupyter Notebook**
	+ Run code manually by clicking the triangle black arrow
	+ Execute as button to automate execution
* **Scheduling Execution**
	+ Click "Execute" and select Type option
	+ Schedule notebook for one-time run or at a scheduled time
* **Notebook Scheduling Features**
	+ Integration with Cloud Storage/BigQuery
	+ Scaling up/down hardware and git integration

---

### 14.2.8. Creating a User‐Managed Notebook

**Creating User-Managed Notebooks with TensorFlow**

* Choose a framework (e.g., Python 3, TensorFlow) during notebook creation
* Advanced networking options available for shared VPCs
* JupyterLab access and terminal integration provided with user-managed notebooks

---

## 14.3. Training a Model as a Job in Different Environments

* **Vertex AI Training**: Two types of training supported: 
  * AutoML: minimal technical effort model creation
  * Custom training: full control over application functionality and customization options

---

### 14.3.1. Training Workflow with Vertex AI

* **Vertex AI Training Options:**
  * _Training Pipelines_: Create AutoML or custom-trained models using pre-defined workflows
  * _Custom Jobs_: Specify settings for running custom training code, including worker pools and machine types
  * _Hyperparameter Tuning Jobs_: Optimize hyperparameters across a series of trials

* **Supported Frameworks:**
  * PyTorch
  * TensorFlow (with TensorFlow Hub for model deployment)

---

### 14.3.2. Training Dataset Options in Vertex AI

* **Training Data Storage**
  * Store data in Google Cloud Storage or BigQuery
  * Use managed notebooks for seamless integration with Cloud Storage and BigQuery
  * Alternatively, use a managed dataset for centralized management and automation of tasks

* **Training Jobs**
  * Configure custom jobs to access remote files via NFS shares
  * Choose between prebuilt containers and custom containers for training

---

### 14.3.3. Pre‐built Containers

* **Vertex AI Pre-built Container Training**
  * Organize code according to application structure (root folder with `setup.py` and `task.py`)
  * Upload Python source distribution to Cloud Storage bucket
  * Use command `gcloud ai custom-jobs create` to build Docker image, push to Container Registry, and create a custom job

* **Custom Job Command Parameters**
  * LOCATION: region where the container or Python package will be run
  * JOB_NAME: display name for the CustomJob
  * MACHINE_TYPE: type of machine for training
  * REPLICA_COUNT: number of worker replicas to use

---

### 14.3.4. Custom Containers

* **Custom Container Benefits**
  * Faster start-up time
  * Use preferred ML framework
  * Extended support for distributed training
  * Latest version of ML framework supported
* 
  * Create a custom container for Vertex AI training by creating a Dockerfile, building it, and pushing it to an Artifact Registry.
  * Follow these steps:
    * Set up files in required folder structure: `root`, `Dockerfile`, and `trainer` with `task.py`.
    * Build the Docker image using `docker build -f Dockerfile -t ${IMAGE_URI} ./`
    * Run local container with `docker run ${IMAGE_URI}`
    * Push image to Artifact Registry with `docker push ${IMAGE_URI}`

* **Custom Container Example**
  ```

---

  FROM image:tag
  WORKDIR /root

  RUN pip install pkg1 pkg2 pkg3
  RUN curl https://example-url/path-to-data/data-filename --output /root/data-filename
  COPY your-path-to/model.py /root/model.py
  COPY your-path-to/task.py /root/task.py
  ENTRYPOINT ["python", "task.py"]
  ```
* 
  * Use `gcloud ai custom-jobs create` to start training with a custom container.

---
### 14.3.5. Distributed Training

* **Distributed Training**: Run multiple machines (nodes) in a training cluster to allocate resources for a custom training job.
    * _Replica_: A running job on a given node called a replica, grouped into worker pools with the same configuration.
    * _Worker Pool_: A group of replicas that perform specific tasks in the distributed training process.
* **Vertex AI Reduction Server**: Use a container image to set up an all-reduce algorithm for distributed training, increasing throughput and reducing latency.
    * *Supports Tensor Fusion for small tensor batch processing with Horovod.*

---

    * Refer to [https://cloud.google.com/blog/topics/developers-practitioners/optimize-training-performance-reduction-server-vertex-ai](https://cloud.google.com/blog/topics/developers-practitioners/optimize-training-performance-reduction-server-vertex-ai)

---
*Distributed Training*
Position in workerPoolSpecs[] | Task Performed in Cluster
---|---
First (`workerPoolSpecs[0]`) | Primary, chief, scheduler, or “master.” Exactly ‐one replica is designated the _primary replica_. This task manages the others and reports status for the job as a whole.
Second (`workerPoolSpecs[1]`) | Secondary, replicas, workers.

<!-- _class: centered -->

---

## 14.4. Hyperparameter Tuning

* **Hyperparameters**: parameters of the algorithm not learned directly from data
* * Not set during training, but before learning begins *
* * Examples: learning rate, batch size, activation functions *

---

### 14.4.1. Why Hyperparameters Are Important

* **Hyperparameter Selection**: crucial for neural network success
    * _Influences model behavior and performance_
        + Low learning rate: misses important patterns
        + High learning rate: finds accidental coincidences easily
    * _Solved using algorithms_:
        * Grid Search: exhaustive search through manually specified hyperparameters
        * Random Search: random combinations of hyperparameters for optimal solution
        * Bayesian Optimization (Vertex AI default): uses past evaluations to select next set

---

### 14.4.2. Techniques to Speed Up Hyperparameter Optimization

* **Speeding Up Hyperparameter Optimization**
  * Use a simple validation set instead of cross-validation for large datasets (speedup ~k)
  * Parallelize training with hyperparameter optimization across multiple machines (speedup ~n)
  * Pre-compute and cache results to avoid redundant computations
  * Reduce number of hyperparameter values considered using grid search

* **Improving Performance**
  * Use random search algorithm for fewer trials

---

### 14.4.3. How Vertex AI Hyperparameter Tuning Works

* **Hyperparameter Tuning**: Hyperparameter tuning optimizes target variables by running multiple trials with specified hyperparameters.
    * **Configuring Hyperparameter Tuning**:
        + Create a `config.yaml` file with API fields for the `HyperparameterTuningJob`, including metric, parameter, and trial settings.
        + Define the name and goal of each metric, as well as the minimum and maximum values for tuning parameters.
    * **Creating a Custom Job**: Run the following shell command to create a custom job for hyperparameter tuning, specifying the region, display name, and configuration file.

---

### 14.4.4. Vertex AI Vizier

* **Vertex AI Vizier**: A black-box optimization service for tuning hyperparameters in complex ML models.
    * Used when objective function is unknown or too costly to evaluate.
        * Optimizes hyperparameters, model parameters, and works with any system that can be evaluated.
            * Examples include optimizing neural network parameters, user interface elements, computing resources, and recipe ingredient proportions.

---

#### 14.4.4.1. How Vertex AI Vizier Differs from Custom Training

* **Vertex AI Vizier**: Optimizes complex models with many parameters for ML and non-ML use cases
    * Uses Bayesian optimization by default to determine best hyperparameter settings
    * Supports custom training jobs and integration with other systems, including multicloud

---

## 14.5. Tracking Metrics During Training

* **Debugging Machine Learning Models**: Tracking and debugging machine learning model metrics using interactive shells, TensorFlow Profiler, and What‐If Tool.

---

### 14.5.1. Interactive Shell

* **Debugging with Interactive Shell**: Use an interactive shell to inspect your training container, run debugging utilities, and analyze GPU usage.
    * Enable an interactive shell by setting `enableWebAccess` to true in the Vertex AI console or programmatically.
    * Accessing interactive shell requires the job to be in the RUNNING state.
* **Monitoring Training Metrics**: View logs, metrics, and profiling information using various tools such as:
    * Cloud Monitoring
    * Table 8.6 (tools: py-spy, `nvidia-smi`, Perf)
    * GPU-enabled containers have preinstalled command-line tools for monitoring GPU usage

---

*Interactive Shell*
Visualize Python Execution with py‐spy | Retrieve Information about GPU Usage | Analyze Performance with Perf
---|---|---
py‐spy is a sampling profiler for Python programs. It lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way. | GPU‐enabled containers running on nodes with GPUs typically have several command‐line tools preinstalled that can help you monitor GPU usage. You can use `nvidia‐smi` to monitor GPU utilization of various processes or use `nvprof` to collect a variety of GPU profiling information. | Perf lets you analyze the performance of your training node. It's a way to do Linux profiling with performance counters.

<!-- _class: centered -->

---

### 14.5.2. TensorFlow Profiler

* **Vertex AI TensorBoard**: An enterprise-ready managed version of TensorBoard for monitoring and optimizing model training performance.
    * _Key features:_ Monitor resource consumption, identify bottlenecks, optimize model training speed and cost
        * Access the dashboard from Google Cloud console (custom jobs page or experiments page)
    * **TF Profiler:** Visualize profiling results for remote Vertex AI training jobs on demand

---

### 14.5.3. What‐If Tool

* **What-If Tool**: allows interactive inspection of AI Platform Prediction models through an interactive dashboard
    * _Integrated with TensorBoard, Jupyter Notebooks, Colab notebooks, and JupyterHub_
    * Preinstalled on Vertex AI Workbench user-managed notebooks and TensorFlow instances
    * Requires installation of witwidget library and configuration using WitConfigBuilder

---

## 14.6. Retraining/Redeployment Evaluation

* Machine learning models lose performance over time due to changes in user behavior and training data.
    * **Changes that affect model performance:**
        - _Data Drift_: Shifts in the distribution of input data
        - _Concept Drift_: Changes in the underlying relationship between input features and output labels

---

### 14.6.1. Data Drift

* **Data Drift**: A change in the statistical distribution of production data compared to baseline training data, potentially due to changes in input data.
    * _Causes_: Changes in feature attribution or data itself.
    * _Detection methods_: Examine feature distribution, correlation between features, and check data schema against baseline using a monitoring system.

---

### 14.6.2. Concept Drift

* **Concept Drift**: Changes in the statistical properties of a target variable over time.
* *Example:* Sentiments around topics change as people's opinions evolve.
* **Detection Method:** Monitor deployed models using Vertex AI Model Monitoring.

---

### 14.6.3. When Should a Model Be Retrained?

* **Periodic Training**: Retrain model at regular intervals (e.g., weekly, monthly, yearly) based on business use case needs.
* _Performance-based Trigger_: Automatically retrain model when performance falls below set threshold.
* *Data Changes Trigger*: Retrain model when data drift occurs, often due to changes in production.

---

*When Should a Model Be Retrained?*
Periodic training | You can choose an interval such as weekly, monthly, or yearly for retraining your model. It depends on how frequently your training data gets updated. Retraining your model based on an interval only makes sense if it aligns with your business use case. The selection of a random period for model retraining can give you a worse model than the previous model.
---|---
Performance‐based trigger |  If your model performance falls below your set threshold, which is the ground truth or baseline data, this automatically triggers the retraining pipeline. This approach assumes that you have implemented a sophisticated monitoring system in production.
Data changes trigger | If data drift happens, that should trigger a build for model retraining. Usually model performance changes in production, which can lead to data drift.
Retraining on demand | This is a manual and traditional way of retraining your models that employs traditional techniques.

<!-- _class: centered -->

---

## 14.7. Unit Testing for Model Training and Serving

* **Machine Learning Testing Challenges**: testing code, model, and data all control system behavior
* **Testing Strategies**:
    * Check output shape and alignment with labels
    * Verify output ranges align with expectations (e.g., class probabilities sum to 1)
    * Ensure single gradient step decreases loss

---

### 14.7.1. Testing for Updates in API Calls

* **Testing API Updates**: Write a unit test to generate random input data and perform one step of gradient descent.
    * **Alternative Approach**: Retraining the model is resource-intensive, but can be used for more comprehensive testing if needed.

---

### 14.7.2. Testing for Algorithmic Correctness

* **Check Model Correctness**: Train model for iterations and verify decreasing loss
* * Test without regularization *
* * Verify sub-computation correctness, e.g., one iteration per input element *

---

## 14.8. Summary

* **File Ingestion**
  * _Structured_: Pub/Sub and BigQuery Data Transfer Service for real-time data collection
  * _Unstructured_: Pub/Sub Lite for real-time data ingestion, Datastream for third-party data migration
  * _Semi-structured_: Datastream and Cloud Data Fusion for transformation and processing

* **Model Training**
  * Using Vertex AI training with frameworks like scikit-learn, TensorFlow, PyTorch, and XGBoost
  * Prebuilt and custom containers for model deployment

* **Testing and Hyperparameter Tuning**
  * Unit testing data and models in machine learning using Vertex AI
  * Hyperparameter tuning algorithms available in Google Cloud, including Vertex AI Vizier

---

## 14.9. Exam Essentials

* **File Ingestion**: Understand how to ingest various file types into training using Google Cloud data analytics platforms (e.g., Pub/Sub, BigQuery, Datastream).
    * Collect and store data in Google Cloud Storage
    * Transform and process data with services like Cloud Dataflow and Cloud Dataproc
* **Vertex AI Workbench**: Know how to use the Vertex AI Workbench environment using common frameworks.
    * Manage notebooks (user vs. managed)
    * Create and configure notebooks for ETL and machine learning tasks
* **Model Training and Serving**:
    * Unit test model data and algorithms
    * Track metrics during training with Interactive shell, Tensorflow Profiler, and What-If tool

---

* **Hyperparameter Tuning**: Understand hyperparameter tuning methods (grid search, random search, Bayesian search) and when to use them.
    * Set up hyperparameter tuning using custom jobs and Vertex AI Vizier
* **Retraining and Redeployment Evaluation**:
    * Handle underfitting and overfitting with regularization techniques (L1, L2)
    * Understand bias-variance trade-off while training neural networks

---
# 15. Chapter 9Model Explainability on Vertex AI

---

## 15.1. Model Explainability on Vertex AI

* _Model Explainability Matters_: The impact of model predictions on business outcomes increases, making it crucial for developers to explain model decisions.
* _Critical Decisions Demand Justification_: Models predicting sensitive outcomes (e.g., credit approval or medication dosage) require human explanations to address questions and concerns.
* _Transparency is Key_: Gaining visibility into the training process and developing human-explainable ML models are essential for building trust in AI-driven predictions.

---

### 15.1.1. Explainable AI

* **Explainability** refers to the ability to understand an ML system's internal mechanics.
    * It has two types: _global_ and _local_.
        + _Global explainability_ focuses on making the overall model transparent, while
            *_Local explainability_* explains individual predictions.

---

### 15.1.2. Interpretability and Explainability

* **Interpretability**: associating causes with effects
* **Explainability**: justifying model results through hidden parameters
    * _Deep neural networks lack inherent interpretability due to complex parameter interactions._

---

### 15.1.3. Feature Importance

* **Feature Importance**: explains how valuable each feature is relative to others using a score
    * Helps with **Variable Selection**, removing non-important features to save compute & infrastructure costs
        * Reduces training time and unnecessary data processing
    * Prevents **Data Leakage**, avoiding added target variables in training datasets

---

### 15.1.4. Vertex Explainable AI

* **Vertex Explainable AI**: integrates feature attributions into Vertex AI for understanding model outputs in classification and regression tasks.
    * Provides insights on how much each feature contributed to the predicted result.
    * Helps verify model behavior, detect bias, and improve model performance.

---

#### 15.1.4.1. Feature Attribution

**Vertex AI Feature Attribution**
 
* * *
 
The Vertex AI feature attribution functionality provides explainability for AutoML Tables and AutoML Images, and can be integrated into custom TensorFlow models using the Vertex AI Explainable SDK.
 
   * **Sampled Shapley:** assigns credit to each feature and considers different permutations of features, providing a sampling approximation of exact Shapley values. 
   * **Integrated gradients:** calculates the gradient to efficiently compute feature attributions, mostly used in deep neural networks with image use cases. 

---

   * **XRAI (eXplanation with Ranked Area Integrals):** assesses overlapping regions of the image to create a saliency map, highlighting relevant regions.

   | Method | Supported Data Types | Model Types |
   ---|---|---|
   | Sampled Shapley | Tabular | Nondifferentiable models |
   | Integrated gradients | Image and tabular data | Differentiable models |
   | XRAI | Image data | Models with image inputs |

   * **Differentiable vs. Nondifferentiable Models:** 
     + Differentiable models: can calculate derivatives, used for integrated gradients.
     + Nondifferentiable models: include operations like decoding and rounding tasks, used for sampled Shapley.

* * *
 

---

For in-depth information, refer to the _AI Explanations Whitepaper_.

---
*Feature Attribution*
Method | Supported Data Types | Model Types | Use Case | Vertex AI–Equivalent Model
---|---|---|---|---
Sampled Shapley | Tabular | Nondifferentiable models (explained after the table), such as ensembles of trees and neural networks. | Classification and regression on tabular data | Custom‐trained models (any prediction container)

<!-- _class: centered -->

---

#### 15.1.4.2. Vertex AI Example–Based Explanations

* **Example-based explanations**: enable active learning for misclassification analysis by selectively labeling data
    * Can be applied to images, text, and tables
    * Generates embeddings for diverse data types

---

### 15.1.5. Data Bias and Fairness

* **Bias in Machine Learning**: Biased data can lead to unfair treatment of individuals based on characteristics such as race, gender, or orientation.
* **Detecting Bias**: Use tools like Vertex AI's Explainable AI feature attributions technique, What-If Tool, and Language Interpretability Tool to detect bias in datasets.
    * *_Vertex AI_* provides interactive dashboards for inspecting models and detecting bias in tabular and structured datasets.

---

### 15.1.6. ML Solution Readiness

* **ML Solution Readiness**: Key concepts for successful implementation of machine learning solutions
    * **Responsible AI**:
        * Follows principles to ensure fairness and transparency in AI models
        * Tools include Explainable AI, Model Cards, and TensorFlow open source toolkit
    * **Model Governance**:
        * Ensures guidelines and processes for implementing company AI principles
        * Best practices include human review of model output, responsibility assignment matrices, and benchmarking

---

### 15.1.7. How to Set Up Explanations in the Vertex AI

* **Configuring Explanations**
  * For custom-trained models, configure explanations using Vertex AI (`https://cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based`)
  * AutoML tabular classification and regression do not require specific configuration
* **Explanation Types**
  * Online explanations: synchronous requests to Vertex AI API for feature attributions
  * Batch explanations: asynchronous requests with predictions and feature attributions
  * Local kernel explanations: use User-Managed Vertex AI Workbench notebook for offline explanations

---

## 15.2. Summary

* **Explainable AI**: Definition and difference between _explainability_ and _interpretability_, with a focus on model interpretability
* **Key concepts**:
	+ _Feature importance_: explaining models to identify key factors driving predictions
	+ Data bias and fairness, as well as ML solution readiness
* **Vertex AI platform**: Explanation of the platform's support for explainable AI techniques

---

## 15.3. Exam Essentials

* **Explainability on Vertex AI**: Understand the importance of explaining machine learning models, how global and local explanations differ, and feature attribution options like Sampled Shapley algorithm and integrated gradients.
* **Feature Importance**:
  * Helps determine bias and fairness in data
  * Supported by explainable AI SDK for TensorFlow prediction container
* **Explainable AI Support**: Available for Vertex AI AutoML tabular and image models using Explainable AI SDK

---

# 16. Chapter 10Scaling Models in Production

---

## 16.1. Scaling Prediction Service

* You deploy a trained TensorFlow model by saving it as a _**Saved Model**_.
* A saved model contains the trained parameters and computation, making it usable for sharing or deployment with other TensorFlow tools.
* Saved models are stored as a directory on disk, including the _**`saved_model.pb` file**_, which describes the function `tf.Graph`.

---

### 16.1.1. TensorFlow Serving

**TensorFlow Serving**

* _Host trained TensorFlow model as API endpoint_
* Supports REST and gRPC API endpoints
* Handles model serving and version management

**Setup Steps:**
* Install with Docker (recommended)
* Train and save model with TensorFlow
* Serve saved model using TensorFlow Serving

---

#### 16.1.1.1. Serving a Saved Model with TensorFlow Serving

* **REST API Request**: The TensorFlow ModelServer accepts POST requests to `/v1/models/${MODEL_NAME}/versions/${MODEL_VERSION}` with verbs classify|regress|predict.
    * **JSON Data Payload**: The `predict()` endpoint requires a JSON data payload with `signature_name`, `instances` as a list, and `content-type: application/json`.
* **Predict Response Format**: The SavedModel's SignatureDef defines the output tensors:
    * `class_ids`: DT_INT64 with shape (−1, 1)
    * `classes`: DT_STRING with shape (−1, 1)
    * `logits` and `probabilities`: DT_FLOAT with shape (−1, 3)
* **Example Response**: A JSON object with the prediction response:

---

    * `predictions`: a list of dictionaries containing class IDs, classes, logits, and probabilities.

---
## 16.2. Serving (Online, Batch, and Caching)

* _Serving Options in ML Systems_
	+ Batch Prediction (Offline Serving)
	+ Online Prediction
* **Recommended Strategies**
	+ Caching for improved performance
	+ Architecture considerations for optimal serving

---

### 16.2.1. Real‐Time Static and Dynamic Reference Features

* **Types of Input Features**: 
    * _Static Reference Features_: values do not change in real-time, usually updated in batches
    * _Dynamic Real-Time Features_: computed on the fly for event-stream processing pipelines
* **Use Cases**: estimating house prices, product recommendations; predicting engine failure with sensor data; recommending news articles based on user viewing history
* **Feature Storage and Retrieval_:
    * Static features: NoSQL databases optimized for singleton lookup operations (e.g. Firestore)
    * Dynamic features: low-latency read/write databases (e.g. Cloud Bigtable)

---

*Real‐Time Static and Dynamic Reference Features*
Static Reference Features | Dynamic Real‐Time Features
---|---
Their values do not change in real time. Instead, the values are usually updated in a batch. | Real‐time features are computed on the fly in an event‐stream processing pipeline.
These types of features are usually available in a data warehouse—for example, customer ID and movie ID. | For real‐time features, you need a list of aggregated values for a particular window (fixed, sliding, or session) in a certain period of time and not an overall aggregation of values within that period of time.
Use cases are estimating the price of a house based on the location of the house or recommending similar products given the attributes of the products that a customer is currently viewing. | Use cases can be predicting whether an engine will fail in the next hour given real‐time sensor data. Another use case can be in recommending the next news article to read based on the list of last N viewed articles by the user during the current session.
These types of static reference features are stored in a NoSQL database that _is_ optimized for singleton lookup operations, such as Firestore. BigQuery is not optimized for singleton reads, for example, a query like "Select 100 columns from several tables for a specific customer ID,” where the result is a single row with many columns. | You can use a Dataflow streaming pipeline to implement this use case for dynamic feature read. For dynamic feature creation, the pipeline captures and aggregates (sum, mean, and so on) the events in real time and stores them in a low‐latency read/write database. Cloud Bigtable is a good option for a low‐latency read/write database for feature values.
Static reference architecture (see Figure 10.2). | Dynamic reference architecture (see Figure 10.3).

<!-- _class: centered -->

---

### 16.2.2. Pre‐computing and Caching Prediction

* **Pre-computing predictions**: Store pre-computed predictions in a low-latency data store like Memorystore or Datastore for online serving.
* **Offline batch scoring job**: Run a batch prediction job on prepared data to produce predictions, which are stored by a unique key.
* **Client-side fetch**: Client fetches pre-computed predictions from the data store instead of calling the model for online prediction.

---

## 16.3. Google Cloud Serving Options

* **Deployment Options**: 
    * Online predictions
    * Batch predictions
        * For AutoML and custom models

---

### 16.3.1. Online Predictions

* To set up a real-time prediction endpoint, you can either train models using Vertex AI's AutoML or custom models, or import a pre-trained model from another location
    * Import requirements: match filenames to specific format (e.g. `saved_model.pb` for TensorFlow)
        * Custom container image and Cloud Build may be required

---

#### 16.3.1.1. Deploying the Model

* **Model Deployment**: Vertex AI provisions container resources and sets up autoscaling for specified models.
    * Can deploy multiple models per endpoint
    * Can deploy models to multiple endpoints
* Deployments: Using API or Google Cloud Console.

---

#### 16.3.1.2. Make Predictions

* To run data through an endpoint, it must be preprocessed to match the expected format defined in `task.py`.
    * This can be done by using the `predict` function of the `Endpoint` object.
    * The `predict` function returns confidence levels for each prediction.
* Preprocessing requirements vary depending on the container used:
    * For prebuilt containers, input data must be formatted as JSON.
    * For custom containers, input data must also be formatted as JSON, with an additional parameters field.

---

#### 16.3.1.3. A/B Testing of Different Versions of a Model

* **A/B Testing**: Compares two versions of a machine learning model to determine which one performs better.
    * _Tests a control version (A) against a variant version (B)_ 
    * _Measures success based on key metrics_
* **Deploying Models**: Gradually replaces one model with another by adding the new model to the same endpoint, serving a small percentage of traffic initially.
* **Vertex AI A/B Testing**: Limited capabilities for A/B testing, but using the model evaluation feature with Model Monitoring provides an alternative setup.

---

#### 16.3.1.4. Undeploy Endpoints

* **Unnecessary Endpoints**: Undeploy endpoints when not in use to avoid charges.
* **Best Practice**: Use `endpoint.undeploy()` to undeploy endpoints programmatically.
    * Example Python code: `endpoint.undeploy(deployed_model_id=endpoint.list_models()[0].id)`

---

#### 16.3.1.5. Send an Online Explanation Request

* **Online Explanations**: Send requests like prediction requests but return feature attributions along with predictions
    * Format: Same as online prediction requests
    * Response: Include feature attributions and predictions

---

### 16.3.2. Batch Predictions

**Batch Prediction**
Run model on input data in Google Cloud Storage
Format input data according to AutoML or custom model requirements
Options for input data:
* JSON Lines file stored in Cloud Storage
* TFRecord files stored in Cloud Storage with gzip compression
* CSV files with double quotation marks around strings
* BigQuery table as input

---

*Batch Predictions*
Input | Description
---|---
JSON Lines | Use a JSON Lines file to specify a list of input instances to make predictions about. Store the JSON Lines file in a Cloud Storage bucket.
TFRecord | You can optionally compress the TFRecord files with gzip. Store the TFRecord files in a Cloud Storage bucket. Vertex AI reads each instance in your TFRecord files as binary, then base64‐encodes the instance as a JSON object with a single key named b64.
CSV files | Specify one input instance per row in a CSV file. The first row must be a header row. You must enclose all strings in double quotation marks (").
File list | Create a text file where each row is the Cloud Storage URI to a file. Example: `gs://path/to/image/image1.jpg`.
BigQuery | Specify a BigQuery table as projectId.datasetId.tableId. Vertex AI transforms each row from the table to a JSON instance.

<!-- _class: centered -->

---

## 16.4. Hosting Third‐Party Pipelines (MLflow) on Google Cloud

* **Overview of MLflow**: An open-source platform for managing machine learning life cycles, compatible with various libraries and programming languages.
    * Provides four primary functions:
        + Tracking experiments
        + Packaging ML code
        + Managing models
        + Centralized model registry
* **Hosting on Google Cloud**: Leverages scalability and availability of Google Cloud Vertex AI platform, with access to high-performance compute resources.
    * Create PostgreSQL DB for metadata storage
    * Use Google Cloud Storage bucket for artifact storage
    * Install MLFlow using Compute Engine instance or Kubernetes

---

## 16.5. Testing for Target Performance

* Test model performance in production using real-time data
  * Monitor model age and performance throughout the ML pipeline
    * Ensure model weights and outputs are numerically stable (no NaN or null values)

---

## 16.6. Configuring Triggers and Pipeline Schedules

* **Triggering Training or Prediction Jobs on Vertex AI**
	+ Use Cloud Scheduler to set up a cron job schedule
	+ Utilize Vertex AI managed notebooks for Jupyter Notebook execution and scheduling
	+ Leverage Cloud Build, Cloud Run, and event-driven serverless Cloud Functions with Pub/Sub for custom deployment and triggering

---

*Configuring Triggers and Pipeline Schedules*
Option | Description
---|---
Vertex AI Pipelines | Vertex AI Pipelines helps you to automate, monitor, and govern your ML systems by orchestrating your ML workflow in a serverless manner and storing your workflow's artifacts using Vertex ML Metadata. By storing the artifacts of your ML workflow in Vertex ML Metadata, you can analyze the lineage of your workflow's artifact.
Cloud Composer | Cloud Composer is designed to orchestrate data‐driven workflows (particularly ETL/ELT). It's built on the Apache Airflow project, but Cloud Composer is fully managed. Cloud Composer supports your pipelines wherever they are, including on‐premises or across multiple cloud platforms. All logic in Cloud Composer, including tasks and scheduling, is expressed in Python as directed acyclic graph (DAG) definition files.

<!-- _class: centered -->

---

## 16.7. Summary

* **TF Serving Overview**: Covered details of TF Serving for scaling prediction service, including output analysis based on SignatureDef.
* **Architecture Options**: Discussed static and dynamic reference architectures, pre-computing, and caching while serving predictions.
* **Model Deployment and Monitoring**: Explored deploying models using online and batch mode with Vertex AI Prediction and Google Cloud options, as well as tools for model monitoring and performance testing.

---

## 16.8. Exam Essentials

* **TensorFlow Serving Overview**: Understand TensorFlow Serving, its deployment, and setup options, including Docker configurations.
    * Deploying Trained Models
    * Scaling Prediction Services (online, batch, caching)
        + Understanding Online vs Batch Caching
    * Google Cloud Serving Options
        + Real-time Endpoints using Vertex AI Prediction
    * Performance Testing with Vertex AI Model Monitoring
    * Trigger and Pipeline Configuration for Automated Deployment

---

# 17. Chapter 11Designing ML Training Pipelines

---

## 17.1. Orchestration Frameworks

* **ML Pipeline Orchestration**: An orchestrator manages the various steps of the machine learning (ML) pipeline, such as data cleaning, transformation, and model training.
* **Benefits**: 
  * Automates execution of each step based on predefined conditions
  * Useful in both development and production phases

---

### 17.1.1. Kubeflow Pipelines

**What is Kubeflow?**
Kubeflow is the ML toolkit for Kubernetes, allowing deployment and management of complex systems on various clouds and platforms.
### Key Components
* **Architecture**: Builds on top of Kubernetes for deploying and managing ML workflows.
* **Kubeflow Pipelines**: A platform for building, deploying, and managing multistep ML workflows using Docker containers.
    * _Runs in Kubernetes pods_
    * _Launches multiple containers for each step in the workflow_

---

### 17.1.2. Vertex AI Pipelines

* **Automated Infrastructure Setup**: Use Vertex AI Pipelines to run Kubeflow or TFX pipelines without setting up infrastructure, allowing for serverless deployment.
* 
  * _Lineage_ provides data tracking from source system to transformations and consumption by models, including metadata and artifact lineage for better understanding of pipeline performance.
* 
  * **Pipelining**:
    *   Automates monitoring and experimentation with interdependent parts of an ML workflow
    *   Portable, scalable, and container-based
    *   Components are defined by code, composed of inputs, outputs, and a container image

---

### 17.1.3. Apache Airflow

* **Apache Airflow Overview**
  * An open source workflow management platform for data engineering pipelines
  * Started at Airbnb in October 2014 as a solution to manage complex workflows
  * Represents workflows as directed acyclic graphs (DAGs) with tasks, dependencies, and data flows.

---

### 17.1.4. Cloud Composer

* **Cloud Composer**: Fully managed workflow orchestration service built on Apache Airflow
    * _Benefits:_ No installation or management overhead, easy creation of Airflow environments and use of native tools
    * **Use cases:** Orchestrate data-driven workflows (ETL/ELT), batch workloads with low latency

---

### 17.1.5. Comparison of Tools

* **Comparison Summary**
    * Kubeflow Pipelines: Orchestrates ML workflows in supported frameworks (TensorFlow, PyTorch, MXNet) with Kubernetes.
        * On-premises or cloud deployment
    * Vertex AI Pipelines: Managed serverless pipeline for Kubeflow Pipelines or TFX Pipelines, no infrastructure management required.
        * No failure handling out of the box
    * Cloud Composer: Managed ETL/ELT pipelines using Apache Airflow, Python-based implementation.

---

*Comparison of Tools*
****|  Kubeflow Pipelines | Vertex AI Pipelines | Cloud Composer
---|---|---|---
**Management and support for frameworks** | Kubeflow Pipelines is used to orchestrate ML workflows in any supported framework such as TensorFlow, PyTorch, or MXNet using Kubernetes.
It can be set up on‐premises or in any cloud. | Managed serverless pipeline to orchestrate either Kubeflow Pipelines or TFX Pipeline. No need to manage the infrastructure. | Managed way to orchestrate ETL/ELT pipelines using Apache Airflow. It's a Python‐based implementation.

<!-- _class: centered -->

---

## 17.2. Identification of Components, Parameters, Triggers, and Compute Needs

* Triggering an MLOps Pipeline: Automate retraining of models with new data, on demand, schedule, or availability.
* **Triggers for Retraining**: New data, model performance degradation, statistical property changes, or other conditions.
* **Deployment**: No new pipelines are deployed, only prediction services or newly trained models are served.

---

### 17.2.1. Schedule the Workflows with Kubeflow Pipelines

* **CI/CD with Kubeflow Pipelines**
  * Use Python SDK (`kfp.Client`) for programmatically operating pipelines
  * Invocation can be done through:
    * Cloud Scheduler (on schedule)
    * Pub/Sub and Cloud Functions (response to event)
    * Cloud Composer or Data Fusion (as part of a bigger workflow)

* **Cloud Build pipeline configuration**
  * Can skip triggers when only documentation files are edited or experimentation notebooks are modified

---

### 17.2.2. Schedule Vertex AI Pipelines

* **Scheduling with Cloud Scheduler:**
  * Schedule pipeline execution using an HTTP trigger and a Cloud Scheduler job
* **Scheduling with Cloud Pub/Sub:**
  * Trigger pipeline run with an event-driven Cloud Function and a Pub/Sub topic subscription

---

## 17.3. System Design with Kubeflow/TFX

* **System Design Overview**
  * Kubeflow DSL
  * TFX

---

### 17.3.1. System Design with Kubeflow DSL

* **Kubeflow Pipelines Overview**: 
    * Uses Argo Workflows by default
    * Exposes a Python DSL for authoring pipelines
    
* **Creating a Pipeline**:
    * Create container (simple function or Docker)
    * Define operation with container, args, data mounts, and variables
    * Sequence operations (parallel and dependencies)

---

#### 17.3.1.1. Kubeflow Pipelines Components

* To invoke a component in the pipeline, create a _component op_ using one of three methods:
    * Implementing a lightweight Python component
    * Creating a reusable component
    * Using predefined Google Cloud components
* These component ops are automatically created from specifications through `ComponentStore.load_components`.

---

### 17.3.2. System Design with TFX

* **TFX Overview**: Google's production-scale machine learning platform based on TensorFlow, providing configuration framework and shared libraries for ML workflows.
    * Orchestrate ML workflows on platforms like Apache Airflow, Apache Beam, and Kubeflow Pipelines
    * Provides components and libraries for building and managing ML pipelines
* **TFX Pipeline Components**: A sequence of components implementing an ML pipeline for scalable, high-performance tasks
    * ExampleGen: ingests input dataset
    * StatisticsGen: calculates statistics
    * SchemaGen: creates data schema
    * ... (Trainer, Tuner, Evaluator, Model Validator, Pusher, Model Server)

---

* **Orchestrating TFX Pipelines**: Can be orchestrated using Apache Airflow or Kubeflow, with various methods available on GCP.

---
## 17.4. Hybrid or Multicloud Strategies

* _Multicloud_: combining at least two public cloud providers (e.g., GCP, AWS, Azure) for hybrid operations.
    * **Integrations**: 
        * GCP AI APIs with AWS Lambda
        * BigQuery Omni with S3 and Azure Blob Storage
    * Example: training custom ML models on Vertex AI using data from BigQuery Omni-accessible buckets
* _Hybrid cloud_: combining private and public cloud environments.
    * **Anthos features**:
        * Querying data without managing infrastructure
        * Speech-to-Text On-Prem
        * Running GKE, Kubeflow Pipelines, and Cloud Run on-premises

---

## 17.5. Summary

* **Orchestration Tools**: 
    * Kubeflow, Vertex AI Pipelines, Apache Airflow, and Cloud Composer are used for ML pipeline automation.
        + Vertex AI Pipelines is a managed serverless way to run Kubeflow and TFX workflows.
* **Scheduling**: 
    * Kubeflow uses Cloud Build for automated deployment triggers, while Vertex AI Pipelines uses Cloud Function event triggers.
* **System Design**:
    * Kubeflow Pipelines use a component-based approach with a UI and TensorBoard visualization.

---

## 17.6. Exam Essentials

* **Orchestration Frameworks**: 4 main frameworks for automating ML workflows: 
  * _Kubeflow Pipelines_: uses Cloud Build, supports TFX and Kubeflow components
  * _Vertex AI Pipelines_: runs on GCP, supports Kubeflow and TFX components
  * _Apache Airflow_: standalone workflow management platform
  * _Cloud Composer_: integrates with Google Cloud services

* **Components and Triggers**: 
  * Parameters: use environment variables or command-line arguments
  * Triggers: schedule using Cloud Function event triggers (Vertex AI) or Cloud Build (Kubeflow)
  * Compute needs: vary depending on the framework, e.g. Kubeflow uses Cloud Run

---

# 18. Chapter 12Model Monitoring, Tracking, and Auditing Metadata

---

## 18.1. Model Monitoring

* **Model Validation Challenges**: Deploying a model is just the beginning; understanding its performance on real-time data, adapting to changes, and detecting drift are crucial.
    * * *
        + _Drift_: Model becomes less accurate over time due to changing environments and input patterns
            - **Concept Drift**: Change in the underlying concept or pattern in the data
                - *_Data Drift_*: Change in the distribution of the data

---

### 18.1.1. Concept Drift

* _Concept Drift_: Relationship between input variables and predicted variables that changes over time due to non-static assumptions of a machine learning model
* Example: Spam filtering where spammers modify emails to bypass detection filters, forcing the system to adapt
    * **Adversarial Dynamics**: Humans and machines (e.g., spam filter) interact in an adversarial manner, causing the concept drift

---

### 18.1.2. Data Drift

* **Data Drift**: Change in input data fed to the machine learning model compared to original training data.
* *Causes*: Changes in statistical distribution, input schema at source (e.g., new product labels), or changes in column meaning over time.
* _Model Monitoring_: Continuously evaluate the model with same metrics used during training phase to detect and act on model deterioration due to data drift.

---

## 18.2. Model Monitoring on Vertex AI

* Vertex AI offers model monitoring features to detect skew and drift in input feature distributions.
	+ _Training-serving skew_ detects differences between training and production data inputs.
	+ Prediction drift detects changes in input statistical distributions over time.
* Skew and drift detection are available for:
	+ Categorical features (e.g., color, country, zip code)
	+ Numerical values (e.g., price, speed, distance)

---

### 18.2.1. Drift and Skew Calculation

**Baseline Distribution Method**

* **Categorical Features:** Count/percentage of instances for each possible value
* **Numerical Features:** Count/percentage of values in equal-sized buckets
* **Comparison Method:**
	+ _Skew Detection:_ L-infinity distance between baseline and latest distribution
	+ _Drift Detection:_ Jensen-Shannon divergence between baseline and latest distribution

---

#### 18.2.1.1. Practical Considerations of Enabling Monitoring

* To monitor data cost-effectively, consider the following settings:
  * _Prediction request sampling rate_: sample production inputs to reduce costs.
  * _Monitoring frequency_: set the rate of monitoring logged inputs for skew or drift.
  * _Alerting thresholds_: configure threshold values for features to detect statistical distance from baseline distributions.

---

### 18.2.2. Input Schemas

**Input Schema**
* **Required for custom-trained models**: Provide an input schema when configuring model monitoring
* * Input schema is automatically parsed for AutoML models.

---

#### 18.2.2.1. Automatic Schema Parsing

* Model monitoring can automatically parse input schema when enabled, detecting skew or drift
* It analyzes the first 1,000 requests to detect schema, efficacy is best with key/value pairs format
* Example input format: `{"key": value}` where `key` is feature name and `value` follows colon

---

#### 18.2.2.2. Custom Schema

* **Vertex AI Schema** 
    * _type_: object, array, or string
    * _Properties_: specifies data type for each feature (string, number, etc.)
    * Example: `make`, `model`, `year` are strings, `known_defects` is an array of strings

---

## 18.3. Logging Strategy

* **Model Logging in Prediction**: Logging requests can be useful for monitoring trends in input features and updating training data.
* **Vertex AI Support**: Prediction logs are enabled for AutoML tabular, image, and custom-trained models during deployment or endpoint creation.
* *_Additional use cases include auditing requirements_*

---

### 18.3.1. Types of Prediction Logs

* **Types of Logs**: 
  * _Event Logs_: records actions taken by users
  * _Feature Logs_: contains feature values used in predictions
  * _Prediction Logs_: holds prediction results

---

#### 18.3.1.1. Container Logging

* Logs _stdout_ and _stderr_ from prediction nodes to Cloud Logging for debugging purposes
* Facilitates understanding of the larger logging platform on GCP for better model diagnostics

---

#### 18.3.1.2. Access Logging

* *Access Logging: Enabling logging of timestamp and latency for each request to Cloud Logging*
    * Enabled by default on v1 service endpoints
    * Can be enabled at deployment time for custom models*

---

#### 18.3.1.3. Request‐Response Logging

* Logs online prediction requests and responses to a BigQuery table for data augmentation
* Can be enabled at creation or updated later to add more data to training or testing datasets

---

### 18.3.2. Log Settings

* Logging settings can be updated when creating or redeploying the endpoint, but changes to existing deployments require undeploying and redeploying with new settings.
* Consider logging costs for high QPS models; large numbers of logs increase costs.
    * Example `gcloud` command to configure logging:
        `--disable-container-logging --enable-access-logging`

---

### 18.3.3. Model Monitoring and Logging

* **Interaction Between Model Monitoring and Request-Response Logging**
    * Cannot both be enabled at the same time
    * Enabling one after the other will render the other unusable in certain situations

---

## 18.4. Model and Dataset Lineage

* **Metadata**: recording experiment parameters, artifacts, and metrics for analysis and tracking
    * **Purpose**:
        * Detect model degradation after deployment
        * Compare hyperparameter effectiveness
        * Track lineage of ML artifacts (datasets, models)
    * **Use cases**:
        * Rerun ML workflows with same parameters
        * Track downstream usage for audit purposes

---

### 18.4.1. Vertex ML Metadata

* _Vertex ML Metadata_ uses Google's open source ML Metadata (MLMD) library for analyzing, debugging, and auditing purposes.
    * **Key Concepts:**
        * _Metadata Store_: Top-level container for metadata resources, regional and project-scoped
        * _Metadata Resources_: Graph-like data model representing relationships between resources, including:
            * _Artifacts_
            * _Context_
            * _Execution_
            * _Events_

---

#### 18.4.1.1. Manage ML Metadataschemas

* **Metadata Schema**: The metadata resource follows a predefined schema called `MetaDataSchema`, with system schemas under the namespace `system`.
    * _Example:_
        ```
title: system.**Model**
type: **object**
properties:
 framework:
  type: **string**
  description: "The ML framework used, eg: 'TensorFlow' or 'PyTorch'."
 framework_version:
  type: **string**
  description: "The version used, eg: '1.16' or '2.5'"
 payload_format:
  type: **string**
  description: "The format of the model stored: eg: 'SavedModel' or 'pkl'"
```
* **Create Artifact**: `create_artifact_sample` function creates a new artifact in Vertex ML Metadata using Python.

---

    * Parameters: project, location, uri, artifact_id, display_name, schema_version, description, metadata
    * Example:
        ```
def create_artifact_sample(
  project: str,
  location: str,
  uri: Optional[str] = None,
  artifact_id: Optional[str] = None,
  display_name: Optional[str] = None,
  schema_version: Optional[str] = None,
  description: Optional[str] = None,
  metadata: Optional[Dict] = None,
):
    system_artifact_schema = artifact_schema.Artifact(
      uri=uri,
      artifact_id=artifact_id,
      display_name=display_name,
      schema_version=schema_version,
      description=description,
      metadata=metadata,
    )

---

    return system_artifact_schema.create(project=project, location=location,)
```
* **Lookup Artifact**: `list_artifact_sample` function lists artifacts in Vertex ML Metadata using Python.
    * Parameters: project, location, display_name_filter, create_date_filter
    * Example:
        ```
def list_artifact_sample(
  project: str,
  location: str,
  display_name_fitler: Optional[str] = "display_name=\"my_model_*\"",
  create_date_filter:  Optional[str] = "create_time>\"2022-06-11\"",
):
    aiplatform.init(project=project, location=location)
    combined_filters = f"{display_name_fitler} AND {create_date_filter}"
    return aiplatform.Artifact.list(filter=combined_filters)

---
#### 18.4.1.2. Vertex AI Pipelines

* **Lineage Tracking**: Model metadata and artifacts are automatically stored in the metadata store for tracking pipeline execution history.
* **Artifact Generation**: Pipelines generate a series of artifacts, including model evaluation metrics and pipeline execution metadata.
* **Visual Lineage**: A visual representation shows pipeline lineage, allowing users to understand model data origin, deployment version, and sorting by schema and date.

---

## 18.5. Vertex AI Experiments

* **Vertex AI Experiments**: Automates trial management for machine learning model development
    * Tracks experiment steps (preprocessing, training, etc.)
    * Monitors input variables (algorithms, hyperparameters, etc.)
    * Evaluates output results (models, metrics, checkpoints, etc.)

---

## 18.6. Vertex AI Debugging

* **Debugging GPU Issues**: Vertex AI allows direct connection to the container for efficient debugging
    * Use interactive Bash shell within the container, set `enableWebAccess` to true
        * Ensure service account has necessary permissions
            + Run `py-spy` with Python execution profiling
                - Install using pip3 (`pip3 install py-spy`)

---

## 18.7. Summary

* **Model Maintenance**: Monitoring deployed models for performance degradation
* **Logging Strategies**: Various logging options in Vertex AI
  * _Tracking Models_
  * Tracking model lineage using Vertex ML Metadata and Vertex AI Experiments

---

## 18.8. Exam Essentials

* **Model Monitoring**: Continuously monitor model performance after deployment to detect changes in input, specifically:
	+ Data drift
	+ Concept drift
* **Logging Strategies**: Log deployment performance and create new training data to inform model updates.
	+ Learn logging techniques for Vertex AI
* **Vertex ML Metadata**: Manage model lineage and artifacts using a managed solution on GCP.

---

# 19. Chapter 13Maintaining ML Solutions

---

## 19.1. MLOps Maturity

* **Machine Learning Journey**: Organizations progress from manual model training to full automation through pipelines.
* **MLOps Phases**:
    * *_Level 0: Manual Phase_* - Data extraction and analysis
    * *_Level 1: Strategic Automation Phase_* - Model training, evaluation, and validation
    * *_Level 2: CI/CD Automation Phase_* - Deployment, monitoring, and scaling

---

### 19.1.1. MLOps Level 0: Manual/Tactical Phase

* **Exploration Phase**: Building proof of concepts, testing AI/ML use cases, and validating business improvements through model experimentation and validation.
    * Typically involves a team or individual training models
    * Models are stored and shared using a model registry before deployment

---

#### 19.1.1.1. Key Features of Level 0

* _Tactical Phase Overview_
  * Manual task execution with no automation
  * Limited scalability and lack of regularity in retraining
  * No consideration for continuous integration or deployment
* 
* _Key Issues_
  * Division between ML and MLOps teams leads to detection of training-serving skew issues
  * Lack of model monitoring and degradation handling

---

#### 19.1.1.2. Challenges

* **Model Degradation**: Well-trained models often underperform in real-life scenarios due to differences between training data and real data.
    * _Solution requires constant monitoring and updating of predictions_
    * _Frequent retraining and experimenting with new algorithms/algorithms are necessary to leverage technological improvements_

---

### 19.1.2. MLOps Level 1: Strategic Automation Phase

* **MLOps Level 1 Phase**: Organizations use pipelines to automate model training, continuous delivery, and validation.
    * Requirements: Automated data and model validation, pipeline triggers, Feature Store, metadata management
    * Key Features:
        - Orchestration of ML development environment
        - Centralized source code repository for data pipelines

---

#### 19.1.2.1. Key Features of MLOps Level 1

* **Level 1 Phase**: Key Features
    * Automated experimentation with orchestrated steps increasing iteration speed
    * Continuous training on new data in production environment
    * Unified MLOps practices through shared code between experimentation and production
        * Modular components for reusability, composability, and sharing
    * Automated continuous delivery of new models to prediction service

---

#### 19.1.2.2. Challenges

* *Manual pipeline deployment and trigger by data changes is inefficient for new model deployments.*
    * **Limitation:** No support for deploying models based on new ML ideas without manual intervention.
    * *_Requires automation:_* CI/CD setup for automated build, test, and deploy of ML pipelines.

---

### 19.1.3. MLOps Level 2: CI/CD Automation, Transformational Phase

* **Transformational Phase**: Organizations with mature AI practices use ML experts in product teams and across business units.
* **Dataset Access**: Datasets are shared across silos for ML projects between product groups.
* **CI/CD Automation**: Entire pipeline is automated through CI/CD, including model updates.

---

#### 19.1.3.1. Key Features of Level 2

* **Level 2 Adoption**: Moving to level 2 involves adopting the CI/CD model for ML pipelines, automating retraining, testing, and deployment.
    * *_Pipeline_*: Development, automation, testing, and deployment of ML models with shared source code and continuous delivery.
    * *_Testing_*: Integration testing, validation, and error checking for each pipeline component.
    * *_Delivery_*: Verifying model compatibility, load testing, and deployment strategies (blue/green, canary, shadow).

---

## 19.2. Retraining and Versioning Models

### Model Retraining Frequency
* **Key Considerations**: 
    * Monitor performance over time to determine degradation.
    * Collect real data for evaluation and new training datasets.
    * Determine retraining frequency based on model performance.
* **Retraining Options**:
  * Regularly scheduled intervals (e.g., weekly, monthly)
  * Adaptive threshold-based approach
  * Data-driven decision-making

---

### 19.2.1. Triggers for Retraining

* **Model Retraining Policy**: 
    * Trigger retraining based on predetermined policies (e.g. absolute threshold or rate of degradation)
    * Considerations: training costs, training time, delayed training, scheduled training
        * Minimize frequent retreining to avoid unnecessary costs and degradation
        * Balance trade-off between model performance and consistency
        * Scheduled training can provide predictable costs and performance

---

### 19.2.2. Versioning Models

* **Model Versioning**: allows deploying multiple versions of a model, with version IDs for selection
    * **Benefits**: solves backward compatibility issues and enables choosing between old and new models
        * **Monitoring**: enables comparison of different versions through REST endpoints
    * **Alternative Approach**: deploying new models instead of updating existing ones for complex behaviors

---

## 19.3. Feature Store

* Feature engineering is a crucial step in building good ML models but can be time-consuming.
    * _Lack of sharing and reuse leads to duplicated effort_ 
        * Non-reusable features create ad hoc pipelines, reducing data governance
            * Cross-collaboration suffers due to separate feature development

---

### 19.3.1. Solution

* **Feature Stores**: Central location for feature metadata and storage, enabling versioning, documentation, and access control.
    * Allows fast processing of large feature sets and low-latency access for real-time predictions and training.
        + Key benefits: efficient data management, improved prediction performance.

---

### 19.3.2. Data Model

* **Vertex AI Feature Store data model**: stores data in a time-series model to manage changes over time.
* The data is arranged in a hierarchy with:
  * **Featurestore** → **EntityType** → **Feature**
    + Entities must be unique and of type String
    + Features can have feature values (e.g. teams)

---

*Data Model*
Row | player_id | Team | Batting_avg | Age
---|---|---|---|---
1 | player_1 | RedSox | 0.289 | 29
2 | player_2 | Giants | 0.301 | 32
3 | player_3 | Yankees | 0.241 | 35

<!-- _class: centered -->

---

### 19.3.3. Ingestion and Serving

* **Ingestion**: Vertex AI Feature Store supports both batch and streaming ingestion, with features often stored in BigQuery.
    * Batch ingestion is used during model training, while online ingestion is used for online inference.
* **Retrieval**: Retrieving data from the Feature Store can be done through either batch or online methods.

---

## 19.4. Vertex AI Permissions Model

* **Managing Access**: Use Identity and Access Management (IAM) to control access to resources like datasets, models, and perform operations like training, deploying, and monitoring.
    * _Least Privilege_: Restrict users and applications to only necessary actions.
    * Manage service accounts and keys to ensure security assets are up-to-date.
* **GCP IAM**: Review GCP's IAM fundamentals before using Vertex AI permissions model.
    * Familiarity with GCP's IAM model, especially in Compute Engine or Google Cloud Storage, is helpful.
* **IAM Best Practices**: Follow best practices for using IAM security, including:
    * _Auditing_: Enable audit logs and use cloud logging roles.

---

### 19.4.1. Custom Service Account

* Using a Vertex AI training job's default service account can provide unnecessary access.
* Custom service accounts with limited permissions should be used instead.
* This helps minimize potential security risks.

---

### 19.4.2. Access Transparency in Vertex AI

* **Logging Requirements**: Verify access with logs for compliance and legal purposes.
    * Logs include:
        *_Cloud Audit logs_*: users from your organization
        *_Access Transparency logs_*: Google personnel actions

---

## 19.5. Common Training and Serving Errors

* **Common Errors in TensorFlow**: Understanding common errors is crucial for effective debugging
    * _Error Types_: Knowledge of error types is essential to address problems effectively
    * _Framework Dependency_: Errors can vary depending on the framework used, but TensorFlow will be the focus

---

### 19.5.1. Training Time Errors

* **Common Training Phase Errors**:
    * _Insufficient input transformation or encoding_
    * Mismatched tensor shapes
    * Out-of-memory errors due to large instance sizes

---

### 19.5.2. Serving Time Errors

* **Serving Time Errors**: Occur during deployment, with different error types than training-time errors
* *Causes:* 
    + Input data not transformed or encoded
    + Signature mismatch has occurred
* Refer to TensorFlow API documentation for full list of errors: *www.tensorflow.org/api_docs/python/tf/errors*

---

### 19.5.3. TensorFlow Data Validation

* **TensorFlow Data Validation**: tool to analyze training and serving data, detecting errors by:
  * Computing statistics
  * Inferring schema
  * Detecting anomalies

---

### 19.5.4. Vertex AI Debugging Shell

* Vertex AI provides an interactive shell for debugging training, allowing inspection of containers and validation of configurations
* The interactive shell supports tracing and profiling tools, GPU utilization analysis, and IAM permission validation
* *Full documentation is available at [https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell)*

---

## 19.6. Summary

* **Maintenance of ML Applications**: automation of training, deployment, and monitoring through CI/CD principles
* **Retraining Policy Balance**: balancing model quality with training cost
* **Feature Store Solution**: solving inefficiencies by sharing features between departments using open source software or Vertex AI Feature Store

---

## 19.7. Exam Essentials

* MLOps maturity levels include:
  * Experimental phase: No automation
  * Strategic phase: Basic automation
  * Fully mature CI/CD-inspired architecture: Automated pipelines and version control
* Key concepts in MLOps include:
  * Model versioning and retraining triggers, which determine when to update models based on degradation or time
  * Feature store usage, where shared features are managed across teams

---

# 20. Chapter 14BigQuery ML

---

## 20.1. BigQuery – Data Access

* **Accessing Data in BigQuery**: three methods are available: 
    * Web console with SQL queries
    * Jupyter Notebook using `%%bigquery` magic command
    * Python API to run queries and capture results in Pandas DataFrame 

    [Figure 14.1] (accessing data through web console)
    [Figure 14.2] (accessing data through Jupyter Notebook)

---

## 20.2. BigQuery ML Algorithms

**BigQuery ML**
* A serverless method for training and predicting machine learning models using standard SQL queries
* No need to write Python code, fully integrated with BigQuery

---

### 20.2.1. Model Training

* **Creating a Model**: Use `CREATE MODEL` with options to specify model type and input label columns.
* **Model Options**:
	+ `model_type`: specifies model category (e.g. regression, classification)
	+ `input_label_cols`: identifies target column in data
* **Available Models**: see Table 14.1 for list of models available on BigQuery ML

---

*Model Training*
Category | Model Type | Description
---|---|---
Regression | LINEAR_REG, BOOSTED_TREE_REGRESSOR, DNN_REGRESSOR, AUTOML_REGRESSION | To predict a real value
Classification | LOGISTIC_REG, BOOSTED_TREE_CLASSIFIER, DNN_CLASSIFIER, DNN_LINEAR_COMBINED_CLASSIFIER, AUTOML_CLASSIFIER | To predict either a binary label or multiple labels
Deep and wide models | DNN_LINEAR_COMBINED_REGRESSOR,
DNN_LINEAR_COMBINED_CLASSIFIER | Deep and wide models used for recommendation systems and personalization
Clustering | KMEANS | Unsupervised clustering models
Collaborative filtering | MATRIX_FACTORIZATION | For recommendations
Dimensionality reduction | PCA, AUTOENCODER | Unsupervised preprocessing step
Time‐series forecasting | ARIMA_PLUS | Forecasting
General | TENSORFLOW | Generic TensorFlow model

<!-- _class: centered -->

---

### 20.2.2. Model Evaluation

* To evaluate a machine learning model, use `ML.EVALUATE` with a separate, unseen dataset.
    * This ensures the model's performance is not biased by training data.
* Use `ML.EVALUATE` with `( SELECT * FROM test.creditcardtable)` to evaluate on a specific dataset.

---

### 20.2.3. Prediction

* The `ML.PREDICT` function predicts values from a model in BigQuery ML.
    * It takes an entire table or a single row as input and returns the predicted values along with probabilities for each label.
        * New columns `_predicted_<label_column_name>_` and `_predicted_<label_column_name>_probs_` are added to the output table.

---

## 20.3. Explainability in BigQuery ML

* **Explainability in BigQuery**: Get global feature importance values at the model level or get explanations for each prediction using SQL functions.
  * Enables explainability during training with `enable_global_explain=TRUE`.
  * Returns a table with input features and their floating-point number representing importance.

* **Computational Cost**: Adding explainability increases computational cost, especially with methods like Shapley that have exponential complexity with the number of features.

* **Model Types and Explainability Methods**:
    * Linear and logistic regression: Shapley values and standard errors, p‐values
    * Boosted Trees: Tree SHAP, Gini‐based feature importance

---

    * Deep Neural Network and Wide‐and‐Deep: Integrated gradients
    * Arima_PLUS: Time‐series decomposition

---
*Explainability in BigQuery ML*
Model Type | Explainability Method | Description
---|---|---
Linear and logistic regression | Shapley values and standard errors, p‐values | This is the average of all the marginal contributions to all possible coalitions.
Boosted Trees | Tree SHAP, Gini‐based feature importance | Shapley values optimized for decision tree–based models.
Deep Neural Network and Wide‐and‐Deep | Integrated gradients | A gradients‐based method to efficiently compute feature attributions with same axiomatic properties as Shapley.
Arima_PLUS | Time‐series decomposition | Decompose into multiple components if present in the time series.

<!-- _class: centered -->

---

## 20.4. BigQuery ML vs. Vertex AI Tables

**BigQuery vs Vertex AI**
* **Overview**: 
  * _BigQuery_: Serverless data warehouse for SQL experts, ideal for complex queries and automation.
  * _Vertex AI_: Cloud-based machine learning platform for data scientists, focusing on fine-grained control and custom operations.

**Choosing Between BigQuery and Vertex AI**
* For analysts or business users: **BigQuery**
* For machine learning engineers: **Vertex AI**

---

## 20.5. Interoperability with Vertex AI

* **Interoperability**: Vertex AI and BigQuery ML integrate at multiple points in the machine learning pipeline
    * **Seamless Integration**: Six key integration points enable easy collaboration between the two products
        * _Shared Data Sources_
        * _Automated Model Deployment_
        * _Model Serving and Inference_
        * _Data Preprocessing and Processing_
        * _Training and Hyperparameter Tuning_
        * _Model Monitoring and Maintenance_

---

### 20.5.1. Access BigQuery Public Dataset

* **BigQuery Public Datasets**: Over 200 publicly available datasets stored by Google and accessible through GCP projects.
* **Access and Cost**: Access datasets for free, pay only for queries run on these datasets.
* *_Complementary Use Cases_*: Utilize datasets with Vertex AI to train ML models or augment existing data.

---

### 20.5.2. Import BigQuery Data into Vertex AI

* You can create a dataset in Vertex AI using a BigQuery URL
* Provide source URL as `bq://project.dataset.table_name` to start creating a dataset
* Integration allows seamless connection to data in BigQuery without exporting and importing data

---

### 20.5.3. Access BigQuery Data from Vertex AI Workbench Notebooks

* Using managed notebook instances in Vertex AI Workbench allows direct access to BigQuery datasets
    * Enables browsing datasets, running SQL queries, and downloading into Pandas DataFrames
    * Simplifies data analysis and manipulation for Jupyter Notebook users

---

### 20.5.4. Analyze Test Prediction Data in BigQuery

* **Model Prediction Export**: Train a model with a train and test dataset, then export predicted results from test dataset to BigQuery for analysis.
* *This allows for post-training testing and prediction evaluation.* 
* *Enables further analysis of test predictions using SQL methods in BigQuery.*

---

### 20.5.5. Export Vertex AI Batch Prediction Results

* **Direct Input/Output with BigQuery**: Batch predictions in Vertex AI can directly point to a BigQuery table for input and store predictions back in BigQuery.
* _Benefits_: Standardized MLOps using Vertex AI with data in BigQuery.
* *Example use case*: Storing predictions alongside original data in a unified repository.

---

### 20.5.6. Export BigQuery Models into Vertex AI

* **BigQuery Model Export**: Export model from BigQuery to GCS for flexible deployment.
    * Can be imported into Vertex AI without additional work using the Vertex AI Model Registry.
* **Model Registration Limitations**:
  * ARIMA_PLUS models
  * XGBoost models
  * Models with transformations

---

## 20.6. BigQuery Design Patterns

* _Data science patterns_ refer to frequent situations with known solutions in machine learning.
* Design patterns provide well-thought-out approaches for addressing these recurring issues.
* BigQuery ML offers **novel** and **elegant** solutions to tackle these patterns.

---

### 20.6.1. Hashed Feature

* **Solution to Categorical Variable Problems**: 
  * Addresses incomplete vocabulary, high cardinality, and cold start issues
  * Utilizes hashing to transform variable into low-cardinality domain

* _Key Hashing Function_: ABS(MOD(FARM_FINGERPRINT(zipcode), numbuckets))
* **Benefits**: Deterministic, well-distributed, and widely available.

---

### 20.6.2. Transforms

* **Transformations in BigQuery ML**: BigQuery ML applies transformations to input data before feeding it into the model.
    * These transformations must be applied when deploying the model in production to ensure consistency.
    * The `TRANSFORM` clause is used to specify these transformations, which are then automatically added to the model during prediction.
* **Available Transforms**: BigQuery ML offers various transforms, including:
    * _Feature Cross_, _Quantile Bucketize_, and others
* **Model Compatibility**: Models with transforms will only work within BigQuery ML and may not be compatible when exported to other services like Vertex AI.

---

## 20.7. Summary

* _BigQuery ML_ revolutionized machine learning use in SQL community
* Enables democratization of ML through simplified pipeline and transformation capabilities
* Highly interoperable with _Vertex AI_ for seamless collaboration

---

## 20.8. Exam Essentials

* **BigQuery and ML Overview**: 
    * Learn BigQuery's history and innovation of integrating machine learning into data analysis
    * Understand how to train, predict, and provide model explanations using SQL
* **BigQuery ML vs Vertex AI**:
  * _Differences between BigQuery ML and Vertex AI_
  * Integration points for seamless collaboration between services
* **BigQuery Design Patterns**: 
  * Applications of BigQuery's solutions for common machine learning problems

---

# 23. Online Test Bank

---

## 23.1. Register and Access the Online Test Bank

* To access the online test bank for your book, go to `www.wiley.com/go/sybextestprep` and follow these steps:
  * Click "here to register" and select your book
  * Complete registration information and receive a pin code via email
  * Enter pin code on create an account or login page to activate access

---

# 24. WILEY END USER LICENSE AGREEMENT

---

