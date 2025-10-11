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

* _Identify the impact, success criteria, and data available for a use case_ 
  * Understand stakeholders' expectations and priorities
  * Determine the most impactful aspect of the use case
* **Match the use case with a machine learning approach**
  * Choose an algorithm and metric suitable for the problem
  * Consider feasibility based on existing technology, data, and budget

---

## 7.2. Machine Learning Approaches

**Machine Learning Landscape**

* Many ML problems are well-researched with elegant solutions
* Some algorithms are not perfect and some problems can be solved in multiple ways
* There are hundreds of ways to apply machine learning techniques, requiring a broad knowledge of approaches
* Each approach solves a specific class of problems distinguished by data type and prediction type

---

### 7.2.1. Supervised, Unsupervised, and Semi‐supervised Learning

* **Machine Learning Approaches**: 
  * _Supervised Learning_: Using labeled datasets to train models, e.g., image classification.
  * _Unsupervised Learning_: Classifying or grouping data without labels, e.g., clustering algorithms and topic modeling.
    * *_Clustering Algorithms_*: Grouping similar data points together.
    * *_Autoencoders_*: Reducing dimensionality of input data.
    * *_Topic Modeling_*: Classifying documents into topics based on word and sentence patterns.

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

* **Classification**: predicting labels or classes from input data (e.g., dogs vs. cats) 
    * Binary classification: 2-class problem (dogs vs. cats)
    * Multiclass classification: problem with multiple classes
* **Regression**: predicting continuous values from input data (e.g., house price, rainfall amount)
* **Forecasting**: predicting future values in a time-series dataset (e.g., temperature measurements) 
    * Can be converted to regression or classification problems

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

* **Choosing an ML Metric**: To determine if a trained model is accurate enough, use an _ML metric_ (or a suite of metrics) to evaluate its performance.
* **Classification Metrics**: For binary classification problems like detecting a rare disease from X-rays, use:
	* **Recall** for low false negative rates
	* **Precision** for reducing false positives
	* **F1 score** as the harmonic mean of precision and recall

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

**ROC Curve Summary**

* **Definition:** Receiver Operating Characteristic curve plots binary classification model performance
* 
  * _X-axis: False positive rate_
  * _Y-axis: True positive rate_
* 
  * _Ideal point: Top-left corner (100% true positive, 0% false positive)_
*

---

### 7.3.2. The Area Under the Precision‐Recall (AUC PR) Curve

* **Precision-Recall Curve**: Graphical plot showing relationship between recall and precision, with x-axis representing recall and y-axis representing precision.
* _AUC PR Best Performance_: Horizontal line at top of graph, indicating 100% precision and 100% recall, which is never achieved but aims for.
* _Dataset Imbalance_: AUC PR preferred over other metrics when dataset is highly imbalanced to avoid skewing.

---

### 7.3.3. Regression

* *_Metrics for Evaluating Regression Models_*
  * *_Mean Absolute Error (MAE)_*: Average absolute difference between actual and predicted values.
  * *_Root-Mean-Squared Error (RMSE)_*: Square root of average squared difference between target and predicted values.
  * *_Root-Mean-Squared Logarithmic Error (RMSLE)_*: Asymmetric metric using natural logarithm, penalizes under prediction.

---

## 7.4. Responsible AI Practices

* **Key Considerations for ML Solutions**
    * Fairness: mitigate bias in models using statistical methods
    * Interpretability: improve visibility into model predictions with model explanations
    * Privacy and Security: detect and prevent data leakage and cybersecurity threats

---

## 7.5. Summary

* *Business Use Case Understanding*: Learn to break down a business question into its core components.
* *Machine Learning Problem Statement*: Frame a problem in terms of data, actions, and outcomes for a machine learning solution.
* *First Steps*: Understand the ask's dimensions, including what, how, and why.

---

## 7.6. Exam Essentials

* **Machine Learning for Business Challenges**
Translate business challenges to machine learning by understanding:
* _Problem types_: regression, classification, and forecasting
* ML metrics: precision, recall, F1, AUC ROC, RMSE, MAPE
* _Responsible AI principles_: fairness, interpretability, privacy, security

---

# 8. Chapter 2Exploring Data and Building Data Pipelines

---

## 8.1. Visualization

* *_Data Visualization_* 
    * Helps in data cleaning by identifying imbalances
    * Facilitates feature engineering to understand feature influence on models
    * Two main types:
        * *_Univariate Analysis_*: Independent analysis of features (box plots, distribution plots)
        * *_Bivariate Analysis_*: Comparison of data between two features (line plots, bar plots, scatterplots)

---

### 8.1.1. Box Plot

* A box plot displays the distribution of data using 25th, 50th, and 75th quartiles.
* The body represents the interquartile range where most observations are present.
* Whiskers show maximum and minimum values, with outliers beyond these points.

---

### 8.1.2. Line Plot

* A line plot displays the relationship between two variables, analyzing trends in data over time.
* It is used to identify patterns and changes in data as it moves over time.
* *Visual representation of data changes over time.*

---

### 8.1.3. Bar Plot

* A bar plot displays **trends and comparisons** between categorical data
* Common applications include analyzing sales figures, website visitors, and product revenue over time
* Used for _visualizing_ trends and patterns in data.

---

### 8.1.4. Scatterplot

* **Scatterplot**: Visualizes relationships between 2 variables, showing clusters and patterns in a dataset.
    * Used for:
        * _Visualizing data distributions_
        * Identifying correlations between variables
        * Detecting outliers and anomalies

---

## 8.2. Statistics Fundamentals

* *_Three Measures of Central Tendency_* 
    * **Mean**: Average value of a dataset
    * **Median**: Middle value in a sorted dataset
    * **Mode**: Most frequently occurring value

---

### 8.2.1. Mean

Mean is the accurate measure to describe the data when we do not have any outliers present.

---

### 8.2.2. Median

* **Median**: calculated when data contains an outlier; found by arranging values from lowest to highest
* _Example_: if even numbers are present, the median is the average of two middle numbers; for odd numbers, it's the single middle value.
* **Calculation**: take mean of two middle numbers (if even) or single middle number (if odd).

---

### 8.2.3. Mode

* *_Mode_*: The value(s) that appear most frequently in a dataset
    * It is used when the majority of data points are the same, but there's an outlier
    * Example: Dataset 1, 1, 2, 5, 5, 5, 9 where 5 appears most

---

### 8.2.4. Outlier Detection

* **Effect of outliers on mean**: The presence of an outlier can significantly impact the mean, making it less representative of the dataset's central tendency.
    * _Outliers_ have a large influence on the mean, making it more susceptible to changes in data.
        + Adding an outlier like 210 skews the mean from 29.16 (without outlier) to 12.72 (with outlier).

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

### Understanding Statistical Measures

#### **Standard Deviation**
* _Measure of data spread_
* Square root of variance
* Identifies outliers as points more than 1 standard deviation from the mean

#### **Covariance**
* Measure of how two variables vary together

---

### 8.2.6. Correlation

Correlation is a measure of how two variables are related, ranging from -1 to +1.
* _Types of Correlation_:
  * **Positive Correlation**: Increase in one variable results in increase in another
  * **Negative Correlation**: Increase in one variable results in decrease in another
  * **Zero Correlation**: No substantial impact between variables
* Correlation helps detect label leakage, where high correlation between features and target can lead to biased models.

---

## 8.3. Data Quality and Reliability

* *_Data Quality Matters_* 
  * Unreliable data can lead to poor model performance
  * Consider data with missing values, duplicates, and bad features as "unclean"
  * Ensure data is reliable by checking for label errors, noise in features, and outliers

---

### 8.3.1. Data Skew

* *_Data Skew_*: when the normal distribution curve is not symmetric, resulting in uneven data distribution.
  * Causes of skew include outliers and extreme values.
  * Types of skew: right-skewed and left-skewed data
    * Right-skewed data: occurs with outlier-prone distributions like income data

---

### 8.3.2. Data Cleaning

* **What is Normalization?**: transforms features to be on a similar scale
* *Improves model performance and training stability*
* **Why is it used?**: To prevent features with large ranges from dominating the model

---

### 8.3.3. Scaling

## Scaling in Feature Values
Scaling converts floating-point feature values to a standard range (e.g., 0-1) to improve model performance.
### Benefits:
* **Improved Gradient Descent Convergence**
* **Removal of NaN Traps**
* **Reduced Impact of Outliers**

### Use Cases:
* Uniformly distributed data with no skew
* No outliers in the data

---

### 8.3.4. Log Scaling

* *_Log Scaling_*: scales data to a common range by taking the logarithm of values.
    * Used for data with varying scales, such as large and small numbers.
    * Example: log(10,000) = 4, log(100) = 2

---

### 8.3.5. Z‐score

* **Z-score**: calculated as (value - mean) / stddev
* *_Outliers_*: values beyond ±3 standard deviations from the mean
* _Example_: scaled value = 1.5 for original value = 130, mean = 100, stddev = 20

---

### 8.3.6. Clipping

* **Feature Clipping**: capping extreme outlier values to a fixed limit
    * _Pre-clip_ vs. _Post-clip_: performed before or after other normalization techniques
    * Purpose: prevent outliers from dominating the data

---

### 8.3.7. Handling Outliers

* *_Outliers_*: Values that are significantly different from others in a dataset.
    * **Detection Techniques**: Box plots, Z-score, Clipping, Interquartile Range (IQR)
        * _Methods for handling outliers_: Removing, Imputing with mean/mode/boundary values

---

## 8.4. Establishing Data Constraints

* **Defining a Data Schema**
  * A schema describes the property of your data, including data type, range, format, and distribution
  * A schema is an output of the data analysis process, providing a consistent and reproducible check for data quality issues
    * _Advantages:_
      * Enables metadata-driven preprocessing for feature engineering and data transformation
      * Validates new data and catches anomalies like skews and outliers during training and prediction

---

### 8.4.1. Exploration and Validation at Big‐Data Scale

* **TensorFlow Data Validation (TFDV)**
    * Helps validate large ML datasets in memory
    * Detects data anomalies and schema anomalies
    * Part of the _TensorFlow Extended (TFX)_ platform 
        * Provides libraries for data validation, schema validation, and more

---

## 8.5. Running TFDV on Google Cloud Platform

* **TFDV Core**: Built on Apache Beam SDK for batch & streaming pipelines
* *Talent is not required, Dataflow runs pipelines at scale using Apache Beam*
* *Integrates with BigQuery, Google Cloud Storage and Vertex AI Pipelines*

---

## 8.6. Organizing and Optimizing Training Datasets

* *_Key Components of a Dataset_* 
  * **Training Dataset**: used to train the model
  * **Validation Dataset**: used for hyperparameter tuning and evaluation
  * **Test Dataset**: used to evaluate the performance of the trained model

---

### 8.6.1. Imbalanced Data

* **Imbalanced Data**: When two classes are unequal, it results in imbalanced data.
    * _Causes problems_ for training models
        * May spend too much time on majority class
    * Downsampled minority class can improve balance
        * Example: downsampling by 10 improves balance

---

### 8.6.2. Data Splitting

* **Data Preprocessing**: Start with random splitting of data
*   *Avoids skew due to naturally clustered examples*
*   However, it may cause skew when data points share similar characteristics (e.g., same topic)
*   Example: Training and testing sets might contain the same stories with the same topic

---

### 8.6.3. Data Splitting Strategy for Online Systems

* **Splitting Data for Time-Based Models**
  * Split data by time to mirror the lag between training and prediction
  * Use a time-based approach with large datasets (e.g., millions of examples)
  * Avoid random splits; use domain knowledge instead

---

## 8.7. Handling Missing Data

* **Handling Missing Data**: 
    * Deleting rows/columns with missing values, or replacing with mean/median/mode.
    * Imputing categorical values with most frequent category, using _last observation carried forward (LOCF)_ method for time-series datasets.
    * Using machine learning algorithms that can ignore or predict missing values.

---

## 8.8. Data Leakage

* **Data Leakage**: occurs when model exposed to test data during training, leading to overfitting
* *Causes of Data Leakage*: 
  * Incorrectly adding target variable as feature
  * Including test data in training data
  * Applying preprocessing techniques to entire dataset
* **Prevention Measures**:
  * Selecting uncorrelated features with the target variable
  * Splitting data into test, train, and validation sets
  * Preprocessing training and test data separately

---

## 8.9. Summary

* **Data Visualization**: Visualizing data using box plots, line plots, and scatterplots to understand data distribution.
    * *_Key statistics_*: Mean, median, mode, and standard deviation to identify outliers.
* **Data Preprocessing**
    * *_Scaling techniques_*: Log scaling, scaling, clipping, z-score to improve data quality
    * *_Data validation_*: Establishing data constraints and defining a data schema for ML pipelines.

---

## 8.10. Exam Essentials

* _Data Visualization:_ Understanding box plots, line plots, scatterplots, and statistical terms like mean, median, mode, standard deviation, and correlation to visualize and analyze data.
  * **Statistics Fundamentals:** Describing outliers, skewness, and data cleaning techniques to ensure accurate data representation.
  * _Data Quality and Constraints:_ Validating data, establishing a schema, and applying data normalization and scaling techniques to define data constraints.

* _Data Preprocessing:_
  * **Data Splitting:** Dividing datasets into training, test, and validation sets for optimal model performance.

---

  * **Handling Imbalanced Data:** Applying sampling strategies to balance imbalanced datasets.
  * **Missing Data Handling:** Removing, replacing, or generating missing values using various techniques.

---
# 9. Chapter 3Feature Engineering

---

## 9.1. Consistent Data Preprocessing

* **Data Transformation Approaches**
  * Pretraining Data Transformation: Transformation performed before model training, advantages include one-time computation and dataset analysis.
    * Disadvantages include reproduction at prediction time and updating challenges.
  * Inside Model Data Transformation: Transformation within the model code, decoupling data and transformation is easy, but can increase model latency.
    * Example solution using _tf.Transform_ .

---

## 9.2. Encoding Structured Data Types

* *_Feature engineering key characteristics_*
	+ Related to business objectives
	+ Known at prediction time
	+ Numeric with magnitude
	+ Enough examples
* *_Types of data used in feature engineering_*
	+ **Categorical Data**: defines category with limited values (e.g. yes/no, male/female)
	+ **Numeric Data**: represents scalar value or continuous data (e.g. observations, measurements)

---

### 9.2.1. Why Transform Categorical Data?

*_Categorical Data Limitation_* 

* Most ML algorithms require numeric input and output variables.
* Categorical data must be converted to numeric data for use in these algorithms.

---

### 9.2.2. Mapping Numeric Values

* *_Data Encoding_*: Integer and floating-point data do not require special encoding as it can be scaled using a numeric weight.
* *Transformations for Numeric Data*: Two types of transformations are applied: **_normalization_** and **_bucketing_**.

---

#### 9.2.2.1. Normalizing

* Normalization techniques are used to handle **differently scaled numeric features**, improving model convergence
    * Techniques like **AdaGrad** and **Adam** help by creating separate learning rates for each feature
        * This prevents data ranges from slowing down gradient descent

---

#### 9.2.2.2. Bucketing

**Transforming Numeric Data to Categorical**
_bucketing simplifies numeric data into categories_

* _Methods:_
  * *_Equal-spaced boundaries:_* Divide range into discrete buckets (e.g., rainfall ranges)
  * *_Quantile boundaries:_* Equal number of points in each bucket with flexible boundaries

---

### 9.2.3. Mapping Categorical Values

* *_Data Conversion Techniques_* 
    * One-hot encoding
    * Label encoding
    * Binary encoding

---

#### 9.2.3.1. Label Encoding or Integer Encoding

* *_Label Encoding_* 
    * _Assigns unique integers to distinct categories_
    * _Useful for small datasets with limited categories_

---

#### 9.2.3.2. One‐Hot Encoding

* _**One-hot encoding is a technique for converting categorical variables into binary representation**_
    * _It creates new variables for each unique value in the categorical feature, representing it as a binary vector._
    * _Used when the features are nominal and no ordinal relationship exists, to convert categorical data into a numerical format._

---

*One‐Hot Encoding*
Categorical Value | Integer Encoding or Creating a Vocabulary Mapping | One‐Hot Encoding
---|---|---
Red | 0 | 00
Blue | 1 | 01

<!-- _class: centered -->

---

#### 9.2.3.3. Out of Vocab (OOV)

* **Handling Outliers**: Create a single category `_out of vocabulary_` to group rare outliers together, reducing unnecessary training on individual outliers.
 
*  Using this approach simplifies model training and improves performance.
* This technique is often used in situations where outliers occur very infrequently in the dataset.

