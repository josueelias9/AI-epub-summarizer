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

* **Identify impact**: Understand the benefits of the use case for the company and end user.
  * _Business impact_
  * _Data privacy and security_
  * _Timeline_

* **Match with machine learning approach**: Select an algorithm and metric to solve the problem.
  * _Analyze data availability_
  * _Understand the ML model's limitations_

* **Evaluate feasibility**: Determine if the problem can be solved using machine learning, considering existing technology, available data, and budget.

---

## 7.2. Machine Learning Approaches

**Overview of Machine Learning Approaches**

* There are hundreds of ways to apply machine learning techniques
* Approaches are categorized into specific classes of problems
* Understanding the landscape of ML methods is crucial for solving use cases
* Wide knowledge of machine learning approaches is necessary to find the correct solution

---

### 7.2.1. Supervised, Unsupervised, and Semi‐supervised Learning

* **Machine Learning Approaches**: Classification based on type of learning
    * _Supervised Learning_: Using labeled dataset to train models, e.g., image classification.
        + Examples: Regression, Classification, Sentiment Analysis.
    * _Unsupervised Learning_: Using unlabeled data, e.g., clustering and topic modeling.
        + Examples: K-means Clustering, Principal Component Analysis, Topic Modeling.

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

* **Classification**: predicts "labels" or categories (e.g., dogs vs. cats), with binary classification having 2 labels and multiclass classification having more.
    * Can have thousands of labels, e.g., object detection with millions of classes
* **Regression**: predicts a number (e.g., house price, rainfall amount)
    * Predicted value's range depends on use case
* _Forecasting_: uses time-series data to predict future values
    * Input is indexed in time order, e.g., temperature readings taken every hour

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

* **Classification Metric**: There are various metrics to evaluate a classification model, such as precision, recall, and F1 score.
    * *_Precision_*: measures the percentage of correct positive predictions, lower false positives. Formula: `True Positives / (True Positives + False Positives)`
    * *_Recall_*: measures the percentage of correctly predicted positive data points, lower false negatives. Formula: `True Positives / (True Positives + False Negatives)`
    * *_F1 score_*: harmonic mean of precision and recall, lowers both false positives and false negatives together. Formula: `(2 x Precision x Recall) / (Precision + Recall)`

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

**ROC Curve**
* Receiver operating characteristic curve (ROC) plots binary classification model performance
	+ False positive rate on x-axis, true positive rate on y-axis
* Ideal point: top-left corner (100% TP, 0% FP)
* A diagonal line is the worst case; goal is to stretch curve away from it

**AUC**
* Area under ROC curve (AUC) compares two models
	+ Measures ranking quality not absolute values
* Helps choose model regardless of threshold choice
* Advantages:
	+ **Scale-invariant:** No dependence on scale
	+ **Classification threshold-invariant:** Irrespective of chosen threshold

---

### 7.3.2. The Area Under the Precision‐Recall (AUC PR) Curve

* The area under the precision-recall (AUC-PR) curve measures the relationship between recall and precision.
* The best AUC-PR curve is horizontal at the top-right corner, representing 100% precision and recall.
* A highly imbalanced dataset favors AUC-PR as it helps to mitigate skewed results.

---

### 7.3.3. Regression

**Regression Metrics**

* *_Mean Absolute Error_*: average absolute difference between actual and predicted values
* *_Root-Mean-Squared Error_*: square root of average squared difference, penalizes large predictions
    * *_RMSLE_*: similar to RMSE, uses natural logarithm, penalizes under prediction
* *_Mean Absolute Percentage Error_*: average percentage difference between labels and predicted values
* *_R-squared_*: square of Pearson correlation coefficient, measures fit (0-1 range)

---

## 7.4. Responsible AI Practices

* **Key Considerations for AI and Machine Learning**
    * Fairness: Avoid biases in models by measuring bias in datasets and testing for bias
    * Interpretability: Use model explanations to gain insights into complex models like neural networks
    * Privacy and Security: Protect sensitive data, minimize leakage during training and deployment phases

---

## 7.5. Summary

* *Taking a Business Use Case: Framing a Machine Learning Problem Statement*
  * Understanding the ask
  * Identifying key dimensions of a business use case

---

## 7.6. Exam Essentials

* **Machine Learning for Business Challenges**
  * Identify business use cases that involve machine learning
    * _Problem type_: regression, classification, forecasting
    * _Key metrics_: precision, recall, F1, AUC ROC, RMSE, MAPE
  * Understand Google's Responsible AI principles for fairness, interpretability, privacy, and security

---

# 8. Chapter 2Exploring Data and Building Data Pipelines

---

## 8.1. Visualization

* Data visualization is a technique to find trends and outliers in data, aiding data cleaning and feature engineering.
    * Univariate Analysis: analyzes each feature independently (e.g., box plots, distribution plots)
        * Examines range, outliers, and distributions of individual features
    * Bivariate Analysis: compares two features to identify correlations (e.g., line plots, bar plots, scatterplots)

---

### 8.1.1. Box Plot

* A box plot visualizes data with 25th, 50th (median), and 75th quartiles.
* The body represents the interquartile range with maximum observations.
* Outliers are points outside the whiskers or straight lines representing max/min values.

---

### 8.1.2. Line Plot

* A line plot displays relationships between two variables over time, showing trends in data changes.
* It helps analyze data patterns and identify trends.
* Used to visualize data changes over time.

---

### 8.1.3. Bar Plot

* **What is a bar plot?**: A graph used to analyze trends in data and compare categorical values.
* **Common uses**: Analyzing sales figures, website traffic, or revenue over time.
* *_Visualizes categorical data_*, making it easy to identify patterns and trends.

---

### 8.1.4. Scatterplot

* A **scatterplot** is a common data visualization tool used to *visualize relationships between two variables* and *identify clusters in datasets*.

---

## 8.2. Statistics Fundamentals

* Three measures of central tendency in statistics are:
  * **Mean**: average value
  * **Median**: middle value when data is sorted
  * **Mode**: most frequently occurring value

---

### 8.2.1. Mean

Mean is the accurate measure to describe the data when we do not have any outliers present.

---

### 8.2.2. Median

* **Median calculation**: Find the middle value(s) in a dataset arranged from lowest to highest.
    * _If even numbers_: Calculate the average of the two middle values.
    * _If odd numbers_: The median is the single middle value.

---

### 8.2.3. Mode

* **Mode**: the value(s) that appear most frequently in a dataset.

---

### 8.2.4. Outlier Detection

* **Mean and Outliers**: The mean is affected by outliers, which can significantly change its value.
    * _Effect on Measures_: Adding an outlier changes the mean, median, and mode values.
        - Mean: 12.72 (without outlier) vs. 29.16 (with outlier)
        - Median: 13 (without outlier) vs. 14 (with outlier)
        - Mode: 15 (both with and without outlier)

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

* **Key Statistics**:
  * _Standard Deviation_: Square root of variance, identifies outliers (data points > 1 SD from mean)
  * _Covariance_: Measure of variation between two random variables

---

### 8.2.6. Correlation

* **Correlation Basics**
  * Correlation is normalized covariance with a value range of -1 to +1.
  * Pearson's correlation coefficient measures the strength and direction of linear relationships between two variables.

* **Types of Correlation**
  * _Positive Correlation_: Increase in one variable leads to increase in another.
  * _Negative Correlation_: Increase in one variable leads to decrease in another.
  * _Zero Correlation_: No substantial impact from change in one variable on the other.

* **Detecting Label Leakage with Correlation**
  Highly correlated labels can cause models to learn irrelevant features, such as hospital names, instead of target variables.

---

## 8.3. Data Quality and Reliability

* **Data Quality**: The reliability of your model depends on the quality and consistency of the training data.
	* _Key Data Quality Checks_:
		+ Check for label errors
		+ Detect noise in features
		+ Identify outliers and data skew

---

### 8.3.1. Data Skew

* **Data Skew**: Data that follows a non-symmetric normal distribution curve.
* *Causes:* Outliers and uneven data distribution.
* **Characteristics:** 
    * Right-skewed: income data with extreme outliers
    * Left-skewed: data with few high values and many low values

---

### 8.3.2. Data Cleaning