---

#### 9.2.3.4. Feature Hashing

* **Hashing**: applies a hash function to categorical features and uses their hash values as indices
* _Advantage_: no need to reassemble vocabulary if feature distribution changes
* **Collision problem**: hashing can cause inconsistencies (collisions) for important terms

---

#### 9.2.3.5. Hybrid of Hashing and Vocabulary

* *Hashing-based approach to represent categories outside of pre-defined vocabulary*
    * Reduces complexity by mapping non-vocabulary categories to hash values
    * Enables model to learn categories not included in the predefined vocabulary

---

#### 9.2.3.6. Embedding

* **What is Embedding**: 
    * _Continuous-valued feature_ that represents categories
    * Often created by converting index values into a numerical vector

---

### 9.2.4. Feature Selection

* **Feature Selection** selects a subset of useful input variables to predict a target variable, reducing noise and overfitting issues.
    * Can be done using:
        * Keeping only the most important features
        * Finding a combination of new features
        * _Techniques include: backward selection, Random Forest, PCA, t-SNE_

---

## 9.3. Class Imbalance

* **Classification Model Outcomes**
  * _True Positive_: Correctly predicts positive class (e.g., patient is actually sick)
  * True Negative: Correctly predicts negative class
  * False Positive: Incorrectly predicts positive class (e.g., patient is not sick but test says so)
  * **False Negative**: Incorrectly predicts negative class (patient is sick but test determines not so)

---

### 9.3.1. Classification Threshold with Precision and Recall

**Classification Threshold**
A **classification threshold** is a chosen value that maps logistic regression output to a binary category. It's usually set between 0 and 1.

* *_Increasing threshold_* reduces false positives, increasing _precision_, but decreasing recall.
* *_Decreasing threshold_* increases false negatives, increasing recall, but decreasing precision.
* *_Precision_ vs Recall_: improving one decreases the other_.

---

### 9.3.2. Area under the Curve (AUC)

* **Classification Metrics**: Two types of area under the curve used in classification problems
    * *_AUC-ROC_*: balanced dataset with equal numbers of examples per class
    * *_AUC-PR_*: imbalanced dataset where classes have unequal numbers of examples

---

#### 9.3.2.1. AUC ROC

* **ROC Curve**: a graph showing classification model performance at all thresholds
    * Plots true positive rate vs false positive rate
* **AUC ROC**: measures 2D area under the curve, between 0.0 and 1.0
    * Represents binary classification model's ability to separate classes

---

#### 9.3.2.2. AUC PR

* **Precision-Recall Curve**: a graph showing Precision values on the y-axis and Recall values on the x-axis
    * _Effective for imbalanced binary classification models_, as it focuses on the minority class.
    * The area under the curve (AUC PR) measures the 2D area underneath, providing more attention to the minority class.

---

## 9.4. Feature Crosses

* _Feature Cross_: A synthetic feature created by multiplying two or more features.
  * Can be used to increase predictive ability when individual features are not sufficient
    * Example: combining location (market, curbside) and time of day
  * Used to represent nonlinearity in linear models with complex data
    * Example: creating a feature cross from dot and rectangle features to learn separation classes

---

## 9.5. TensorFlow Transform

* **Efficient Input Pipeline**: Key to increasing TensorFlow model performance
* * _TF Data API_*: A unified interface for reading data from various sources, including files, databases, and APIs.
* * _TensorFlow Transform_*: A library for data preprocessing and transformation, enabling efficient data processing and caching.

---

### 9.5.1. TensorFlow Data API (tf.data)

* **Optimize Model Execution Speed**
    * Use `tf.data.Dataset.prefetch` to overlap preprocessing and model execution
    * Utilize `tf.data.Dataset.interleave` for parallel data reading and caching
        * Apply `cache` transformation during the first epoch
            * Reduces file opening and data reading operations

---

### 9.5.2. TensorFlow Transform

* **TensorFlow Transform**: allows transformations before training to avoid training-serving skew, creating a reproducible graph during training.
    * Utilizes tf.Transform and Cloud Dataflow in Google Cloud.
    * Includes steps such as data analysis, transformation, serving, and metadata production.
* Pipeline components:
    * **Data Ingestion & Validation**
        * TensorFlow Data Validation
        * Cloud Dataflow
    * **Data Transformation**
        * TensorFlow Transform
        * Cloud Dataflow
    * **Model Training & Tuning**
        * TensorFlow Estimators/TF Keras
        * Vertex AI Training

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

* _Data Transformation Tools in Google Cloud_
  * **Cloud Data Fusion**: a managed service for building ETL pipelines, supporting Cloud Dataproc
  * _Dataprep by Trifacta_: a serverless tool for visually exploring, cleaning, and preparing data

---

## 9.7. Summary

* **Feature Engineering**: Transforming numerical and categorical features is crucial for model training and serving.
    * _Key techniques:_ Bucketing, normalization, linear encoding, one-hot encoding, out-of-vocabulary hashing, and embedding
    * _Additional concepts:_
        * Dimensionality reduction using PCA
        * Class imbalance and AUC-PR vs. AUC-ROC

---

## 9.8. Exam Essentials

* **Data Processing Consistency**: Understand when to transform data before or during training, benefits, and limitations.
  * _Encoding structured data types_: techniques like bucketing, normalization, hashing, and one-hot encoding for numeric and categorical data.
  * _Feature selection and cross_: dimensionality reduction, feature cross importance, and scenarios requiring it.
  * _GCP Data Tools_: Cloud Data Fusion (ETL) and Cloud Dataprep (data processing), choosing the right tool for the task.

---

# 10. Chapter 4Choosing the Right ML Infrastructure

---

## 10.1. Pretrained vs. AutoML vs. Custom Models

* _Pretrained Models_: 
  * Use existing models trained on large datasets by Google.
  * Easy to use and fast integration with APIs.
  * No need to think about algorithm, deployment, or scalability.

* _AutoML_:
  * Build custom model using own data.
  * Chooses best ML algorithm without needing expert knowledge.
  * Requires provisioning cloud resources for training and deployment.

* _Custom Models_: 
  * Top tier in pyramid; offers flexibility in algorithm, hardware, and data types.
  * Suitable when use case is unique and no AutoML available.

---

## 10.2. Pretrained Models

* **Pretrained Models**: Machine learning models trained on large datasets, performing well in benchmark tests, and available for use through Google Cloud's web console or SDK.
* **Google Cloud Pretrained Models**: Various models including:
  * _Vision AI_
  * _Video AI_
  * _Natural Language AI_
  * _Translation AI_
  * _Speech-to-Text_ and _Text-to-Speech_
* **Platforms Offering Solutions**: Document AI and Contact Center AI, which include pretrained models and uptrain capabilities.

---

### 10.2.1. Vision AI

* **Vision AI**: convenient access to ML algorithms for image processing and analysis
    * Provides services such as:
        * Object detection and face recognition
        * Handwriting analysis (optical character recognition)
    * Available at `https://cloud.google.com/vision`

---

### 10.2.2. Video AI

* **Video AI API**: Recognizes objects, places, and actions in videos with pretrained machine learning models.
* *Key benefits:*
    - Can process stored or streaming video
    - Recognizes over 20,000 different objects, places, and actions
    - Returns results in real-time for livestreams
* **Use Cases:**
    * _Video recommendation system_: recommends videos based on user viewing history and generated labels.
    * _Video archiving_: indexes video metadata for mass media companies.
    * _Ad relevance improvement_: compares video content with inserted ads for improved user experience.

---

### 10.2.3. Natural Language AI

**Google Natural Language AI Services**
* Provides entity extraction, sentiment analysis, syntax analysis, and categorization
    * Entity extraction identifies key entities with additional information (e.g., Wikipedia links)
    * Sentiment analysis scores text as positive, negative, or neutral by sentence, entity, and document
* **Use Cases:**
  * Measure customer sentiment for specific products
  * Extract medical insights from healthcare texts using Healthcare Natural Language API

---

### 10.2.4. Translation AI

* **Translation Service**: detects over 100 languages and translates between any pairs of languages using Google Neural Machine Translation technology
    * *_Service Tiers_*: Basic and Advanced, with differences including glossary support and document translation capabilities
        + *_Advanced Tier_*: also includes real-time audio translation with Media Translation API

---

### 10.2.5. Speech‐to‐Text

* *Speech-to-Text service*: converts recorded audio or streaming audio into text
* Commonly used for creating subtitles and translating them into multiple languages

---

### 10.2.6. Text‐to‐Speech

* _Text‐to‐Speech service_ provides realistic speech with humanlike intonation using DeepMind's AI expertise
    * Supports 220+ voices in 40+ languages and variants, including creating unique brand voices
        * Available at `_https://cloud.google.com/text-to-speech/docs/voices`_

---

## 10.3. AutoML

* **Automated Machine Learning (AutoML)**: automates model training tasks for popular ML problems like image classification, text classification, and more.
* AutoML uses a web console or SDK to initiate the training process with minimal user configuration.
* Available for various data types:
  * *_Structured data_*
  * Images/video
  * *_Natural language_*
  * *_Recommendations AI/Retail AI_*

---

### 10.3.1. AutoML for Tables or Structured Data

* *_Structured data_*: Data in a well-defined schema, typically represented as a rectangular table.
    * *_Training methods_*:
        + **BigQuery ML**: A SQL-based approach for training models
        + **Vertex AI Tables**: A serverless approach that uses Python, Java, or Node.js to deploy and serve predictions
* *_Vertex AI AutoML Tables algorithms_*:
    * *_Classification_*: AUC ROC, AUC ROC, Logloss, Precision at Recall, Recall at Precision
    * *_Regression_*: RMSE, RMSLE, MAE
    * *_Time-series data_*: Forecasting RMSE, RMSLE, MAPE, Quantile loss

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

* **Vertex AI AutoML**: Simplifies building machine learning models for image and video data
    * Supports various tasks: image classification, multiclass classification, object detection, image segmentation, video classification, action recognition, and object tracking
        * *AutoML Edge model*: Optimized for edge devices, using less memory and low latency for iPhones, Android phones, and Edge TPU devices

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

* **Machine Learning for Text**: Easy to build models using Vertex AI AutoML text
    * Solves 4 main problems: 
        * _Text classification_: predict label for a document
        * Multi-label classification: predict multiple labels for a document
        * Entity extraction: identify entities in text
        * Translation: convert text from source language to target language

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

### Google Cloud Retail AI Solution

* AutoML solution for retail domain offering **Google-quality search**, **image search**, and **personalized recommendations**
* Solutions include:
	+ _Retail Search_: customizes Google's understanding of user intent and context
	+ _Vision API Product Search_: trains on product images for image-based searching
	+ _Recommendations AI_: drives engagement through relevant recommendations based on customer behavior and product metadata

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

* **Document AI**: extracts details from scanned images of old documents, forms, and government papers using machine learning models.
    * **Key Features**:
        * Detects document quality
        * Extracts text and layout information
        * Identifies and extracts key/value pairs
    * _Processors_: interfaces between documents and machine learning models for specific tasks (general, specialized, custom)

---

### 10.3.6. Dialogflow and Contact Center AI

* Dialogflow is a *conversational AI platform* offering from Google Cloud that provides chatbots and voicebots.
    * Integrated into telephony services for a *_Contact Center AI_* solution, enabling businesses to provide intelligent customer interactions
        * Also available as a standalone service for various applications and use cases

---

#### 10.3.6.1. Virtual Agent (Dialogflow)

* **Virtual Agent Strategy**: Rapidly develop advanced virtual agents for enterprises, handling most common cases and forwarding complex ones to human agents.
* * * 
  * _Primary Function_: Handle topic switching and supplemental questions.
  * _Key Feature_: Multichannel support 24/7.

---

#### 10.3.6.2. Agent Assist

* **Agent Assist**: Identifies customer intent and provides pre-crafted responses and transcripts to assist with calls.
* *_Real-time support_*: Agent Assist provides assistance in the moment, using a centralized knowledge base.
* *Automated response aid*: Enhances agent capabilities by offering ready-to-send answers.

---

#### 10.3.6.3. Insights

* *Natural Language Processing (NLP)*: Analyzes calls to measure driver sentiment
    * Calls drivers to gauge customer feedback
        + Helps leadership optimize call center performance

---

#### 10.3.6.4. CCAI

* *_Contact Center AI platform_*: Cloud native platform for multichannel customer-agent communications
* *_Dialogflow and CCAI_*: Advanced machine learning techniques, but details are not within the scope of this exam.

---

## 10.4. Custom Training

* **Training on Custom Hardware**: With custom training, you have full flexibility to choose from a wide range of hardware options for training your model.
    * _GPUs can significantly speed up deep learning model training_, reducing compute-intensive operations like matrix multiplications by an order of magnitude.
        + Trained on a single CPU, model training can take days or weeks; with GPU acceleration, it can be reduced to hours.

---

### 10.4.1. How a CPU Works

* **CPU Basics**
  * A processor that runs various types of workloads
  * Designed to be flexible and perform many operations
  * Loads data from memory, performs operation, and stores result back into memory for each task
* **Serial Computation Limitation**
  * CPU performs computations sequentially, which can lead to inefficiency

---

### 10.4.2. GPU

**GPUs in Vertex AI**
GPUs bring additional firepower to Vertex AI, accelerating data processing and image rendering. A GPU is a specialized chip with thousands of arithmetic logic units (ALUs) that work together in parallel.

**Configuring GPUs**

* To use GPUs, specify the type of GPU (`machineSpec.acceleratorType`) and number of GPUs per VM (`machineSpec.acceleratorCount`).
* Restrictions apply to instance types, location availability, and resource compatibility.

---