* **Normalization**: transforms features to a consistent scale
    * Improves model performance and training stability
    * Enhances data preparation (_[see Google Machine Learning documentation](https://developers.google.com/machine-learning/data-prep/transform/normalization))_)

---

### 8.3.3. Scaling

### **Scaling Benefits**

* Improves gradient descent convergence in deep neural networks
* Removes "NaN traps" by scaling all numbers to a standard range
* Prevents features with wide ranges from dominating the model

---

### 8.3.4. Log Scaling

* **Log Scaling**: used for _large data samples_ that follow a power-law distribution, e.g., 10,000 vs. 100.
* **Purpose**: scales data to a common range (e.g., 0-100) by taking the logarithm of values.

---

### 8.3.5. Z‐score

* **Scaling by Z-score**: Scales values as standard deviations away from the mean
* _Formula_: `Scaled value = (value - mean) / stddev`
* **Example**: Given mean 100 and stddev 20, a value of 130 results in a z-score of 1.5

---

### 8.3.6. Clipping

* *_Feature Clipping_*: Capping extreme outlier values (above/below) to a fixed value
* Can be performed *_before_* or *_after_* normalization techniques
* Affects data by limiting extreme values, but may lose information

---

### 8.3.7. Handling Outliers

* **Outlier Detection**: Values that deviate significantly from the rest of the data
  * Use visualization techniques like box plots and Z-score to detect outliers
  * Other methods include clipping and IQR analysis
* **Handling Outliers**: Remove or replace detected outliers
  * Replace with mean, median, mode, or boundary values

---

## 8.4. Establishing Data Constraints

* **Defining Data Schema**: Establishing a schema for ML pipelines ensures consistent and reproducible data handling, capturing key characteristics like data type, range, and distribution.
    * **Advantages**:
        * Enables metadata-driven preprocessing for feature engineering and data transformation
        * Validates new data, catching anomalies like skewness and outliers during training and prediction.

---

### 8.4.1. Exploration and Validation at Big‐Data Scale

* _TensorFlow Data Validation (TFDV)_ helps validate ML data at scale by detecting anomalies and schema issues.
* TFDV is part of the _TensorFlow Extended (TFX)_ platform, providing libraries for data validation, schema validation, and more.
* Key uses include:
  * **Exploratory Data Analysis**: produces a data schema to understand the data and define a contract between the ML pipeline and data.
  * **Production Pipeline Phase**: defines a baseline to detect new data skew or drift in the model during training and serving.

---

## 8.5. Running TFDV on Google Cloud Platform

* _Apache Beam SDK_ powers TFDV APIs for batch and streaming pipelines
* Dataflow is a managed service that runs Apache Beam pipelines at scale
    * Integrates with **BigQuery** and **data lakes (GCS)** for data warehousing and storage
    * Supports `Vertex AI Pipelines` for machine learning

---

## 8.6. Organizing and Optimizing Training Datasets

* **Data Splitting**
  * Training Dataset: used to train the model
  * Validation Dataset: used for hyperparameter tuning and evaluating the model's behavior during training
  * Test Dataset: used to evaluate the model's performance after training and validation, without leaking data from other sets.

---

### 8.6.1. Imbalanced Data

* **Imbalanced Data**: occurs when two classes in a dataset are not equal, affecting model training
    * _oversampling_ ( duplicating minority samples) and _undersampling_ (deleting majority samples) can introduce bias and are less effective
    * downsampling the majority class and upweighting the downsampled class is an effective approach to balance data
* **Downsampling and Upweighting**: balances dataset by reducing majority class samples and increasing importance of minority class examples
    * faster model convergence due to increased minority class examples

---

### 8.6.2. Data Splitting

* **Splitting Data**: Random splitting can cause skew if it separates similar topics or time-based constraints.
    * **Time-based Split**: Split data based on publication timeline to avoid separating stories with same topic.
        * **Overlapping Concerns**: Using June and July as training/testing sets would still allow some overlap.

---

### 8.6.3. Data Splitting Strategy for Online Systems

* **Splitting Data by Time**
  * Ensures validation set mirrors the lag of time between training and prediction
  * Recommended for online systems with large datasets (e.g., millions of examples)
  * Use domain knowledge to decide whether a random or time-based split is appropriate

---

## 8.7. Handling Missing Data

* **Handling Missing Data**: There are several ways to handle missing data in datasets, including:
  * Deleting rows or columns with missing values
  * Replacing missing values with mean, median, or mode of remaining values
    * _**Pros: prevents loss of data, works well with small datasets. Cons: doesn't factor in covariance between features and can cause data leakage.**
  * Imputing missing values with the most frequent category or a new category

---

## 8.8. Data Leakage

* **Data Leakage**: exposing model to test data during training causes underperformance when exposed to unseen data.
    * *Causes overfitting as model has learned from both training and test data.*
    * *Can occur due to incorrect feature selection, poor data splitting, or preprocessing techniques.*
    * *Can be prevented by selecting uncorrelated features, splitting data into separate sets for training, validation, and testing, and pre-processing data separately.*

---

## 8.9. Summary

* **Data Visualization**: Understanding why visualization is necessary and various techniques such as box plots, line plots, and scatterplots.
    * **Statistical Fundamentals**: Mean, median, mode, standard deviation, and their relevance in detecting outliers and checking data correlation.
    * _Data Preprocessing_: Techniques like log scaling, scaling, clipping, and z-score to improve data quality.
* _Data Validation_:
  - Establishing data constraints
  - Validating data schema using TFDV for large-scale deep learning systems
* _Data Splitting_:
  - Strategies for splitting data, including time-based split for online systems and clustered data

---

    * _Dealing with Missing Data_: Approaches to handle missing values, including imputation and interpolation.
    * _Data Leakage Prevention_: Measures to prevent data leakage in machine learning pipelines.

---
## 8.10. Exam Essentials

* **Data Analysis Fundamentals**
    * Understanding statistical terms such as mean, median, mode, and standard deviation
    + Identifying outliers and checking data correlation using line plots
    * Ensuring data quality through cleaning, normalizing, and validating datasets
        - Removing skew, applying log scaling, scaling, clipping, and z-score techniques
    * Defining a data schema and validating data for machine learning pipelines
* **Data Management**
    * Splitting datasets into training, test, and validation data
    + Handling clustered and online data with appropriate splitting techniques
    * Applying sampling strategies for imbalanced data

---

        - Using techniques such as undersampling, oversampling, or generating synthetic samples
* **Handling Challenges**
    * Dealing with missing data through removal, replacement, or machine learning-based methods
    + Avoiding data leaks and label leakage by implementing data anonymization and protection measures

---
# 9. Chapter 3Feature Engineering

---

## 9.1. Consistent Data Preprocessing

* **Data Transformation Approaches**
  * Pretraining Data Transformation: Perform transformations before model training, advantages include efficient computation and dataset analysis.
    * Disadvantages include needing to reproduce transformation at prediction time and updating can be slow.
  * Inside Model Data Transformation: Transform data within the model during training, decouples data from transformation and allows easy changes.
    * Disadvantage includes potential increase in model latency due to heavy computations.

---

## 9.2. Encoding Structured Data Types

* A good feature should relate to business objectives, be predictable at prediction time, numeric with magnitude, and have sufficient examples.
* Feature engineering categories include:
  * *_Categorical Data_*: defines a limited set of distinct values (e.g., yes/no, male/female)
  * *_Numeric Data_*: represents scalar or continuous values (e.g., observations, measurements)

---

### 9.2.1. Why Transform Categorical Data?

* **Categorical Data Limitation**: Most ML algorithms require numeric input and output variables.
* _Conversion Needed_
* * Categorical data must be converted to numeric data for algorithm use.

---

### 9.2.2. Mapping Numeric Values

* *_Numeric Data Transformation_* 
    * Normalization: scales values to a common range
    * Bucketing: groups values into categories or bins

---

#### 9.2.2.1. Normalizing

* Normalization techniques are used to handle numeric features with different ranges or extreme values.
    * Scaling (e.g. age, income) to prevent slow convergence for models like ADAM
    * Clipping or log scaling to prevent NaN errors from large values (e.g. city data)

---

#### 9.2.2.2. Bucketing

**Bucketing: Transforming Numeric Data to Categorical**
* Converts floating-point values into categorical data
* Used for predicting variables like house price based on location
* Two methods:
  * **Equal-Spaced Buckets**: Creates buckets with fixed boundaries, varying data points
  * **Quantile Buckets**: Each bucket has equal points, variable boundaries

---

### 9.2.3. Mapping Categorical Values

* **Converting Categorical Data**: Methods to transform categorical data into numerical data for model understanding
    * _One-hot encoding_
    * _Label encoding_
    * _Ordinal encoding_

---

#### 9.2.3.1. Label Encoding or Integer Encoding

* **Label Encoding**: assigning unique integers to categories using a vocabulary.
    * Can be applied when categories have limited ranges (e.g., breeds of dog) or ordinal values (e.g., days of the week).
        * Example: mapping ratings to integers like 1 for "satisfactory", 2 for "good", and 3 for "best".

---

#### 9.2.3.2. One‐Hot Encoding

* **One-Hot Encoding**: technique for categorical variables where order does not matter, used when features are nominal.
    * Creates a new variable for each categorical feature by converting it into a binary representation (e.g., Red = 00, Blue = 01).
    * Used to convert categorical variables into integer values or binary representation.

---

*One‐Hot Encoding*
Categorical Value | Integer Encoding or Creating a Vocabulary Mapping | One‐Hot Encoding
---|---|---
Red | 0 | 00
Blue | 1 | 01

<!-- _class: centered -->

---

#### 9.2.3.3. Out of Vocab (OOV)

* Creating an "out of vocabulary" category for outliers reduces training time by eliminating the need to give them unique representation. 
* This single category groups together extremely rare data points that are unlikely to influence model performance.
* By doing so, the machine learning system can focus on more representative and frequent data points.

---

#### 9.2.3.4. Feature Hashing

* **Hashing**: Applying a `hash function` to categorical features to create indices
*   _Advantages_:
    * Does not require assembling a vocabulary
    * Can handle changing feature distributions without retraining
*   _Disadvantage_: May cause collisions due to the nature of hashing

---

#### 9.2.3.5. Hybrid of Hashing and Vocabulary

* *_Hashing Approach_*: Replace out-of-bucket categories with hashed categories using a predefined vocabulary.
* *_Advantages_*:
  * Out-of-box categories are represented by hashing
  * Model can learn categories outside the predefined vocabulary

---

#### 9.2.3.6. Embedding

* **Embeddings in DL Models**: Embeddings are categorical features converted into continuous-valued representations.
* *Main Applications*: Text classification and document classification using bag-of-words or documents.
*  Used to capture semantic relationships between words.

---

### 9.2.4. Feature Selection

* **Feature Selection**: Selecting a subset of most useful input variables for model prediction
* **Dimensionality Reduction**:
	+ Reduces noise, overfitting problems, and computational resources
	+ Increases model performance
	+ Can be achieved through:
		- Keeping only the most important features (e.g. backward selection, Random Forest)
		- Combining new features (e.g. PCA, t-SNE)

---

## 9.3. Class Imbalance

* **Class Imbalance in Classification Models**: Classification models suffer from class imbalance issues due to incorrect predictions of positive and negative classes.
    * A **false negative** is a critical issue, where a sick patient is misclassified as not sick, leading to poor outcomes.
    * False negatives are often more problematic than false positives, as they can lead to missed diagnoses and harm.

---

### 9.3.1. Classification Threshold with Precision and Recall

**Classification Threshold**
A value chosen by humans to map logistic regression output to a binary category.

* **Definition**: A value between 0 and 1 that determines when a prediction is classified as positive.
* **Importance**: Strongly influences number of false positives and false negatives, with different thresholds emphasizing precision or recall.

---

### 9.3.2. Area under the Curve (AUC)

* **Classification AUC Metrics**: 
    * _AUC-ROC_ measures balanced datasets.
        + Equal number of examples per class.
    * _AUC-PR_ measures imbalanced datasets.
        + Most classes have a small number of instances (e.g., fraud vs. non-fraud).

---

#### 9.3.2.1. AUC ROC

* **Definition**: A graph showing a classification model's performance at all thresholds, plotting true positive rate and false positive rate.
* **AUC-ROC**: Measures the 2D area under the ROC curve, ranging from 0.0 to 1.0, representing a binary model's ability to separate classes.
    * **Interpretation**: A closer AUC value indicates better class separation.

---

#### 9.3.2.2. AUC PR

* **Precision-Recall Curve**: a graph showing Precision values on y-axis and Recall values on x-axis
* **AUC PR**: measures the 2D area under the curve, giving more weight to minority class
* *_Key advantage_*: provides attention to minority class in imbalanced binary classification models

---

## 9.4. Feature Crosses

* **Feature Cross**: a synthetic feature created by multiplying two or more features
* **Why Use Feature Cross**: to increase predictive ability when single features are not sufficient, and to represent nonlinearity in linear models by multiplying features
    * Example: combining `location (market, curbside)` and `time of day` to improve prediction accuracy

---

## 9.5. TensorFlow Transform

* **Efficient Input Pipeline for TensorFlow**
  * _Improves model performance by reducing data loading time_
  * _Increases scalability and reduces computational overhead_

---

### 9.5.1. TensorFlow Data API (tf.data)

* **Improving Model Execution Speed**: Efficient data input pipeline can reduce device idle time
* **Key Transformations**:
    * `_tf.data.Dataset.prefetch_` decouples data production and consumption
    * `_tf.data.Dataset.interleave_` parallelizes data reading to mitigate extraction overhead
    * `_tf.data.Dataset.cache_` caches data in memory during the first epoch

---

### 9.5.2. TensorFlow Transform

* **TensorFlow Transform**: allows transformations prior to training model, reducing training-serving skew.
    * _Uses TFX_ and enables data analysis, transformation, metadata production, and model feeding.
    * _Supported on Google Cloud using Cloud Dataflow_, reading data from BigQuery, writing to Cloud Storage as TFRecords.

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

* **Chapter 8**: Covers the complete data analytics ecosystem from collecting to storing data
* 
  * **Cloud Data Fusion**
    * A web-based, managed service for building and managing ETL/ELT pipelines
    * Supports Cloud Dataproc for Hadoop and Spark workloads
  * 
  * **Dataprep by Trifacta**
    * A serverless tool for visually exploring, cleaning, and preparing data for analysis and machine learning

---

## 9.7. Summary

* **Feature Engineering**: Transforming numerical and categorical features for model training and serving
    * Numerical features: bucketing, normalization, PCA (for dimensionality reduction)
    * Categorical features: linear encoding, one-hot encoding, out of vocabulary, hashing, embedding
        * For imbalanced classes, use AUC PR instead of AUC ROC
* **Feature Importance**: Selecting relevant features and feature crossing for improved performance

---

## 9.8. Exam Essentials

* **Data Transformation** 
  * Understand when to transform data before or during model training.
  * Techniques: bucketing, normalization, hashing, one-hot encoding for numeric and categorical data.
  * Benefits and limitations of transforming data before training.

* **Feature Engineering**
  * Feature selection: dimensionality reduction, techniques like PCA.
  * Class imbalance: true positives, false positives, accuracy, AUC, precision, recall.
  * Feature cross: important in certain scenarios, use with caution.

* **TensorFlow Transform and GCP Tools**
  * TensorFlow Transform: pipeline architecture on Google Cloud using BigQuery and Cloud Data Fusion.

---

  * GCP data and ETL tools: Cloud Data Fusion for no-code ETL, Cloud Dataprep for data cleaning.

---
# 10. Chapter 4Choosing the Right ML Infrastructure

---

## 10.1. Pretrained vs. AutoML vs. Custom Models

* **Pretrained Models**: 
  * Models already trained on large datasets by Google
  * Easy to use and fast integration into applications
  * Ideal first choice, but may not meet specific requirements

* *_Serverless_** method: 
  * No provisioning of cloud resources required
  * Charges based on API request frequency
  * Free tier available for some APIs

* **AutoML**: 
  * Chooses best ML algorithm and only requires data
  * Second level in the pyramid, used when pretrained models don't work
  * Requires provisioning of cloud resources during training and deployment

---

## 10.2. Pretrained Models

* **Pretrained Models**: machine learning models trained on large datasets, performing well in benchmark tests.
    * _Key benefits:_ supported by large teams, frequently retrained for improved performance.
        * **Access:** available through web console, CLI, SDKs (Python, Java, Node.js), and Google Cloud platform.

---

### 10.2.1. Vision AI

* **Vision AI** provides image analysis capabilities through Google Cloud
    * Performs tasks like object detection, facial recognition, and handwriting reading
        + _Image classification_: labels for objects in the photo (e.g. Table, Furniture)
        + _Object detection_: identifies specific objects in the image
        + _Optical Character Recognition_ (_OCR_): reads handwritten text

---

### 10.2.2. Video AI

* **Video AI API**: recognizes objects, places, and actions in videos
    * _Applies to stored or streaming videos with real-time results_
    * Recognizes over 20,000 different objects, places, and actions
* **Use Cases**
    * **Building Video Recommendation Systems**: uses labels and user history for personalized recommendations
    * **Indexing Video Archives**: creates metadata index for large video collections
    * **Improving User Experience**: compares video content with advertisements for relevance

---

### 10.2.3. Natural Language AI

* **Summary of Natural Language AI**: Provides insights from unstructured text using pretrained machine learning models for entity extraction, sentiment analysis, syntax analysis, and general categorization.
* **Key Services**:
  * Entity Extraction: Identifies entities with additional context (e.g., Wikipedia links)
  * Sentiment Analysis: Assigns positive, negative, or neutral scores to sentences, entities, and text
  * Syntax Analysis: Analyzes part of speech, dependency, lemma, and morphology
* **Use Cases**:
  * Customer Sentiment Analysis
    * Use entity analysis for important details from documents (e.g., emails, chat, social media)

---

    * Use sentiment analysis to understand customer opinion on specific products

---
### 10.2.4. Translation AI

* **Translation Service**: Detects over 100 languages and translates between any pairs, utilizing Google's industry-standard GNMT technology.
    * _Supported Features_:
        * Advanced version uses a glossary for more accurate translations
        * Can translate entire documents (PDFs, DOCs, etc.)
    * Price difference between Basic and Advanced versions

---

### 10.2.5. Speech‐to‐Text

* *_Speech-to-Text Service_* 
    * Converts audio to text
    * Used for creating subtitles and translations for video recordings and streaming

---

### 10.2.6. Text‐to‐Speech

* The Text‐to‐Speech service provides realistic speech with humanlike intonation using DeepMind's AI expertise.
* It supports 220+ voices across 40+ languages and variants, allowing for unique brand voice creation. 
* * Voices can be customized to represent a brand at all touchpoints.*

---

## 10.3. AutoML

* **AutoML**: Automates model training tasks, allowing users to input data and configure settings for automated training.
* **Available Data Types**:
    * _Structured Data_
    * _Images/Video_
    * _Natural Language_
    * _Recommendations/AI for Retail_

---

### 10.3.1. AutoML for Tables or Structured Data

* **Overview of AutoML Tables**: AutoML Tables provides two methods for training models: BigQuery ML and Vertex AI Tables, which can be triggered using Python, Java, or Node.js, or via REST API.
    * **Vertex AI AutoML Tables algorithms**
        * Classification: AUC ROC, AUC ROC, Logloss, Precision at Recall, Recall at Precision
        * Regression: RMSE, RMSLE, MAE
        * Time-series data: Forecasting - RMSE, RMSLE, MAPE, Quantile loss

    * **Configuring AutoML job**: Budget and Enable early stopping settings affect the training process, with budget determining maximum hours allowed and enabling early stopping to stop training if a threshold is met.

---

    * **Model types for forecasting**: 
        * AutoML: built-in model suitable for various use cases
        * Seq2seq+: effective for small dataset sizes (< 1 GB)
        * Temporal Fusion Transformer: high accuracy and interpretability model

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

* **Image classification with AutoML**: Predict one or multiple correct labels for an image using user-provided label lists.
* **Video classification and action recognition with AutoML**: Get label predictions for entire videos, shots, and frames, as well as identify actions within a video.
* _AutoML Edge models_ are optimized for low memory and latency deployment on edge devices such as iPhones, Android phones, and Edge TPU devices.

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

* *_Vertex AI AutoML Text_* provides machine learning models for text problems
    * Solved problems include:
        * *_Classification and Sentiment Analysis_*
        * *_Multi-Label Classification_*
        * *_Entity Extraction_*
        * *_Text-to-Text Translation_*

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

* _Google Retail AI_ is a solution that offers retailers a Google-quality search, image search, and personalized recommendations.
    * The solution consists of three main parts: **Retail Search**, **Vision API Product Search**, and **Recommendations AI**.
        * **Recommendations AI** uses customer behavior data to create models for product recommendations.

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

* **Document AI**: extracts details from digitized documents, including forms, passports, and government documents.
    * Provides structure extraction, text layout analysis, key/value pair identification, entity extraction, document classification, and review capabilities.
    * Includes customizable processors for specific use cases and a Document AI Warehouse for storing, searching, and organizing extracted data.

---

### 10.3.6. Dialogflow and Contact Center AI

* Dialogflow offers a conversational AI platform, integrating chatbots and voicebots for various services
* It provides a Contact Center AI (CCAI) solution, combining telephony and other services

---

#### 10.3.6.1. Virtual Agent (Dialogflow)

* **Virtual Agent Design**
  - Handle common cases automatically
  - Forward complex calls to human agents
  - Utilize historical call data for optimization

---

#### 10.3.6.2. Agent Assist

* **Agent Assist**: Provides real-time support to agents during calls
    * Identifies intent and offers prepared responses
    * Accesses a centralized knowledge base for information

---

#### 10.3.6.3. Insights

* **Service Overview**: Uses NLP to analyze driver calls and measure sentiment to inform call center operations
* **Key Functionality**: Measures customer sentiment to help leadership make data-driven improvements
* **Outcome**: Enhanced call center operations through data-informed decision making

---

#### 10.3.6.4. CCAI

* **Contact Center AI Platform**: A cloud-native platform for multichannel communications between customers and agents.
* 
* **Dialogflow and CCAI**: Advanced machine learning techniques, mostly hidden from machine learning engineers.
* 
* Machine learning engineer knowledge goes beyond the scope of this exam.

---

## 10.4. Custom Training

* **GPU Acceleration**: Custom training on GPUs accelerates compute-intensive operations like matrix multiplications for deep learning models.
* **CPU vs GPU Training Time**: Training on a single CPU can take days or months, while offloading computation to a GPU reduces training time by an order of magnitude.
* *_Massive Parallelism_*: GPUs enable massively parallel architectures that benefit from extensive computation, reducing training times and increasing efficiency.

---

### 10.4.1. How a CPU Works

* A **CPU** is a general-purpose processor that can run various types of applications.
    * It loads data from memory, performs an operation, and stores the result back into memory for every single operation.
    * This serial computation architecture is inefficient for tasks requiring trillions of calculations, such as training large ML models.

---

### 10.4.2. GPU

**Using GPUs in Vertex AI**
* **GPUs Bring Additional Firepower**: Specialized chips for rapid data processing, originally designed for movies and video games.
* **GPU Architecture**: Thousands of arithmetic logic units (ALUs) work together to process large amounts of data in parallel.
* **Configuring GPUs**: Specify GPU type and count in `WorkerPoolSpec` and consider instance type restrictions.

---

### 10.4.3. TPU

* **TPUs for ML**: Google-designed hardware accelerators for machine learning workloads
    * _Specialized_ for matrix processing and multiply-accumulate operations
    * _High-performance_: each MXU performs 16,000 operations per cycle using bfloat16 format
    * _Designed for large matrices_, key to neural network training loops

---

#### 10.4.3.1. How to Use TPUs

* **TPU Configurations**: Cloud TPU offers:
    * Single TPU device
    * TPU Pod (group of connected devices)
    * TPU slice (subdivision of a TPU Pod)
    * TPU VM (virtual machine with TPU capabilities)
    
* **Scalability**: Recommended starting point is a single TPU, scaling to a TPU Pod for production.

---

#### 10.4.3.2. Advantages of TPUs

* _TPU acceleration outperforms GPU performance by a significant margin_ 
  * Can speed up model training from months to weeks or days
  * Can reduce training time for models by orders of magnitude

---

#### 10.4.3.3. When to Use CPUs, GPUs, and TPUs

* **Hardware Choice**
  * *_CPUs_* for rapid prototyping, small models, or custom C++ operations
  * *_GPUs_* for existing source code changes, medium-to-large models, or unavailable TPUs ops
  * *_TPUs_* for matrix computations, large-scale models, and weeks/months of training

* **Workloads Not Suited for Cloud TPUs**
  * Branching programs, sparse data, high precision, or deep neural networks with custom C++ operations

---

#### 10.4.3.4. Cloud TPU Programming Model

* **Data Transfer Bottleneck**: Data transfer between Cloud TPU and host memory is slow due to PCIe bus limitations.
* **Optimal Programming Model**: Execute most of the training loop on the TPU to minimize idle time and maximize performance.
* **Partial Compilation Limitation**: Partial compilation with TPU and host execution can lead to inefficient use of resources.

---

## 10.5. Provisioning for Predictions

* **Predictions Phase**: Focuses on making accurate predictions using pre-trained models.
    * _Methods_: Online prediction (near real-time) and batch prediction (reasonable time, cost optimization)
        + Continuous workload with scaling requirements
    * Key Considerations:
        + Scaling behavior
        + Ideal machine type for optimal performance

---

### 10.5.1. Scaling Behavior

* **Autoscaling in Vertex AI**: automatically scales prediction nodes when CPU usage is high
* **Monitoring Resources**: GPU usage also needs to be monitored, as it affects CPU, memory, and GPU resource utilization.

---

### 10.5.2. Finding the Ideal Machine Type

* **Cloud Deployment**
Deploy a custom prediction container as a Docker container to a Compute Engine instance, benchmarking until 90% CPU utilization is reached.
    * Determine QPS cost per hour for different machine types, considering single-threaded web server limitations.
    * GPU acceleration options available, but with restrictions on model type and region availability.

* **Edge Deployment Use Cases**
Explore deployment of trained models at edge devices, considering factors such as:
    * Model format (e.g. TensorFlow SavedModel)
    * Web server effectiveness and latency requirements
    * Throughput and resource utilization (CPU, memory, GPU)

---

### 10.5.3. Edge TPU

* **Edge Inference**: Real-time data collection and processing on limited-bandwidth devices
* _What is Edge TPU?_: A coprocessor accelerating ML inference with 4 trillion operations per second (4 TOPS) on 2 watts of power
* **Availability**: Available in various form factors for prototyping and production, sold under Coral.ai brand

---

### 10.5.4. Deploy to Android or iOS Device

* **ML Kit**: A package that brings Google's machine learning expertise to mobile developers
    * Allows deployment of models optimized for low-bandwidth devices
    * Enables offline predictions with fast response times

---

## 10.6. Summary

* **Google Cloud Hardware Options**: Available for training and prediction workloads, including GPUs and TPUs.
* **Hardware Deployment**: Deploying models to edge devices, expanding functionality and performance.
* **Cloud Computing Scalability**: Simplifies model training and prediction with various hardware accelerators.

---

## 10.7. Exam Essentials

* _Choose the Right ML Approach_
  * Pretrained Models: Use pre-trained models for straightforward problems
  * AutoML: Automate model selection and training for complex problems
  * Custom Models: Build custom models for tailored solutions
  * **Use Serverless Solutions**: Leverage pretrained models and domain-specific solutions for scalability

---

# 11. Chapter 5Architecting ML Solutions

---

## 11.1. Designing Reliable, Scalable, and Highly Available ML Solutions

* **ML Pipeline Steps**: Data collection, data transform, model training, model tuning, model deploying, model monitoring
    * **Automating Pipeline**: Google Cloud Storage, Dataflow, scalable compute (distributed training)
        + *_Google Vertex AI_* for custom training and hyperparameter tuning
    * **Model Deployment**: *_Vertex AI Prediction_*
    * *_Reproducing Pipeline_*: *_Vertex AI Pipelines_*

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

**Overview of Google Cloud ML Services**

* **Top Layer**: AI Solutions (e.g., Document AI, Contact Center AI) - Managed SaaS offerings for easy implementation
	+ Built on top of Vertex AI services
* **Middle Layer**: Vertex AI - Includes pretrained APIs, AutoML, and Workbench for building custom models
	+ Serverless and scalable
* **Bottom Layer**: Infrastructure (compute instance, containers, TPUs, GPUs, storage) - Managed by user for scalability and reliability

---

*Choosing an Appropriate ML Service*
GCP Service | When to Use
---|---
BigQuery ML | You have structured data stored in a BigQuery data warehouse because BigQuery ML requires a tabular dataset. You are comfortable with SQL and the models available in BigQuery ML match the problem you are trying to solve. We are going to cover all the models in Chapter 14.
AutoML (in the context of Vertex AI) | Your problem fits into one of the types that AutoML supports, such as classification, object detection, sentiment analysis, and translation.

<!-- _class: centered -->

---

## 11.3. Data Collection and Data Management

* **Data Stores**: 
    * _Google Cloud Storage_: Object storage for large files and blobs
    * **BigQuery**: Fully managed, SQL-like query engine for structured data
    * _Vertex AI's datasets_: For training and annotation sets in machine learning
        * Vertex AI Feature Store: For managing features and their versions

---

### 11.3.1. Google Cloud Storage (GCS)

* **Google Cloud Storage**: stores objects like images, videos, audio, and unstructured data
* **Data Sharding**: combines individual data types into large files (over 100 MB) with up to 10,000 shards for improved read/write throughput

---

### 11.3.2. BigQuery

* **Use BigQuery for tabular data storage**: faster speed with table format instead of view.
* **Access BigQuery**: Google Cloud console, bq command-line tool, BigQuery REST API, Vertex AI Jupyter Notebooks
    * **Supported frameworks**: TensorFlow/tfio, TFX, Dataflow, and other using the Python Client library

---

*BigQuery*
Framework | Google Cloud tool to read data from BigQuery
---|---
TensorFlow or Keras | `tf.data.dataset reader for BigQuery` and tfio.BigQuery.BigQueryClient()

<!-- _class: centered -->

---

### 11.3.3. Vertex AI Managed Datasets

* **Managed Datasets**: Use Vertex AI managed datasets for training custom models, providing benefits such as centralized management, integrated labeling, and easy tracking of lineage.
* * *
  • Managed datasets support image, video, tabular (CSV, BigQuery tables), and text formats
  • Integrated data labeling for unlabeled unstructured data using Vertex AI data labeling

---

### 11.3.4. Vertex AI Feature Store

* **Vertex AI Feature Store**: Fully managed repository for organizing ML features.
    * _Allows independent use or integration with Vertex AI workflows_
    * Enables fast online predictions, batch exports, and feature creation
        * _Reduces need to compute and save feature values manually_

---

### 11.3.5. NoSQL Data Store

**NoSQL Data Stores for Static Feature Lookup**
=============================================

### Overview

For static feature lookup during prediction, analytical data stores like BigQuery are not suitable due to low-latency singleton read operations. Instead, use a NoSQL database optimized for such operations.

### NoSQL Data Store Options
| **Data Store** | **Description** | **Use Cases** |
| --- | --- | --- |
| Memorystore | Managed in-memory database with submillisecond latency | User-feature lookup, media gaming applications |
| Datastore | Fully managed, scalable NoSQL document database | Product recommendation system, fraud detection |

---

| Bigtable | Massively scalable NoSQL database service with low-latency workloads | Ad prediction, booking recommendation |

### Performance Considerations
* Avoid storing data in block storage (e.g. NFS, VM hard disk)
* Store data in Google Cloud Storage or BigQuery instead of directly reading from databases like Cloud SQL for performance

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

* **Machine Learning Workflows**: Data collection, preprocessing, model training, evaluation, and deployment phases
    * **Automation**: Orchestrate pipeline steps for continuous model training
        + Requires integration with production environment using Kubeflow or Vertex AI Pipelines

---

### 11.4.1. Use Vertex AI Pipelines to Orchestrate the ML Workflow

**Vertex AI Pipelines**
=======================

*   **Overview**: Automates, monitors, and governs ML systems using serverless orchestration and storing workflow artifacts in Vertex ML Metadata.
*   **Supported Frameworks**: TensorFlow Extended v0.30.0+, Kubeflow Pipelines v1.8.9+ or higher
*   **Key Benefits**:
    *   Simplifies pipeline management across different ML environments
    *   Reduces node count and resource requirements due to serverless architecture

---

### 11.4.2. Use Kubeflow Pipelines for Flexible Pipeline Construction

* **Kubeflow Overview**: An open source Kubernetes framework for developing and running portable ML workloads.
    * **Key Features**:
        * Composes, orchestrates, and automates ML systems
        * Supports local, on-premises, and cloud deployments (e.g., Google Cloud)
    * **Pipeline Orchestration**: Executes required Google Cloud services to automate production ML pipelines.

---

### 11.4.3. Use TensorFlow Extended SDK to Leverage Pre‐built Components for Common Steps

* **TFX and TensorFlow**: frameworks for defining, launching, and monitoring machine learning models in production
    * Recommended for using structured and textual data with existing TensorFlow setup
    * Useful for working with large datasets

---

### 11.4.4. When to Use Which Pipeline

* **Vertex AI Pipelines**: Run pipelines with Kubeflow Pipelines SDK v1.8.9 or higher, or TensorFlow Extended v0.30.0 or higher.
    * **Orchestration**: Kubeflow Pipelines and TFX provide GUIs for easy configuration, operation, monitoring, and maintenance of ML pipelines.
        * **Recommendation**: Use Vertex AI Pipelines for its built-in support for common ML operations and lineage tracking, which is crucial for validating pipeline correctness in production.

---

## 11.5. Serving

* **Machine Learning Model Deployment**: After training, evaluation, and tuning, an ML model is deployed to production for predictions.
    * **Prediction Methods**: 
        * _Offline Prediction_: Predictions made using the trained model without real-time data.
        * **Online Prediction**: Predictions made using the trained model with real-time data.

---

### 11.5.1. Offline or Batch Prediction

* **Offline Batch Prediction**: Performing predictions on large batches of data without an active internet connection.
* Use cases include: recommendations, demand forecasting, segment analysis, and text classification.
* Can be run using Vertex AI with data stored in BigQuery or Google Cloud Storage.

---

### 11.5.2. Online Prediction

**Online Predictions**
* **Synchronous**: caller waits for prediction before performing subsequent steps
* **Asynchronous**: end user gets notified or polls a data store for real-time predictions using **Push** (notification) or **Poll** (periodic queries)

**Minimizing Latency**
* Minimize latency at the model level: smaller models with fewer neural network layers and less compute
* Minimize latency at the serving level: low-latency read lookup data store, precomputing predictions, and caching

---

## 11.6. Summary

* **Designing Reliable ML Solutions on GCP**
    * Best practices for designing scalable and highly available ML solutions
    * Service selection from the GCP AI/ML stack (Layers 1-3)
* **Data Management and Storage**
    * Data collection and management strategy in Vertex AI platform with BigQuery
    * NoSQL data store options for submillisecond latency
* **Automation and Orchestration**
    * Techniques for ML pipeline automation (Vertex AI Pipelines, Kubeflow Pipelines, TFX pipelines)

---

## 11.7. Exam Essentials

* **Key Considerations for Scalable ML Solutions**
  * Choose an appropriate ML service based on your use case and expertise.
  * Implement data collection, management, and automation/orchestration strategies.
  * Deploy models using best practices for serving data, including batch vs real-time predictions and latency management.

---

# 12. Chapter 6Building Secure ML Pipelines

---

## 12.1. Building Secure ML Systems

* **Data Security in Cloud Systems**: Google Cloud provides built-in security measures to protect user and employee data
    * Encryption of stored data (at rest) is used to secure data on servers
    * Encryption of data in transit is used to secure data during transfer between systems

---

### 12.1.1. Encryption at Rest

* **Encryption in Google Cloud** 
    * Data is encrypted at rest by default using customer-managed or service-managed encryption keys
    * Can use Authenticated Encryption with Associated Data (AEAD) for table-level encryption in BigQuery
* **Hashes for data integrity** 
    * Google Cloud Storage supports CRC32C and MD5 hashes to check data integrity
* **Encryption types**
    * Server-side encryption: occurs after data is received, before storage
        * _Key management using Google Cloud Key Management Service_
    * Client-side encryption: occurs before data is sent, resulting in encrypted data that also undergoes server-side encryption

---

*Encryption at Rest*
Server‐Side Encryption | Client‐Side Encryption
---|---
Encryption that occurs after the cloud storage receives your data, but before the data is written to disk and stored. | Encryption that occurs before data is sent to Cloud Storage and BigQuery. Such data arrives at Cloud Storage and BigQuery already encrypted but also undergoes server‐side encryption.
You can create and manage your encryption keys using a Google Cloud Key Management Service. |  You are responsible for the client‐side keys and cryptographic operations.

<!-- _class: centered -->

---

### 12.1.2. Encryption in Transit

* **Data Encryption**: Google Cloud uses Transport Layer Security (TLS) to encrypt data in transit.

---

### 12.1.3. Encryption in Use

* **Encryption in Use**: protects data in memory from compromise by encrypting it while processing
    * Examples: _Confidential Computing_, Confidential VMs, and Confidential GKE Nodes
        * **Data Security Resources**: [https://cloud.google.com/blog/topics/developers-practitioners/data-security-google-cloud](https://cloud.google.com/blog/topics/developers-practitioners/data-security-google-cloud)

---

## 12.2. Identity and Access Management

* **IAM Overview**: Identity and Access Management (IAM) manages access to data and resources in Google Cloud.
    * _Manage access at project or resource level._
    * _Customize permissions using project-level and resource-level policies._

* **Project-Level Roles**: Grant access to resources by assigning roles to principals (users, groups, or service accounts).
    * *_Grant write permission to particular feature stores_*
    * *_Read permission for all users_* 

* **Vertex AI IAM Roles**:
    * _Predefined roles:_ Vertex AI Administrator and User
    * _Basic roles:_ Owner, Editor, Viewer
    * _Custom roles:_ Create own role with specific permissions

---

### 12.2.1. IAM Permissions for Vertex AI Workbench

* **Vertex AI Workbench**: A Google Cloud Platform data science service that uses JupyterLab to explore and access data.
* **Notebook Types**:
  * **User-Managed Notebook**: Highly customizable, but requires more setup and management.
  * **Managed Notebook**: Less customizable, with features like automatic shutdown and integration with Cloud Storage and BigQuery.
* **Access Modes**:
  * **Single User Only**: Grants access only to the specified user.
  * **Service Account**: Grants access to a service account, allowing multiple users to access.

---

### 12.2.2. Securing a Network with Vertex AI

* **Google Cloud Shared Responsibility Model**: The cloud provider is responsible for monitoring and responding to security threats, while users are responsible for protecting their data and assets.
* **Shared Fate Model**: An ongoing partnership between the cloud provider and customer to improve security, with components including:
  * **Help getting started**: Secure blueprints and infrastructure as code (IaC)
  * **Risk protection program**
  * **Assured workloads and governance**

---

#### 12.2.2.1. Securing Vertex AI Workbench

* **Secure your managed notebooks instance**
  * Use a private IP address when creating a workbench to reduce exposure and increase security.
  * Connect the instance to a VPC network using private services access or shared VPC network to use internal IP addresses.

* _Best practices for securing Vertex AI Workbench_
  * Enable private services access in your VPC network
  * Use VPC Service Controls to control access to specific services and limit traffic

---

#### 12.2.2.2. Securing Vertex AI Endpoints

**Vertex AI Endpoints**

* **Public Endpoint**: publicly accessible to the Internet, available by default when creating an endpoint.
* **Private Endpoint**: securely connects to your data without traversing the public Internet, requires VPC Network Peering setup.
    * Set up private endpoints from the Vertex AI console, select "Private" option under "Create Endpoint".
* **VPC Network Peering**: enables direct connection between your VPC network and Vertex AI for secure communication.

---

#### 12.2.2.3. Securing Vertex AI Training Jobs

**Connecting to Vertex AI Training Jobs with Private IP Addresses**

Using private IP addresses provides more network security and lower latency than public IP addresses.
*   **Benefits:** Improved network security and reduced latency
*   **Method:** Peer your network with Vertex AI custom training jobs using VPC (see [https://cloud.google.com/vertex-ai/docs/training/using-private-ip](https://cloud.google.com/vertex-ai/docs/training/using-private-ip))
*   **Additional Security Measures:** Use both VPC Service Controls and IAM for defense in depth

---

#### 12.2.2.4. Federated Learning

* **Federated Learning**: enables collaborative learning on device data while keeping training data local, ensuring privacy and security.
* **Key Benefits**:
  * Smarter models
  * Lower latency
  * Less power consumption
* **Example Use Case**: Hospitals participating in clinical trials can train shared ML models locally with secure communication to the cloud for model updates.

---

#### 12.2.2.5. Differential Privacy

* **Differential Privacy**: A system for publicly sharing dataset information while withholding individual details
* **Purpose**: Prevent sensitive data from being memorized by machine learning algorithms
* **Benefits**: Design responsible machine learning models on private data using differential privacy and federated learning techniques.

---

#### 12.2.2.6. Format‐Preserving Encryption and Tokenization

* _Format-Preserving Encryption (FPE)_ preserves the format of data during encryption, allowing only specific information to be exposed.
    * Used in: Payment Card Verification and Legacy Databases to protect sensitive data without restructures databases or storing encrypted data at a centralized location.
    * Key difference from Tokenization: FPE obfuscates sensitive info, while tokenization removes it entirely.

---

## 12.3. Privacy Implications of Data Usage and Collection

* **Sensitive Data Types**: 
  * _Personally identifiable information (PII)_, including:
    * Name
    * Address
    * Social Security number (SSN)
    * Date of birth
    * Financial information
    * Passport number
    * Telephone numbers
    * Email addresses
* **Health Information Protection**:
  * HIPAA Privacy Rule provides federal protections for _protected health information (PHI)_

---

### 12.3.1. Google Cloud Data Loss Prevention

* **Google Cloud Data Loss Prevention (DLP) API**: removes identifying information from text content, including PII, using techniques such as masking, tokenization, encryption, or bucketing.
    * _Data profiles_: identifies sensitive and high-risk data across BigQuery tables and columns
    * _Risk analysis_: determines effective de-identification strategy or monitors for changes/outliers with metrics like _k_-anonymity and _l_-diversity
* **DLP Job Architecture**:
  * _Data de-identification streaming pipeline_: uses Dataflow to trigger DLP job for sensitive data in text
  * _Configuration management_: manages templates and configuration using Cloud KMS for security

---

  * _Data validation and re-identification pipeline_: validates de-identified data, stores in BigQuery or other storage, and re-identifies with Dataflow pipeline

---
### 12.3.2. Google Cloud Healthcare API for PHI Identification

* **De-identification in Healthcare**: Removes sensitive information from healthcare data using configurable operations.
    * **Methods**:
        * Google Cloud Healthcare API: removes PHI from text, images, FHIR, and DICOM data
        * Dataflow pipeline: configures and runs the DLP API on CSVs, BigQuery tables, and text strings
* **De-identified Data**: No longer considered protected health information under HIPAA Privacy Rule.
    * **Identifiers**:
        * 18 specific PHI identifiers, as defined in HIPAA

---

### 12.3.3. Best Practices for Removing Sensitive Data

* **Handling Sensitive Data**: approaches vary based on data structure, using views, Cloud DLP, NLP API, and masking techniques.
* **Data Reduction Techniques**:
  * **PCA (Principal Component Analysis)**: combines features to reduce dimensionality, making it harder to identify individuals.
  * **Coarsening**: decreases granularity of data to make it less identifiable, while maintaining comparable benefits.
    * Examples:
      * IP addresses: zero out last octet
      * Numeric quantities: bin numbers for anonymity (e.g., age, birthdays)
      * Zip codes: coarsen to first three digits

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

* **Data Security in Machine Learning**
  * _Encryption at rest_ and _in transit_ are used to protect data
  * IAM is used for secure access control to Vertex AI Workbench
  * Secure ML development techniques like federated learning and differential privacy are employed
* **PII and PHI Data Management**
  * Cloud DLP and Cloud Healthcare APIs are used for PII and PHI data protection
  * A scalable architecture pattern for large dataset management is proposed

---

## 12.5. Exam Essentials

* **Build Secure ML Systems**:
    * Understand encryption at rest and in transit for Google Cloud
    * Set up IAM roles and network security for Vertex AI Workbench
    * Learn about differential privacy, federated learning, and tokenization

* **Understand Privacy Implications**
    * Identify and mask PII and PHI type data using DLP API and Healthcare API
    * Apply best practices for removing sensitive data

---

# 13. Chapter 7Model Building

---

## 13.1. Choice of Framework and Model Parallelism

* **Parameter growth**: Modern deep learning models require more parameters, leading to larger datasets
* **Distributed training**: Multinode training is necessary for large-scale deep learning on big datasets 
    * _Data parallelism_ vs _Model parallelism_: Both approaches are used in distributed deep learning training

---

### 13.1.1. Data Parallelism

* *_Data parallelism_*: splitting dataset among GPUs or nodes, using same parameters for forward propagation
    * Small batches are sent to every node, gradient computed and sent back to main node
    * *_Synchronous_* vs *_asynchronous_* strategies differ in distributed training

---

#### 13.1.1.1. Synchronous Training

* **Synchronous Training**: Model sends data to multiple GPUs/accelerators, each with a full model copy, computing outputs and gradients simultaneously.
* *_Key feature_*: All-reduce algorithm collects trainable parameters from all workers and accelerators.
* **Parallelization**: Multiple GPUs/accelerators work together on different parts of the data.

---

#### 13.1.1.2. Asynchronous Training

* **Asynchronous Training**: allows workers to train independently, reducing downtime and idle time.
    * **Benefits**: scalability, reduced worker downtime
        * * *

    **All-Reduce Sync Strategy**: suitable for TPU and multi-GPUs, but not ideal for all use cases.

---

### 13.1.2. Model Parallelism

* **Model Parallelism**: 
    * Model partitioning into parts, each placed on an individual GPU.
    * Benefits: scales training to multiple GPUs or machines, overcomes memory limitations of a single GPU.
* **Distributed Training Strategies in TensorFlow**:
    * MirroredStrategy: synchronous distributed training on multiple GPUs
    * ParameterServerStrategy: designated machines as workers and parameter servers for asynchronous training.

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

* **Artificial Neural Networks**: One-hidden layer network with a single output layer
* _Mainly used in supervised learning_, especially for numerical and structured data types, such as regression problems
* *Examples include feedforward neural networks*

---

### 13.2.2. Deep Neural Network (DNN)

* **Definition**: Deep neural networks are Artificial Neural Networks (ANNs) with multiple hidden layers.
* **Characteristics**: Typically have at least two layers, making them a subset of _deep nets_ or multi-layered networks.
* *_Deep Net_* refers to any ANN with multiple hidden layers

---

### 13.2.3. Convolutional Neural Network

* **Convolutional Neural Networks (CNNs)** 
    * **Key Use Case:** Image Classification
        * *Designed primarily for processing and analyzing images*

---

### 13.2.4. Recurrent Neural Network

* **Recurrent Neural Networks (RNNs)**: designed for sequences of data, effective in natural language processing and time-series forecasting.
    * _Popular RNN variant_: Long Short-Term Memory (LSTM) network
        * Used for prediction tasks like assigning class labels or predicting numerical values.
* **Neural Network Training**: trained using stochastic gradient descent with a chosen loss function.
    * _Goal of training_: find weights and biases resulting in low average loss across all examples.

---

### 13.2.5. What Loss Function to Use

* **Activation Functions and Loss Functions**: The choice of activation function in the output layer directly affects the chosen loss function.
    * _**Regression**: Mean squared error (MSE) with a linear activation unit_
    * _**Binary Classification**: Binary cross-entropy, categorical hinge loss, or squared hinge loss with sigmoid activation_
    * _**Multiclass Classification**: Categorical cross-entropy with softmax activation_
        - Use `sparse_categorical_crossentropy` for mutually exclusive classes
        - Use `categorical_cross_entropy` for non-mutually exclusive classes

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

* **Gradient Descent Algorithm** 
    * Calculates the negative gradient of the loss curve
    * Takes steps in the opposite direction of the positive gradient to minimize loss
        * Direction: Steepest descent of the loss function
            * Magnitude: Reduces the magnitude of loss with each step

---

### 13.2.7. Learning Rate

* **Learning Rate**: The scalar value used to scale the gradient vector to determine the next point in gradient descent.
    * Determines how large a step is taken at each iteration
    * Affects convergence speed and stability of the algorithm

---

### 13.2.8. Batch

* **Batch Size**: The number of examples used to calculate the gradient in a single iteration.
    * Reduces computation time for smaller batches, but increases it for larger ones
        * Helps prevent slow iterations with large datasets

---

### 13.2.9. Batch Size

* **Batch Size**: The number of examples in a batch
*   _Typical values_: 10 to 1,000 for mini-batches
*   *Fixed or dynamic*: Usually fixed, but can be dynamic with TensorFlow*

---

### 13.2.10. Epoch

* *_Epoch_*: Training iteration using all available data exactly once
* *A single epoch consists of one or more batches*
* *A forward pass and backward pass count as one pass per epoch*

---

### 13.2.11. Hyperparameters

* Hyperparameters for ML models include loss, learning rate, batch size, and epoch
    * Tuning learning rate can significantly impact training time
        * Small learning rates result in faster but slower convergence
        * Large batch sizes may speed up computation but slow down convergence

---

#### 13.2.11.1. Tuning Batch Size

* **Batch Size Tuning** 
    * A small mini-batch size improves accuracy but increases iterations and updates during training
    * Larger batch sizes reduce training time, but decrease accuracy and may cause memory issues
    * Smaller batches result in more frequent gradient updates, reducing loss per epoch

---

#### 13.2.11.2. Tuning Learning Rate

* Achieving an optimal learning rate is crucial for efficient training to avoid wasted time and resources.
* A lower learning rate results in more training time, increasing cloud GPU costs.
* If the learning rate is too small or too large, training can be slow or unstable, leading to divergence.

---

## 13.3. Transfer Learning

* **Transfer Learning**: Applying knowledge gained from one problem to a related but different problem in machine learning
*   **Deep Learning Technique**: Using a pre-trained neural network as a starting point for training on a new, similar problem
    *   _Optimization_ to save time or improve performance

---

## 13.4. Semi‐supervised Learning

* **Semi-supervised Learning**: Combines small amounts of labeled data with large amounts of unlabeled data for machine learning.
* *_Definition_*: Fills the gap between supervised and unsupervised learning, using a mix of labeled and unlabeled data during training.
* **Key characteristic**: Balances small amounts of labeled examples with large quantities of unlabeled examples.

---

### 13.4.1. When You Need Semi‐supervised Learning

**Semi-Supervised Learning**
* Increases training data size when labeled data is scarce
* Used for fraud detection, clustering, speech recognition, and more

* **Benefits:** 
    * Accurate model outputs on new, unlabeled data
    * Can be used when collecting more labeled data is not feasible

---

### 13.4.2. Limitations of SSL

* *Semi-supervised learning* uses a small amount of labeled and large amounts of unlabeled data for classification tasks.
* However, its effectiveness depends on the representativeness of labeled data in the entire distribution.
* Inaccurate results can occur if labeled data is not representative.

---

## 13.5. Data Augmentation

* **Neural Network Training**: Neural networks require a proportional number of examples to achieve good performance, and parameter complexity increases with task difficulty.
* **Data Augmentation**: To address limited data, minor alterations (flips, translations, rotations) are applied to existing datasets, creating synthetically modified data for training.
* *_Types of Data Augmentation_*:
  * Offline augmentation: altering data before training
  * Online augmentation: altering data in real-time during training

---

### 13.5.1. Offline Augmentation

* **Offline Augmentation**: Increases dataset size by performing transformations beforehand
* *Example:* Rotating images increases dataset size by a factor of 2 
* *Preferable for smaller datasets due to increased size.*

---

### 13.5.2. Online Augmentation

* **Online Data Augmentation**: Performing data augmentation transformations on mini-batches before feeding them to machine learning models.
* **Data Augmentation Techniques for Images**:
  * Flip, Rotate, Crop, Scale
  * Gaussian noise for enhanced learning capability
  * Translate
  * Conditional GANs for domain transformation

---

## 13.6. Model Generalization and Strategies to Handle Overfitting and Underfitting

* **Key Terms:**
  * _Bias:_ difference between average prediction and correct value (error rate of training data)
  * _Variance:_ error rate of testing data
    * A model with high bias oversimplifies the model and pays little attention to training data.
    * A model with high variance pays too much attention to training data, leading to poor generalization on unseen data.

---

### 13.6.1. Bias Variance Trade‐Off

* **Bias-Variance Tradeoff**: Model complexity affects bias and variance.
    * High bias (simple models): high bias, low variance
    * High variance (complex models): high variance, low bias
* **Underfitting vs Overfitting**: 
    * Increase capacity to reduce underfitting
    * Specialized techniques required for overfitting

---

### 13.6.2. Underfitting

* An **underfit model** fails to learn a problem, performing poorly on both training and test datasets.
    * High bias, low variance, and inability to learn regardless of training dataset samples.
        * Reasons for underfitting include: dirty data, high bias, or complex models not well-suited for data.
* Methods to reduce underfitting:
            * Increase model complexity
            * Increase feature engineering
            * Remove noise from data

---

### 13.6.3. Overfitting

* **Overfitting**: 
    * Model learns training data too well, resulting in low bias and high variance
    * Leads to poor performance on unseen examples or statistical noise
* **Ways to Avoid Overfitting**:
    * Regularization techniques (e.g. Dropout, Noise)
    * Early stopping: stop training when model performance degrades

---

### 13.6.4. Regularization

* **Regularization**: Shrinks learned estimates toward 0, reducing overfitting by adding a penalty term to the loss function.
    * _L1 Regularization_: Combats overfitting by making some features obsolete, robust to outliers, and helps with feature selection.
    * _L2 Regularization_: Forcing weights to be small but not exactly 0, improving generalization in linear models.

* **Training Issues**:
    * *_Exploding Gradients_*: Batch normalization, lower learning rate, and regularization techniques help prevent large gradients that cause convergence issues.
    * *_Dead ReLU Units_*: Lowering the learning rate can help ReLU units recover from getting stuck below 0.

---

    * *_Vanishing Gradients_*: Using ReLU instead of sigmoid activation function helps prevent small gradients.

* **Improving Training**:
    * Increase depth and width of neural network
    * Decrease learning rate or increase test data for smaller datasets

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

* **Summary of Chapter**
  * Covered model parallelism and data parallelism strategies
  * Discussed neural network training techniques (loss functions, gradient descent, hyperparameters)
    * Examined importance of hyperparameters on network performance
  * Explored transfer learning and semi-supervised learning concepts

---

## 13.8. Exam Essentials

* **Parallelism**: Choose between framework or model parallelism for large neural networks.
    * _Data Parallel_: Train on multiple nodes with identical data
    * _Model Parallel_: Split model across multiple nodes, each node computes a portion of the model
* 
* **Hyperparameter Tuning**:
  * Understand loss functions (sparse cross-entropy, categorical cross-entropy)
  * Learn from hyperparameters: gradient descent, learning rate, batch size, epoch
  * Strategies to tune: grid search, random search, Bayesian optimization
* 
* **Transfer Learning and Transfer Augmentation**: Pretrained models trained on large datasets can help with limited data.

---

    * Use pre-trained models as a starting point for your own model
    * Apply transfer learning to adapt models to new tasks
*

---
# 14. Chapter 8Model Training and Hyperparameter Tuning

---

## 14.1. Ingestion of Various File Types into Training

* Data for training can be structured (e.g., tables, CSV files), semi-structured (e.g., PDFs, JSON files) or unstructured (e.g., chats, audio)
* Data types include batch data or real-time streaming data
* Data size ranges from small megabytes to petabyte scale

---

### 14.1.1. Collect

* **Batch/Streaming Data Collection**: 
  * _Use Google Cloud services to collect batch or streaming data from various sources_
  * **Google Pub/Sub and Pub/Sub Lite**:
    * Real-time analytics with scalable performance
    * Stream data directly to BigQuery from third-party applications
    * Optimized for cost over reliability (Pub/Sub Lite)
  * **Datastream**: 
    * Serverless CDC and replication service for heterogeneous databases
    * Supports streaming from Oracle and MySQL databases into Cloud Storage
    * Integrated with Dataflow and leverages templates for load data into BigQuery, Cloud Spanner, and Cloud SQL
  * **BigQuery Data Transfer Service**:

---

    * Load data from external sources (Teradata, Amazon Redshift, S3) into BigQuery

---
### 14.1.2. Process

* *_Data Preprocessing Tools_*
	+ Data cleaning and handling
	+ Data transformation and normalization
	+ Feature engineering and extraction

---

#### 14.1.2.1. Cloud Dataflow

* **Cloud Dataflow**: Serverless, fully managed data processing service for streaming and batch data
    * Uses Apache Beam with exactly-once streaming semantics, ensuring each message is processed only once
    * Allows building pipelines, monitoring execution, transforming, and analyzing data to simplify business logic

---

#### 14.1.2.2. Cloud Data Fusion

* **Cloud Data Fusion**: A UI-based ETL (Extract, Transform, Load) tool for data integration and processing without coding.

---

#### 14.1.2.3. Cloud Dataproc

* **Dataproc**: A fully managed service for running Apache Spark, Flink, Presto, and 30+ open-source tools on Google Cloud Platform.
    * Supports batch processing, querying, streaming, and machine learning
    * Automates cluster creation, management, and shutdown to reduce costs
* **Integration with other services**:
    * Seamlessly integrates with BigQuery for data transformation and reporting
    * Uses HDFS for storage and automatically installs the Cloud Storage connector
* **Connectors**: Supports various connectors such as Cloud Storage, BigQuery, Cloud Bigtable, and Pub/Sub Lite Spark connector.

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

* **Cloud Composer**: a fully managed data workflow orchestration service using Apache Airflow.
    * Supports hybrid and multicloud architecture for on-premises, multiple clouds, or Google Cloud.
    * Integrates end-to-end with Google Cloud products such as BigQuery, Dataflow, and Dataproc.

---

#### 14.1.2.5. Cloud Dataprep

* **Cloud Dataprep**: A UI-based ETL tool for visual exploration, cleaning, and preparing structured and unstructured data for analysis, reporting, and machine learning.

---

#### 14.1.2.6. Summary of Processing Tools

* **Summary of Processing Tools**: 
    * _Dataflow_: for batch and interactive processing
    * _Fusion Tables_: for real-time analytics
    * _Cloud Functions_: for event-driven processing
* Note: Not exhaustive, as figure is not shown.

---

### 14.1.3. Store and Analyze

* **Data Storage Options**
  * Tabular data: BigQuery, BigQuery ML
  * Image, video, audio, unstructured data: Google Cloud Storage
  * Unstructured data: Vertex Data Labeling, Vertex AI Feature Store
* 
* **Storage Best Practices**
  * Avoid storing data in block storage like NFS and VMs
  * Use large container formats on Cloud Storage for image, video, audio, and unstructured data

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

* **Vertex AI Workbench Overview**: A Jupyter Notebook-based environment for data science workflow, integrating with Google Cloud services.
* **Managed Notebooks vs User-Managed Notebooks**:
    * Managed notebooks: More features, automatic shutdown, UI integration with Cloud Storage and BigQuery, automated notebook runs.
    * User-managed notebooks: Fewer features, no automatic shutdown, UI integration limitations, custom containers and frameworks available.
    * Consider user-managed notebooks for specific networking and security needs.

---

*Developing Models in Vertex AI Workbench by Using Common Frameworks*
Managed notebook | User‐managed notebook
---|---
**Automated shutdown for idle instances:** Choosing a managed notebook will shut down your Jupyter Notebooks when not in use. This feature helps save costs because the instances will shut down when not in use automatically. | **Automated shutdown for idle instances:** This feature is not supported out of the box. However, you can create a monitor to see when instances are idle using Cloud Monitoring and Cloud Functions and shut them down when not in use.
**UI integration with Cloud Storage and BigQuery:** From within JupyterLab's navigation menu on a managed notebooks instance, you can use the Cloud Storage and BigQuery integration to browse data and other files that you have access to and load data into your notebook. | **UI integration with Cloud Storage and BigQuery:** There is no UI integration. However, you can use the BigQuery connector to connect to BigQuery data using code or you can also use the BigQuery magic (`%%`) command to run BigQuery SQLl commands on a Jupyter Notebook.

<!-- _class: centered -->

---

### 14.2.1. Creating a Managed Notebook

**Creating a Managed Notebook in Vertex AI**
* Go to Vertex AI and enable all APIs
* Click on Workbench > New Notebook and create the notebook
* Wait for it to be created, then click "Open JupyterLab" to access your environment

---

### 14.2.2. Exploring Managed JupyterLab Features

* **Getting Started**: After clicking Open JupyterLab, frameworks like Serverless Spark and PySpark are available for use.
    * **Features**: The JupyterLab environment comes with tutorials, a terminal option to run commands on the entire notebook.
    * **Notebook Environment**: Supports running Dataproc cluster within the notebook.

---

### 14.2.3. Data Integration

* Open the Browse GCS icon in the left navigation bar
* Load data from cloud storage folders
* Access Google Cloud Storage directly from the managed notebook

---

### 14.2.4. BigQuery Integration

* Click the BigQuery icon to access your BigQuery tables
* Alternatively, use the Open SQL editor to query tables directly from JupyterLab

---

### 14.2.5. Ability to Scale the Compute Up or Down

* *_Access Click N1-Standard-4 instance_* 
    * *_Modify hardware settings_* 
        * *_Attach GPU (if available)_*

---

### 14.2.6. Git Integration for Team Collaboration

* Integrate or clone an existing git repository for project collaboration
    * Use the left navigation branch icon or run `git clone <your-repository name>` in the terminal

---

### 14.2.7. Schedule or Execute a Notebook Code

* **Execute a Notebook Automatically**: Click Execute in Jupyter interface to execute notebooks manually or set up auto-execution by clicking on the triangle black arrow.
    * To enable auto-execution, click on Submit notebooks to Executor and select scheduling options.
* **Scheduling Options**: Choose Type option to schedule notebook run for one-time execution or at a scheduled time.

---

### 14.2.8. Creating a User‐Managed Notebook

* **Choosing User-Managed Notebooks**: 
    * Select a framework (e.g., Python 3, TensorFlow) when creating a notebook.
    * Configure networking with shared VPCs for advanced options.

* **Key Features**:
    * No need for large hardware or compute instance for development in JupyterLab.
    * Training and prediction are performed outside the notebook environment using SDKs or APIs.

---

## 14.3. Training a Model as a Job in Different Environments

* **Vertex AI Training Modes**: 
  * _AutoML_: Minimal technical effort required
  * Custom training: Full control over model development and outcome targeting

---

### 14.3.1. Training Workflow with Vertex AI

* **Training Options in Vertex AI**
  * Training pipelines: orchestrate custom training jobs and hyperparameter tuning for AutoML or custom models
    * Create AutoML‐trained model or custom‐trained model
    * Add dataset or upload model to Vertex AI for prediction serving
  * Custom jobs: specify settings for custom training code, including worker pools and machine types
    * Used by custom‐trained models only
  * Hyperparameter tuning jobs: search for best hyperparameter combination (not supported in AutoML)

---

### 14.3.2. Training Dataset Options in Vertex AI

**Training Datasets on Vertex AI**

* **Dataset Options**
  * _No Managed Dataset_: Use Cloud Storage or BigQuery data, integrating with Vertex AI notebooks via GCS FUSE.
  * _Managed Dataset_: Centralized management of datasets, labeling, and governance, including automatic splitting and performance tracking.

**Mounting NFS Shares for Remote File Access**

* Configure custom training jobs to mount NFS shares, accessing remote files as local with high throughput and low latency.

---

### 14.3.3. Pre‐built Containers

* **Pre-built Container Setup**: Organize code according to application structure, upload training code to Cloud Storage bucket, and choose compute instances.
    * Use standard dependencies or libraries by specifying in `setup.py`.
    * Create a source distribution using `sdist` command.
* **Creating Custom Job**: 
    * Build Docker image based on prebuilt container image and local Python code
    * Push image to Container Registry and create custom job using `gcloud ai custom-jobs create`
        * Specify region, display name, worker pool spec, and executor image URI.

---

### 14.3.4. Custom Containers

* **Benefits of Custom Container**
  * Faster start-up time
  * Use the ML framework of your choice
  * Extended support for distributed training
  * Use the newest version of an ML framework

* **Creating a Custom Container for Vertex AI Training**

1. Create a Dockerfile, build and push to Artifact Registry:
  * Set up files with required folder structure
  * Install dependencies and copy training code
  * Configure entry point to invoke training code
2. Use the following commands to build and run the container:
  ```bash
docker build -f Dockerfile -t ${IMAGE_URI} .
docker run ${IMAGE_URI}
```
3. Push the image to Artifact Registry and create a custom job:
  ```

---

gcloud ai custom-jobs create \
   --region=_LOCATION_ \
   --display-name=_JOB_NAME_ \
   --worker-pool-spec=machine-type=_MACHINE_TYPE_ ,replica-count=_REPLICA_COUNT_ ,container-image-uri=_CUSTOM_CONTAINER_IMAGE_URI_
```

---
### 14.3.5. Distributed Training

* To run a distributed training job with Vertex, specify multiple machines (nodes) in the training cluster
    * Configure worker pools with different tasks and replicas, including primary, secondary, workers, parameter servers, reduction server, and evaluators
    * Use CLUSTER_SPEC or TF_CONFIG environment variables to reference specific parts of the training cluster

---

*Distributed Training*
Position in workerPoolSpecs[] | Task Performed in Cluster
---|---
First (`workerPoolSpecs[0]`) | Primary, chief, scheduler, or “master.” Exactly ‐one replica is designated the _primary replica_. This task manages the others and reports status for the job as a whole.
Second (`workerPoolSpecs[1]`) | Secondary, replicas, workers.

<!-- _class: centered -->

---

## 14.4. Hyperparameter Tuning

* **Hyperparameters**: parameters set before training that are not learned directly from data
    * _Defined by the algorithm itself_
    * Not adjusted during training, but rather chosen beforehand
        * Examples: learning rate, regularization strength, batch size
    * Must be tuned before training begins

---

### 14.4.1. Why Hyperparameters Are Important

* **Hyperparameter Selection**: crucial for neural network success
    * Influences model behavior and predictive accuracy
    * Involves searching hyperparameter space efficiently using algorithms like Grid Search, Random Search, or Bayesian Search
        + **Search Algorithms**:
            * *_Grid Search_*: exhaustive search through manually specified hyperparameters
            * *_Random Search_*: generates random combinations of hyperparameters to find best solution
            * *_Bayesian Search_* (Vertex AI default): uses past evaluations to select next hyperparameter set

---

### 14.4.2. Techniques to Speed Up Hyperparameter Optimization

* **Hyperparameter Optimization Techniques**
  * Use simple validation sets instead of cross-validation for large datasets
  * Parallelize training across multiple machines using distributed computing
  * Cache pre-computed computations to avoid redundant calculations
  * Decrease number of hyperparameter values to consider in grid search

---

### 14.4.3. How Vertex AI Hyperparameter Tuning Works

* **Hyperparameter Tuning**: runs multiple trials with varying hyperparameters to optimize target metrics, such as accuracy.
  * **Custom Job Configuration**:
    * Create a `config.yaml` file specifying API fields, including metric ID, goal, parameter ID, and search algorithm.
    * Define VM type, Docker container image URI, and trial count for the custom job.
* **Hyperparameter Tuning Steps**:
  * Install `cloud-ml hypertune` package in the Dockerfile for a custom container.
  * Add hyperparameter tuning code to the training application's main function.
  * Build and push the container to Artifact Registry, then configure a hyperparameter tuning job using gcloud CLI commands.

---

### 14.4.4. Vertex AI Vizier

* **Vertex AI Vizier**: black-box optimization service for complex ML models without known objective functions
* **Use cases**:
  * Tuning hyperparameters for neural network recommendation engines
  * Optimizing user interface elements and computing resources
  * Identifying optimal recipe ingredient ratios

---

#### 14.4.4.1. How Vertex AI Vizier Differs from Custom Training

* **Vertex AI Vizier**: independent service for optimizing complex models with many parameters
* **Use cases**: ML and non‐ML, training jobs or integration with other systems (multicloud)
* *_Hyperparameter tuning_*: uses Vertex AI Vizier to determine best settings for an ML model, using Bayesian optimization by default

---

## 14.5. Tracking Metrics During Training

* **Tracking Machine Learning Model Metrics**: 
  * Using interactive shells
  * TensorFlow Profiler
  * What‐If Tool

---

### 14.5.1. Interactive Shell

* **Interactive Shell in Vertex AI**: 
    * Enable an interactive shell by setting enableWebAccess API field to true while setting up custom jobs programmatically or checking Enable training debugging in the console.
    * Available only while job is in RUNNING state; link to web terminal created for each node.

* **Logging and Metrics**:
    * Logs available in Cloud Monitoring after Vertex AI exports metrics.
    * View logs by clicking on the View logs link on the Vertex AI training page.

* **Tools for Tracking Metrics and Profiling**:
    * py-spy: visualizes Python program execution time
    * `nvidia-smi` and `nvprof`: monitors GPU usage in GPU-enabled containers

---

    * Perf: analyzes performance of training node using Linux profiling with performance counters

---
*Interactive Shell*
Visualize Python Execution with py‐spy | Retrieve Information about GPU Usage | Analyze Performance with Perf
---|---|---
py‐spy is a sampling profiler for Python programs. It lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way. | GPU‐enabled containers running on nodes with GPUs typically have several command‐line tools preinstalled that can help you monitor GPU usage. You can use `nvidia‐smi` to monitor GPU utilization of various processes or use `nvprof` to collect a variety of GPU profiling information. | Perf lets you analyze the performance of your training node. It's a way to do Linux profiling with performance counters.

<!-- _class: centered -->

---

### 14.5.2. TensorFlow Profiler

* **Vertex AI TensorBoard Profiler**: Monitors model training performance, pinpoints bottlenecks for faster and cheaper training.
* **Accessing the dashboard**: Custom jobs page or experiments page in Google Cloud console.
* *To capture a profiling session, ensure your training job is in RUNNING state.*

---

### 14.5.3. What‐If Tool

* **Interactive Visualization of AI Models**: The What-If Tool allows you to inspect and compare AI Platform Prediction models using an interactive dashboard.
* **Configuration Steps**:
  * Install the `witwidget` library and configure `WitConfigBuilder`
  * Set model details, target feature, and label vocabulary
  * Pass `config_builder` to `WitWidget` with a specified display height

---

## 14.6. Retraining/Redeployment Evaluation

* *_Data drift_*: Change in the distribution of training data over time
* *_Concept drift_*: Change in the underlying patterns or relationships in the data
* *_Model performance decay_*: Gradual decrease in model accuracy as user behavior and training data evolve

---

### 14.6.1. Data Drift

* **Data Drift**: Change in statistical distribution of production data from baseline data used to train or build the model
    * _Causes_: change in feature attribution, change in input data (e.g., unit changes)
    * _Detection_: examining feature distribution, correlation between features, or checking data schema

---

### 14.6.2. Concept Drift

* **Concept Drift**: Change in statistical properties of the target variable over time
    * Example: Sentiment analysis models may need to adapt as user opinions evolve
    * _Monitoring deployed models can help detect drift_, using tools like Vertex AI Model Monitoring.

---

### 14.6.3. When Should a Model Be Retrained?

* **Retraining Strategies**: 
  * Periodic training: Retrain model at set intervals (e.g., weekly, monthly) based on updated training data alignment with business use case.
  * Performance-based trigger: Retrain if model performance falls below threshold, assuming sophisticated monitoring system.
  * Data changes trigger: Retrain when data drift occurs in production.

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

* **Testing Challenges**: testing machine learning systems is hard due to the interconnected code, model, and data
* **Model Testing**
    * *_Unit tests_*: test individual units of code (e.g., ensuring a single gradient step decreases loss)
        * Checking output shapes and ranges align with expectations
        * Verifying decrease in loss after one gradient step on batch data

---

### 14.7.1. Testing for Updates in API Calls

* **Testing API Updates**: Instead of retuning the entire model, write a unit test with random input data to verify a single step of gradient descent completes without errors.
    * This method is more resource-efficient than retraining the entire model.
    * It allows for quick validation and testing of API updates.

---

### 14.7.2. Testing for Algorithmic Correctness

* **Validate Model Correctness**:
	+ Train model for iterations, verify loss decreases
	+ Train without regularization, verify memorization (loss close to 0)
	+ Test specific subcomputations (e.g., network parts run once per input element)

---

## 14.8. Summary

* **AI/ML File Ingestion**: stages of file ingestion (collect, process, store, analyze) with services like Pub/Sub, BigQuery Data Transfer Service, and Datastream
    * **Model Training**: training using Vertex AI with frameworks scikit-learn, TensorFlow, PyTorch, XGBoost
        * **Model Evaluation**: unit testing, hyperparameter tuning, and tracking with Vertex AI interactive shell and metrics
* **Hyperparameter Tuning**: search algorithms (e.g. Grid Search) and tools like Vertex AI Vizier

---

## 14.9. Exam Essentials

* **File Ingestion**: Understand various file types (structured, unstructured, semi-structured) for AI/ML workloads in GCP. Use Pub/Sub, BigQuery Data Transfer Service, and Cloud Dataflow for data ingestion.
* **Vertex AI Workbench**: Understand feature differences between managed and user-managed notebooks. Know when to use each type of notebook and how to create them.
    * Manage environment and frameworks (scikit-learn, TensorFlow, PyTorch, XGBoost) using Vertex AI training along with architecture.

---

* **Model Training and Serving**: Unit test data and models for machine learning, test API updates, and algorithm correctness. Track metrics during training using Interactive shell, Tensorflow Profiler, and What‐If tool.
    * Understand hyperparameter tuning (grid search, random search, Bayesian search) and use custom jobs to set up tuning.
* **Hyperparameter Tuning**: Use Vertex AI Vizier for hyperparameter tuning, understanding its differences from setting up custom hyperparameter tuning.

---
# 15. Chapter 9Model Explainability on Vertex AI

---

## 15.1. Model Explainability on Vertex AI

* **Model Prediction Explainability**: As model impact on business outcomes increases, model developers' responsibility to explain predictions also grows.
    * _High-stakes applications_: Model developers must justify decisions like loan approvals or patient medication doses.
    * _Low-stakes applications_: Consumers may not need explanations for movie recommendations.

---

### 15.1.1. Explainable AI

* **Explainability** refers to understanding an ML or deep learning system's internal mechanics.
  * _Global explainability_ makes the overall model transparent and comprehensive.
  * _Local explainability_ explains individual predictions.
* Explainability builds trust, improves adoption, and helps with debugging complex models.

---

### 15.1.2. Interpretability and Explainability

* **Interpretability vs Explainability**: 
    * _Interpretability_ focuses on associating causes with effects.
    * _Explainability_ focuses on understanding model parameters' influence on results.

---

### 15.1.3. Feature Importance

* **Feature Importance**: technique that assigns scores to features based on their contribution to model predictions.
    * **Benefits**:
        * _Variable selection_: remove unnecessary variables to save compute and infrastructure costs and training time.
        * **Data leakage prevention**: identify target variable as a feature to avoid data leakage and incorrect results.

---

### 15.1.4. Vertex Explainable AI

* **Vertex Explainable AI**: integrates feature attributions into Vertex AI to understand model outputs for classification and regression tasks.
    * Provides insights into feature contributions to predicted results, enabling model verification, bias recognition, and improvement ideas.
        * Supports AutoML models, custom-trained TensorFlow models based on tabular or image data.

---

#### 15.1.4.1. Feature Attribution

**Vertex AI Feature Attribution**

* **Method 1: Sampled Shapley**
	+ Assigns credit to each feature, considering different permutations
	+ Provides a sampling approximation of exact Shapley values
	+ Used for nondifferentiable models (e.g. ensembles of trees and neural networks)
* **Method 2: Integrated Gradients**
	+ Gradient-based method for efficient computation
	+ Mostly used in deep neural networks with image use cases
	+ Provides feature importance on individual examples, but not global
* **Method 3: XRAI (eXplanation with Ranked Area Integrals)**
	+ Combines integrated gradients with additional steps to determine region contributions

---

	+ Used for image data and models that accept image inputs
	+ Provides explanations in images by highlighting relevant regions

---
*Feature Attribution*
Method | Supported Data Types | Model Types | Use Case | Vertex AI–Equivalent Model
---|---|---|---|---
Sampled Shapley | Tabular | Nondifferentiable models (explained after the table), such as ensembles of trees and neural networks. | Classification and regression on tabular data | Custom‐trained models (any prediction container)

<!-- _class: centered -->

---

#### 15.1.4.2. Vertex AI Example–Based Explanations

* **Active Learning with Example-Based Explanations**: Enables selective labeling of data using explanations that show which class an instance belongs to.
    * Can be applied to various data types (images, text, tables).
        * Currently in public preview and not included in the exam questions.

---

### 15.1.5. Data Bias and Fairness

* **Data Bias**: occurs when certain parts of data are not collected or misrepresented, leading to skewed outcomes.
    * Examples: surveys with biased questions, systemic or historical beliefs, non-random sampling, or small sample sizes.
* **ML Fairness**: ensures that biases in data and model inaccuracies do not lead to unfair treatment of individuals based on characteristics such as race, gender, etc.
    * Techniques for detection:
        * AutoML tables: Explainable AI feature attributions
        * Vertex AI interactive dashboard with What-If Tool (features overview functionality)
* **Bias Detection Tools**: 
    * Language Interpretability Tool (for NLP models)

---

### 15.1.6. ML Solution Readiness

**ML Solution Readiness**

* _Key concepts:_ **Responsible AI**, **Model Governance**
* 
  * **Responsible AI:** Use tools like Explainable AI, Model cards, and TensorFlow open source toolkit to inspect and understand AI models.
  * **Model Governance:**
    * Assign responsibility for model output and prediction
    * Use benchmark datasets and fairness indicators to detect implicit bias
    * Implement human-in-the-loop review and what-if analysis

---

### 15.1.7. How to Set Up Explanations in the Vertex AI

* You need to configure explanations for custom-trained models to use Vertex Explainable AI.
    * To get batch explanations, set generateExplanation field to true when creating a batch prediction job.
    * Local kernel explanations can be generated in User-Managed Vertex AI Workbench notebook without deploying the model to Vertex AI.

---

## 15.2. Summary

* **Explainable AI**: Aims to provide insights into machine learning models' decisions
    * Key aspects: Explainability vs interpretability, feature importance, data bias, and fairness
    * Importance of explainability for ML model trust

---

## 15.3. Exam Essentials

* **Model Explainability on Vertex AI**: Understand what explainability means and its importance, including feature importance and global vs local explanations.
    * Supported feature attribution methods: Sampled Shapley algorithm, integrated gradients, XRAI
    * Ex explainable AI available for TensorFlow prediction container and AutoML models

---

# 16. Chapter 10Scaling Models in Production

---

## 16.1. Scaling Prediction Service

* **Deploying a TensorFlow Model**: A saved model contains trained parameters and computation, allowing for sharing or deployment with various frameworks.
* **Saved Models**: Created by calling `tf.saved_model.save()`, stored as a directory on disk, and include a `saved_model.pb` file describing the function `tf.Graph`.
* **Key Benefits**: No need for original model building code to run, useful for sharing, deploying, or using with TensorFlow Lite, TensorFlow.js, TensorFlow Serving, or TensorFlow Hub.

---

### 16.1.1. TensorFlow Serving

**TensorFlow Serving Overview**
 
* Host trained TensorFlow models as API endpoints through a model server.
* Handles model serving and version management.
* Supports REST and gRPC API endpoints.

**Setup Steps**

1. Install TensorFlow Serving with Docker or manually (docker recommended).
2. Train and save a model using TensorFlow.
3. Serve the saved model using TensorFlow Serving.

---

#### 16.1.1.1. Serving a Saved Model with TensorFlow Serving

* **REST API Request**
    * The TensorFlow ModelServer accepts POST requests to `http://host:port/<URI>:<VERB>`, where `URI` is `/v1/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]` and `<VERB>` is either `classify`, `regress`, or `predict`.
* **Prediction Response**
    * The `predict()` response returns a JSON object with the following structure:
        * `predictions`: a list of objects containing `class_ids`, `probabilities`, `classes`, and `logits` tensors.

---

## 16.2. Serving (Online, Batch, and Caching)

* **Best Practices for Serving**
  * Use a combination of batch prediction and online prediction for optimal performance
  * Implement caching mechanisms to reduce latency and improve scalability
  * Optimize model serving architecture for efficient processing and storage

---

### 16.2.1. Real‐Time Static and Dynamic Reference Features

* _Two types of input features are used: static and dynamic._
    * **Static Reference Features**: Values do not change in real time, updated in batches. Used for estimating prices or recommending products.
        * Stored in NoSQL databases optimized for singleton lookup operations (e.g., Firestore).
* **Dynamic Real-Time Features**: Computed on the fly, used for predicting events or recommending articles based on current user behavior.
    * Stored in low-latency read/write databases (e.g., Cloud Bigtable).

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

* **Pre-computation Approach**: Pre-compute predictions in batch scoring job, store them in low-latency data store (e.g. Memorystore or Datastore), and let clients fetch pre-existing predictions.
* **Benefits**: Reduces online prediction latency for specific entities or feature combinations with high cardinality.
    * Example: Hybrid approach can be used to precompute for top N entities (e.g. most active customers) and use model directly for others.

---

## 16.3. Google Cloud Serving Options

* **Prediction Types in Google Cloud**: Online predictions make immediate predictions on incoming data, while batch predictions process entire datasets at once.
* 
* **Vertex AI Support**: Both AutoML and custom models can utilize online and batch prediction capabilities.
 
* *_No specific job setup information provided_*

---

### 16.3.1. Online Predictions

* To set up a real-time prediction endpoint, you can either train models using *_Vertex AI_* or import existing models from other sources (*_on-premise_, _other cloud_, or _local device_*).
    * Importing prebuilt containers requires artifacts with specific filenames (*_TensorFlow SavedModel_*, *_scikit-learn_*, or *_XGBoost_*).
    * For custom container hosting, create a container image and push it to Artifact Registry.
* Steps for setup:
  * Deploy the model resource to an endpoint
  * Make a prediction
  * Undeploy if not in use

---

#### 16.3.1.1. Deploying the Model

* **Model Deployment**: Vertex AI automatically provisions resources and sets up autoscaling for containerized models (TensorFlow, scikit-learn, or XGBoost) deployed using the Prediction endpoint.
    * Users can deploy multiple models to a single endpoint.
    * Models can be deployed to multiple endpoints.

---

#### 16.3.1.2. Make Predictions

* **Preprocessing Data**: Preprocess input instances to match `task.py` format using the `predict` function.
* *_Endpoint_:_ *_Get a REST endpoint ID_ for real-time prediction.
    * _Format Input Data_: JSON for prebuilt containers, or with additional parameters field for custom containers.

---

#### 16.3.1.3. A/B Testing of Different Versions of a Model

* **A/B Testing**: compares two versions of a machine learning model to determine which one performs better.
    * Tests control (A) version against variant (B) version to measure success based on key metrics.
    * Allows for gradual deployment and replacement of models.
* **Vertex AI A/B Testing**: uses traffic-split parameter to deploy multiple models to the same endpoint, serving a percentage of traffic before increasing to 100%.
* **Additional Capabilities**: Vertex AI model evaluation feature allows for model performance measurement, tracking, and decision-making on model progression to online testing or production.

---

#### 16.3.1.4. Undeploy Endpoints

* **Undeploying Endpoints**: Undeploy endpoints when not in use to avoid incurring charges.
* _When to undeploy_ : During weekdays or when the business is inactive for a few hours.
* *Example usage:* `endpoint.undeploy(deployed_model_id=deployed_model_id)`

---

#### 16.3.1.5. Send an Online Explanation Request

* **Send Online Explanation Request**: Use `aiplatform.Endpoint().explain()` with instances and parameters to get online explanations
* **Returns Predictions and Feature Attributions**: Similar responses to prediction requests, including feature attributions and predictions
* _No Python SDK Example Code Required_: The provided code snippet is not necessary as the explanation request can be sent directly through the `aiplatform.Endpoint` class

---

### 16.3.2. Batch Predictions

* **Batch Prediction**: Run model on production data, saves output to Cloud Storage.
    * Input data must be formatted for specific AutoML or custom model requirements (JSON Lines, TFRecord, CSV files, etc.).
    * Output options: BigQuery table or Google Cloud Storage bucket. 
        * Model monitoring can be enabled in Preview mode to detect skew.

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

* **MLflow Overview**: An open-source platform for managing the machine learning life cycle, supporting multiple libraries and programming languages.
  * *_Functions:_* 
    + Experiment tracking
    + Packaging ML code
    + Model management and deployment
    + Centralized model store (Model Registry)
* **Hosting on Google Cloud**: Leverage scalability and availability of Vertex AI for model training and hosting. Use high-performance compute resources such as GPUs, TPUs, and CPUs.
  * *_Setup:_* 
    + PostgreSQL DB for metadata storage
    + Google Cloud Storage bucket for artifact storage
    + Compute Engine instance or Kubernetes for installation

---

## 16.5. Testing for Target Performance

* **Test for Production Performance**
  * Check training-serving skew with real-time data
  * Monitor model age and performance throughout the ML pipeline
  * Test numerical stability of weights and outputs (no NaN or null values) 
* _Additional Tools: Vertex AI Model Monitoring and Feature Store_
  * Detects skew and monitors model performance over time

---

## 16.6. Configuring Triggers and Pipeline Schedules

**Triggering Training or Prediction Jobs on Vertex AI**
 
* Use Cloud Scheduler to set up a cron job schedule.
* Utilize Vertex AI managed notebooks for Jupyter Notebook execution and scheduling.
* Leverage Cloud Build, Cloud Run, event-driven serverless Cloud Functions, and Cloud Pub/Sub for custom training and deployment.

**Orchestration Options**

* **Cloud Workflows**: orchestrate multiple HTTP-based services into a durable workflow.
* **Vertex AI Pipelines**: automate, monitor, and govern ML systems by orchestrating workflows in a serverless manner.

---

*Configuring Triggers and Pipeline Schedules*
Option | Description
---|---
Vertex AI Pipelines | Vertex AI Pipelines helps you to automate, monitor, and govern your ML systems by orchestrating your ML workflow in a serverless manner and storing your workflow's artifacts using Vertex ML Metadata. By storing the artifacts of your ML workflow in Vertex ML Metadata, you can analyze the lineage of your workflow's artifact.
Cloud Composer | Cloud Composer is designed to orchestrate data‐driven workflows (particularly ETL/ELT). It's built on the Apache Airflow project, but Cloud Composer is fully managed. Cloud Composer supports your pipelines wherever they are, including on‐premises or across multiple cloud platforms. All logic in Cloud Composer, including tasks and scheduling, is expressed in Python as directed acyclic graph (DAG) definition files.

<!-- _class: centered -->

---

## 16.7. Summary

* **TF Serving Scaling**:
	* Covered `predict` function details and understanding output from SignatureDef
	* Discussed online serving architecture (static and dynamic)
	* Examine pre-computing and caching while serving predictions
* **Model Deployment and Production**:
	+ Deploy models using online and batch mode with Vertex AI Prediction and Google Cloud options
	+ Address performance degradation in production (training-serving skew, data quality changes)
* **Automating Model Pipelines**:
	+ Configure triggers and schedules using Cloud Run, Cloud Build, Cloud Scheduler, Vertex AI managed notebooks, and Cloud Composer

---

## 16.8. Exam Essentials

* **TensorFlow Serving Overview**: TensorFlow Serving is a system to deploy and serve pre-trained machine learning models. It allows for scalable prediction services, Google Cloud serving options, and model performance testing.
* **Prediction Services**:
  * _Online Serving_: real-time invocation of models with dynamic reference features
  * _Batch Serving_: offline invocation of models with cached responses
  * _Caching_: strategy to improve serving latency
* 
  * **Google Cloud Options**: set up real-time endpoints, batch jobs, and automated pipelines using Google Cloud Vertex AI Prediction, Workflows, Vertex AI Pipelines, and Cloud Composer.

---

# 17. Chapter 11Designing ML Training Pipelines

---

## 17.1. Orchestration Frameworks

* An **orchestrator** manages the steps of an ML pipeline, such as data cleaning, transformation, and model training.
* It automatically executes the pipeline based on defined conditions and runs in a sequence.
* Orchestrating is useful for both development and production phases to automate the execution of the pipeline.

---

### 17.1.1. Kubeflow Pipelines

**Kubeflow Overview**

* Kubeflow is the ML toolkit for Kubernetes
* **Builds on Kubernetes for deploying, scaling, and managing complex systems**
* Allows deployment of any ML framework (TensorFlow, PyTorch, MXNet) on various clouds or local platforms

**Kubeflow Pipelines**

* Platform for building, deploying, and managing multistep ML workflows based on Docker containers
* **Description of an ML workflow in the form of a graph, including all components and their relations**
* Runs pipelines by launching Kubernetes pods corresponding to steps (components) in the workflow

---

### 17.1.2. Vertex AI Pipelines

### **Serverless Machine Learning Pipelines**

*   Run Kubeflow Pipelines or TensorFlow Extended pipelines on Vertex AI Pipelines without server setup
*   Bring existing pipeline code and run it serverless on Vertex AI Pipelines

### **Key Features of Vertex AI Pipelines**

*   Provides data lineage for tracking data movement and transformations
*   Automates, monitors, and experiments with interdependent parts of an ML workflow

### **Pipeline Components and Structure**

*   Defined by code as a self-contained set of code that performs one part of the pipeline's workflow
*   Can be built custom or reused from pre-built components

### **Running Vertex AI Pipelines**


---

*   Supports Kubeflow Pipelines SDK v1.8.9+ and TensorFlow Extended v0.30.0+
*   Migrate existing pipelines to Vertex AI Pipelines with reference guide at `https://cloud.google.com/vertex-ai/docs/pipelines/migrate-kfp`

---
### 17.1.3. Apache Airflow

* **Apache Airflow**: An open source workflow management platform for data engineering pipelines
    * Founded in 2014 at Airbnb to manage complex workflows
        * Represents workflows as directed acyclic graphs (DAGs) with tasks, dependencies, and data flows

---

### 17.1.4. Cloud Composer

* **Cloud Composer**: A fully managed workflow orchestration service built on Apache Airflow
* **Benefits**:
  * No installation or management overhead
  * Use Airflow-native tools with a focus on workflows, not infrastructure
* **Use cases**: 
  * Orchestrate data-driven workflows (ETL/ELT)
  * Batch workloads with low latency

---

### 17.1.5. Comparison of Tools

* **Orchestrators Comparison** 
    * Kubeflow Pipelines: orchestrate ML workflows in frameworks like TensorFlow and PyTorch, set up on-premises or in cloud.
    * Vertex AI Pipelines: managed serverless pipeline for Kubeflow Pipelines, no infrastructure management needed.
    * Cloud Composer: manages ETL/ELT pipelines using Apache Airflow, Python-based implementation.

---

*Comparison of Tools*
****|  Kubeflow Pipelines | Vertex AI Pipelines | Cloud Composer
---|---|---|---
**Management and support for frameworks** | Kubeflow Pipelines is used to orchestrate ML workflows in any supported framework such as TensorFlow, PyTorch, or MXNet using Kubernetes.
It can be set up on‐premises or in any cloud. | Managed serverless pipeline to orchestrate either Kubeflow Pipelines or TFX Pipeline. No need to manage the infrastructure. | Managed way to orchestrate ETL/ELT pipelines using Apache Airflow. It's a Python‐based implementation.

<!-- _class: centered -->

---

## 17.2. Identification of Components, Parameters, Triggers, and Compute Needs

* **Triggering an MLOps Pipeline**
Automate retraining of ML models with new data, on demand or schedule, based on various conditions such as model performance degradation or availability of new data.
* To train a new ML model, the deployed CT pipeline is executed without deploying new pipelines or components, only a new prediction service or trained model is served.
* A new pipeline is deployed for a new implementation through a CI/CD pipeline.

---

### 17.2.1. Schedule the Workflows with Kubeflow Pipelines

* **CI/CD with Kubeflow Pipelines**
    * Kubeflow Pipelines uses a Python SDK (`www.kubeflow.org/docs/components/pipelines/v1/sdk/sdk-overview`) to operate pipelines programmatically.
    * Services for invoking Kubeflow Pipelines include:
        * Cloud Scheduler
        * Pub/Sub and Cloud Functions
        * Cloud Composer or Cloud Data Fusion
        * Argo built-in scheduler

---

### 17.2.2. Schedule Vertex AI Pipelines

* **Scheduling with Cloud Scheduler**
  * Schedule pipeline execution using Cloud Scheduler with an event-driven Cloud Function and HTTP trigger
  * Upload compiled pipeline JSON to Cloud Storage bucket and create Cloud Function with HTTP trigger
  * Create Cloud Scheduler job, allowing manual run (optional)
* **Scheduling with Cloud Pub/Sub**
  * Trigger pipeline run using event-driven Cloud Function and Cloud Pub/Sub topic
  * Specify Pub/Sub trigger in Cloud Functions, enabling function call on message publication

---

## 17.3. System Design with Kubeflow/TFX

* **System Design Overview**: 
  * _Kubeflow DSL_
  * _TFX_

---

### 17.3.1. System Design with Kubeflow DSL

* **Kubeflow Pipelines**: pipelines stored as YAML files executed by Argo Workflows
* **Python DSL**: authoring pipelines using a custom-built language for ML workflows
    * **Container Creation**:
        * Create container with Python function or Docker container
        * Define operations referencing container, args, data mounts, and variables

---

#### 17.3.1.1. Kubeflow Pipelines Components

* To invoke a component in the pipeline, create a _component op_ using one of three methods:
    * Lightweight Python component
    * Reusable component with `component.yaml` file
    * Predefined Google Cloud components
* Component ops are automatically created from specifications using `ComponentStore.load_components`.

---

### 17.3.2. System Design with TFX

* **TFX Overview**: 
  * A Google production-scale machine learning platform based on TensorFlow
  * Provides a configuration framework and shared libraries for production-ready ML workflows
* **TFX Pipeline Components**:
  * ExampleGen: ingests input dataset, optionally splitting it
  * Transform: performs feature engineering on the dataset
  * Trainer: trains the model
  * Evaluator: validates training results, checks for anomalies and missing values
    * Note that ModelValidator is deprecated and fused with Evaluator

---

## 17.4. Hybrid or Multicloud Strategies

* **Multicloud**: Combining at least two public cloud providers (e.g., GCP + AWS) for flexible deployment options.
  * Integrate GCP AI APIs with on-premises or applications using AWS Lambda
  * Run BigQuery analytics on data stored in Azure Blob Storage or Amazon S3
* **Hybrid Cloud**: Combining private and public cloud environments, enabling flexibility and scalability.
  * Anthos: A hybrid and multicloud platform for cloud modernization and ML development
    * Supports BigQuery Omni and hybrid AI offerings
    * Enables on-premises deployment of GKE, Kubeflow Pipelines, and Cloud Run

---

## 17.5. Summary

* **Orchestration Tools**: 
  * *_Kubeflow_*: Managed platform for ML workflows, integrates with Cloud Build and TensorBoard
  * *_Vertex AI Pipelines_*: Serverless workflow management, integrates with Cloud Function event triggers
  * *_Cloud Composer_*: Orchestrates TFX pipelines on Kubeflow and GKE

* **Scheduling and Deployment**:
  * *_Kubeflow_*: Use Cloud Build to trigger deployments
  * *_Vertex AI Pipelines_*: Use Cloud Function event triggers for scheduling
* 
  * *_TFX_*: Supports bringing own orchestrator or runtime, can be run on Kubeflow, Cloud Composer, and Vertex AI Pipelines

---

## 17.6. Exam Essentials

* **Orchestration Frameworks**: 
  * _Kubeflow Pipelines_: Run on GCP, uses Cloud Build for deployment
  * _Vertex AI Pipelines_: Run on GCP, integrates with Kubeflow and TFX
  * _Apache Airflow_ and _Cloud Composer_: Alternatives to Kubeflow and Vertex AI

* **Scheduling ML Workflows**: 
  * Use Cloud Build for Kubeflow
  * Use Cloud Function event triggers for Vertex AI Pipelines
  * Schedule pipelines using Kubeflow Pipelines or TFX

* **System Design**:
  * _Kubeflow and TFX_: Create tasks as components, orchestrate with cloud runtimes

---

# 18. Chapter 12Model Monitoring, Tracking, and Auditing Metadata

---

## 18.1. Model Monitoring

**Model Performance After Deployment**
* A deployed model may not perform well on real-time data due to changes in the environment.
* Changes can occur unexpectedly, such as a pandemic or subtle changes in input data.
* The model's performance degrades over time if it is not adapted to new data.

**Concept Drift and Data Drift**
* _Drift_: A concept that occurs when the distribution of data changes over time.
* Two types:
  * **Concept Drift**: Changes in the underlying concepts or relationships between variables.
  * **Data Drift**: Changes in the distribution of input data.

---

### 18.1.1. Concept Drift

* **Concept Drift**: Relationship between input variables and predicted variables changes over time
    * _Example:_ Spam emails: as filters improve, spammers adapt by modifying their emails
        * Adversarial agents engage in a cat-and-mouse game to outmaneuver detection systems

---

### 18.1.2. Data Drift

* **Data Drift**: Change in input data fed to machine learning models compared to original training data.
    * Can occur due to changes in statistical distribution or input schema (e.g., new product labels, changed column meanings).
    * Requires continuous monitoring of data to detect model deterioration and take corrective action.

---

## 18.2. Model Monitoring on Vertex AI

* Vertex AI offers model monitoring features to detect:
    + _Training-serving skew_ (difference in input feature distribution between training data and production)
    + _Prediction drift_ (change in input statistical distribution over time)
* Detection is available for categorical and numerical features, including:
  * Categorical features: color, country, zip code
  * Numerical values: price, speed, distance

---

### 18.2.1. Drift and Skew Calculation

* **Baseline Calculation**
    * For categorical features: count or percentage of instances by category
    * For numerical features: count or percentage in buckets (equal-sized)
* **Distribution Comparison**
    * Categorical: L-infinity distance between baseline and latest production distribution
    * Numerical: Jensen-Shannon divergence between baseline and latest production distribution

---

#### 18.2.1.1. Practical Considerations of Enabling Monitoring

* To monitor data effectively without increasing costs, consider the following:
  * Configure a prediction request sampling rate for only a sample of production inputs.
  * Set the monitoring frequency to control how often logged inputs are analyzed for skew or drift.
  * Set alerting thresholds for each feature to detect statistical distance exceeding a certain value.

---

### 18.2.2. Input Schemas

**Input Parsing in Vertex AI**

* _Automatically parsed for AutoML models_
* _Schema not required but recommended for custom-trained models_

---

#### 18.2.2.1. Automatic Schema Parsing

* **Automatic Schema Detection**: Vertex AI model monitoring automatically parses the input schema when enabled for skew or drift, analyzing the first 1,000 requests.
    * _Schema efficacy_ is best with key-value pairs format (_e.g._ {"feature": value})
    * Example: {"make":"Ford", "model":"focus", year: "2011", "color":"black"}

---

#### 18.2.2.2. Custom Schema

* **Vertex AI Schema Requirements**
  * Use Open API schema format for analysis instance
  * Type can be _object_, _array_, or _string_
    * _object_: key/value pairs, properties specify each feature type
    * _array_ or _csv-string_: array-like format, order of features must be specified

---

## 18.3. Logging Strategy

* **Logging**: Collecting requests to track trends in input features and for auditing purposes.
    * **Implementation**: Enabled during model deployment or endpoint creation in Vertex AI.
        * **Applicable domains**: Regulated financial verticals may require logging for all models, while other cases may be useful for updating training data.

---

### 18.3.1. Types of Prediction Logs

* *_Prediction Node Logs_* 
  * *_Event Tracing Log_*: records events that occur during prediction node execution
  * *_Performance Log_*: tracks performance metrics such as latency and throughput
  * *_Error Log_*: logs errors that occur in the prediction nodes

---

#### 18.3.1.1. Container Logging

* **Logging Output**: Logs *_stdout_* and *_stderr_* from prediction nodes to Cloud Logging
* **Debugging Utility**: Useful for diagnosing issues with containers or models
* **Cloud Platform Integration**: Integrates with Google Cloud Platform's logging services

---

#### 18.3.1.2. Access Logging

* **Cloud Logging**: logs timestamp and latency data for requests
* *Enabled by default for v1 service endpoints*
* *Can be configured via deployment options*

---

#### 18.3.1.3. Request‐Response Logging

* Logs online prediction requests and responses to a BigQuery table for data augmentation
* Can be enabled during or after creating a prediction endpoint
    * Allows for increased training or test data through recorded interactions

---

### 18.3.2. Log Settings

* **Update Log Settings**: Update log settings when creating an endpoint or redeploying a model.
* **Consider Costs of Logging**: High QPS may produce significant logs, affecting costs.
* **Logging Configuration**: Use `gcloud` command to specify logging configuration, e.g.:
 
  * `‐‐disable‐container‐logging`
  * `‐‐enable‐access‐logging`

---

### 18.3.3. Model Monitoring and Logging

* **Restrictions between model monitoring and request-response logging**
  * Model monitoring cannot be enabled if request-response logging is already enabled
  * Request-response logging can only be enabled or disabled, not modified, once model monitoring is initially enabled

---

## 18.4. Model and Dataset Lineage

* **Metadata Importance**: metadata (parameters, artifacts, metrics) is crucial in tracking and comparing experiments, detecting model degradation, and understanding lineage of ML artifacts.
* **Metadata Benefits**:
  * Detect degradation
  * Compare hyperparameter effectiveness
  * Track lineage for source discovery
* **Metadata Use Cases**
  * Rerun ML workflows with same parameters
  * Audit downstream usage

---

### 18.4.1. Vertex ML Metadata

* **Vertex ML Metadata**: Open source ML metadata library for Google Cloud
  * Based on MLMD library developed by TensorFlow Extended team
* **Data Model**
  * **Metadata Store**: Regional container for all metadata resources, shared across orgs
    * _Artifacts_: Data created by or consumed by ML workflows (e.g. datasets, models)
  * _Context_: Group of artifacts and executions, useful for comparing metrics and identifying best models
* **Key Resources**
  * _Execution_: Step in a machine learning workflow, annotated with runtime parameters

---

#### 18.4.1.1. Manage ML Metadataschemas

* **Metadata Resource Schema**: `_system schemas_` for common resource types stored under namespace `system`, including `Model`, with properties such as framework, version, and payload format.
* **Create Artifact Operation**:
  * Define a function with parameters such as project, location, URI, artifact ID, display name, schema version, description, and metadata.
  * Call the `create()` function of the `Artifact` class to create a system artifact instance in the metadata store.
* **Lookup Artifact Operation**:
  * Use a function to query or look up an artifact like dataset or model using filters such as display name and creation date.

---

#### 18.4.1.2. Vertex AI Pipelines

* Vertex AI Pipelines store model metadata and artifacts in the metadata store for _lineage tracking_.
    * Automatically generates a series of artifacts with each pipeline run, including dataset summaries and model evaluation metrics.
    * Provides a visual representation of the lineage, allowing you to track data usage and model deployment.

---

## 18.5. Vertex AI Experiments

* **Vertex AI Experiments**: Automates trial tracking and analysis for machine learning models
    * Tracks experiment steps (preprocessing, embedding, training), input (algorithms, hyperparameters, datasets), and output (models, metrics, checkpoints)
    * Provides a single pane of glass to view experiments in the Google Cloud console

---

## 18.6. Vertex AI Debugging

* _Debugging issues in Vertex AI training_
    * Connect to the container running the custom training job
        * Install interactive Bash shell (pre-installed in some containers)
        * Enable `enableWebAccess` API field for interactive shells
        * Verify service account permissions and setup

---

## 18.7. Summary

* **Model Maintenance**: Monitoring deployed models for performance degradation
* **Logging Strategies**: Various options in Vertex AI for logging and tracking
* **Model Lineage Tracking**: Using Vertex ML Metadata and Vertex AI Experiments to track model development history

---

## 18.8. Exam Essentials

* **Model Monitoring**: Continuously monitor model performance after deployment to detect changes in input data, such as data drift and concept drift.
  * **Logging Strategies**: Implement logging to track deployment performance and create new training data, using Vertex AI's logging capabilities.
    * **Vertex ML Metadata**: Utilize Vertex ML Metadata for storing and accessing model metadata, tracking lineage of models and artifacts.

---

# 19. Chapter 13Maintaining ML Solutions

---

## 19.1. MLOps Maturity

* **MLOps Phases**: Organizations journey through 3 phases of machine learning adoption:
    * **Level 0 (Manual)**: Manual model training and development
    * **Level 1 (Strategic Automation)**: Automated pipelines and deployment
    * **Level 2 (CI/CD)**: Full automation with continuous integration and continuous deployment
* **Key Steps in ML**: 
    * Data extraction, analysis, preparation
    * Model training, evaluation, validation
    * Deployment and monitoring
* **MLOps Leveling**: Defined by automation level of these steps:
    * MLOps 0: Manual
    * MLOps 1: Strategic automation
    * MLOps 2: CI/CD automation

---

### 19.1.1. MLOps Level 0: Manual/Tactical Phase

* **Experimentation Phase**: Organizations experiment with ML to build proof of concepts, test AI/ML use cases, and validate business improvements.
    * Focused on individual or team experimentation and model training.
    * Output is a trained model handed off to the release/deployment team for deployment.

---

#### 19.1.1.1. Key Features of Level 0

* **Tactical Phase Key Points**
    * No automation in tasks; all manual
    * Separate teams for data science and MLOps with limited handoff processes
    * Limited scalability due to manual iterations
    * No consideration of Continuous Integration (CI) or Continuous Deployment (CD)

---

#### 19.1.1.2. Challenges

* _Model degradation_ is a major challenge during this phase
    * Can be mitigated by actively monitoring prediction quality
    * Frequent retraining and algorithm experimentation are necessary

---

### 19.1.2. MLOps Level 1: Strategic Automation Phase

* **MLOps Level 1 (Strategic Phase)**: Organizations with defined business objectives, prioritize ML to solve problems.
    * Key services include:
        * Automated pipeline triggers
        * Feature Store
        * Metadata management

---

#### 19.1.2.1. Key Features of MLOps Level 1

* **Level 1 Phase:**
  * Features:
    * Orchestration of experimentation steps
    * Automated continuous training in production
    * Unification with best practices (unified codebases)
  * Benefits:
    * Increased iteration speed
    * Continuous delivery of new models

---

#### 19.1.2.2. Challenges

* **Manual Pipeline Management**: team manages only a few pipelines, with manual deployment for new pipelines.
* *Pipelines are mainly triggered by data changes.*
* Automating pipeline management through CI/CD setup is necessary for using non-existent technologies.

---

### 19.1.3. MLOps Level 2: CI/CD Automation, Transformational Phase

* An organization in the transformational phase leverages AI for innovation and agility
* ML experts are integrated into product teams and across business units
* Datasets are shared across silos and ML projects collaborate between product groups * CI/CD automation is utilized throughout the entire pipeline, including model updates.

---

#### 19.1.3.1. Key Features of Level 2

* **Level 2 Adoption**: Moving to level 2 involves adopting a CI/CD model for machine learning (ML) pipelines.
    * _Key Features_: 
        * Automated pipeline development, testing, and deployment
        * Continuous retraining and monitoring of models
        * Blue/green deployment options for model rollout
    * **Goal**: Automate ML solution maintenance to adapt to rapid technological advancements.

---

## 19.2. Retraining and Versioning Models

* **Drift Detection Limitations**: Model performance can degrade over time, requiring retraining.
* **Key Considerations**:
  * Monitor for drift detection and training-serving skew
  * Collect real data for evaluation and new training datasets
  * Determine when to retrain the model
* **Retraining Frequency**: Establish a strategy for using collected data to train new models.

---

### 19.2.1. Triggers for Retraining

**Retraining Model Policies**

* **Trigger retraining based on accuracy levels:**
  + Absolute threshold (e.g., below 90% accuracy)
  + Rate of degradation (e.g., sudden drop of more than 2% in accuracy)
* **Consider the impact on model performance and deployment:**
  + Minimize frequent retraining to avoid high training costs
  + Balance model degradation vs. delayed training for new models

---

### 19.2.2. Versioning Models

**Model Versioning**
* Enables deployment of multiple models with version IDs for backward compatibility
    * Allows users to select older models when new ones are released
    * Solves disruptions caused by unexpected changes in behavior or performance

---

## 19.3. Feature Store

* **Feature Engineering Challenges**: Feature engineering is a valuable investment but often leads to repetitive tasks due to lack of sharing.
* * **Main Issues**: 
    + Non-reusable features
    + Governance complexity
    + Team divisions
* **Consequences**: Reduces ML solution effectiveness, hinders productization and creates governance issues.

---

### 19.3.1. Solution

* **Feature Stores**: centralized location for features and metadata, applying software engineering principles like versioning, documentation, and access control
    * Key features: fast processing of large feature sets and low-latency access for real-time and batch predictions
    * Examples: Feast (open-source), Google Cloud Vertex AI Feature Store

---

### 19.3.2. Data Model

* The Vertex AI Feature Store uses a time-series model to store data.
    * **Key Concepts:**
        * _Featurestore_: A container with one or more entity types.
        * _EntityType_: Stores similar or related features, e.g., batters and team.
            * **Entity Structure:** `player_id` (unique String), team, batting_avg, age.

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

* **Ingestion**: supports both batch and streaming ingestion into BigQuery
    * Supports batch ingestion during model training
    * Supports online ingestion for online inference
* **Retrieval**: two methods: batch and online
    * Batch method returns values up to time t
    * Online method returns values at or before time t

---

## 19.4. Vertex AI Permissions Model

* **IAM Overview**: Identity and Access Management (IAM) controls access to resources and operations like training, deploying, and monitoring.
    * Enforce permissions using IAM
    * Refer to Chapter 6: Building Secure ML Pipelines for discussion
* **GCP IAM Fundamentals**: Revisit GCP's IAM fundamentals before diving into Vertex AI permissions model. 
* **IAM Best Practices**:
    * **Least Privilege:** Restrict users and applications to only necessary actions.
    * Manage service accounts and keys, enable audit logs and cloud logging roles.
    * Use policy management to ensure policies are implemented at every level

---

### 19.4.1. Custom Service Account

* Using default service accounts created by Vertex AI can lead to unnecessary permissions
* Custom service accounts with specific permissions are recommended for security and cost efficiency

---

### 19.4.2. Access Transparency in Vertex AI

* **Logging Requirements**: Many domains require logging for access verification and compliance.
* *_Cloud Audit logs_*: Capture user activity from your organization.
* *_Access Transparency logs_*: Capture actions of Google personnel in your project.

---

## 19.5. Common Training and Serving Errors

* Common errors during training and serving can be identified by understanding their underlying causes
* Familiarizing yourself with these common errors enables effective debugging using TensorFlow as the framework

---

### 19.5.1. Training Time Errors

* **Common Errors in Training Phase**
  * _Insufficient input transformation or encoding_
  * _Mismatched tensor shapes_
  * _Out-of-memory errors due to large instance sizes_

---

### 19.5.2. Serving Time Errors

* *_Serving time errors occur only during deployment_* 
    * _Typical errors include: untransformed input data, signature mismatch_

---

### 19.5.3. TensorFlow Data Validation

* **TensorFlow Data Validation**: Analyzes training and serving data to prevent errors, including:
  * Computing statistics
  * Inferring schema
  * Detecting anomalies

---

### 19.5.4. Vertex AI Debugging Shell

* **Vertex AI Interactive Shell**: an interactive shell for debugging training, allowing inspection of training containers
    * _Runs tracing and profiling tools_
    * _Analyzes GPU utilization_
    * _Validates IAM permissions for the container_

---

## 19.6. Summary

* **Long-term ML application maintenance** is based on CI/CD principles, focusing on automation of training, deployment, and monitoring.
* The balance between model quality and retraining policy cost must be considered.
* A feature store can solve the inefficiency problem caused by departments not sharing features.

---

## 19.7. Exam Essentials

* MLOps maturity levels:
  * Experimental phase: basic automation
  * Strategic phase: automation with some integration
  * Mature phase: CI/CD-inspired architecture for scalability and efficiency
* Key concepts:
  * Model versioning: tracking changes and triggers for retraining
    * _Retraining triggers_ can be based on model degradation or time-based schedules
  * Feature store: managing shared features across teams for efficient collaboration

---

# 20. Chapter 14BigQuery ML

---

## 20.1. BigQuery – Data Access

* **Data Access Methods**
    * Three ways to access data: 
        * Using the web console with SQL queries
        * Running SQL queries in a Jupyter Notebook using `%%bigquery`
        * Using Python API in Jupyter Notebook
    * **Python API Example**
        * Import BigQuery library and create client
        * Pass query as string, capture results in Pandas DataFrame

---

## 20.2. BigQuery ML Algorithms

**BigQuery ML**

* Allows creation of machine learning models using standard SQL queries
* No need for Python code; serverless architecture makes training and prediction easy

---

### 20.2.1. Model Training

* To create a model in BigQuery ML, use `CREATE MODEL` with options for model type and input label columns.
    * Model types include regression, classification, clustering, collaborative filtering, dimensionality reduction, time-series forecasting, and generic models like TensorFlow.
    * The `CREATE OR REPLACE MODEL` statement can be used to reuse model names and create a new one if it does not exist.

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

* Use a separate dataset for model evaluation using `ML.EVALUATE` to ensure accuracy.
    * This step should be performed on a data set not seen by the model.
    * Results are displayed in a web interface and can be queried easily.

---

### 20.2.3. Prediction

* The `ML.PREDICT` function predicts values from a BigQuery ML model.
    * Passes an entire table to predict and returns a new table with predicted values and probabilities.
        * Example use case: `SELECT * FROM ML.PREDICT(MODEL 'dataset1.creditcard_model1', (SELECT * FROM 'dataset1.creditcardpredict' LIMIT 1))`

---

## 20.3. Explainability in BigQuery ML

* **Explanation**:
  * Explanability is crucial for debugging models and improving transparency.
  * In BigQuery, global feature importance values can be accessed at the model level or per prediction using SQL functions.

* **Enabling Global Explanation**
  * Set `enable_global_explain=TRUE` during training to enable global explanations.
  * Use `ML.GLOBAL_EXPLAIN(MODEL 'model1')` to query global explanations.

* **Model Explainability Methods**:
  * Table 14.2: Model types and explainability methods
    + Linear/logistic regression: Shapley values, standard errors, p-values
    + Boosted Trees: Tree SHAP, Gini-based feature importance

---

    + Deep Neural Network/Wide-and-Deep: Integrated gradients
    + Arima_PLUS: Time-series decomposition

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

**Summary**

* *_BigQuery_*: serverless data warehouse for SQL experts, ideal for complex queries and automation.
* *_Vertex AI_*: designed for machine learning engineers, with fine-grained control over training and prediction flow.
* *_Choose BigQuery_* for analysts or business users, *_Vertex AI_* for machine learning engineers.

---

## 20.5. Interoperability with Vertex AI

* **Vertex AI and BigQuery ML Integration**: The two Google Cloud products are designed to work together, with multiple integration points throughout the machine learning pipeline.
 
* Key Integration Points:
  * Data ingestion
  * Model training and deployment
  * Model monitoring and management
  * Data processing and feature engineering

---

### 20.5.1. Access BigQuery Public Dataset

* **BigQuery Datasets**: Over 200 publicly available datasets through Google Cloud Public Datasets Program.
    * Accessible for free, only paying for queried results.
    * Can be used in GCP projects and also with Vertex AI for machine learning tasks.

---

### 20.5.2. Import BigQuery Data into Vertex AI

* **Creating a Vertex AI Dataset**: You can create a dataset by providing a source URL, including BigQuery URLs, in a few steps.
  * _Use `bq://project.dataset.table_name` as the `bq_source`_
  * No need to export and import data from/to BigQuery

---

### 20.5.3. Access BigQuery Data from Vertex AI Workbench Notebooks

* Using managed notebook instance in Vertex AI Workbench allows direct access to BigQuery dataset and SQL query execution.
* Enables data exploration, visualization, machine learning model experimentation, and feature engineering with various datasets.
* Facilitates seamless integration of Jupyter Notebook with BigQuery for efficient data analysis.

---

### 20.5.4. Analyze Test Prediction Data in BigQuery

* **Exporting Model Predictions**: When training a model, provide train and test datasets. Export the test prediction results directly to BigQuery for analysis.
    * Enables further testing of models using SQL queries
    * Facilitates data-driven insights into model performance

---

### 20.5.5. Export Vertex AI Batch Prediction Results

* You can use BigQuery tables as input data for batch predictions in Vertex AI
* Predictions are sent directly back to BigQuery and stored as a table
* Useful when integrating with existing MLOps pipelines that use Vertex AI and BigQuery

---

### 20.5.6. Export BigQuery Models into Vertex AI

* You can export a BigQuery model to GCS and then import it into Vertex AI for complete freedom.
* To simplify the process, you can register your BigQuery ML models directly in the Vertex AI Model Registry.
* Currently, some models (ARIMA_PLUS, XGBoost, transform-based) are not supported for direct export.

---

## 20.6. BigQuery Design Patterns

* BigQuery ML introduces novel solutions to common data science and machine learning problems
* These solutions are referred to as design patterns, addressing recurring issues in the field
* Elegant new approaches provide a way to tackle familiar challenges

---

### 20.6.1. Hashed Feature

* **Categorical Variable Issues**: Incomplete vocabulary, high cardinality, and cold start problems
    * **Data Scaling**: High cardinality creates scaling issues for ML models
    * **New Values**: New values can't be predicted with existing training data (cold start problem)
* **Solution**: Transform categorical variable to low cardinal domain using hashing functions like FarmHash

---

### 20.6.2. Transforms

* **Model Pipelining**: inputs are modified or enhanced before feeding into a model, and transformations must be applied during deployment.
    * **BigQuery Solution**: uses `TRANSFORM` clause in `CREATE_MODEL` function
    * _Example Transformations_: Feature Cross, Quantile Bucketize

---

## 20.7. Summary

* **BigQuery ML**: democratized machine learning in the SQL community
* * **Key Features**:
  * Uses SQL for ML pipeline actions and transformations
  * High interoperability with Vertex AI
  * Unique design patterns for efficient model creation

---

## 20.8. Exam Essentials

* **BigQuery and ML Overview**: Learn BigQuery's history, innovation of bringing ML to data analysis, and SQL-based training/prediction/model explanation.
    * _**Integration between BigQuery ML and Vertex AI**: Understand the differences in design for analysts/SQL experts vs ML engineers, and how they work together seamlessly._
    * **BigQuery Design Patterns**: Apply reusable solutions (hashing, transforms, serverless predictions) to machine learning pipelines.

---

# 23. Online Test Bank

---

## 23.1. Register and Access the Online Test Bank

* To access online test bank content, go to `www.wiley.com/go/sybextestprep` and follow the registration instructions.
    * Select your book from the list and complete required information, including security verification.
    * Enter pin code received via email to activate account.
        * Log in with new username and password, then access test bank content.

---

# 24. WILEY END USER LICENSE AGREEMENT

---