* * Google provides a compatibility table for quick reference: [https://cloud.google.com/vertex-ai/docs/training/configure-compute#gpu-compatibility-table](https://cloud.google.com/vertex-ai/docs/training/configure-compute#gpu-compatibility-table)

**Key Points**

* * GPUs are available in A2 and N1 machine series.
* Not all GPU types are available in all regions.
* Number of GPUs per instance is restricted, with tables providing guidance on compatible instances.

---
### 10.4.3. TPU

* **GPUs Limitation**: GPUs have limitations due to their semi-general-purpose design and need for frequent register access.
* _**TPUs Design**_: TPUs are specialized hardware accelerators designed specifically for machine learning workloads.
    * **Matrix Processing**: TPUs excel at matrix processing, performing massive multiply-accumulate operations on large matrices.

---

#### 10.4.3.1. How to Use TPUs

**Cloud TPU Configurations**
 
* * A single TPU device
* * A **TPU Pod**: A group of TPU devices connected by high-speed interconnects, scaling workloads with little code changes
* * A **TPU Slice**: A subdivision of a TPU Pod for more precise control

---

#### 10.4.3.2. Advantages of TPUs

* **TPUs outperform GPUs by orders of magnitude**, accelerating training times from _months (CPUs)_ to _hours (GPUs) and potentially just days (TPUs)_.

---

#### 10.4.3.3. When to Use CPUs, GPUs, and TPUs

* **Hardware Selection**: Choose CPU for rapid prototyping, small models with limited I/O, or custom TensorFlow operations in C++.
    * _Use GPU_ when source code is too tedious to change, custom ops are needed, medium-to-large models require TPUs.
* **Cloud TPU Limitations**: Do not use TPUs for programs requiring conditionals, sparse data, high precision, or deep neural networks with custom C++ ops.
    * _Best suited for matrix computations and large models_
* **TPU Training Efficiency**: Run multiple iterations of the training loop to remove dramatic inefficiency.

---

#### 10.4.3.4. Cloud TPU Programming Model

* **Data Transfer Bottleneck**: Data transfer between Cloud TPU and host memory via PCIe bus is a significant bottleneck due to its slow speed compared to TPU interconnect and HBM.
    * _Optimal Programming Model_: Executing most of the training loop on the TPU, ideally all of it, to minimize idle time.

---

## 10.5. Provisioning for Predictions

* **Prediction Phase**: Focuses on deploying a model to make predictions
    * _Methods_: Online prediction (near real-time) and batch prediction (near reasonable time)
    * _Workload characteristics_: Continuous, with demand-driven scaling required

---

### 10.5.1. Scaling Behavior

* _**Autoscaling in Vertex AI**: Automatically scales prediction nodes when CPU usage is high._
* *To monitor resources on GPU nodes: CPU, Memory, and GPU usage need to be configured as triggers.*
* *Ensure proper trigger configuration for efficient resource utilization.*

---

### 10.5.2. Finding the Ideal Machine Type

* To determine the ideal machine type for a custom prediction container from a cost perspective, consider:
    * _Queries per second (QPS) cost per hour_ of different machine types
    * Resource utilization (_CPU_, _memory_, _GPU_) and limitations (_single-threaded web server_)
    * Latency and throughput requirements

* Consider using GPUs to accelerate predictions, but be aware of restrictions such as:
    * _Only compatible with TensorFlow SavedModel or custom containers_
    * Limited availability in some regions
    * _One type of GPU per DeployedModel resource_

---

### 10.5.3. Edge TPU

* **Edge Inference**
  * Accelerates ML inference on IoT devices with limited bandwidth and offline capabilities
  * Enables real-time data analysis and decision-making
  * Improves device performance and reduces power consumption

* **Google Edge TPU**
  * 4 trillion operations per second (4 TOPS) with 2 watts of power
  * Available for prototyping and production devices in various form factors

---

### 10.5.4. Deploy to Android or iOS Device

* **ML Kit**: A mobile development package that brings Google's machine learning expertise to iOS and Android apps
    * Allows training of ML models on Google Cloud, using AutoML or custom models
    * Enables predictions on device for low latency and offline support

---

## 10.6. Summary

* **Google Cloud Models**: pretrained models available on Google Cloud for various applications
* **Hardware Options**: GPUs, TPUs, and edge computing for training and prediction workloads
* *_Deploying Beyond the Cloud_*: using edge devices for model deployment

---

## 10.7. Exam Essentials

* _**Machine Learning Approach Selection**: Choose between pretrained models, AutoML, or custom models based on solution readiness, flexibility, and approach._
* * **Hardware Provisioning for Training**: Understand GPU, TPU, and instance type requirements for training, as well as differences in hardware for deployment._
* * **Hardware Provisioning for Predictions**: Scalability, CPU, and memory constraints require cloud-based CPUs and GPUs for predictions, while TPUs are used in edge devices._

---

# 11. Chapter 5Architecting ML Solutions

---

## 11.1. Designing Reliable, Scalable, and Highly Available ML Solutions

* **ML Pipeline**:
  * Data collection: Google Cloud storage, Pub/Sub (streaming data), BigQuery
  * Data transformation: Dataflow
  * Model training: Custom models (Vertex AI Training and Vertex AutoML)
  * Tuning and experiment tracking: Vertex AI hyperparameter tuning and Vertex AI Experiments
* **Automating the pipeline**: 
  * Orchestration and CI/CD: Vertex AI Pipelines
  * Model deployment and monitoring: Vertex AI Prediction and Vertex AI Model Monitoring

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

* **Google Cloud ML Services Layers**
  * _Top Layer: AI Solutions (Managed SaaS)_
    * Document AI, Contact Center AI, Enterprise Translation Hub
  * _Middle Layer: Vertex AI Services_
    * Pretrained APIs for common use cases
    * AutoML for enriching models with business data
    * Workbench for custom model development
  * _Bottom Layer: Infrastructure (Managed by User)_
    * Compute instance and containers

---

*Choosing an Appropriate ML Service*
GCP Service | When to Use
---|---
BigQuery ML | You have structured data stored in a BigQuery data warehouse because BigQuery ML requires a tabular dataset. You are comfortable with SQL and the models available in BigQuery ML match the problem you are trying to solve. We are going to cover all the models in Chapter 14.
AutoML (in the context of Vertex AI) | Your problem fits into one of the types that AutoML supports, such as classification, object detection, sentiment analysis, and translation.

<!-- _class: centered -->

---

## 11.3. Data Collection and Data Management

* _Data Stores in Google Cloud_
    * **Google Cloud Storage**: object-based storage for large files and blobs
    * *_NoSQL Data Store_*: flexible schema, high scalability, and performance
        * **Vertex AI's datasets**: manage training and annotation sets for machine learning
            * **Vertex AI Feature Store**: stores and manages model artifacts and features

---

### 11.3.1. Google Cloud Storage (GCS)

* _Google Cloud Storage (GCS)_ is a service for storing various types of data
    * Supports images, videos, audio, and unstructured data
        * Can combine these into large files >= 100 MB with up to 10,000 shards for improved read/write throughput

---

### 11.3.2. BigQuery

* **Store data in BigQuery**: Use BigQuery for tabular data storage, especially for training data.
    * _Use tables instead of views_ to improve query speed.
* **Access BigQuery functionality**:
  * Google Cloud console: Search for BigQuery
  * `bq` command-line tool
  * BigQuery REST API
  * Vertex AI Jupyter Notebooks with BigQuery Magic or Python client

---

*BigQuery*
Framework | Google Cloud tool to read data from BigQuery
---|---
TensorFlow or Keras | `tf.data.dataset reader for BigQuery` and tfio.BigQuery.BigQueryClient()

<!-- _class: centered -->

---

### 11.3.3. Vertex AI Managed Datasets

* **Use managed datasets for custom models**
  * Manage datasets in a central location.
  * Easily track lineage and compare model performance
* *_Alternative:_* Use your own storage and control over data splitting if needed.
* *_Data labeling:_* Use Vertex AI's data labeling service to label unlabeled and unstructured data.

---

### 11.3.4. Vertex AI Feature Store

* **Vertex AI Feature Store**: A fully managed centralized repository for ML features
* *_Benefits_*:
	+ No need to compute feature values and save them in various locations
	+ Helps detect drifts and mitigate data skew due to centralized creation of features
	+ Enables fast online predictions with real-time retrieval of feature values

---

### 11.3.5. NoSQL Data Store

### Static Feature Lookup

For static feature lookup during prediction, use:
* **NoSQL database**: Optimized for singleton lookup operations
* * _Use Memorystore_, *_Datastore_ or *_Bigtable_* *
* _Avoid block storage_ such as NFS or VM hard disk, and _avoid reading from databases directly_

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

* **Machine Learning Workflow**: Machine learning workflows define the phases of a project, including data collection, model training, evaluation, and deployment.
* _Key Integration Challenge_: Integrating an ML system into a production environment requires orchestrating pipeline steps and automating execution for continuous model training.
* * **Pipeline Solutions**: Kubeflow Pipelines and Vertex AI Pipelines offer automated pipeline solutions to streamline machine learning workflows.

---

### 11.4.1. Use Vertex AI Pipelines to Orchestrate the ML Workflow

**Vertex AI Pipelines**
Managed service for automating, monitoring, and governing ML systems
* Orchestrates ML workflow in serverless manner
* Stores workflow artifacts using Vertex ML Metadata
* Supports Kubeflow Pipelines SDK v1.8.9 and higher or TensorFlow Extended v0.30.0 and higher

**Key Benefits**

* Simplifies pipeline management across different ML environments
* Reduces the need for on-premises infrastructure with a small number of nodes

---

### 11.4.2. Use Kubeflow Pipelines for Flexible Pipeline Construction

* _Kubeflow_ is an open source Kubernetes framework for developing and running portable machine learning (ML) workloads.
    * **Kubeflow Pipelines** lets you compose, orchestrate, and automate ML systems using a flexible and user-friendly approach.
        * Supports deployment on-premises, locally, or in the cloud with services like Google Cloud.

---

### 11.4.3. Use TensorFlow Extended SDK to Leverage Pre‐built Components for Common Steps

* **TFX vs TensorFlow Extended SDK**: 
  * TFX for general machine learning model deployment
  * TensorFlow Extended SDK when using:
    * _Structured data_
    * _Large datasets_
    * Existing TensorFlow usage

---

### 11.4.4. When to Use Which Pipeline

* **Summary of Vertex AI Pipelines**
  * Supported platforms: Kubeflow Pipelines v1.8.9+, TensorFlow Extended v0.30.0+
  
  * _Orchestrators_ like Kubeflow make ML pipeline management easier with GUIs and scheduling capabilities
  * Recommended for TFX users to simplify pipeline creation, operation, and maintenance
  
  * Vertex AI Pipelines provide built-in support for common ML operations and lineage tracking

---

## 11.5. Serving

* **Prediction Methods**: Machine learning models can make predictions in either *_offline_* or *_online_* modes.
* _Offline_ mode makes predictions using pre-trained data
* _Online_ mode makes predictions in real-time, adjusting to new data as it becomes available

---

### 11.5.1. Offline or Batch Prediction

* **Offline Batch Prediction**: Performs prediction on batches of data without real-time interaction
* *Use cases:* Recommendations, demand forecasting, segment analysis, and text classification
* **Vertex AI Integration**: Runs batch prediction jobs on BigQuery or Google Cloud Storage

---

### 11.5.2. Online Prediction

**Online Predictions**

* **Synchronous**: Caller waits for prediction from ML service before performing subsequent steps.
  * Deploy model as HTTPS endpoint using Vertex AI
  * Use App Engine or GKE as ML gateway for feature preprocessing

* **Asynchronous**
  * **Push**: Model generates predictions and notifies end user directly (e.g. fraud detection)
    * Example: Google Cloud architecture for push notifications
  * **Poll**: Model stores predictions in low-latency read database, end user polls periodically (e.g. targeted marketing)
    * Example: Google Cloud architecture for poll-based online prediction

**Minimizing Latency**


---

* **Model Level**: Minimize time taken by model to make prediction when invoked with request
  * Build smaller model with fewer neural network layers and less compute required
* **Serving Level**: Minimize time taken by system to serve prediction when receiving request
  * Store input features in low-latency read lookup data store
  * Precompute predictions in offline batch-scoring job

---
## 11.6. Summary

* **Designing an ML Solution on GCP**
	+ Reliable, scalable, and highly available solutions
	+ Choosing the right service from the three layers of the GCP AI/ML stack
* **Data Management and Storage**
	+ Data collection and management strategy for Vertex AI platform with BigQuery
	+ NoSQL data store options for submillisecond and millisecond latency
* **Automation and Orchestration**
	+ ML pipeline automation techniques (Vertex AI Pipelines, Kubeflow Pipelines, TFX pipelines)

---

## 11.7. Exam Essentials

* _Design reliable, scalable, and highly available ML solutions using Google Cloud AI/ML services_
  * Choose an appropriate ML service based on your use case and expertise
  * Understand data collection and management, including various types of data stores
  * Implement automation and orchestration with Vertex AI Pipelines or Kubeflow/TFX pipelines
  * Deploy models efficiently, balancing batch prediction vs. real-time prediction and managing latency

---

# 12. Chapter 6Building Secure ML Pipelines

---

## 12.1. Building Secure ML Systems

* **Data Security in Google Cloud**: Ensures the security of users' and employees' data through various built-in security measures.
    * *_Encryption_*: Protects data both while it is stored on servers (at rest) and when it is transmitted over the internet (in transit).
        + **At Rest Encryption**: Protects data from unauthorized access while it is stored on Google Cloud's servers.
        + **In Transit Encryption**: Protects data as it is transmitted between devices, applications, and Google Cloud services.

---

### 12.1.1. Encryption at Rest

* **Encryption Overview**
    * _Google encrypts data at rest by default, with customer-managed options available_
    * Encryption occurs before data is sent to Cloud Storage and BigQuery (client-side) or after it arrives (server-side)

* **Data Integrity**
    * Google Cloud Storage supports CRC32C and MD5 hashes for data integrity
    * Server-side encryption provides protection against corruption

* **Encryption Key Management**
    * Customer-managed keys can be used with Google Cloud Key Management Service

---

*Encryption at Rest*
Server‐Side Encryption | Client‐Side Encryption
---|---
Encryption that occurs after the cloud storage receives your data, but before the data is written to disk and stored. | Encryption that occurs before data is sent to Cloud Storage and BigQuery. Such data arrives at Cloud Storage and BigQuery already encrypted but also undergoes server‐side encryption.
You can create and manage your encryption keys using a Google Cloud Key Management Service. |  You are responsible for the client‐side keys and cryptographic operations.

<!-- _class: centered -->

---

### 12.1.2. Encryption in Transit

* **Security Protocol**: Google Cloud uses *Transport Layer Security (TLS)* to protect data in transit.
* *Data Encryption*: TLS ensures encrypted data exchange between devices and Google Cloud services.
* *Secure Communication*: TLS protocol provides secure communication channels for sensitive data.

---

### 12.1.3. Encryption in Use

* *_Encryption in Use_* 
    * Protects data in memory from compromise or exfiltration
    * Example: Confidential Computing encrypts data while processing
    * Available through Confidential VMs and GKE Nodes

---

## 12.2. Identity and Access Management

* _Identity and Access Management (IAM) in Google Cloud is used to manage access to data and resources, including Vertex AI._
  * *_Project-level roles_* : Assign one or more roles to a principal (user, group, or service account) for access to project resources.
  * *_Resource-level roles_* : Set an IAM policy on a specific resource for granular permissions control.

* Note: Only resource-level policies are supported for Vertex AI Feature Store and entity type resources. Project-level policies take precedence over resource-level policies.

---

### 12.2.1. IAM Permissions for Vertex AI Workbench

* **Vertex AI Workbench**: Data science service leveraging JupyterLab to explore and access data, with encryption at rest and in transit provided by Google.
  * Provides two types of notebooks: user-managed and managed
    + User-managed notebooks are highly customizable but require more setup and management
      * Can use tags to control instances
* **Access Modes**: 
  * Single User Only
  * Service Account, which requires a service account key with proper permissions
    + Creating a service account key is a security risk, should be avoided if possible

---

### 12.2.2. Securing a Network with Vertex AI

* **Google Cloud Shared Responsibility Model**: 
    * The cloud provider monitors security threats, while end users protect their data and assets.
* **Shared Fate Model**:
    * An ongoing partnership between the cloud provider and customer to improve security.
    * Includes components such as secure blueprints, risk protection programs, and assured workloads.

* _Key Takeaways_
  * Secure your data with Google Cloud's shared responsibility model and shared fate model.
  * Learn how to secure Vertex AI Workbench notebook environment, endpoints, and training jobs.

---

#### 12.2.2.1. Securing Vertex AI Workbench

* **Security Best Practices**
  * Use a private IP address for your Vertex AI Workbench to reduce attack surface and expose sensitive data.
    * _Specify the `‐‐no‐public‐ip` command when creating a workbench._
* Connect your instance to a VPC network in the same project to use internal IP addresses instead of external IP addresses.
* Use VPC Service Controls to control access to specific services, protect training data and models from leaving your service perimeter.

---

#### 12.2.2.2. Securing Vertex AI Endpoints

### Public vs Private Endpoints in Vertex AI
* _Public Endpoints_: publicly accessible to the Internet
  * Available by default when creating an endpoint with Vertex AI
  * Data traverses public Internet, increasing latency and security concerns
* _Private Endpoints_: secure connection to endpoint without data on public Internet
  * Set up through VPC Peering for increased security and lower latency

### Setting Up Private Endpoints
* Create private endpoint in the Vertex AI console
  * Go to Endpoint > Create Endpoint > Select Private
* Configure VPC Network Peering for low-latency connection

### Vertex AI Matching Engine
* High-scale, low-latency vector database

---

  * Refers to semantic similarity matching or approximate nearest neighbor (ANN) service

---
#### 12.2.2.3. Securing Vertex AI Training Jobs

**Using Private IP Addresses for Vertex AI Training**
* Connects training jobs to Google Cloud or on-premises networks using VPC peering
* Provides network security and lower latency compared to public IP addresses
* Allows access to private IP addresses for training code execution

**Network Security and Defense**
* Use VPC Service Controls and IAM for defense in depth
* Prevents service operations from copying data to public buckets or external tables

---

#### 12.2.2.4. Federated Learning

* **Federated Learning**: enables mobile devices or organizations to collaboratively learn a shared prediction model while keeping training data on-device.
* *Key Benefits*: 
  * Smarter models
  * Lower latency
  * Less power consumption
  * Ensures privacy and security of training data
* *Example*: hospitals train shared ML models with patient data remaining on-device, only updating the centralized cloud server with model updates.

---

#### 12.2.2.5. Differential Privacy

* **Differential Privacy**: _system for sharing dataset information while hiding individual identities_
    * Enables training machine learning models on private data without memorizing sensitive info
    * Measures the degree of privacy protection provided by an algorithm
        * Allows responsible training of models on private data using techniques like Federated Learning

---

#### 12.2.2.6. Format‐Preserving Encryption and Tokenization

**Format-Preserving Encryption (FPE)**

* _Preserves data format during encryption_
* Used for secure storage and transmission of sensitive data
    * Examples: payment card verification, legacy database systems
    * _Key difference from tokenization_: obfuscates sensitive information, while tokenization removes it entirely

---

## 12.3. Privacy Implications of Data Usage and Collection

* **Data Sensitive Topics**
	* _personally identifiable information (PII)_: data allowing an individual to be identified
	* _protected health information (PHI)_: sensitive medical data with federal protections under HIPAA

---

### 12.3.1. Google Cloud Data Loss Prevention

* **De-identification with Google Cloud DLP**: removes identifying information from text content, including PII
    * _Masking_: replaces characters with symbols or tokens
    * _Replacing_: replaces sensitive data with a token using cryptographic hashing
    * _Encrypting_: encrypts and replaces sensitive data with a randomly generated key
* **Key Concepts**:
  * *_Data Profiling_*: identifies sensitive data across the organization
  * *_Risk Analysis_*: determines an effective de-identification strategy or monitors for changes/outliers
  * *_Inspection (Jobs and Triggers)_*: scans content for sensitive data, schedules jobs to run

---

### 12.3.2. Google Cloud Healthcare API for PHI Identification

* _HIPAA_ requires special care for PHI linked to 18 identifiers, such as name or SSN.
* Google Cloud Healthcare API's de-identification removes PHI from various data types.
    * _Configurable_ and covers text, images, FHIR, and DICOM data.
* De-identified health information is not protected under HIPAA Privacy Rule.

---

### 12.3.3. Best Practices for Removing Sensitive Data

* **Sensitive Data Handling**: Removing sensitive data requires different approaches depending on its structure and type.

  * *Structured datasets*: Create a view that restricts access to columns in question.
  * *Unstructured content*: Use Cloud DLP or NLP API with regex to identify patterns.
  * *Images, videos, audio, etc.*: Use APIs like Cloud Speech API and Vision AI to detect sensitive data.

* **Data Coarsening Techniques**: 
  * *IP addresses*: Zero out the last octet of IPv4 addresses.
  * *Numeric quantities*: Bin numbers to reduce individual identification.
  * *Zip codes*: Coarsen to include just the first three digits.

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

* *_Security Best Practices for Machine Learning_*: encryption at rest, encryption in transit, IAM access management
* *_Secure ML Development Techniques_*: federated learning, differential privacy
* *_PII and PHI Data Management_*: Cloud DLP, Cloud Healthcare APIs, scalable architecture pattern

---

## 12.5. Exam Essentials

* **Secure ML Systems**
  * Understand encryption at rest and in transit for Google Cloud Storage and BigQuery
  * Set up IAM roles for Vertex AI Workbench management and network security
  * Learn about differential privacy, federated learning, and tokenization concepts
* _Understanding Data Privacy Implications_
  * Identify and mask PII type data with the Google Cloud DLP API
  * Mask PHI type data using the Google Cloud Healthcare API
  * Apply best practices for removing sensitive data

---

# 13. Chapter 7Model Building

---

## 13.1. Choice of Framework and Model Parallelism

* **Distributed Training**: Large deep learning models require massive datasets and rapid training times
* **Multinode Training**: Using multiple nodes for training is necessary to achieve fast training speeds
    * _Data Parallelism_ and _Model Parallelism_ are used to distribute the workload across nodes

---

### 13.1.1. Data Parallelism

* _Data parallelism_ involves splitting data across multiple GPUs or nodes, allowing for concurrent processing.
* The same parameters are used for forward propagation on every node, and gradients are computed and sent back to the main node.
* **Two key strategies**:
  * *_Synchronous_*: all nodes wait for each other's updates
  * *_Asynchronous_*: nodes update independently

---

#### 13.1.1.1. Synchronous Training

* **Synchronous Training**: Model sends parts of data to each GPU or accelerator, where each GPU trains on a separate part of the data.
* _**All-Reduce Algorithm Used**:_ Each GPU computes output and gradient simultaneously, then collects trainable parameters from all GPUs via an all-reduce algorithm.

---

#### 13.1.1.2. Asynchronous Training

* _Asynchronous Training_: allows workers to train independently, reducing idle time
    * enables independent training over input data and updating variables asynchronously
    * improves scalability compared to synchronous training
* **All-Reduce Sync**: suitable for Tensor Processing Unit (TPU) and one-machine multi-GPUs

---

### 13.1.2. Model Parallelism

* **Model Parallelism**: Models are partitioned and placed on individual GPUs, allowing training of large models that don't fit in a single GPU.
    * Splitting the model across multiple GPUs can overcome memory limitations and improve accuracy.
    * _tf.distribute.Strategy_ API is used to distribute training across multiple GPUs or machines.

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

* **Feedforward Neural Networks**: One-hidden layer type of ANN, primarily used for *_supervised learning_* in numerical and structured data, like *_regression problems_*.

---

### 13.2.2. Deep Neural Network (DNN)

* **Definition**: *Deep neural networks (DNNs) are ANNs with multiple hidden layers between input and output layers.* 
* **Qualification**: A DNN typically has at least two hidden layers, making it a _deep net_.

---

### 13.2.3. Convolutional Neural Network

* **Convolutional Neural Networks (CNNs)**: Designed for image input and best suited for *_image classification tasks_*.
* *Can also be applied to:* Various other tasks that involve image processing and analysis.
* *Not limited to:* Classification tasks only, but are a key component in many computer vision applications.

---

### 13.2.4. Recurrent Neural Network

* **Recurrent Neural Networks (RNNs)**: designed for sequences of data, effective for natural language processing and time-series forecasting
    * Use long short-term memory (LSTM) networks for predictions, such as class labels or numerical values
    * _Key application areas_: text analysis, speech recognition, and time-series forecasting
* **Training Neural Networks**: stochastic gradient descent with a chosen loss function
    * _Goal of training_: find weights and biases with low average loss across all examples
    * Loss is prediction error, calculated using a loss function to update weights and biases

---

### 13.2.5. What Loss Function to Use

* The choice of loss function is directly related to the activation function used in the output layer.
* Different ML problems require different loss functions:
  * Regression: Mean Squared Error (MSE)
  * Binary classification: Binary cross-entropy
    * Categorical hinge loss and squared hinge loss (Keras)
  * Multiclass classification:
    * Softmax activation, categorical cross-entropy on one-hot encoded data
    * Sparse categorical cross-entropy on integer encoded data

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

* **Gradient Descent Algorithm**: calculates the gradient of the loss curve
    * _Gradients point in the direction of the steepest increase_
    * **Steepness is minimized by taking a step in the negative gradient**

---

### 13.2.7. Learning Rate

* **Gradient Descent Update**: 
    * The gradient vector guides the update direction.
    * Learning rate (step size) scales the gradient magnitude to determine the step size.
        * Example: `learning_rate * gradient_magnitude`

---

### 13.2.8. Batch

* *Batch size* refers to the number of examples used for one iteration
    * Using a larger batch can lead to longer computation times
        * In practice, using the **entire dataset** as a batch is often impractical and unnecessary

---

### 13.2.9. Batch Size

* _Batch Size_ refers to the number of examples in a batch
* Typical batch sizes range from 10 to 1,000 for mini-batches
* Batch size remains constant during **training** and **inference**, but TensorFlow allows **dynamic batch sizes**.

---

### 13.2.10. Epoch

* **Epoch**: 
  * Iteration for training neural networks
  * Use all training data exactly once
  * Forward pass + Backward pass count as one pass
* 
  * Made up of one or more **_batches_**

---

### 13.2.11. Hyperparameters

* **Hyperparameters in ML Model Training**
    * Adjusting hyperparameters like loss, learning rate, and batch size can significantly impact training time
    * Choosing the right learning rate is crucial, as it affects how quickly the model learns *_i.e., convergence speed_*
        + Too small: slow convergence
        + Too large: potential for overshooting or unstable learning

---

#### 13.2.11.1. Tuning Batch Size

* **Batch Size Tuning**: 
  * Smaller mini-batch sizes generally improve accuracy and stability.
  * Optimal batch size balances training speed and accuracy, avoiding overfitting or underfitting.
    * * Too small: unstable training; too large: slow training with high risk of memory errors.

---

#### 13.2.11.2. Tuning Learning Rate

* _A desirable learning rate minimizes wasted time and resources_
* A balanced learning rate avoids overfitting or underfitting
* _Incorrect rates lead to increased cloud GPU costs and reduced model accuracy_

---

## 13.3. Transfer Learning

* **Transfer Learning**: Saving knowledge from one problem to apply to another related problem
*   _**Technique:**_ Using a pre-trained neural network as a starting point, or transferring layers from a trained model to a new model.
*   *Enables faster training and better performance, even with limited data.*

---

## 13.4. Semi‐supervised Learning

* **Semi-supervised Learning**: Combines small amounts of labeled data with large amounts of unlabeled data for machine learning
    * Involves a mix of labeled and unlabeled examples during training
    * Falls between supervised and unsupervised learning approaches

---

### 13.4.1. When You Need Semi‐supervised Learning

* **Semi-Supervised Learning**: Increases model accuracy by adding labeled data when enough labeled data is not available.
    * _Useful for situations with limited labeled data_, such as fraud detection or anomaly detection, where some instances are known but others are not.
        * _Can be applied to various domains_ such as speech recognition and web content classification.

---

### 13.4.2. Limitations of SSL

* _Semi-supervised learning_ uses a minimal amount of labeled and plenty of unlabeled data for classification tasks
* Its success depends on the representativeness of the labeled data to the entire distribution
* Inaccurate results can occur if the labeled data is not representative

---

## 13.5. Data Augmentation

* **Data Augmentation**: * _Neural networks need large amounts of data examples for good performance_*
* **Data Generation Techniques**:
  * Offline augmentation: modifying existing data with techniques like flips, translations, or rotations
  * Online augmentation: applying data augmentation during training to increase relevant data

---

### 13.5.1. Offline Augmentation

* *_Offline Augmentation_*: transforms data before training
    * increases dataset size by factor equal to number of transformations
        * e.g., rotation increases dataset size by 2x

---

### 13.5.2. Online Augmentation

* **Online Augmentation**: performing data augmentation transformations on mini-batches before feeding them to machine learning models.
* Data augmentation techniques for images:
    * *_Flip_*
    * *_Rotate_*
    * *_Scale_*
    * *_Gaussian Noise_*
    * *_Translate_*

---

## 13.6. Model Generalization and Strategies to Handle Overfitting and Underfitting

* *_Understanding Model Performance_*
  * **Bias:** High bias means high error rate in training data, paying little attention to data.
  * *_High Variance:_* High variance means low performance on test data, overfitting to training data.

*_The Challenge of Generalization_*

 A model with too little capacity cannot learn, and a model with too much capacity can overfit.

---

### 13.6.1. Bias Variance Trade‐Off

* _Key trade-off in complexity_: high bias vs low variance
    * **Model simplicity**: few parameters (high bias, low variance)
    * **Overfitting and underfitting_*
        *_Underfitting_*: increase model capacity (weights), 
        *_Overfitting_*: use specialized techniques

---

### 13.6.2. Underfitting

* **Underfit Model**: _Fails to learn problem, poor performance on datasets_
    * High bias, low variance
    * Reasons:
        * Poorly cleaned training data
        * High bias in model
    * Solutions:
        * Increase complexity
        * Remove noise from data
        * Increase epochs or duration of training

---

### 13.6.3. Overfitting

**Overfitting**
* _Definition:_ Model learns training data too well, performing poorly on new examples or with added noise.
* Two approaches to address:
	+ Increase training examples
	+ Change network complexity and parameters
* **Ways to avoid overfitting:**
  * Regularization techniques
  * Dropout
  * Noise addition
  * Early stopping
  * Data augmentation
  * Cross-validation

---

### 13.6.4. Regularization

* **Regularization** is used to prevent overfitting by reducing fluctuation of coefficients
* L1 and L2 regularization methods are used, with L1 for feature selection and L2 for stable models
    * L1 regularization reduces features, while L2 regularization keeps weights small but not zero
    * L1 is robust to outliers, but L2 is not

* **Common issues in neural networks**:
  * _Exploding gradients_: large weights cause gradients to become too large; batch normalization and lower learning rate can help
  * _Dead ReLU units_: once a unit outputs 0, it can get stuck and gradients cannot flow through; lowering learning rate can help

---

  * _Vanishing gradients_: gradients for lower layers become very small; using ReLU activation function can help

* **Techniques to reduce training loss**:
  * Increase depth and width of neural network
  * Decrease learning rate
    * Using dropout regularization: randomly dropping out unit activations

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

* **Training Neural Networks**: Overview of key concepts including loss function, gradient descent, learning rate, batch size, epoch, and hyperparameters.
    * _Hyperparameter Tuning_: Importance of adjusting hyperparameters such as learning rate and epoch to optimize network performance.
    * _Transfer Learning and Semi-Supervised Learning_: Strategies for using transfer learning and understanding the limitations of semi-supervised learning.

---

## 13.8. Exam Essentials

* **Training Strategies**
    * _Model parallelism_: Split large neural networks across multiple nodes for efficient computation
    * Data parallelism: Train on multiple GPUs or machines in parallel using data replication
    * Distributed training of TensorFlow models: Use TensorFlow's distributed training features

* **Hyperparameter Tuning and Optimization**
    * _Loss functions_: Choose between sparse cross-entropy and categorical cross-entropy depending on task type
    * Gradient descent, learning rate, batch size, and epoch: Understand the role of each hyperparameter in model performance
    * Regularization techniques (L1, L2): Apply to prevent overfitting

* **Transfer Learning**

---

    * _Pretrained models_: Leverage pre-trained models for limited data scenarios with high accuracy

* **Additional Techniques**
    * Data augmentation: Apply techniques like flipping, rotation, and GANs to increase dataset size
    * Semi-supervised learning (SSL): Use when labeled data is scarce, but unlabeled data is abundant

---
# 14. Chapter 8Model Training and Hyperparameter Tuning

---

## 14.1. Ingestion of Various File Types into Training

* **Data Types**: Structured (e.g., databases), semi-structured (e.g., PDFs), and unstructured (e.g., chats, emails)
* **Data Sources**: Batch data, real-time streaming data (e.g., IoT sensors)
* **Data Volumes**: Small (< few megabytes) to petabyte scale

---

### 14.1.1. Collect

* **Google Cloud Services for Batch and Streaming Data**
  * Pub/Sub and Pub/Sub Lite for real-time streaming
    + Serverless scalable messaging service with global reach
    + Integrates with Dataflow, BigQuery, and analytics services
  * Datastream for migrating on-premises databases to Google Cloud
    + Change data capture and replication service for heterogeneous databases
    + Supports Oracle and MySQL databases into Cloud Storage
  * BigQuery Data Transfer Service for loading external data
    + Loads from Teradata, Amazon Redshift, and cloud storage providers

---

### 14.1.2. Process

* *_Data Preprocessing Tools_* 
  * **Data cleaning and handling**
  * **Feature engineering**
  * **Data transformation**

---

#### 14.1.2.1. Cloud Dataflow

* **Cloud Dataflow**: A serverless, fully managed data processing service for streaming and batch data
    * _Applies exactly-once streaming semantics_, ensuring each message is processed exactly once.
    * Enables building and monitoring data processing pipelines with improved performance over MapReduce.

---

#### 14.1.2.2. Cloud Data Fusion

* _Cloud Data Fusion_ 
    * A UI-based ETL (Extract, Transform, Load) tool
    * No code implementation required

---

#### 14.1.2.3. Cloud Dataproc

**Dataproc Overview**

* A fully managed service for running Apache Spark, Flink, Presto, and 30+ open-source tools
* Allows use of open-source data tools for batch processing, querying, streaming, and machine learning
* Provides automated cluster creation, management, and cost savings

**Integration with Google Cloud Platform Services**

* Integrates with BigQuery, Cloud Storage, Cloud Bigtable, Cloud Logging, and Cloud Monitoring
* Enables effortless ETL of raw log data into BigQuery for business reporting

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

* *_Cloud Composer_* is a managed workflow orchestration service that simplifies creating, running, and managing workflows with minimal management overhead
    * _Supports hybrid and multicloud architecture_ for on-premises, multiple clouds, or Google Cloud-only deployments
    * _Provides end-to-end integration_ with Google Cloud products like BigQuery and Dataflow

---

#### 14.1.2.5. Cloud Dataprep

* **Cloud Dataprep**: _UI-based ETL tool for visual exploration, cleaning, and preparing data for analysis and machine learning_
    * Prepares data for any scale
    * Covers structured and unstructured data

---

#### 14.1.2.6. Summary of Processing Tools

* *_GCP Processing Tools_* 
    * **Data Ingestion**: Cloud Pub/Sub, Cloud Storage
    * **Data Transformation**: Cloud Data Fusion, Cloud Transformations
    * **Data Analysis**: BigQuery, Cloud Dataproc
    * **Machine Learning**: AutoML, AI Platform

---

### 14.1.3. Store and Analyze

* **Data Storage Guidance**
  - *_Table Type_* | *_Google Cloud Product_*
  - Tabular data | BigQuery, BigQuery ML
  - Image/video/audio & unstructured data | Google Cloud Storage
  - Unstructured data | Vertex Data Labeling
  - Structured data | Vertex AI Feature Store

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
  * A Jupyter Notebook-based environment for data science workflows
  * Interacts with Vertex AI and other Google Cloud services
  * Two types of notebooks: Managed and User-managed
    * _Managed notebook_: Automated shutdown, UI integration with Cloud Storage and BigQuery, automated notebook runs, custom containers, and frameworks preinstalled.
    * _User-managed notebook_: More control and fewer features compared to managed notebooks.

---

*Developing Models in Vertex AI Workbench by Using Common Frameworks*
Managed notebook | User‐managed notebook
---|---
**Automated shutdown for idle instances:** Choosing a managed notebook will shut down your Jupyter Notebooks when not in use. This feature helps save costs because the instances will shut down when not in use automatically. | **Automated shutdown for idle instances:** This feature is not supported out of the box. However, you can create a monitor to see when instances are idle using Cloud Monitoring and Cloud Functions and shut them down when not in use.
**UI integration with Cloud Storage and BigQuery:** From within JupyterLab's navigation menu on a managed notebooks instance, you can use the Cloud Storage and BigQuery integration to browse data and other files that you have access to and load data into your notebook. | **UI integration with Cloud Storage and BigQuery:** There is no UI integration. However, you can use the BigQuery connector to connect to BigQuery data using code or you can also use the BigQuery magic (`%%`) command to run BigQuery SQLl commands on a Jupyter Notebook.

<!-- _class: centered -->

---

### 14.2.1. Creating a Managed Notebook

### Creating a Managed Notebook in Vertex AI
Create a new notebook using the Workbench by enabling all APIs and clicking on New Notebook.

### Key Steps:

*   Click Create to create the notebook with default settings.
*   A monthly billing estimate is displayed for running the notebook.
*   Wait until the notebook is created, then click Open JupyterLab to access your environment.

---

### 14.2.2. Exploring Managed JupyterLab Features

* *JupyterLab Environment Features:*
  * _Existing notebooks for model building and training_
  * Serverless Spark feature for running Dataproc clusters
  * Terminal option for running terminal commands in notebooks

---

### 14.2.3. Data Integration

* Open the _Browse_ icon in the left navigation bar
* Load data from cloud storage folders using GCS
* Browse and select desired files or folders to integrate into a managed notebook

---

### 14.2.4. BigQuery Integration

* *_Access BigQuery data_* 
    * Click **BigQuery icon** to retrieve data from tables
    * Use _Open SQL editor_ option to query tables directly in JupyterLab

---

### 14.2.5. Ability to Scale the Compute Up or Down

* **Attach GPU**: Click on *_n1-standard-4_* to access a virtual machine with adjustable hardware and options to attach a GPU _without exiting the environment_.

---

### 14.2.6. Git Integration for Team Collaboration

* To integrate or clone a git repository, click on the left navigation branch icon
* Alternatively, use the terminal with the command `git clone <your‐repository name>` to clone your repository

---

### 14.2.7. Schedule or Execute a Notebook Code

* To execute a cell manually, click the triangle black arrow to run it.
    * To execute a cell automatically, click **Execute** 
        * This sends the code to be executed to Vertex AI without leaving the Jupyter interface.

---

### 14.2.8. Creating a User‐Managed Notebook

**Creating User-Managed Notebooks**

To create a user-managed notebook, choose a framework such as TensorFlow during creation.
 
* _Options_: Python 3, TensorFlow, R, JAX, Kaggle, PyTorch
* _Benefits_: Advanced options for networking with shared VPCs and automatic shutdown after training

You can access the notebook through Open JupyterLab and use tools like git integration and terminal access.

* _Note_: No need for large hardware or compute instance as training is done outside the environment using Vertex AI APIs/SDKs.

---

## 14.3. Training a Model as a Job in Different Environments

* *_Vertex AI Training Methods_* 
  * AutoML: Minimal technical effort for creating and training models
  * Custom training: Full control over model functionality and targeted outcome

---

### 14.3.1. Training Workflow with Vertex AI

* **Training in Vertex AI**: Training pipelines create AutoML or custom models, orchestrating hyperparameter tuning and model uploading.
    * _Supported frameworks_: PyTorch, TensorFlow, Scikit, XGBoost
    * _TensorFlow Hub_ option for optimized GCP deployment

---

### 14.3.2. Training Dataset Options in Vertex AI

### Training on Vertex AI
#### Dataset Options

* **No Managed Dataset**: Use data stored in Google Cloud Storage or BigQuery directly.
	+ _Direct access to data from Cloud Storage and BigQuery_
* **Managed Dataset**: Store and manage datasets in a central location for easier label creation, annotation, and governance.

#### Training Jobs
* Configure training jobs to mount remote files via NFS shares for high throughput and low latency.

---

### 14.3.3. Pre‐built Containers

* **Vertex AI Setup**: Organize code according to Vertex AI structure (_root folder with `setup.py` and `trainer/task.py`)
* **Training Pipeline**: Upload Python source distribution to Cloud Storage bucket, then use the `gcloud ai custom-jobs create` command to build a Docker image, push it to Container Registry, and create a custom job.
    * Specify:
        *_LOCATION_* (region)
        *_JOB_NAME_* (display name for CustomJob)
        *_MACHINE_TYPE_* (machine type for training)
        *_EXECUTOR_IMAGE_URI_* (prebuilt container image)

---

### 14.3.4. Custom Containers

* **Custom Containers for Vertex AI**
* 
    * _Use custom containers to run training applications with preferred ML frameworks and dependencies._
    * _Faster start-up time, extended support for distributed training, and use of the latest framework versions._
* 
    * _Steps to create a custom container:_
        1. Create a Dockerfile and push it to an Artifact Registry.
            ```dockerfile
FROM image:tag
WORKDIR /root

RUN pip install pkg1 pkg2 pkg3

COPY your-path-to/model.py /root/model.py
COPY your-path-to/task.py /root/task.py

ENTRYPOINT ["python", "task.py"]
```

        2. Build and run the Docker container.
            ```bash
docker build -f Dockerfile -t ${IMAGE_URI} .

---

docker run ${IMAGE_URI}
```
        
        3. Push the container image to Artifact Registry.
            ```bash
docker push ${IMAGE_URI}
```

---
### 14.3.5. Distributed Training

* _Distributed Training_ : Specify multiple machines in a training cluster to run a distributed training job with Vertex.
    * **Task Distribution**: Configure worker pools with specific tasks:
        * Primary: manages the others and reports status for the job
        * Secondary: performs replicas' work
        * Parameter servers and Reduction Server (optional): coordinates shared model state between workers
* _Reduced Training Performance_ : Use Reduction Server to increase throughput and reduce latency, especially with GPU workers.

---

*Distributed Training*
Position in workerPoolSpecs[] | Task Performed in Cluster
---|---
First (`workerPoolSpecs[0]`) | Primary, chief, scheduler, or “master.” Exactly ‐one replica is designated the _primary replica_. This task manages the others and reports status for the job as a whole.
Second (`workerPoolSpecs[1]`) | Secondary, replicas, workers.

<!-- _class: centered -->

---

## 14.4. Hyperparameter Tuning

* **Hyperparameters vs Model Parameters**: 
    * _Model parameters_ are learned during training, while _hyperparameters_ are set before training
* **Learning Rate Hyperparameter**
    * The learning rate must be chosen before training can begin
* **Importance of Choosing Hyperparameters**: Finding the right hyperparameters is crucial for effective model training

---

### 14.4.1. Why Hyperparameters Are Important

* **Hyperparameter Tuning**: Finding optimal hyperparameters for neural networks to maximize predictive accuracy.
  * _Automated algorithms_ use compute infrastructure to test different configurations and provide optimized values.
  * *_Search algorithms_*:
    * Grid search: Exhaustive search through a manually specified set of hyperparameters
    * Random search: Uses random combinations of parameters, considering the assumption that not all are equally important
    * Bayesian optimization (default Vertex AI algorithm): Takes into account past evaluations to choose the next hyperparameter set

---

### 14.4.2. Techniques to Speed Up Hyperparameter Optimization

* **Hyperparameter Optimization Techniques**
  * Use simple validation set instead of cross-validation for large datasets (factor ~k)
  * Parallelize on multiple machines using distributed training with hyperparameter optimization (factor ~n)
  * Pre-compute and cache redundant computations to avoid unnecessary re-running
  * Reduce number of hyperparameter values to consider in grid search for speedups

---

### 14.4.3. How Vertex AI Hyperparameter Tuning Works

* **Hyperparameter Tuning**: Runs multiple trials with adjusted hyperparameters to optimize target variables (hyperparameter metrics) and improve model performance.
* **Key Steps**:
    * Install `cloud-ml hypertune` package for custom container
    * Configure metric definitions and hyperparameter tuning code in Python
* **Creating a Custom Job**: 
    * Create YAML file with API fields for HyperparameterTuningJob
        * `studySpec`: defines metrics, parameters, and trial job specs
            - `metrics`: specifies hyperparameter metric to optimize
            - `parameters`: defines hyperparameter to tune with specified range

---

            - `trialJobSpec`: configures worker pool and container specs

---
### 14.4.4. Vertex AI Vizier

* **Vertex AI Vizier**: Black-box optimization service for complex ML models
    * _Tunes hyperparameters without a known objective function_
    * _Optimizes model parameters and works with any evaluable system_
    * _Useful for cost-sensitive tasks or when traditional evaluation methods are impractical_

---

#### 14.4.4.1. How Vertex AI Vizier Differs from Custom Training

* **Vertex AI Vizier**: Independent service for optimizing complex models with many parameters.
    * Supports both ML and non‐ML use cases, and can be used in training jobs or with other systems (including multicloud).
        *_Hyperparameter Tuning_*: Built-in feature that uses Bayesian optimization to determine the best hyperparameter settings for an ML model.

---

## 14.5. Tracking Metrics During Training

* **Tracking ML Model Metrics**: *Using tools like an interactive shell, TensorFlow Profiler, and What-If Tool*
 
  (No sub-points necessary)

---

### 14.5.1. Interactive Shell

* **Interactive Shell in Vertex AI**: 
    * An interactive shell is available for debugging and troubleshooting, running tracing and profiling tools.
    * Available while job is in RUNNING state, but access is lost after completion.

* **Vertex AI Logs and Metrics**:
    * View logs by clicking on the View logs link
    * Metrics are exported to Cloud Monitoring and shown in Vertex AI console

* **Tools for Tracking Training Metrics**: 
    * `_py-spy_`: visualizes Python execution time, analyzes performance with Perf
    * `nvidia-smi` and `nvprof`: monitors GPU usage

---

*Interactive Shell*
Visualize Python Execution with py‐spy | Retrieve Information about GPU Usage | Analyze Performance with Perf
---|---|---
py‐spy is a sampling profiler for Python programs. It lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way. | GPU‐enabled containers running on nodes with GPUs typically have several command‐line tools preinstalled that can help you monitor GPU usage. You can use `nvidia‐smi` to monitor GPU utilization of various processes or use `nvprof` to collect a variety of GPU profiling information. | Perf lets you analyze the performance of your training node. It's a way to do Linux profiling with performance counters.

<!-- _class: centered -->

---

### 14.5.2. TensorFlow Profiler

* **Vertex AI TensorBoard Profiler**: monitors and optimizes model training performance
    * _Helps pinpoint and fix performance bottlenecks to train models faster and cheaper_
    * Available from the custom jobs page or experiments page in the Google Cloud console
        * Only works when the training job is in the RUNNING state

---

### 14.5.3. What‐If Tool

* **What-If Tool**: Interactive dashboard for inspecting AI Platform Prediction models
    * Integrates with TensorBoard, Jupyter Notebooks, Colab notebooks, and JupyterHub
    * Preinstalled on Vertex AI Workbench user-managed notebooks and TensorFlow instances
*   _How to use_:
    1. Install `witwidget` library
    2. Configure `WitConfigBuilder`
    3. Pass config builder to `WitWidget`
    * Example code: 
        ```python
     PROJECT_ID = 'YOUR_PROJECT_ID'
     MODEL_NAME = 'YOUR_MODEL_NAME'
     VERSION_NAME = 'YOUR_VERSION_NAME'
     TARGET_FEATURE = 'mortgage_status'
     LABEL_VOCAB = ['denied', 'approved']

---

     config_builder = (WitConfigBuilder(test_examples.tolist(), features.columns.tolist() + ['mortgage_status'])
      .set_ai_platform_model(PROJECT_ID, MODEL_NAME, VERSION_NAME, adjust_prediction=adjust_prediction)
      .set_target_feature(TARGET_FEATURE)
      .set_label_vocab(LABEL_VOCAB)

     WitWidget(config_builder, height=800)
[/code]

---
## 14.6. Retraining/Redeployment Evaluation

* **Model Decay**: Machine learning models lose performance over time due to changing user behavior and training data
    * _Causes:_
        * *_Data Drift_*: Distribution shift in the data
        * *_Concept Drift_*: Change in the underlying relationships between variables

---

### 14.6.1. Data Drift

* **Data Drift**: A change in the statistical distribution of production data from baseline data used to train a model
*  *Causes:* Changes in input data, such as unit conversions (_e.g._ temperature from Fahrenheit to Celsius)
*  *Detection Methods:* Examine feature distribution, correlation between features, or check data schema over baseline

---

### 14.6.2. Concept Drift

* _Concept Drift_: Change in the statistical properties of the target variable over time
* Causes: Shifts in user behavior or opinions on a particular topic
* *Example*: Sentiment around specific topics changes as people's opinions evolve

---

### 14.6.3. When Should a Model Be Retrained?

* *_Retraining Strategies_* 
  * **Periodic Training**: Retrain based on a fixed interval (e.g., weekly, monthly, yearly) when training data updates.
  * **Performance-based Trigger**: Automatically trigger retraining when model performance falls below a set threshold.
  * *_Data Changes Trigger_*: Trigger build for model retraining upon data drift or changes in production.

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

* _Testing Machine Learning Systems_
* *_Types of Tests_*:
    * **Model Input Validation**: checking model output shape, output ranges, and loss convergence
    * **Data Integrity Checks**: verifying dataset assertions and ensuring no label leakage
    * **Unit Tests**: testing individual units of code to ensure they function as expected

---

### 14.7.1. Testing for Updates in API Calls

* **Testing API Updates**: Write a unit test to generate random input data and run a single step of gradient descent
    * Use this approach to test for runtime errors and functional correctness
    * _Avoid_ retraining the entire model, as it would be resource-intensive

---

### 14.7.2. Testing for Algorithmic Correctness

* To verify algorithmic correctness, train your model and check:
  * Loss decreases over iterations
  * Training loss approaches 0 without regularization
  * Specific subcomputations run as expected (e.g., CNN running once per input element)

---

## 14.8. Summary

* **File Ingestion**: File ingestion stages include collection, processing, storage, and analysis
    * Services used for each stage:
        * _Pub/Sub_ for real-time data collection
        * BigQuery Data Transfer Service and Datastream for migrating third-party sources and databases
    * Data transformation using services like Cloud Dataflow, Cloud Data Fusion, etc.

* **Model Training**: Training with Vertex AI supports popular frameworks such as scikit-learn, TensorFlow, PyTorch, XGBoost
    * _Prebuilt containers_ and custom containers can be used for training
    * Hyperparameter tuning using algorithms like Grid Search and Random Search

---

## 14.9. Exam Essentials

* **File Ingestion**: Understand how to ingest various file types into training, including structured, unstructured, and semi-structured files, using services like Pub/Sub, BigQuery Data Transfer Service, and Cloud Datastream.
  * Know how to collect real-time data with Pub/Sub Lite
  * Use Cloud Dataflow, Cloud Data Fusion, and other services for ETL transformations
* **Vertex AI Workbench**: Understand the feature differences between managed and user-managed notebooks, and when to use each.
  * Create notebooks using Vertex AI Workbench and understand their features
* **Model Training and Serving**:
  * Know how to unit test model training and serving data

---

  * Track metrics during training with Interactive shell, Tensorflow Profiler, and What-If tool
* **Hyperparameter Tuning**: Understand the different search algorithms (grid search, random search, Bayesian search) and when to use each.
  * Use custom jobs for hyperparameter tuning
  * Understand Vertex AI Vizier and its differences from setting up hyperparameter tuning

---
# 15. Chapter 9Model Explainability on Vertex AI

---

## 15.1. Model Explainability on Vertex AI

* **Model Explainability**: As model impact on business outcomes increases, so does the responsibility to explain predictions
* **Explainability Scope**: High-impact predictions (e.g., loan approvals, drug dosages) require detailed explanations for stakeholders
* *_Human-Explainable ML_* models are crucial for gaining trust and addressing stakeholder questions

---

### 15.1.1. Explainable AI

* **Explainability** measures the ability to understand internal mechanics of an ML or DL system.
    * _Global_ explainability aims for overall model transparency and comprehensiveness.
        - Increasing trust and adoption through transparent predictions
        - Improving business outcomes by understanding uncertainty
    * _Local_ explainability focuses on individual predictions, helping with debugging and improvement.

---

### 15.1.2. Interpretability and Explainability

* **Key Difference**: 
  * _Interpretability_ is about associating causes and effects
  * _Explainability_ is about justifying model results through its parameters

---

### 15.1.3. Feature Importance

* **Feature Importance**: Technique that assigns scores to features based on their contribution to model predictions
    * Helps reduce computational costs and infrastructure requirements by identifying non-contributing variables
    * Detects data leakage when target variable is included as a feature in training dataset

---

### 15.1.4. Vertex Explainable AI

* **Vertex Explainable AI** explains model outputs for classification and regression tasks, providing feature attribution.
* _Supported services include_:
  * AutoML image models
  * AutoML tabular models
  * Custom-trained TensorFlow models

---

#### 15.1.4.1. Feature Attribution

**Vertex AI Feature Attribution**

* **Method 1:** *Sampled Shapley* - assigns credit to each feature and considers different permutations, providing a sampling approximation of exact Shapley values.
* **Method 2:** *Integrated gradients* - calculates the gradient, informing which pixel has the strongest effect on the model's predicted class probabilities. Used for deep neural networks with image use cases.
* **Method 3:** *XRAI (eXplanation with Ranked Area Integrals)* - assesses overlapping regions of the image to create a saliency map, highlighting relevant regions and providing explanations in images.

**Supported Data Types:**

| Method | Supported Data Types |
| --- | --- |

---

| Sampled Shapley | Tabular, nondifferentiable models (e.g., ensembles of trees) |
| Integrated gradients | Image, tabular data |
| XRAI | Image data |

**Model Types and Use Cases:**

---
*Feature Attribution*
Method | Supported Data Types | Model Types | Use Case | Vertex AI–Equivalent Model
---|---|---|---|---
Sampled Shapley | Tabular | Nondifferentiable models (explained after the table), such as ensembles of trees and neural networks. | Classification and regression on tabular data | Custom‐trained models (any prediction container)

<!-- _class: centered -->

---

#### 15.1.4.2. Vertex AI Example–Based Explanations

* **Example-Based Explanations**: enable selective data labeling and are not limited to images
* *Can generate embeddings for images, text, and tables*
* _Currently in public preview, but useful to understand for Google Cloud's Explainable AI options_

---

### 15.1.5. Data Bias and Fairness

* **Bias in Data**: Data can be biased due to incomplete or misrepresented information, leading to skewed outcomes and unfair model treatment.
* **ML Fairness**: Ensures models do not discriminate against individuals based on characteristics like race, gender, disabilities, or orientation.
* 
    * _**Detection Methods**_: Utilize Explainable AI's feature attributions technique for tabular data, the `What‐If Tool` interactive dashboard, and the open source `Language Interpretability Tool` to detect bias and fairness in datasets.

---

### 15.1.6. ML Solution Readiness

* **Responsible AI**: refers to principles guiding AI development that prioritize fairness, transparency, and accountability
  * _Google's Responsible AI practices_ provide customers with materials on best practices for fair AI development.
  * Tools like `_Explainable AI` and `_Model cards` help inspect and understand AI models.

* **Model Governance**:
  * Provides guidelines and processes to implement company AI principles.
  * Ensures models are transparent, fair, and bias-free.

---

### 15.1.7. How to Set Up Explanations in the Vertex AI

* **Configuring Vertex Explainable AI for Custom-Trained Models**: Configure explanations for custom-trained models to create a model that supports Vertex Explainable AI.
    * _Use the Vertex AI API to configure explainable AI for custom-trained models._
    * *_Enable batch explanations by setting generateExplanation field to true._

* **Explaining Models using Vertex Explainable AI**
    * *_Send synchronous requests (online explanations) and asynchronous requests (batch explanations)._ _
    * *_Use local kernel explanations in User-Managed Vertex AI Workbench notebooks without deploying the model to Vertex AI._
    

---

* **Integrating Explainable AI SDK into Notebooks**: The Explainable AI SDK is preinstalled in user-managed notebook instances. Use it to save model artifacts and identify metadata for explanation requests.

---
## 15.2. Summary

* *_Explainable AI_*: Explainability vs. Interpretability, feature importance, data bias, fairness, ML solution readiness
    * Key Techniques:
        * Sampled Shapley
        * XRAI
        * Integrated Gradients
    * Focus on Vertex AI platform for explainable AI

---

## 15.3. Exam Essentials

* **Explainability**: Understanding why machine learning models make predictions, e.g., feature importance
* **Key Features**:
  * Sampled Shapley algorithm
  * Integrated Gradients
  * XRAI (eXplainable Reinforcement Algorithm for Image)
* _Supporting Explainability_: 
    * TensorFlow prediction container with Explainable AI SDK
    * Vertex AI AutoML tabular and image models

---

# 16. Chapter 10Scaling Models in Production

---

## 16.1. Scaling Prediction Service

* **Deploying a TensorFlow Model**: After training, save the model using `tf.saved_model.save()` and deploy it for sharing or serving.
    * *Saved models are self-contained, including trained parameters and computation.*
        * They can be used with TensorFlow Lite, TensorFlow.js, TensorFlow Serving, or TensorFlow Hub.

---

### 16.1.1. TensorFlow Serving

### TensorFlow Serving Overview
#### Key Features

* Hosts trained TensorFlow models as API endpoints through model servers
* Handles model serving and version management
* Supports loading models from different sources

#### Setup Steps

1. Install TensorFlow Serving with Docker
2. Train and save a model with TensorFlow
3. Serve the saved model using TensorFlow Serving

---

#### 16.1.1.1. Serving a Saved Model with TensorFlow Serving

* **REST API Requests**: 
    * The TensorFlow ModelServer accepts REST API requests using the following format: `POST http://host:port/<URI>:<VERB>`
    * Accepted VERBS are classify, regress, and predict
* **JSON Data Payload**: 
    * To call the `predict()` endpoint, a JSON data payload is required in the following format:
        ```json
{
  "signature_name": "serving_default",
  "instances": instances.tolist()
}
```
    * The `signature_name` specifies the input/output data type and should be passed as a string. 
* **Tensor Instance**: 
    * A tensor instance is an example of what you would pass in the `instances` field:
        ```json
{
  // List of 2 tensors each of [1, 2] shape

---

  "instances": [ [[1, 2]], [[3, 4]] ]
}
```
* **Predict Response**: 
    * The `predict()` response contains the following output(s):
        ```
outputs['class_ids'] tensor_info:
dtype: DT_INT64
shape: (-1, 1)
name: dnn/head/predictions/ExpandDims:0

outputs['classes'] tensor_info:
dtype: DT_STRING
shape: (-1, 1)
name: dnn/head/predictions/str_classes:0

outputs['logits'] tensor_info:
dtype: DT_FLOAT
shape: (-1, 3)
name: dnn/logits/BiasAdd:0

outputs['probabilities'] tensor_info:
dtype: DT_FLOAT
shape: (-1, 3)
name: dnn/head/predictions/probabilities:0
```
    * The response is a JSON object containing the predictions in the following format:
        ```json
{
  "predictions": [
  {

---

  "class_ids": [3],
  "probabilities": [2.0495e-7, 0.0243, 0.9756],
  "classes": ["2"],
  "logits": [-5.74621, 5.94074, 9.62958]
  }
  ]
}
```

---
## 16.2. Serving (Online, Batch, and Caching)

* *_Best Practices for Serving Strategy_*: Batch prediction and online prediction use different architectures
* *_Caching Strategies_*: Implement cache to reduce computation time and improve performance
* *_Key Considerations_*: Balance serving speed with model accuracy and stability

---

### 16.2.1. Real‐Time Static and Dynamic Reference Features

* *_Two types of input features:_*
    * **Static Reference Features**: values that do not change in real time, updated in batches.
    * **Dynamic Real‐Time Features**: computed on the fly, used for real-time predictions.
* *_Use cases:_*
  * Predicting price based on location or recommending similar products.
  * Predicting engine failure based on sensor data or recommending next news article.
* *_Storage and processing:_*
  * Static features: NoSQL databases like Firestore, big data warehouses.
  * Dynamic features: low-latency read/write databases like Cloud Bigtable, streaming pipelines.

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

* **Pre-computing predictions**: Store pre-computed predictions in a low-latency data store for online serving.
  * Benefits: Reduced latency, improved performance
  * Challenges: Limited to single entity or feature combinations, high cardinality may be challenging to handle
  * Hybrid approach: Precompute top N entities and use model directly for others

---

## 16.3. Google Cloud Serving Options

* **Prediction Methods**: 
  * Batch predictions
  * Online predictions (both for AutoML and custom models)
*

---

### 16.3.1. Online Predictions

* To deploy a real-time prediction endpoint, you can use models trained in Vertex AI using AutoML or custom models
    * Or import a model trained elsewhere (on-premise, another cloud, or local device)
        * Ensure model artifacts have correct filenames for import (e.g. `saved_model.pb`, `model.joblib`)
* To set up the endpoint:
  * Deploy the model resource
  * Make a prediction
  * Undeploy the model resource if not in use

---

#### 16.3.1.1. Deploying the Model

* **Deployment Options**: 
  * Deploy models using Vertex AI's Prediction endpoint with autoscaling for container resources.
  * Can deploy multiple models to a single endpoint or multiple endpoints for individual models.

---

#### 16.3.1.2. Make Predictions

* To run data through the endpoint, you must pre-process it according to the `task.py` model format.
    * Pre-processing requirements vary depending on the container used (prebuilt or custom).
        * For prebuilt containers (TensorFlow, scikit-learn, XGBoost), input must be formatted as JSON.
        * For custom containers, input must be formatted as JSON and may include additional parameters.

---

#### 16.3.1.3. A/B Testing of Different Versions of a Model

* **A/B Testing** is a method of comparing two versions of a machine learning model to see which one performs better.
    * It involves deploying two models to the same endpoint and gradually replacing one with the other.
    * This allows for smooth transitions without disrupting the application.

* _Vertex AI A/B testing capabilities_:
    * Not all features are available out-of-the-box, including controlling model traffic and experimentation tracking.
    * The Vertex AI model evaluation feature can be used to create an A/B testing setup in experimental release.

---

#### 16.3.1.4. Undeploy Endpoints

* **Deployments are costly**: Running endpoints incurs charges.
* **Undeploy for cost savings**: Undeploy endpoints when not in use to avoid unnecessary costs.
* *_Use `undeploy` function_*: Deploy the `list_models` Python code snippet to undeploy an endpoint.

---

#### 16.3.1.5. Send an Online Explanation Request

* **Requesting Online Explanations**: Send an online explanation request using the Vertex AI Python SDK.
    * Format similar to online prediction requests
    * Returns predictions and feature attributions 
    * Example code provided

---

### 16.3.2. Batch Predictions

### Batch Prediction

Batch prediction involves:
* Pointing to the model and input data in Google Cloud Storage
* Running a job that predicts using the model on the input data
* Saving the output in Cloud Storage

Format input data according to AutoML or custom model requirements:
* JSON Lines
* TFRecord files
* CSV files
* File list
* BigQuery table

Create batch prediction job through Vertex AI APIs or Google Cloud console.

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

* **MLflow Overview**
  * An open-source platform for managing the end-to-end machine learning life cycle
  * Library agnostic, compatible with various machine learning libraries and programming languages
  * Tackles four primary functions: tracking, projects, models, and model registry
* **Hosting on Google Cloud**
  * Leverage scalability and availability of Google Cloud Vertex AI platform for model training and hosting
  * Access to high-performance compute resources (GPUs, TPUs, CPUs)
  * Can run MLflow using a Google Cloud plug-in without installing the Docker image

---

## 16.5. Testing for Target Performance

* **Testing for Model Performance**
  * Monitor training-serving skew and test with real-time data
  * Check model age and performance throughout the pipeline
  * Test numerically stable weights and outputs (e.g., no NaN or null values)
  
* _Automated Testing Solutions_
  * Vertex AI Model Monitoring and Feature Store can detect skew and monitor performance over time.

---

## 16.6. Configuring Triggers and Pipeline Schedules

* **Triggering Training or Prediction Jobs on Vertex AI**
    * Cloud Scheduler can set up a cron job schedule to trigger jobs.
    * Managed Notebooks allow execution and scheduling of training and prediction jobs using Jupyter Notebook.
    * Cloud Build, Cloud Run, event-driven Cloud Functions, and Pub/Sub are also used for triggering and scheduling jobs.

---

*Configuring Triggers and Pipeline Schedules*
Option | Description
---|---
Vertex AI Pipelines | Vertex AI Pipelines helps you to automate, monitor, and govern your ML systems by orchestrating your ML workflow in a serverless manner and storing your workflow's artifacts using Vertex ML Metadata. By storing the artifacts of your ML workflow in Vertex ML Metadata, you can analyze the lineage of your workflow's artifact.
Cloud Composer | Cloud Composer is designed to orchestrate data‐driven workflows (particularly ETL/ELT). It's built on the Apache Airflow project, but Cloud Composer is fully managed. Cloud Composer supports your pipelines wherever they are, including on‐premises or across multiple cloud platforms. All logic in Cloud Composer, including tasks and scheduling, is expressed in Python as directed acyclic graph (DAG) definition files.

<!-- _class: centered -->

---

## 16.7. Summary

* **TF Serving Overview**
  * Covered details of TF Serving for scaling prediction services
  * Discussed output based on `SignatureDef` of saved TF models
* **Online Serving Architecture**
  * Static and dynamic reference architectures
  * Pre-computing and caching while serving predictions
* **Model Deployment and Monitoring**
  * Online and batch mode deployment options
  * Tools for testing model performance, such as Vertex AI Model Monitoring

---

## 16.8. Exam Essentials

* **TensorFlow Serving Overview**
    * *A framework for serving machine learning models.*
    * *Deploy a trained TensorFlow model using TF Serving and set up various deployment options.*

* **Scaling Prediction Services**
    * *Online batch and caching strategies to improve serving latency.*
    * *Understand differences in architecture and use cases with real-time input features.*

* **Google Cloud Serving Options**
    * *Setup real-time endpoints, batch jobs, and automate pipeline workflows.*
    * *Use Google Cloud Vertex AI APIs, console setup, and managed notebooks for custom models.*

* **Model Performance and Optimization**

---

    * *Understand why model performance degrades in production.*
    * *Use Vertex AI services for model monitoring and optimization.*

* **Configure Triggers and Pipelines**
    * *Set up triggers to invoke trained models or deploy new ones on Google Cloud.*
    * *Automate pipeline workflows with Cloud Scheduler, Workflows, and Cloud Composer.

---
# 17. Chapter 11Designing ML Training Pipelines

---

## 17.1. Orchestration Frameworks

* *_ML Pipeline Orchestration_*: A process that manages steps like data cleaning, transformation, and model training to automate the machine learning (ML) workflow.
  * *_Benefits_*:
    * **Development Phase**: Automates manual execution of ML experiment steps
    * **Production Phase**: Automates pipeline execution based on schedule or conditions

---

### 17.1.1. Kubeflow Pipelines

### Overview of Kubeflow Pipelines
Kubeflow Pipelines is a platform for building, deploying, and managing multistep ML workflows based on Docker containers.
* _Key Components:_ 
  * User interface for managing experiments, jobs, and runs
  * Engine for scheduling multistep ML workflows
  * SDK for defining and manipulating pipelines and components
* _Deployment Options:_ 
  * Google Cloud on GKE or managed Vertex AI Pipelines
  * On-premises or local systems for testing

---

### 17.1.2. Vertex AI Pipelines

* **Vertex AI Pipelines**: automatically provisions and manages infrastructure for Kubeflow or TFX pipelines
    * Run serverless on Vertex AI Pipelines with existing code
    * Provides data lineage and artifact metadata for pipeline runs
* **Pipeline Components**: self-contained sets of code that perform one part of a workflow, such as data preprocessing or training a model
    * Can build custom components or reuse pre-built ones
    * Use Google Cloud pipeline components for features like AutoML

---

### 17.1.3. Apache Airflow

* **Apache Airflow**: open source workflow management platform for data engineering pipelines
    * Started as Airbnb's solution in 2014 for complex workflows
        *_Features_*:
            * Directed acyclic graph (DAG) to represent workflows
            * Tasks with dependencies and data flows

---

### 17.1.4. Cloud Composer

* *_Cloud Composer_* 
  * A fully managed workflow orchestration service built on Apache Airflow
  * No installation or management overhead, allows for fast environment creation and use of Airflow-native tools

---

### 17.1.5. Comparison of Tools

* *_Orchestrator Comparison_* 
    * *Service*: 
        + **Kubeflow Pipelines**: Orchestrate ML workflows with TensorFlow, PyTorch, MXNet using Kubernetes.
        + **Vertex AI Pipelines**: Managed serverless pipeline for Kubeflow Pipelines or TFX Pipeline, no infrastructure management needed.
        + **Cloud Composer**: Orchestrates ETL/ELT pipelines using Apache Airflow, Python-based implementation.
    * *_Failure Handling_* 
        + Kubeflow: Handle failures manually with metrics
        + Vertex AI Pipelines: Leverage Kubeflow failure management on metrics
        + Cloud Composer: Built-in GCP metrics for action on failure or success

---

*Comparison of Tools*
****|  Kubeflow Pipelines | Vertex AI Pipelines | Cloud Composer
---|---|---|---
**Management and support for frameworks** | Kubeflow Pipelines is used to orchestrate ML workflows in any supported framework such as TensorFlow, PyTorch, or MXNet using Kubernetes.
It can be set up on‐premises or in any cloud. | Managed serverless pipeline to orchestrate either Kubeflow Pipelines or TFX Pipeline. No need to manage the infrastructure. | Managed way to orchestrate ETL/ELT pipelines using Apache Airflow. It's a Python‐based implementation.

<!-- _class: centered -->

---

## 17.2. Identification of Components, Parameters, Triggers, and Compute Needs

* _Triggers_ can be set to automate retraining of ML models with new data, on:
	+ Availability of new data
	+ Model performance degradation
	+ Significant changes in statistical properties of the data
* Triggering a pipeline can result in two possible scenarios:
	+ Executing a continuous training (CT) pipeline without deploying new pipelines or components
	+ Deploying a new pipeline and serving a newly trained model

---

### 17.2.1. Schedule the Workflows with Kubeflow Pipelines

**CI/CD with Kubeflow Pipelines**

* Use Kubeflow Pipelines SDK to operate pipelines programmatically
    * Invoke pipelines using services such as Cloud Scheduler, Pub/Sub, and Cloud Functions
        + Schedule on a timeline or respond to events
    * Alternative build systems: Jenkins, Apache Airflow
        + Jenkins available on Google Cloud Marketplace

---

### 17.2.2. Schedule Vertex AI Pipelines

* *Scheduling with Cloud Scheduler*: 
  - upload compiled pipeline JSON to Cloud Storage
  - create Cloud Function and schedule job
* *Scheduling with Cloud Pub/Sub*:
  - specify Pub/Sub trigger in Cloud Function
  - define Pub/Sub topic for function call

---

## 17.3. System Design with Kubeflow/TFX

* **System Design Overview**
    * Kubeflow DSL: a declarative way to define workflows
    * TFX: a more structured approach to system design using a pipeline model

---

### 17.3.1. System Design with Kubeflow DSL

* **Kubeflow Pipelines Overview**
    * Uses Argo Workflows by default
    * Exposes a Python domain-specific language (DSL) for authoring pipelines
* **Creating a Pipeline**
  * Create container as simple Python function or Docker container
  * Define operation referencing container, command-line arguments, data mounts, and variables
  * Sequence operations defining parallelism and dependencies

---

#### 17.3.1.1. Kubeflow Pipelines Components

* **Component Ops**: To invoke a component in the pipeline, create a _component op_ using one of three methods:
    * Lightweight Python component
    * Reusable component with `component.yaml` file
    * Predefined Google Cloud components
* **Auto-Generated Components**: Component specs are automatically created from `component.yaml` files using `ComponentStore.load_components`
* **Predefined Services**: Kubeflow Pipelines provides managed services like BigQuery, Dataflow, and AI platform through predefined components

---

### 17.3.2. System Design with TFX

* **TFX**: A Google production-scale machine learning platform based on TensorFlow, providing a configuration framework and shared libraries for building and managing ML workflows.
  * Orchestrates ML workflows on several platforms (Apache Airflow, Apache Beam, Kubeflow Pipelines)
  * Provides components and libraries for pipelines
* TFX Pipeline Components:
  * ExampleGen: ingests and splits input dataset
  * Trainer: trains the model
  * Evaluator: validates training results and ensures models are "good enough"
* **Orchestration**: TFX pipelines can be run using Apache Airflow, Kubeflow Pipelines, or Cloud Composer.

---

## 17.4. Hybrid or Multicloud Strategies

* **Multicloud**: combination of at least two public cloud providers (e.g., GCP, AWS, Azure)
    * Integrations: GCP AI APIs with AWS Lambda, BigQuery Omni with S3 and Azure Blob Storage
    * Benefits: seamless data transfer, integration of machine learning capabilities
* **Hybrid Cloud**: combination of private on-premises environment and public cloud computing environment
    * Anthos platform provides hybrid ML development features:
        * Simplified data querying with BigQuery Omni
        * Hybrid AI offering with Speech-to-Text On-Prem
        * Integration with GKE, Kubeflow Pipelines, and Cloud Run

---

## 17.5. Summary

* **Orchestration Tools for ML**:
  * Kubeflow, Vertex AI Pipelines, Apache Airflow, and Cloud Composer are used for ML workflow automation.
  * Each tool has its own strengths: Vertex AI Pipelines is managed serverless, Kubeflow runs on GKE.

* **Scheduling ML Workflows**: 
  * Kubeflow uses Cloud Build to trigger deployments, while Vertex AI Pipelines uses Cloud Function event triggers.
  * Pipelines can be run manually or scheduled.

* **System Design with Kubeflow and TensorFlow**:
  * Kubeflow creates tasks as components and orchestrates them through a UI and TensorBoard.
  * TFX pipelines can also be run on Kubeflow, supporting custom orchestrators.

---

## 17.6. Exam Essentials

* **Orchestration Frameworks**: 
  * *_Kubeflow Pipelines_*: Automate ML workflows using Kubeflow Pipelines, compatible with GCP and Vertex AI Pipelines.
  * *_Vertex AI Pipelines_*: Run Kubeflow and TFX on Vertex AI Pipelines for automating ML workflows.
  * *_Apache Airflow_*: Use Cloud Composer to schedule ML workflows.
  * *_Cloud Composer_*: Schedule ML workflows using Cloud Composer.

* **Components and Scheduling**:
  + *_Kubeflow_*: Components include tasks, parameters, triggers, and compute needs. Schedule using Cloud Build or Cloud Function event triggers.
  + *_Vertex AI Pipelines_*: Schedule using Cloud Function event triggers.

* **System Design of TFX/Kubeflow**: 

---

  + *_TFX_*: Orchestrate ML pipelines using Kubeflow or Apache Airflow. Run on GCP using Vertex AI Pipelines.

---
# 18. Chapter 12Model Monitoring, Tracking, and Auditing Metadata

---

## 18.1. Model Monitoring

**Model Deployment Challenges**

* Deploying a model in production is just the first step
* The model's performance may degrade over time due to **_drift_**
* Drift occurs when the environment changes, making the model less accurate

* Types of Drift:
  * _Concept Drift_: Changes in problem definition or goals
  * _Data Drift_: Shifts in distribution of input data

---

### 18.1.1. Concept Drift

* **Concept Drift**: occurs when the relationship between input variables and predicted variables changes over time
    * _Causes_: underlying model assumptions are violated
    * _Example_: email spam filters evolve as spammers adapt their tactics

---

### 18.1.2. Data Drift

* **Data Drift**: Change in input data distribution or schema over time
    * *Example:* Model trained on customer food preference fails when demographics change
    * *Example:* New product labels (SKUs) are added to the dataset, changing the input schema
* **Model Monitoring**: Continuously evaluate model performance with same metrics used during training phase

---

## 18.2. Model Monitoring on Vertex AI

* **Model Monitoring in Vertex AI**: Provides model monitoring features to detect issues like skew and drift.
    * _Skew detection_ detects differences between training and production data, impacting model performance.
    * _Drift detection_ monitors changes in input statistical distribution over time, affecting model performance.
        + _Categorical features_: Limited values, typically grouped by qualitative properties (e.g., color, country, zip code).
        + _Numerical values_: Can take any value (e.g., price, speed, distance).

---

### 18.2.1. Drift and Skew Calculation

* _Baselines:_ 
    * **Skew detection:** Statistical distribution of training data
    * **Drift detection:** Statistical distribution of recent production data
* _Calculations:_ 
    * Categorical features: count or percentage of instances
    * Numerical features: count or percentage of values in equal-sized buckets
* _Comparison and Anomaly Detection:_ 
    * Distance measure: L‐infinity distance (categorical) / Jensen‐Shannon divergence (numerical)
    * Threshold value triggers anomaly detection

---

#### 18.2.1.1. Practical Considerations of Enabling Monitoring

* To effectively monitor data while keeping costs low:
  * Configure a _prediction request sampling rate_ to sample production inputs.
  * Set the **monitoring frequency** to analyze logged input data for skew or drift.
  * Establish alert thresholds for each feature of interest above a default value of 0.3.

---

### 18.2.2. Input Schemas

### Input Values for Model Monitoring
* *_Input values are part of the prediction payload and should be specified using a schema when configuring model monitoring_*
    + **AutoML Models**: _Input schema is automatically parsed_
    + **Custom Models**: _Must provide input schema (key/value format)_

---

#### 18.2.2.1. Automatic Schema Parsing

* **Model Monitoring Automatic Schema Detection**: Vertex AI model monitoring automatically detects the input schema when enabled for skew or drift.
* *_Key-Value Pair Format Required_*_: The automatic detection is most effective when input values are in key/value pair format (_e.g._ "key:value").
* Example: {"make":"Ford", "model":"focus": year: "2011", "color":"black"}

---

#### 18.2.2.2. Custom Schema

### Specifying the Schema in an Analysis Instance

* To ensure correct parsing of input values, specify the schema in an _analysis instance_ using Open API schema format.
* The schema can be one of three formats:
  * _object_: key/value pairs
  * _array_: array-like format
  * _string_: csv-string format
* For _array or string_ format, specify the order of features.

### Example Schema for Car Resale Value Prediction

```
{
  "type": "object",
  "properties": {
    "make": {"type": "string"},
    "model": {"type": "string"},
    "year": {"type": "number"},
    "color": {"type": "string"},
    "known_defects": [
      {"type": "string"}
    ]
  },

---

  "required": ["make", "model", "year", "color"]
}
```

Note: In CSV format, skip optional input features by providing empty fields.

---
## 18.3. Logging Strategy

* **Logging in Model Deployment**
  * Monitoring inputs is crucial
  * Logging requests may be necessary for regulatory audits or data updates
  * Available in Vertex AI for various model types

---

### 18.3.1. Types of Prediction Logs

* *_Three Types of Logs_*:
  * *_Prediction Node Logs_* 
    _Enable to gather data from prediction node_
  * *_Feature Value Logs_* 
    _Enable to see feature values for each prediction result_
  * *_Model Performance Logs_* 
    _Enable to track model performance metrics_

---

#### 18.3.1.1. Container Logging

* Logs *_stdout_* and *_stderr_* from prediction nodes to Cloud Logging
    * Helps with debugging container or model
    * Relevant for understanding the larger logging platform on GCP

---

#### 18.3.1.2. Access Logging

* **Cloud Logging**: Records timestamp and latency for each request to Cloud Logging
* _Enabled by default_ on v1 service endpoints
* *_Optional_*: Enable access logging upon deployment

---

#### 18.3.1.3. Request‐Response Logging

* Logs online prediction requests and responses to a BigQuery table
    * Primary mechanism for creating augmented training or test data
        *_Can be enabled during endpoint creation or updated later_*

---

### 18.3.2. Log Settings

* _Logging Settings Can Be Updated When Deploying a Model_
    * Changes to logging settings require redeployment after undeploying the model
    * High QPS can produce significant logs, affecting costs
* *_Configuring Logging with gcloud_* 
    * Disable container logging to reduce costs: `‐‐disable‐container‐logging`
    * Enable access logging for logs: `‐‐enable‐access‐logging`

---

### 18.3.3. Model Monitoring and Logging

* **Concurrent Usage Restrictions**
  * Model monitoring can't be enabled if request-response logging is already on.
  * Request-response logging can't be modified once model monitoring is enabled after it.

---

## 18.4. Model and Dataset Lineage

* **Importance of Metadata**: _Metadata_ provides crucial information about machine learning (ML) experiments, including parameters, observations, and artifacts, enabling effective tracking and comparison.
* *Key benefits include:* 
    - Detecting model degradation after deployment
    - Comparing hyperparameter effectiveness
    - Tracking lineage for artifact provenance
* *Purpose of metadata:* Facilitate reproducibility, audit, and understanding of ML workflows.

---

### 18.4.1. Vertex ML Metadata

* **Vertex ML Metadata**: records and queries metadata for analyzing, debugging, or auditing machine learning workflows.
    * **Data model**: uses a graph-like structure with four main components: artifacts, context, executions, and events.
        * _**Artifacts**_: data entities created by or consumed by an ML workflow (e.g. datasets, models).
            * *can be part of a* **context**, which groups related experiments and metrics*
        * _**Context**_: group of artifacts and executions that can be queried to analyze results.
    * **Schema**: metadataschema specifies the schema for data types using OpenAPI schema objects in YAML format.

---

#### 18.4.1.1. Manage ML Metadataschemas

* **Vertex ML Metadata Operations**: 
    * Create artifacts using Python or REST/CLI with function parameters: project, location, uri, artifact_id, display_name, schema_version, description, metadata.
    * Lookup artifacts (e.g., dataset, model) using Python or REST/CLI with filter parameters: display_name_filter and create_date_filter.
* **Metadata Schemas**: Predefined system schemas for common resources stored under namespace `system`, such as `_Model` that includes framework, version, and payload format properties.

---

#### 18.4.1.2. Vertex AI Pipelines

* **Lineage Tracking**: Model metadata and artifacts are stored in the metadata store for tracking a pipeline's execution.
* _Automatically generated artifacts_ include dataset summaries, model evaluation metrics, and more.
* Visual representation shows the pipeline's lineage, including data schema and deployment history.

---

## 18.5. Vertex AI Experiments

* **Vertex AI Experiments**: A tool to manage ML model development, tracking trials and analyzing variations.
* *Key Features:* 
  * Tracks experiment steps and input/output
  * Provides a single pane of glass for viewing results in Google Cloud console
  * Accessible through Vertex AI SDK for Python

---

## 18.6. Vertex AI Debugging

* _Debugging Vertex AI Model Training Issues_
    * Run custom training in an interactive Bash shell to access the container where training is running
        * Install Bash shell in training container if not already installed
        * Enable `enableWebAccess` API field to true for interactive shells
    * Use interactive shell to investigate issues, including:
        * Checking permissions for service account used by Vertex AI

---

## 18.7. Summary

* *_Model Operations_*: Monitoring deployed models, tracking model lineage
* *_Logging Strategies_*: Various options available in Vertex AI
* *_Model Tracking_*: Using Vertex ML Metadata and Vertex AI Experiments

---

## 18.8. Exam Essentials

* **Model Monitoring**: Continuously monitor model performance after deployment, focusing on **data drift** and **concept drift**, to detect changes in input data.
    * Use logging strategies to track model performance and create new training data.
    * Leverage Vertex ML Metadata for tracking model lineage and artifacts.

---

# 19. Chapter 13Maintaining ML Solutions

---

## 19.1. MLOps Maturity

* _MLOps Journey_
  * **Phase 1:** Manual Training to Automation (*MLOps Level 0*)
  * **Phase 2:** Strategic Automation with Pipelines (*MLOps Level 1*)
  * **Phase 3:** Full Automation and Transformation (*MLOps Level 2*)

---

### 19.1.1. MLOps Level 0: Manual/Tactical Phase

* **Phase Description**: Organizations experiment with ML to validate business improvements.
    * Focus on building proof of concepts and testing AI/ML use cases
    * Validate ideas for ML adoption in businesses
* _Key Players_: Individual or team experimenting with training models
    * Models are handed off to release/deployment teams using a model registry
    * Models are deployed to serve predictions

---

#### 19.1.1.1. Key Features of Level 0

* **Tactical Phase Process**
  * No automation in manual data analysis, preparation, training, and validation
  * Data scientists and engineers are completely separated, with only a handoff of the model as point of contact
    * _Lack of collaboration and communication between teams_
  * Manual iterations, limited to a few models due to lack of regular retraining
  * No consideration for continuous integration or deployment

---

#### 19.1.1.2. Challenges

* *_Model Degradation_*: well-trained models often underperform in real-life scenarios due to differences between training and real data.
* To mitigate this, *actively monitor predictions*, *retrain models frequently*, and *experiment with new algorithms*.

---

### 19.1.2. MLOps Level 1: Strategic Automation Phase

* **MLOps Level 1 Phase**: Organized phase with prioritized ML to solve business objectives, using pipelines for continuous training and delivery
    * **Key Services**:
        * Automated data and model validation steps
        * Pipeline triggers
        * Feature Store
        * Metadata management
    * _Characteristics_: Shared infrastructure, clear dev/prod separation, automated source code management

---

#### 19.1.2.1. Key Features of MLOps Level 1

* **Level 1 Characteristics**: This phase has distinct features compared to Level 0, including:
    * *_Automated experimentation_*: Each step in the process is orchestrated for faster iteration.
    * *_Continuous training_*: The model is trained automatically in production on new data.
    * *_Modular components_*: Components are reusable, composable, and potentially shareable.

---

#### 19.1.2.2. Challenges

* *_Pipeline Management_*: Team manages few pipelines, with new ones deployed manually.
* *_Triggering Pipelines_*: Mainly triggered by changes to data; not ideal for new model deployments.
* *_CI/CD Setup_*: Required for automation of build, test, and deploy ML pipelines.

---

### 19.1.3. MLOps Level 2: CI/CD Automation, Transformational Phase

* _Transformational Phase:_
	+ AI-driven innovation with agility
	+ ML experts in product teams and business units
	+ Datasets accessible across silos
	+ CI/CD automation for model updates and pipelines

---

#### 19.1.3.1. Key Features of Level 2

* **Level 2 Adoption:** Adopting CI/CD model for ML pipeline automation
    * Automates retraining, testing, and deployment of models
    * Enables continuous delivery and monitoring
    * Facilitates adaptability to rapid changes in ML technology

---

## 19.2. Retraining and Versioning Models

### **Model Drift Detection and Retraining**

* *_Monitoring_*: Track model performance over time using Vertex AI Model Monitoring.
* *_Drift detection_*: Identify when model performance degrades and retrain is necessary.
* *_Retraining frequency_*: Determine optimal interval for retraining based on evaluation of collected real data.

---

### 19.2.1. Triggers for Retraining

### Retraining Model Policies

* **Absolute Threshold**: Trigger retraining when accuracy falls below a set threshold (e.g. 90%).
* _Rate of Degradation_: Trigger retraining with sudden dips in performance (e.g. >2% drop in accuracy per day).

### Considerations for Retraining Policy
* * Training Costs: Minimize frequent retuning to reduce costs *
* * Training Time: Balance wait time vs degraded performance *
* * Scheduled Training: Simple, predictable approach incorporating new data on a regular basis

---

### 19.2.2. Versioning Models

* **Model Versioning**: allows multiple models to coexist with the same API, enabling users to choose between different versions of a model
    * _Solves backward compatibility issues_
    * _Allows for deployment of new models as separate entities, not just updates to existing ones_
    * _Provides monitoring and comparison capabilities across deployed model versions_

---

## 19.3. Feature Store

* Feature engineering is a valuable investment in building good ML models
    * Can lead to non-reusable, ad-hoc features that create problems across teams
        + Lack of governance and sharing
        + Division between teams
    * Leads to training and serving differences, reducing ML solution effectiveness

---

### 19.3.1. Solution

* *_Feature Store_*: Central location for storing features and metadata, enabling data sharing between teams and applying software engineering principles
    * Enables fast processing of large feature sets and low-latency access for real-time predictions and batch access
* **Feast**: Open-source Feature Store created by Google and Gojek, built with Redis and Google Cloud services

---

### 19.3.2. Data Model

* **Vertex AI Feature Store Data Model**
    * Uses a time-series model to store data, enabling dynamic management
        * **Data Hierarchy**: Featurestore > EntityType > Feature
    * **Entity Types**: Container for similar or related features

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

* **Feature Ingestion**: Vertex AI Feature Store supports both batch and streaming ingestion from BigQuery
* **Data Retrieval Methods**:
  * Batch: Used for model training phase
  * Online: Used for online inference, returning data up to a specified time t

---

## 19.4. Vertex AI Permissions Model

* **Understanding IAM**: Identity and Access Management (IAM) is crucial for managing access to resources like datasets, models, and enabling operations like training, deploying, and monitoring.
* * *
* **GCP IAM Fundamentals**: Revisit GCP's IAM fundamentals before diving into the Vertex AI permissions model. Existing experience with GCP's IAM model will be helpful.
* **Best Practices**: Follow these best practices for using IAM security:
  * _Least Privilege_: Restrict users and applications to only necessary actions
  * _Service Account Management_: Actively manage service accounts and keys, and enable audit logs

---

  * _Policy Management_: Implement policies at every level to ensure consistency

---
### 19.4.1. Custom Service Account

* Use custom service accounts instead of default ones to avoid unnecessary permissions
    * Custom service accounts provide exactly the required permissions for your Vertex AI training job
    * This ensures security and reduces potential risks

---

### 19.4.2. Access Transparency in Vertex AI

* **Cloud Audit Logs**: Capture user activity from your organization
* _Access Transparency Logs_: Capture actions of Google personnel in your project
* Note: [Check the supported services](https://cloud.google.com/vertex-ai/docs/general/access-transparency) for a full list.

---

## 19.5. Common Training and Serving Errors

* _Common Errors in TensorFlow Training and Serving_
* **Types of Errors**:
  * _Data-related errors_ 
  * _Model-related errors_ 
  * _Framework-related errors_

---

### 19.5.1. Training Time Errors

* *_Common Errors During Model Training_*
  * *_Preprocessing Issues_*: *Input data not transformed or encoded.*
  * *_Tensor Shape Mismatch_*
  * *_Out-of-Memory Errors_*: Due to large instance sizes on CPU/GPU.

---

### 19.5.2. Serving Time Errors

* _TensorFlow Serving Errors_ 
    * Occur only during deployment
    * Different nature compared to regular TF errors
    * Examples:
        * Input data not transformed or encoded (*not transformed*)
        * Signature mismatch occurred (*)

---

### 19.5.3. TensorFlow Data Validation

* **TensorFlow Data Validation (TFDV)**: Analyzes training and serving data to prevent and reduce errors.
    * _Detects anomalies_ in data
    * _Infer schema_ from data to ensure correct structure
    * _Computes statistics_ on data for quality control

---

### 19.5.4. Vertex AI Debugging Shell

* _Vertex AI provides an interactive shell to debug training_
    * **Debugging Tools:** Run tracing and profiling tools, Analyze GPU utilization
    * *_Validate IAM permissions_* for the container.

---

## 19.6. Summary

* **_MLOps Overview_**
  * Automates training, deployment, and monitoring of ML applications
  * Balances model quality with retraining policy and cost considerations

* *_Feature Store Concept_*
  * Solves inefficiencies caused by feature sharing across departments
  * Implemented using open source software or Vertex AI Feature Store

---

## 19.7. Exam Essentials

* _MLOps Maturity Levels_
  * Experimental phase: basic automation
  * Strategic phase: some automation
  * Mature phase: CI/CD-inspired architecture
* **Model Versioning and Retraining Triggers**
  * Trigger retraining based on model degradation or time intervals
  * Add new version or model when retraining
* _Feature Store Use_
  * Share features across teams to reduce engineering cost
  * Use managed services like Vertex AI Feature Store or open-source solutions like Feast

---

# 20. Chapter 14BigQuery ML

---

## 20.1. BigQuery – Data Access

* **Accessing Data**
    * Using the web console: write a SQL query, execute and display results below the editor.
    * Running in Jupyter Notebook with `%%bigquery` magic command
        * Execute query, display execution and result from BigQuery
    * Using Python API: import library, create client, pass query as string to get results in Pandas DataFrame

---

## 20.2. BigQuery ML Algorithms

* **BigQuery ML**: allows you to create machine learning models using standard SQL queries without writing Python code
    * is a completely serverless method to train and predict models
        * does not require any additional infrastructure or setup

---

### 20.2.1. Model Training

* **Create Model Statement**: `CREATE MODEL` statement creates a query job to process the query.
    * `_model type_ specifies the model to build (regression, classification, time-series)_
    * `_input label cols_ identifies the target column in the data_

* **Available Models**:
  * Regression: LINEAR_REG, BOOSTED_TREE_REGRESSOR, DNN_REGRESSOR, AUTOML_REGRESSION
  * Classification: LOGISTIC_REG, BOOSTED_TREE_CLASSIFIER, DNN_CLASSIFIER, DNN_LINEAR_COMBINED_CLASSIFIER, AUTOML_CLASSIFIER

* **Training a Model**: 
    * _view results of training, iterations, and evaluations (aggregate metrics, score threshold)_
    * _confusion matrix is calculated automatically_

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

* To evaluate a model, use `ML.EVALUATE` with a separate unseen dataset.
* *_Recommended practice_* to prevent overfitting.
    * This is typically done using a test dataset.
        + Example: `ML.EVALUATE` on `projectid.test.creditcard_model1` with `test.creditcardtable`.

---

### 20.2.3. Prediction

* **Prediction with ML.PREDICT function**: passes a table to predict, producing output with _predicted_ <label_column_name>_ and _predicted_ <label_column_name>_probs_ columns.
    * Passes a model and input data to `ML.PREDICT` function
        *_Example_*
            `select * from ML.PREDICT (MODEL 'dataset1.creditcard_model1', (select * FROM 'dataset1.creditcardpredict' limit 1))`
* **Output format**: table with input columns, _predicted_ <label_column_name>_ and _predicted_ <label_column_name>_probs_ columns
    * Includes probability for each label

---

## 20.3. Explainability in BigQuery ML

* **Enable explainability**: Set `enable_global_explain=TRUE` during training using SQL
```sql
CREATE OR REPLACE MODEL
    `model1`
OPTIONS(model_type='logistic_reg', enable_global_explain=TRUE, input_label_cols=['defaultpaymentnextmonth']) AS SELECT * FROM `dataset1.creditcardtable`
```
* **Query global explanations**: Use `ML.GLOBAL_EXPLAIN(MODEL 'model1')` to get a table with feature importance values
* **Explainability methods**: Available for different model types, including:
  * Linear and logistic regression: Shapley values and standard errors, p-values
  * Boosted Trees: Tree SHAP, Gini-based feature importance
  * Deep Neural Network and Wide-and-Deep: Integrated gradients

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

**BigQuery vs. Vertex AI**
=====================================

### **Similarities and Differences**

*   Both products deal with tables but cater to different types of users:
    *   **BigQuery**: Serverless data warehouse for SQL experts, focusing on table operations and joins.
    *   **Vertex AI**: More advanced machine learning features for data scientists familiar with Java or Python, focusing on fine-grained control over data and training processes.

*   BigQuery is ideal for analytics and visualization tasks, while Vertex AI is suited for building complex neural networks and custom TensorFlow operations.


---

*   Key differences lie in the user interface and approach to training and prediction:
    *   **BigQuery**: Automated queries, visualization tools like Looker Studio.
    *   **Vertex AI**: Customizable workflows, Jupyter Notebooks, Pandas DataFrames.

### **Choosing Between BigQuery and Vertex AI**

*   For analytics and business users: Use BigQuery.
*   For machine learning engineers: Use Vertex AI.

---
## 20.5. Interoperability with Vertex AI

* **Integration Points**: Vertex AI and BigQuery ML integrate through:
  * Data ingestion
  * Model training
  * Model deployment
  * Model monitoring
  * Data labeling
  * Experiment management

---

### 20.5.1. Access BigQuery Public Dataset

* **BigQuery Public Datasets**: Over 200 publicly available datasets stored by Google Cloud and accessible through GCP projects
* **Query Costs**: Pay only for queries run on these datasets, no upfront storage costs
* *_Access via Vertex AI_*: Train ML models or augment existing data with public datasets like weather data to improve model accuracy

---

### 20.5.2. Import BigQuery Data into Vertex AI

* You can create a dataset in Vertex AI by providing a source URL that points to a BigQuery dataset.
* This allows for seamless connection to data in BigQuery without exporting and importing the data.
* Use `bq://project.dataset.table_name` as the source URL, like this: `bq://my-project.my-dataset.my-table`

---

### 20.5.3. Access BigQuery Data from Vertex AI Workbench Notebooks

* **Integration Benefits**: Directly browsing BigQuery dataset, running SQL queries, and downloading data into Pandas DataFrame
* *_Enhanced Data Analysis_*: Useful for data scientists performing exploratory analysis, creating visualizations, and experimenting with machine learning models
* *Streamlined Workflow*: Simplifies working with multiple datasets in a Jupyter Notebook

---

### 20.5.4. Analyze Test Prediction Data in BigQuery

* _Model Prediction Export_
  * **Train and Test Data Export**
    *_Directly to BigQuery_*
      + Utilizes model training data for analysis
      + Enables SQL-based predictions analysis

---

### 20.5.5. Export Vertex AI Batch Prediction Results

* You can make batch predictions in **Vertex AI** directly from a *_BigQuery_* table.
* Predictions can also be sent back to BigQuery to be stored as a table.
* This feature integrates well with standardized MLOps using Vertex AI.

---

### 20.5.6. Export BigQuery Models into Vertex AI

* **Model Export**: You can export BigQuery ML models to GCS for import into Vertex AI.
    * **Model Registry Integration**: Upcoming feature allows direct registration of BigQuery ML models in the Vertex AI Model Registry.
        * **Supported Models**: Both BigQuery inbuilt and TensorFlow models are supported, except ARIMA_PLUS, XGBoost, and transform-based models.

---

## 20.6. BigQuery Design Patterns

* _BigQuery ML introduces novel solutions to common data science and machine learning challenges_
* These solutions are based on well-thought-out design patterns
* _Elegant new approaches to tackling frequent problems in the field_

---

### 20.6.1. Hashed Feature

* *_Categorical Variable Issues_*: Incomplete vocabulary, high cardinality, and cold start problem can affect ML models
    * *_Solution_*:
        * Transform high cardinal variables using hashing to reduce dimensionality 
            + *_Example_*: `ABS(MOD(FARM_FINGERPRINT(zipcode), numbuckets))`

---

### 20.6.2. Transforms

* **Transforms in BigQuery ML Models**: The `TRANSFORM` clause applies transformations to input fields before feeding into a model.
    * These transformations must be applied when deploying the model in production.
    * Applies transformations such as feature cross, quantile bucketizing, and scaling.
        * Available transforms include `POLYNOMIAL_EXPAND`, `FEATURE_CROSS`, `NGRAMS`, `QUANTILE_BUCKET`, `HASH_BUCKETIZE`, `MIN_MAX_SCALER` and `STANDARD_SCALER`.

---

## 20.7. Summary

* _BigQuery ML simplifies machine learning_ using SQL, making it more accessible to many users.
* *_Interoperability with Vertex AI_* allows for seamless collaboration between services.
* _Unique design patterns_ enable efficient model creation and data transformation.

---

## 20.8. Exam Essentials

* **BigQuery and Machine Learning Overview**
    * Learn about BigQuery's history and the innovation of bringing machine learning into data analysis
    * Understand how to train, predict, and explain models using SQL
* **BigQuery ML vs Vertex AI**
    * _Differences between BigQuery ML and Vertex AI_
        - *Learn about the design differences between these two services*
    * _Integration Points for Seamless Collaboration_
        - *Understand how to work together with both services*
* _BigQuery Design Patterns for Machine Learning_
    * Learn about easy solutions like hashing, transforms, and serverless predictions

---

# 23. Online Test Bank

---

## 23.1. Register and Access the Online Test Bank

* _Register your book for online access_:
  * Go to `www.wiley.com/go/sybextestprep` and select your book from the list
  * Complete registration information and answer security verification
  * Enter pin code received via email to activate account
* _Access test bank:_
  * Log in with new username and password
  * Refresh page if test bank not visible, or log out and log back in

---

# 24. WILEY END USER LICENSE AGREEMENT

---

