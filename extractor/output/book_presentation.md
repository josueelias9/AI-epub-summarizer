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
  section img {
    max-height: 65vh;
    max-width: 85%;
    object-fit: contain;
    display: block;
    margin: 0 auto;
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

# My Book Summary

### AI-Generated Book Summary

---# 2. Official Google Cloud CertifiedProfessional Machine Learning EngineerStudy Guide

---

# 7. Chapter 1Framing ML Problems

---

## 7.1. Translating Business Use Cases

**Impact**: Key factor; determines success criteria (e.g., increasing profit, reducing fraud).
**Success Criteria**: Identified through stakeholder discussions; varies by role (executives: business impact; CFOs: budget; managers: timelines; data managers: privacy/security).
**Use Case**: Match to ML approach (e.g., regression for house price prediction); ensure fit with business needs and stakeholders.
* **Stakeholders**: Key people influencing project approval;各有不同的关注点（如业务影响、预算、时间线和数据隐私/安全）。
* **机器学习方法匹配**：根据用例选择合适的算法和评估指标；确保与业务需求相符。

---


![center w:85%](images/c01f001.png)

---

## 7.2. Machine Learning Approaches

**Machine Learning Approaches**: Diverse methods tailored for specific problem types.
* **Problem-Specific Categories**: Defined by data type and prediction goals.
* **Comprehensive Knowledge Needed**: For identifying appropriate ML approach based on use case.

---


![center w:85%](images/tip.png)

---

### 7.2.1. Supervised, Unsupervised, and Semi‐supervised Learning

**Supervised Learning**: Uses labeled datasets to train models, e.g., classifying images of dogs or cats.
**Unsupervised Learning**: Deals with unlabeled data, like clustering algorithms (e.g., K-means clustering) and autoencoders for dimensionality reduction.
* **Topic Modeling**: A type of unsupervised learning that groups documents into topics based on common words and sentences.

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

**Classification**: Predicting categorical labels or categories (e.g., dogs vs. cats).
* **Binary Classification**: Two labels (e.g., yes/no, true/false).
    * **Multiclass Classification**: More than two labels (e.g., Cloud Vision API categorizing objects).

**Regression**: Predicting a continuous value (e.g., house price, rainfall amount) using structured data.

**Forecasting**: Predicting future values based on time-series data (e.g., temperature readings over time).

**Clustering**: Grouping data points based on inherent similarities (e.g., city clusters from latitude and longitude).

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

**Machine Learning Metric**: Used to determine if the trained model is accurate enough.

* **Classification Problem**: Choose metrics based on business needs (e.g., accuracy, recall, precision, F1 score).
    * **Recall**: Measures true positives relative to actual positives (low false negatives preferred).
        * Example: Recall = 5 / (5 + 2) = 0.714
    * **Precision**: Measures true positives relative to predicted positives (low false positives preferred).
        * Example: Precision = 5 / (5 + 3) = 0.625
    * **F1 Score**: Harmonic mean of precision and recall, balancing both types of errors.
        * Example: F1 = 2 x (0.625 x 0.714) / (0.625 + 0.714) = 0.666

---


![center w:85%](images/c01-disp-0014.png)

---


![center w:85%](images/c01-disp-1014.png)

---


![center w:85%](images/c01-disp-2014.png)

---


![center w:85%](images/c01-disp-1814.png)

---


![center w:85%](images/c01-disp-4014.png)

---


![center w:85%](images/c01-disp-3014.png)

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

**ROC Curve**: Graphical plot summarizing binary classification model performance with true positive rate on y-axis, false positive rate on x-axis, and different thresholds.

**AUC (Area Under the Curve)**: Measures model performance by calculating the area under the ROC curve, with a higher value indicating better performance; diagonal line represents worst case.

**Advantages of AUC**: Scale-invariant and classification threshold-invariant, ranking predictions without relying on absolute values.

---


![center w:85%](images/c01f002.png)

---


![center w:85%](images/tip.png)

---

### 7.3.2. The Area Under the Precision‐Recall (AUC PR) Curve

**Precision-Recall Curve (AUC PR)**: Graphically illustrates precision-recall pairs; x-axis is recall, y-axis is precision.

**Best AUC PR Curve**: Horizontal line at top; optimal point is 100% precision and 100% recall, unattainable in practice but the target.

**Preference for AUC PR in Imbalanced Datasets**: High true negatives can skew traditional ROC curves, making AUC PR more reliable.

---


![center w:85%](images/c01f003.png)

---

### 7.3.3. Regression

**Regression Metrics**: Evaluate prediction accuracy

- **MAE**: Average absolute difference between actual and predicted values.
- **RMSE**: Square root of the average squared difference, penalizes large errors more.
    * **RMSLE**: Similar to RMSE but uses logarithm to handle skewed data, penalizes underpredictions more.
- **MAPE**: Average absolute percentage difference, measures proportional differences.
- **R²**: Squared correlation coefficient, ranges from 0 to 1, higher values indicate better fit.

---

## 7.4. Responsible AI Practices

**Fairness**: Ensuring ML models do not reflect unfair biases; use statistical methods to measure bias.

**Interpretability**: Understanding model predictions, especially for complex models like neural networks; use model explanations to quantify feature contributions.

**Privacy**: Protecting sensitive data from exposure in the model; employ techniques to minimize data leakage during training and deployment.

**Security**: Addressing cybersecurity threats unique to ML, including data poisoning and model theft; stay vigilant and develop countermeasures.

---

## 7.5. Summary

**Business Use Case**: Identify the problem and define the machine learning question.
* **Dimensions of an Ask**: Understand the scope and requirements.
**Machine Learning Problem Statement**: Frame the business use case into a clear, actionable ML question.

---

## 7.6. Exam Essentials

* **Translate business challenges to machine learning**: Identify the problem, data availability, expected outcomes, stakeholders, budget, and timelines.
    * **Problem types**: Differentiate between regression, classification, and forecasting; know relevant algorithms for each.
* **Use ML metrics**: Understand metrics like precision, recall, F1, AUC ROC, RMSE, and MAPE to match with use cases.
* **Google's Responsible AI principles**: Adhere to fairness, interpretability, privacy, and security practices.

---

# 8. Chapter 2Exploring Data and Building Data Pipelines

---

## 8.1. Visualization

* Data visualization helps identify trends, outliers, imbalanced data, and feature impacts on models.
    * Univariate Analysis: Analyzes each feature independently (box plots, distribution plots).
    * Bivariate Analysis: Compares two features to find correlations (line plots, bar plots, scatterplots).

---

### 8.1.1. Box Plot

* **Box plot**: Visualizes data divided into quartiles, highlighting the interquartile range and outliers.
    * **Interquartile range (body)**: Represents the middle 50% of observations.
    * **Whiskers**: Extend to the minimum and maximum values, excluding outliers.
* **Outliers**: Points lying outside the whiskers.

---


![center w:85%](images/c02f001.png)

---

### 8.1.2. Line Plot

* Line plot: Visualizes relationships between two variables, showing trends in data over time.
* **Figure 2.2**: Illustrates a line plot.

---


![center w:85%](images/c02f002.png)

---

### 8.1.3. Bar Plot

* **Bar Plot**: Used for analyzing trends and comparing categorical data.
* **Example Uses**: Sales figures weekly, website visitors monthly, product revenue monthly.
* **Figure 2.3**: Bar plot shown.

---


![center w:85%](images/c02f003.png)

---

### 8.1.4. Scatterplot

**Scatterplot**: Visualizes relationships between two variables, showing clusters in datasets.

---

## 8.2. Statistics Fundamentals

- **Mean**: Average value of a dataset.
- **Median**: Middle value when data is ordered.
- **Mode**: Most frequently occurring value in a dataset.

---

### 8.2.1. Mean

Mean is the accurate measure to describe the data when we do not have any outliers present.

---

### 8.2.2. Median

**Median**: Used when there are outliers in the dataset.
- **Calculation**: Arrange data values from lowest to highest; for even counts, take the average of the two middle numbers; for odd counts, use the middle number as the median.

---

### 8.2.3. Mode

**Mode**: Used when there's an outlier and most data points are the same; it represents the most frequent value(s) in a dataset.
* **Example**: In the dataset 1, 1, 2, 5, 5, 5, 9, the mode is 5.

---

### 8.2.4. Outlier Detection

**Mean**: Affected by outliers; changes significantly with the addition of an outlier like 210.
* **Variance**: Measures spread as the average squared difference from the mean.

**Median**: Less affected by outliers, remains stable at 13 and 14.
**Mode**: Unchanged, stays at 15 in both cases.

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

**Standard deviation**: Measures the spread of data around the mean; identifies unusual data points.
* **Outliers**: Data points more than one standard deviation from the mean are considered unusual.
**Covariance**: Quantifies the relationship between two variables' variances.

---


![center w:85%](images/note.png)

---

### 8.2.6. Correlation

**Correlation**: Normalized form of covariance ranging from –1 to +1.

**Positive Correlation**: Increase in one variable leads to an increase in another.

**Negative Correlation**: Increase in one variable leads to a decrease in another.

**Zero Correlation**: Change in one variable does not significantly affect the other.

* **Correlation Helps Detect Label Leakage**: Highly correlated features like hospital names can cause models to learn on labels, leading to poor generalization.

---


![center w:85%](images/note.png)

---

## 8.3. Data Quality and Reliability

**Data Quality**: Determines model reliability and performance based on training data size and cleanliness.
- **Reliability**: Degree of trustworthiness; ensure no missing, duplicate values, or bad features (unclean data).
    * Check for label errors and noise in features like GPS measurements.
    * Identify and handle outliers and data skew.
- **Data Quality Parameters**: Defined during collection and discussed further.

---

### 8.3.1. Data Skew

**Data Skew**: When data is not normally distributed, indicating the presence of outliers.

* **Right-Skewed Data**: Characterized by a long tail on the right; examples include income distributions.
* **Implications for Models**: Extreme outliers can affect model prediction accuracy; transformations like log transformation or normalization can help normalize the distribution.
    * **SMOTE, Undersampling, Oversampling**: Techniques to handle skewed target variables.

---


![center w:85%](images/c02f004.png)

---

### 8.3.2. Data Cleaning

* **Normalization**: Transforms features to similar scales for better model performance and training stability.
* **Goal**: Improves model training by standardizing feature ranges.

---

### 8.3.3. Scaling

**Scaling**: Converts feature values into a standard range (e.g., 0 to 1 or –1 to +1) for better model training.
    * **Benefits**: Improves gradient descent convergence, prevents "NaN traps," and ensures features are equally weighted.
**Use Cases**: Suitable for uniformly distributed data with no skew or outliers.

---


![center w:85%](images/note.png)

---

### 8.3.4. Log Scaling

* Log scaling is used for data with a wide range.
    * It brings very large values into a more manageable scale.
* For instance, it converts a value of 100,000 to 5 and 100 to 2 using logarithms.
* This helps in visualizing data within the same range.

---

### 8.3.5. Z‐score

**Z-score**: Measures the number of standard deviations a value is from the mean.

* **Outlier detection**: Values with z-scores outside -3 to +3 are considered outliers.

---

### 8.3.6. Clipping

* Feature clipping: Capping extreme outliers at a fixed value.
* Timing: Can be applied before or after other normalization techniques.

---

### 8.3.7. Handling Outliers

**Outlier**: A value significantly deviating from others due to error or skew.

**Visualization Techniques**:
- *Box plots*: Graphical representation of statistical data based on a five-number summary.
- *Clipping*: Method for capping extreme values at a certain threshold.

**Statistical Techniques**:
- *Z-score*: Measures how many standard deviations an element is from the mean.
- *Interquartile range (IQR)*: Difference between 75th and 25th percentiles, used to identify outliers.

**Handling Outliers**:
- Remove them to avoid model bias.
- Replace with mean, median, mode, or boundary values.

---

## 8.4. Establishing Data Constraints

**Data Schema**: Describes data properties (type, range, format) for ML pipeline consistency.

**Key Insights**: Identifies quality issues like missing values, outliers.

**Schema Benefits**:
* Enables metadata-driven preprocessing for feature engineering.
* Facilitates validation of new data, catching anomalies during training and prediction.

---

### 8.4.1. Exploration and Validation at Big‐Data Scale

**TensorFlow Data Validation (TFDV)**: A tool for detecting data and schema anomalies at scale.

**TensorFlow Extended (TFX) Platform**: Includes TFDV, along with libraries for preprocessing (`TensorFlow Transform`), model evaluation (`TensorFlow Model Analysis`), and serving models (`TensorFlow Serving`).

- **Exploratory Data Analysis Phase**: Helps create a data schema to ensure consistency between your ML pipeline and input data.
- **Production Pipeline Phase**: Uses the schema to detect data skew or drift, ensuring model performance remains stable.

---


![center w:85%](images/c02f005.png)

---

## 8.5. Running TFDV on Google Cloud Platform

* **Apache Beam SDK**: Foundation for building batch and streaming pipelines in TFDV.
* **Dataflow**: Managed service running Apache Beam pipelines at scale.
    * **Integration**: Native with BigQuery, Google Cloud Storage, and Vertex AI Pipelines.

---

## 8.6. Organizing and Optimizing Training Datasets

**Training Dataset**: Used to train the model; model learns from this data.
**Validation Dataset**: Used for evaluation and hyperparameter tuning; model does not learn from this data.
**Test Dataset**: Used after training to evaluate model performance; must be distinct from training and validation sets.

---


![center w:85%](images/c02f006.png)

---

### 8.6.1. Imbalanced Data

**Imbalanced Data**: When classes are not equally represented, e.g., 995 non-fraud vs 5 fraud transactions.

* **Oversampling/Undersampling**: Balancing by duplicating minority or removing majority samples introduces bias.

**Downsampling and Upweighting**: 
    * Downsample majority class (e.g., no-fraud) to balance data.
    * Increase example weight of downsampled class during training, e.g., 10x importance.

---


![center w:85%](images/c02f007.png)

---


![center w:85%](images/note.png)

---


![center w:85%](images/c02f008.png)

---

### 8.6.2. Data Splitting

**Random splitting**: Can cause a skew in time-sensitive datasets.

**Time-based splitting**: Helps by dividing data based on publication date, ensuring topics are not overrepresented in both training and testing sets.

* **Example**: Train with April stories, test with May stories to avoid overlap.

---

### 8.6.3. Data Splitting Strategy for Online Systems

**Time-based data splitting**: Ensures the validation set reflects the lag between training and prediction.

* **Steps for online systems**:
    * Collect 30 days of data.
    * Train on days 1-29, validate on day 30.

**Advantages**: Works best with large datasets (e.g., millions of examples).

---

## 8.7. Handling Missing Data

**Handling Missing Data**: Techniques to manage incomplete data in datasets.

  * **Data Deletion**: Remove rows or columns with null or NaN values. Loss of information; poor model performance if much data is missing.
  * **Imputation**: Replace missing values with statistical measures (mean, median) for continuous features and the most frequent category for categorical ones. Prevents data loss but may cause data leakage.
  * **LOCF**: Use last valid observation to fill gaps in time-series data. Reduces bias.
  * **Algorithmic Methods**: Some algorithms like k-NN and Naive Bayes can handle missing values. Random Forest adapts well to nonlinear and categorical data.

---

  * **Predictive Imputation**: Use machine learning models to predict missing values based on correlations with other variables. Effective for complex datasets.

---
## 8.8. Data Leakage

**Data leakage**: Exposing model to test data during training leads to overfitting, poor performance on unseen data.

- **Incorrect feature inclusion**: Mistakenly including target variable as a feature.
- **Improper data splitting**: Including test data in the training dataset.
    * **Label leakage**: Correlation between target variable and features not available after deployment.
- **Preprocessing issues**: Applying techniques to the entire dataset instead of separately.

**Classic example (time-series)**: Using future data for current predictions leads to leaked models due to random splits.

**Detection and prevention**:

- Avoid correlated features with the target.

---

- Use separate test, train, and validation sets; validation set mimics real-life scenarios.
- Preprocess training and test data independently.
- For time-series data, apply cutoffs based on prediction time.
- Employ cross-validation for limited data, computing parameters separately per fold.

**Key**: Reflect differences between production and training data in splits.

---
## 8.9. Summary

**Data Visualization**: Use box plots, line plots, and scatterplots  
**Statistical Fundamentals**: Mean, median, mode, standard deviation for outlier detection  
**Data Cleaning & Normalizing Techniques**: Log scaling, scaling, clipping, z-score

**Data Constraints & Validation**: Define data schema in ML pipelines; use TFDV for large-scale validation

**Data Splitting Strategy**: Time-based splitting for online systems and clustered data

**Missing Data & Leakage Handling**: Strategies to manage them effectively

---

## 8.10. Exam Essentials

* **Visualize data**: Use box plots, line plots, and scatterplots for understanding distributions and relationships.
* **Statistical fundamentals**: Describe mean, median, mode, standard deviation; check correlations using line plots.
* **Data quality & reliability**: Remove outliers, understand skewness; apply techniques like log scaling, z-score normalization.
* **Define data constraints**: Set up a data schema in ML pipelines; validate data using TFDV for large datasets.
* **Optimize training data**: Split data into training, test, and validation sets; handle imbalanced data with appropriate sampling strategies.

---

* **Handle missing data**: Remove, replace, or use ML to fill missing values.
* **Avoid data leaks**: Prevent leakage in features and labels by carefully managing data splits.

---
# 9. Chapter 3Feature Engineering

---

## 9.1. Consistent Data Preprocessing

**Pretraining Data Transformation**: Perform transformations before model training on a complete dataset; computation is performed only once but requires rerunning for updates, leading to slow iterations.

* **Inside Model Data Transformation**: Transformations are part of the model code, making it easier to use the same transformation during training and serving. However, large or computation-heavy transformations can increase model latency.

---

## 9.2. Encoding Structured Data Types

**Feature**: Should align with business objectives, be known at prediction time, numeric, and have sufficient examples.

* **Categorical Data**: Represents categories with discrete values (e.g., yes/no, male/female).

* **Numeric Data**: Consists of scalar or continuous values from observations or measurements.

---

### 9.2.1. Why Transform Categorical Data?

**Categorical Data Handling**: Decision trees can process categorical data directly; other ML algorithms need it converted to numeric.
* **Conversion Requirement**: Categorical variables must be transformed into numeric formats for most ML algorithms, then reversed if used as output.
**Prediction Process**: Convert numeric outputs back to categorical labels for final predictions.

---

### 9.2.2. Mapping Numeric Values

* Integer and floating-point data require no special encoding.
* Numeric data may need normalizing or bucketing transformations.
    * Normalizing scales values to a standard range.
    * Bucketing categorizes continuous values into discrete bins.

---

### 9.2.3. Mapping Categorical Values

**Categorical Data Transformation**: Convert categories into numbers for model understanding.

---

### 9.2.4. Feature Selection

**Feature selection**: Selecting useful input variables for prediction.

**Dimensionality reduction**: Reducing data dimensions to improve performance, with methods like PCA and t-SNE.

    * **Backward selection and Random Forest**: Techniques for keeping important features only.

---

## 9.3. Class Imbalance

**Class imbalance**: Focuses on outcomes specific to classification models.
- **True positive**: Correctly predicting the positive class (e.g., identifying sick patients).
- **True negative**: Correctly predicting the negative class (e.g., identifying healthy patients as not sick).
- **False positive**: Incorrectly predicting the positive class (e.g., labeling healthy patients as sick).
- **False negative**: Incorrectly predicting the negative class (e.g., labeling sick patients as not sick); critical to minimize for medical tests.
    * **Minimize false negatives**: Essential to avoid misidentifying sick patients as healthy.

---

### 9.3.1. Classification Threshold with Precision and Recall

**Classification Threshold**: A value chosen by a human to map logistic regression outputs to binary categories; typically 0.5 but can be adjusted based on specific needs.

**Precision and Recall**:
- **Precision**: The ratio of true positives to the total number of positive predictions.
- **Recall (True Positive Rate)**: The percentage of actual positives that are correctly identified by the model.

**Threshold Adjustment**:
- Raising the threshold reduces false positives, increasing precision; useful when minimizing false alarms is crucial.
- Lowering the threshold reduces false negatives, increasing recall; beneficial when missing positive cases is undesirable.

---


![center w:85%](images/note.png)

---

### 9.3.2. Area under the Curve (AUC)

**AUC ROC**: Used for balanced datasets with equal class examples.

**AUC PR**: Used for imbalanced datasets, like identifying fraud in credit card transactions.

---

## 9.4. Feature Crosses

* **Feature Cross**: Multiplies two or more features to create a synthetic feature, often used in machine learning.
    * **Use Case 1**: Enhances predictive ability when individual features are not sufficient; e.g., [location × time of day] improves prediction of crowd levels.
* **Nonlinearity Representation**: Used in linear models to handle complex patterns by multiplying features; e.g., AB = A * B, making it easier to separate classes that cannot be linearly divided.
* **Summary**: Feature crosses are essential for converting numerical and categorical data into more predictive features, improving model complexity handling and classification accuracy.

---


![center w:85%](images/c03f001.png)

---


![center w:85%](images/c03f002.png)

---


![center w:85%](images/c03f003.png)

---

## 9.5. TensorFlow Transform

**Efficient Input Pipeline**: Essential for improving TensorFlow model performance.

* **TF Data API**: Enables building complex input pipelines efficiently.
* **TensorFlow Transform**: Used for data preprocessing to ensure consistency and quality in training data.

---

### 9.5.1. TensorFlow Data API (tf.data)

* Prefetch transformation overlaps preprocessing and model execution using `tf.data.Dataset.prefetch`.
* Interleave transformation parallelizes data reading with `tf.data.Dataset.interleave` to mitigate extraction overhead.
* Cache transformation stores data in memory during the first epoch via `tf.data.Dataset.cache` to reduce file opening and reading operations.

---

### 9.5.2. TensorFlow Transform

**TensorFlow Transform**: Performs data transformations before model training to avoid skew between training and serving.

**TFX Pipelines**: Utilize Google Cloud services like Cloud Dataflow and BigQuery for transforming and storing data as TFRecords, with artifacts saved in Cloud Storage.

* **GCP Services Integration**: Steps 1-6 use Cloud Dataflow for transformation; steps involve BigQuery data extraction and Cloud Storage for artifact storage.

---


![center w:85%](images/c03f004.png)

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

**Cloud Data Fusion**: Code-free web UI for building ETL/ELT pipelines from various sources; supports Cloud Dataproc for Hadoop and Spark workloads.

**Dataprep by Trifacta**: Serverless tool for visual data exploration, cleaning, and preparation; suggests transformations and predicts outcomes without writing code.

---

## 9.7. Summary

**Feature Engineering**: Transforming numerical and categorical features for model training and serving.

* **Numerical Features**: Techniques include bucketing and normalization.
* **Categorical Features**: Techniques encompass linear encoding, one-hot encoding, out-of-vocabulary, hashing, and embedding.
* **Dimensionality Reduction**: Importance of feature selection; techniques like PCA.
* **Class Imbalance**: Impact on precision and recall; AUC PR over AUC ROC for imbalanced classes.
* **Feature Crosses**: Benefits in capturing interactions between features.
* **TensorFlow Data Representation**: Using `tf.data` for data representation.

---

    * **tf.Transform**: Processing pipelines with `tf.Transform`, applicable on Google Cloud.
        * **Google Cloud Tools**: Overview of Cloud Data Fusion and Cloud Dataprep for ETL processes.

---
## 9.8. Exam Essentials

* **Data Processing**: Transform data before or during training; understand benefits and limitations.
    * **Encoding Structured Data**: Use techniques like bucketing, normalization, hashing, and one-hot encoding for numeric and categorical data.
* **Feature Selection**: Needed to reduce dimensionality; use methods such as dimensionality reduction.
* **Class Imbalance**: Understand metrics like true positive, false positive, accuracy, AUC, precision, recall; measure accuracy effectively in imbalanced classes.
    * **Feature Cross**: Important for interactions; use in specific scenarios.

---

* **TensorFlow Transform**: Know TensorFlow Data and Transform; architect pipelines on Google Cloud with BigQuery and Cloud Data Fusion.
* **GCP Tools**: Use Cloud Data Fusion and Dataprep for ETL and data processing, respectively.

---
# 10. Chapter 4Choosing the Right ML Infrastructure

---

## 10.1. Pretrained vs. AutoML vs. Custom Models

**Pretrained Models**: Ready-to-use models trained by Google; easy to integrate via APIs.

**AutoML**: Builds custom models using your data; requires cloud resources but no ML expertise needed.

* **Custom Models**: Offers flexibility in algorithm choice and hardware provisioning; suitable for unique use cases, requiring ML expertise.

---


![center w:85%](images/c04f001.png)

---


![center w:85%](images/tip.png)

---

## 10.2. Pretrained Models

**Pretrained Models**: Machine learning models trained on large datasets and available for quick use.

**Google Cloud Pretrained Models**: 
* Vision AI, Video AI, Natural Language AI, Translation AI, Speech-to-Text, and Text-to-Speech.

**Google Cloud Platforms**: Offer solutions with integrated pretrained models and uptrain capabilities:
* Document AI
* Contact Center AI

---

### 10.2.1. Vision AI

**Vision AI**: Provides access to ML algorithms for image processing without building a complete infrastructure.

- **Functions**: Image classification, object and face detection, optical character recognition (OCR)
- **Usage**: Quick browser-based try at `https://cloud.google.com/vision`; production uses uploaded images or URLs
    * **Predictions**:
        - Detected objects
        - Image labels (e.g., Table, Furniture, Plant)
        - Dominant colors for organization
        - Safe Search classification (Adult, Spoof, Medical, Violence, Racy)

---


![center w:85%](images/c04f002.png)

---

### 10.2.2. Video AI

**Object, place, and action recognition**: Identifies over 20,000 elements in videos for metadata tagging.

**Real-time processing**: Analyzes stored or streaming videos with instant results.

**Metadata application**: Enhances searchability and categorization of video catalogs.

* **Video recommendation system**: Utilizes API labels and viewing history to personalize recommendations.
* **Video archive indexing**: Creates an index from unindexed archives, benefiting mass media companies.
* **Advertising relevance**: Matches ad content with video labels in real time to ensure relevance.

---

### 10.2.3. Natural Language AI

**Natural Language AI**: Provides insights from unstructured text through entity extraction, sentiment analysis, syntax analysis, and categorization.

* **Entity Extraction**: Identifies people, organizations, products, events, locations, etc., with optional Wikipedia links.
    * Example: Distinguishes "Mr. Wood" as a person in the sentence “Mr. Wood is a good actor.”

**Sentiment Analysis**: Scores sentences, entities, and texts as positive, negative, or neutral with magnitude.

* **Syntax Analysis**: Analyzes part of speech, dependencies, lemmas, and morphology.

**Categorization**: Classifies documents into over 700 predefined categories.


---

- Use Case 1: Measure customer sentiment on specific products.
- Use Case 2: Extract medical insights using Healthcare Natural Language API for healthcare applications (separate service).

---
### 10.2.4. Translation AI

**Translation AI**: Detects over 100 languages using GNMT technology.
* **Levels**: Basic vs Advanced; Advanced offers glossaries and document translations.

**Media Translation API**: Real-time audio translation from source to target language, ideal for low-latency streaming.

---

### 10.2.5. Speech‐to‐Text

**Speech-to-Text**: Converts audio to text.

* **Use cases**: Creating subtitles for videos and live streams.
* **Integration**: Often combined with translation services for multilingual subtitles.

---

### 10.2.6. Text‐to‐Speech

* **Text-to-Speech service**: Provides realistic speech with humanlike intonation using DeepMind's AI expertise.
* **Voices and Languages**: Supports 220+ voices across 40+ languages and variants; create a unique brand voice.
    * **List of supported languages**: `https://cloud.google.com/text-to-speech/docs/voices`

---

## 10.3. AutoML

* **AutoML (Automated ML)**: Automates model training for common ML problems like image classification, text classification.
* **Training Process**: Users provide data and configure settings; the rest is automated via web console or SDKs.
* **Data Types & Use Cases**:
    * **Structured Data**
    * **Images/Video**
    * **Natural Language**
    * **Recommendations AI/Retail AI**

---

### 10.3.1. AutoML for Tables or Structured Data

* BigQuery ML: SQL-based training and prediction, serverless approach (Chapter 14)
    * Vertex AI Tables: Trained using Python, Java, Node.js, or REST API

* **TABLE 4.1**: AutoML Tables algorithms
    * Table (IID): Classification uses AUC ROC, Logloss; Regression uses RMSE, MAE
    * Time-series data: Forecasting uses RMSE, MAPE, Quantile loss

* Configure the “budget” and enable early stopping in Vertex AI AutoML to save costs if training completes within the budget

* For forecasting, choose from:
    * **AutoML**: General model for various use cases
    * Seq2seq+: Effective for small datasets (< 1 GB)
    * **Temporal Fusion Transformer**: High accuracy and interpretability

---


![center w:85%](images/c04f003.png)

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

**Vertex AI AutoML**: Simplifies building models for image and video data.
- **Image Data**: Supports classification (single label), multiclass classification, object detection, and segmentation.
- **Video Data**: Handles classification, action recognition, and object tracking.
    * **AutoML Edge Model**: Optimized for deployment on edge devices with lower memory usage and latency; currently supports iPhones, Android phones, and Edge TPU devices.
* **Model Size Trade-off**: Options available for Edge TPU to balance accuracy and latency.

---


![center w:85%](images/c04f004.png)

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

**AutoML Text**: Predicts one or multiple labels for documents and extracts entities.

**AutoML Text (continued)**: 
* **Text Classification**: Assigns a single correct label to a document.
* **Multi-Label Classification**: Identifies all correct labels for a document.
* **Entity Extraction**: Identifies entities within text items.

**Text to Text**: Converts text from one language to another.

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

**Retail Search**: Provides Google-quality search capabilities, customizable to retail needs.
* **Vision API Product Search**: Trains on product images for image-based searches.
**Recommendations AI**: Analyzes customer behavior and provides targeted recommendations across channels.
* **Training & Charges**: Customers upload catalogs, feed user events; charged for model training and requests.
* **Model Types (Table 4.4)**: Predicts "Others you may like," "Frequently bought together," "Recommended for you," and "Similar items."

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

**Document AI**: A platform for extracting details from various documents like scanned images, forms, and government IDs.

  * **Extracts text, layouts, key/value pairs, and entities**
  * **Supports document quality detection and deskewing**
  * **Classifies and splits documents**

**Document AI Concepts:**
- **Processors**: Interfaces for machine learning models to perform specific tasks (general, specialized, custom)
- **Document AI Warehouse**: Stores, searches, organizes, governs, and analyzes documents with structured metadata

---

### 10.3.6. Dialogflow and Contact Center AI

* Dialogflow: Conversational AI from Google Cloud for chatbots and voicebots
    * CCAI: Integrated into telephony services for comprehensive contact center solutions

---

## 10.4. Custom Training

**Custom Training**: Offers full flexibility in choosing hardware options for training models.
* **GPUs**: Accelerate deep learning model training by leveraging massively parallel architectures, ideal for compute-intensive operations like matrix multiplications.
    * **Time Reduction**: Can drastically reduce training time from days or weeks to hours.

---

### 10.4.1. How a CPU Works

**CPU**: Processor for running general workload; supports many operations.

**CPU Architecture**: Loads data from memory, performs an operation, and stores the result back into memory.

* **Serial Computation**: Inefficient for trillions of calculations, common in ML model training.

---

### 10.4.2. GPU

**GPUs**: Specialized chips with thousands of ALUs that process data in memory for rapid image rendering, significantly speeding up tasks like large matrix multiplications and differential operations.

**Machine Series Requirements**: Use A2 or N1 machine series; specify GPU type (e.g., NVIDIA_TESLA_T4, P100) and count per VM in `WorkerPoolSpec`.

* **GPU Availability and Restrictions**: Check available locations on `cloud.google.com/vertex-ai/docs/general/locations`; restrictions include number of GPUs per instance and sufficient virtual CPUs/memory; refer to Google's compatibility table for detailed specifications.

---


![center w:85%](images/tip.png)

---

### 10.4.3. TPU

**Tensor Processing Units (TPUs)**: Specialized hardware accelerators designed for machine learning workloads.
* **Matrix Multiply Units (MXUs)**: Each TPU contains multiple MXUs, each with 128 × 128 multiply/accumulators capable of performing 16,000 operations per cycle in bfloat16 format.
* **Core Task**: TPUs excel at matrix processing, crucial for neural network training.

---


![center w:85%](images/c04f005.png)

---

## 10.5. Provisioning for Predictions

**Prediction phase**: Differing from training, involves online or batch methods; online requires real-time response, batch focuses on cost-effective processing.

* **Scaling behavior**: Continuous workload requiring dynamic resource adjustment based on demand.
* **Machine type**: Key consideration for optimal prediction performance and efficiency.

---

### 10.5.1. Scaling Behavior

* **Autoscaling configuration**: Scales prediction nodes based on CPU usage.
* **GPU nodes**: Configure triggers for monitoring CPU, memory, and GPU usage.

---

### 10.5.2. Finding the Ideal Machine Type

**Cost Optimization**: Benchmark instance performance by running prediction calls until 90+ percent CPU utilization, then calculate QPS cost per hour for different machine types.

**Resource Utilization and Model Compatibility**: Ensure your custom container accounts for single-threaded limitations, effective resource usage (CPU, memory), latency, throughput, and price. Consider using GPUs only with TensorFlow SavedModels or custom containers designed for GPU acceleration.

**Edge Deployment Use Cases**: Explore scenarios where trained models need to be deployed on edge devices for real-time inference.

---

### 10.5.3. Edge TPU

**Edge Devices**: Collect real-time data, make decisions, take actions, and communicate with other devices or the cloud.

**Edge Inference**: Run ML inference on device to handle limited bandwidth and offline operation.

**Google Edge TPU**: Accelerates ML inference with 4 TOPS performance at 2 watts; available in various form factors like single-board computer and system-on-module (sold under Coral.ai).

---


![center w:85%](images/tip.png)

---

### 10.5.4. Deploy to Android or iOS Device

* **ML Kit**: A package from Google for integrating machine learning into mobile apps (iOS and Android)
* **Model Training**: Can be done on Google Cloud, using AutoML or custom models
* **Deployment**: Models are deployed to Android or iOS apps, with predictions made on-device for fast response times and offline support

---

## 10.6. Summary

* Pretrained models on Google Cloud
* AutoML for various scenarios
* Hardware options: GPUs and TPUs for training
    * Training vs prediction workloads
* Edge device deployment concepts

---

## 10.7. Exam Essentials

* **Choose the right ML approach**: Select between pretrained models, AutoML, or custom models based on requirements.
* **Provision hardware for training**: Understand GPU and TPU options; choose instance types suitable for specialized hardware during training.
* **Provision hardware for predictions**: Use CPUs and GPUs in the cloud for scalability; employ TPUs on edge devices.

---

# 11. Chapter 5Architecting ML Solutions

---

## 11.1. Designing Reliable, Scalable, and Highly Available ML Solutions

**ML Pipeline Steps**: Data collection, data transform, model training, tuning, deploying, monitoring

* **Scalable Storage**: Google Cloud Storage for managing and storing data
* **Scalable Infrastructure**: Google Cloud Dataflow for PySpark transforms
    * **Distributed Training**: For large models, use distributed compute infrastructure
* **Model Training & Tuning**: Use Vertex AI Training or AutoML for custom models; Vertex AI Hyperparameter Tuning for automated model tuning and tracking with Vertex AI Experiments

**Deployment & Monitoring**: Vertex AI Prediction for scalable production deployment; Vertex AI Model Monitoring for drift detection


---

**Orchestration & CI/CD**: Vertex AI Pipelines for managing the complete ML workflow

**Explanations & Responsible AI**: Vertex Explainable AI, model cards

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

**Google Cloud ML Stack**: Divided into three layers based on ease of use

- **Top Layer (AI Solutions)**: Managed SaaS offerings like Document AI, Contact Center AI, and Enterprise Translation Hub. Built on Vertex AI services.
  
- **Middle Layer (Vertex AI Services)**: 
  * Pretrained APIs for common use cases in sight, language, conversation, and structured data.
  * AutoML for customizing models with your own data.
  * Vertex AI Workbench for custom model development.

- **Bottom Layer**: Infrastructure including compute instances, containers (GKE), TPUs, GPUs, and storage. Requires self-managed scalability and reliability.

**Table 5.2**: When to Use Google Cloud Services


---

| GCP Service       | When to Use                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| BigQuery ML       | Structured data in BigQuery; comfortable with SQL; models match your needs. |
| AutoML (Vertex AI)| Problem fits supported types like classification, object detection, etc.; data matches format and limits. |
| Custom Model      | Problem doesn't fit other services; running training elsewhere for consistency. |

---

![center w:85%](images/c05f001.png)

---


![center w:85%](images/note.png)

---

*Choosing an Appropriate ML Service*
GCP Service | When to Use
---|---
BigQuery ML | You have structured data stored in a BigQuery data warehouse because BigQuery ML requires a tabular dataset. You are comfortable with SQL and the models available in BigQuery ML match the problem you are trying to solve. We are going to cover all the models in Chapter 14.
AutoML (in the context of Vertex AI) | Your problem fits into one of the types that AutoML supports, such as classification, object detection, sentiment analysis, and translation.

<!-- _class: centered -->

---

## 11.3. Data Collection and Data Management

* **Google Cloud Storage**: Handles large-scale storage needs.
* **BigQuery**: Manages high-volume, low-latency analytics queries.
* **Vertex AI's Datasets**: Manages training and annotation sets for machine learning.
* **Vertex AI Feature Store**: Stores and manages features used in models.
* **NoSQL Data Store**: Supports flexible, scalable unstructured data storage.

---

### 11.3.1. Google Cloud Storage (GCS)

**Google Cloud Storage (GCS)**: Service for storing objects in Google Cloud.
- **Use Cases**: Storing images, videos, audio, and unstructured data.
- **File Size and Sharding**: Supports large files ≥ 100 MB; sharding into 100 to 10,000 shards improves throughput.

---

### 11.3.2. BigQuery

**BigQuery**: Store tabular data for better performance, especially for training.

* **Access Methods**: Google Cloud console, `bq` command-line tool, BigQuery REST API, Vertex AI Jupyter Notebooks.
* **API Tools (Table 5.3)**: 
    * TensorFlow/Keras: `tf.data.dataset reader for BigQuery`, `tfio.BigQuery.BigQueryClient()`
    * TFX: `BigQuery client`
    * Dataflow: `BigQuery I/O connector`
    * Other frameworks: `BigQuery Python Client library`

---

*BigQuery*
Framework | Google Cloud tool to read data from BigQuery
---|---
TensorFlow or Keras | `tf.data.dataset reader for BigQuery` and tfio.BigQuery.BigQueryClient()

<!-- _class: centered -->

---

### 11.3.3. Vertex AI Managed Datasets

**Vertex AI Managed Datasets**: Simplify training by using predefined formats (image, video, tabular, text).

**Advantages of Managed Storage**:
* Centralize dataset management.
* Integrate automated data labeling for unstructured data.
* Facilitate model lineage tracking and iterative development.
* Enable model performance comparison through AutoML and custom models.
* Generate data statistics and visualizations.
* Automatically split data into training, test, and validation sets.

**When Not to Use Managed Datasets**: More control over data splitting or when data lineage isn't critical.

---


![center w:85%](images/tip.png)

---

### 11.3.4. Vertex AI Feature Store

**Vertex AI Feature Store**: Centralized repository for ML features; supports independent use or integration with Vertex AI workflows.

- **Benefits**: Reduces need to store feature values across multiple locations (e.g., BigQuery, Google Cloud Storage); facilitates drift detection and data skew mitigation through centralized management.

**Real-time Feature Retrieval**: Enables fast online predictions by fetching feature values on-demand.

---

### 11.3.5. NoSQL Data Store

**NoSQL Data Stores**: Optimized for singleton lookup operations.

- **Memorystore**
  * **Description**: Managed in-memory database with submillisecond latency.
  * **Use Cases**: Real-time bidding, media and gaming applications.

- **Datastore**
  * **Description**: Fully managed document database for scalable, high-performance application development.
  * **Use Cases**: E-commerce product recommendations.

- **Bigtable**
  * **Description**: Scalable NoSQL database service for high throughput and low-latency workloads.
  * **Use Cases**: Fraud detection, ad prediction, booking recommendations.


---

**Data Storage Recommendations**: Avoid block storage like NFS or VM hard disks; use BigQuery, Google Cloud Storage, or a NoSQL data store for performance.

---

![center w:85%](images/note.png)

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

**Machine Learning Workflows**: Define phases like data collection, preprocessing, building datasets, model training, evaluation, and deployment.

**ML Pipelines**: Connect steps of an ML solution for automated execution and continuous training.

**Kubeflow Pipelines**: A Kubernetes-based pipeline tool for ML projects (introduced by Google).

**Vertex AI Pipelines**: Serverless alternative to Kubeflow Pipelines, simplifying ML workflow management.

---

### 11.4.1. Use Vertex AI Pipelines to Orchestrate the ML Workflow

**Vertex AI Pipelines**: A managed service for automating, monitoring, and governing ML workflows in a serverless manner.

- **Artifacts Storage**: Stores workflow artifacts like training data, hyperparameters, and code using Vertex ML Metadata.
- **Pipeline Support**: Runs pipelines built with Kubeflow SDK v1.8.9+ or TensorFlow Extended v0.30.0+, with TensorFlow use cases specifically for defining pipeline operations.

**Managed Steps**: Can be calls to Google Cloud services.

- **Experiment Tracking**: Supports experiments, which are GA in Vertex AI Pipelines and Kubeflow Pipelines, ensuring compatibility and ease of use across different ML environments.

---

- **Resource Requirements**: Requires minimal resources (small nodes with modest CPU and RAM), as most work is handled within the managed service.

---

![center w:85%](images/note.png)

---

### 11.4.2. Use Kubeflow Pipelines for Flexible Pipeline Construction

* **Kubeflow**: Open source Kubernetes framework for ML workloads
* **Kubeflow Pipelines**: Service for composing, orchestrating, and automating ML systems; uses SDK for pipeline authoring
    * **Google Cloud Pipeline Components**: Integrates Vertex AI functionality like AutoML into pipelines
* **Orchestration and Automation**: Executes required Google Cloud services for production ML pipelines, with support for various compute workloads including Dataproc and AutoML

---


![center w:85%](images/c05f002.png)

---

### 11.4.3. Use TensorFlow Extended SDK to Leverage Pre‐built Components for Common Steps

**TensorFlow**: Provides components for common ML workflow steps like data ingestion and training.

**TFX (TensorFlow Extended SDK)**: Frameworks, libraries, and components for defining, launching, and monitoring production models. Recommended if you use TensorFlow, structured/textual data, or large datasets.

* **Google Cloud Implementation**: Covered in Chapter 3, "Feature Engineering." More details available at <https://neptune.ai/blog/deep-dive-into-ml-models-in-production-using-tfx-and-kubeflow>.

---

### 11.4.4. When to Use Which Pipeline

**Vertex AI Pipelines**: Supports Kubeflow Pipelines SDK v1.8.9+ or TensorFlow Extended v0.30.0+.

* **TFX (TensorFlow Extended)**: Recommended for processing large datasets; creates a DAG and uses Apache Beam, supporting distributed backends like Cloud Dataflow.
    * **Apache Beam**: Manages pipelines under the hood, easily executable on distributed processing backends.

**Orchestrators (e.g., Kubeflow)**: Simplify configuration, operation, monitoring, and maintenance of ML pipelines; often come with user-friendly GUIs.

**Vertex AI Pipelines**: Preferred for common ML operations, tracking metadata and lineage crucial for production validation.

---

## 11.5. Serving

* **Model Deployment**: Deploy trained, evaluated, and tuned ML models to production for predictions.
* **Prediction Methods**:
    * **Offline Prediction**: Model predicts outputs for a batch of input data at once.
    * **Online Prediction**: Model processes and predicts output for each input instance sequentially.

---

### 11.5.1. Offline or Batch Prediction

* Offline/batch prediction: Running batch jobs with trained models to predict on data batches.
    * Use cases: Recommendations, demand forecasting, segment analysis, text classification.
* Vertex AI batch prediction: Tool for running batch prediction jobs on BigQuery or Google Cloud Storage data.
* Architecture: High-level setup on Google Cloud for offline batch prediction (Figure 5.3).

---


![center w:85%](images/c05f003.png)

---

### 11.5.2. Online Prediction

**Near Real-Time Predictions**: Sent via HTTPS endpoints, used in real-time bidding and sentiment analysis.

  * **Synchronous Predictions**: Caller waits for response before proceeding (use Vertex AI, App Engine, or GKE for feature preprocessing).
  * **Asynchronous Predictions**:
    * **Push**: Model sends predictions as notifications (e.g., fraud detection).
    * **Poll**: Store predictions in a database and periodically retrieve them.

* * *

**Minimizing Latency**:
  * **Model Level**: Build smaller models, use accelerators like Cloud GPU or TPU.
  * **Serving Level**: Use low latency data stores, precompute predictions, cache results.

---


![center w:85%](images/c05f004.png)

---


![center w:85%](images/c05f005.png)

---


![center w:85%](images/tip.png)

---

## 11.6. Summary

**GCP ML Services**: Use appropriate services from GCP AI/ML stack layers

**Data Management & Storage**: Utilize BigQuery for data management and NoSQL store for sub/millisecond latency

**Pipeline Automation**: Employ Vertex AI Pipelines, Kubeflow Pipelines, or TFX for ML automation

**Model Serving**: Serve models in batch mode or real-time using Vertex AI Prediction; optimize latency with efficient architecture patterns

---

## 11.7. Exam Essentials

* **Design scalable and available ML solutions**: Use Google Cloud AI/ML services for reliability.
* **Choose appropriate ML service**: Select from GCP's AI/ML stack based on use case and expertise.
* **Implement automation and orchestration**: Use Vertex AI Pipelines, Kubeflow, or TFX pipelines as needed.
    * **Serve data effectively**: Deploy models with best practices; use batch or real-time prediction appropriately.

---

# 12. Chapter 6Building Secure ML Pipelines

---

## 12.1. Building Secure ML Systems

**Data Security**: Ensuring user and employee data protection is crucial for enterprises.

**Encryption Measures**:
- **Encryption at Rest**: Google Cloud encrypts stored data to protect it from unauthorized access.
- **Encryption in Transit**: Data in transit is also encrypted to secure it during transmission.

---

### 12.1.1. Encryption at Rest

**Cloud Storage & BigQuery Encryption**: Data is encrypted at rest by default, with Google managing the keys or allowing customer-managed keys.

* **AEAD Encryption in BigQuery**: Individual table values can be encrypted using AEAD functions; refer to `https://cloud.google.com/bigquery/docs/reference/standard-sql/aead-encryption-concepts`.

**Encryption Types**:
- *Server-Side*: Occurs after data receipt but before disk storage.
- *Client-Side*: Data is encrypted before transmission, with client responsible for keys and operations.

**Data Integrity**: Cloud Storage supports CRC32C and MD5 hashes to check data integrity.

---


![center w:85%](images/tip.png)

---

*Encryption at Rest*
Server‐Side Encryption | Client‐Side Encryption
---|---
Encryption that occurs after the cloud storage receives your data, but before the data is written to disk and stored. | Encryption that occurs before data is sent to Cloud Storage and BigQuery. Such data arrives at Cloud Storage and BigQuery already encrypted but also undergoes server‐side encryption.
You can create and manage your encryption keys using a Google Cloud Key Management Service. |  You are responsible for the client‐side keys and cryptographic operations.

<!-- _class: centered -->

---

### 12.1.2. Encryption in Transit

* **Transport Layer Security (TLS)**: Protects data during read and write operations over the Internet.

---

### 12.1.3. Encryption in Use

**Confidential Computing**: Protects data in memory by encrypting it during processing.

**Encryption in Use**: Safeguards data from compromise or exfiltration while being processed.

* **Confidential VMs and Confidential GKE Nodes**: Tools for encrypting data in use.

---

## 12.2. Identity and Access Management

**IAM in Google Cloud**: Manages access to data and resources.
- **Project-level roles**: Assign roles to principals for project-wide access; commonly used for service accounts in Vertex AI Workbench, custom training, and predictions.
    * **Service accounts**: Accounts for applications or compute workloads.
- **Resource-level roles**: Define permissions for specific resources via policies; currently supported only for Vertex AI Feature Store and entity type resources.

**IAM Roles in Vertex AI**: 
- **Predefined roles**: Grant project-wide access with related permissions (e.g., Vertex AI Administrator, User).

---

- **Basic roles**: Standard access control roles applicable to all Google Cloud services.
    * **Viewer**, **Editor**, **Owner**
- **Custom roles**: Allow creating tailored permission sets and assigning them to users.

*Note: Not all predefined roles support resource-level policies.*

---

![center w:85%](images/note.png)

---

### 12.2.1. IAM Permissions for Vertex AI Workbench

**Vertex AI Workbench**: Data science service on GCP that uses JupyterLab, allowing customization of Virtual Private Clouds (VPC).

* **Notebook Types**:
    * **User-managed notebook**: Highly customizable but require more setup time; use tags in metadata.
    * **Managed notebooks**: Less customizable, integrate with Cloud Storage and BigQuery, automatically shut down idle instances.

* **Access Modes**:
    * **Single User Only**: Grants access to a specified user.
    * **Service Account**: Grants access via a service account that can be shared among multiple users. Requires setting up an environment variable for authentication in Google Colab.

---


![center w:85%](images/c06f001.png)

---


![center w:85%](images/c06f002.png)

---


![center w:85%](images/c06f003.png)

---


![center w:85%](images/tip.png)

---

### 12.2.2. Securing a Network with Vertex AI

**Google Cloud shared responsibility model**: The cloud provider is responsible for securing the cloud infrastructure, while users must protect their data and assets.

**Shared fate model**: Enhances collaboration between the cloud provider and user to continuously improve security through secure blueprints, risk protection programs, and assured workloads.

* **Vertex AI Workbench notebook environment**: Secure using Vertex AI Workbench notebooks blueprint with default security recommendations.
* **Vertex AI endpoints**: Protect public and private endpoints appropriately.
* **Vertex AI training jobs**: Ensure secure execution of training tasks.

---

## 12.3. Privacy Implications of Data Usage and Collection

**PII**: Data allowing identification of a specific individual.

**PHI**: Sensitive health data protected by HIPAA, including medical records and billing info.

* **HIPAA Privacy Rule**: Federal protections for PHI, ensuring patient rights while permitting necessary disclosures.

---

### 12.3.1. Google Cloud Data Loss Prevention

**Google Cloud Data Loss Prevention (DLP) API**: Removes identifying information from text content using de-identification techniques like masking, tokenization, encryption, and bucketing.

**Data Profiles**: Automatically scans BigQuery tables and columns across the organization, projects, and folders to identify sensitive data and create risk profiles at different levels.

**Risk Analysis**: Computes re-identification risk metrics (k-anonymity, l-diversity, k-map, δ-presence) before or after de-identification to monitor changes in data.


---

* **Jobs and Triggers**: Runs actions like scanning content for sensitive data or calculating re-identification risks. Schedules DLP jobs using job triggers that can be set up to run on Cloud Storage repositories and other data sources.

**Data De-Identification Streaming Pipeline**: Uses Dataflow to de-identify streaming and batch text data, storing the results in Google Cloud Storage or BigQuery.

* **Configuration Management**: Manages templates and configurations for DLP jobs with security admins using Cloud KMS for key management.

**Data Validation and Re-identification Pipeline**: Validates and re-identifies large-scale datasets stored in BigQuery or other storage types.

---

![center w:85%](images/c06f005.png)

---

### 12.3.2. Google Cloud Healthcare API for PHI Identification

**HIPAA**: Requires special handling of PHI linked to 18 specific identifiers.

**Google Cloud Healthcare API**:
- Offers de‐identify operation to remove or mask sensitive information from text, images, FHIR, DICOM.
- Detects and masks protected PHI in DICOM and FHIR data.

**De‐identification command**: Targets the 18 HIPAA-defined identifiers to convert PHI into non-protected health information.

**DLP API Dataflow pipeline**: Simplifies configuring and running DLP API on CSVs, BigQuery tables, and text strings for healthcare data.

---

### 12.3.3. Best Practices for Removing Sensitive Data

**Data Views**: Create database views that exclude sensitive columns, allowing continuous training without data engineers' access.

**Cloud DLP**: Utilize Cloud DLP for unstructured content with identifiable patterns using regex.

**PCA/Dimension Reduction**: Use Principal Component Analysis (PCA) to combine features into a single column, masking sensitive data through ML techniques.

* **Coarsening**: Reduce granularity of fields like IP addresses, numeric quantities, and zip codes to protect individual identification.

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

**Encryption**: Protects data at rest and in transit.
* **IAM for Vertex AI Workbench**: Manages access control for your data science team.

**Secure ML Development**: Includes techniques like federated learning and differential privacy.
* **Cloud DLP & Healthcare APIs**: Manage PII and PHI data securely.
* **Large Dataset Architecture**: Scales PII identification and de-identification efficiently.

---

## 12.5. Exam Essentials

* **Secure ML systems**: Implement encryption at rest and in transit for Cloud Storage and BigQuery; manage IAM roles and network security for Vertex AI Workbench.
* **Privacy implications**: Use DLP API to identify and mask PII; use Healthcare API to identify and mask PHI.
* **Best practices**: Remove sensitive data by following recommended methods.

---

# 13. Chapter 7Model Building

---

## 13.1. Choice of Framework and Model Parallelism

* Modern deep learning models have more parameters
* Larger datasets require multinode training for efficient training
    * Data parallelism and model parallelism are common techniques used

---

### 13.1.1. Data Parallelism

* Data parallelism: Split dataset into parts, assign each part to a GPU/node with the same parameters.
    * Synchronous training: Gradient updates are aggregated before parameter updates across nodes.
    * Asynchronous training: Node updates parameters independently without waiting for others.
* Reduce learning rate if using many nodes to maintain smooth training.
* Reference: [Data Parallelism vs Model Parallelism](https://analyticsindiamag.com/data-parallelism-vs-model-parallelism-how-do-they-differ-in-distributed-training)

---

### 13.1.2. Model Parallelism

**Model Parallelism**: Splits a model across multiple GPUs to train large models that exceed single-GPU memory limits.
- **Benefits**: Allows training of larger models by distributing layers across GPUs, e.g., ResNet50 split into 10 GPU segments.

**Distributed Training Strategies in TensorFlow**: 
- **MirroredStrategy**: Synchronous multi-GPU training on a single machine.
- **MultiWorkerMirroredStrategy**: Synchronous distributed training across multiple machines with potential multiple GPUs per machine.
- **TPUStrategy**: Synchronous TPU core training.
- **ParameterServerStrategy**: Asynchronous training using parameter servers.

**Training and Deployment**: 

---

- Trained models can be deployed via `tf.serving`, TFLite, or TensorFlow.js.

---

![center w:85%](images/c07f002.png)

---


![center w:85%](images/note.png)

---


![center w:85%](images/c07f003.png)

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

* **Artificial Neural Networks (ANNs)**: Simplest type with one hidden layer.
* **Feedforward Neural Network**: Classic example of ANNs; used for supervised learning with numerical, structured data like regression problems.
    * **Supervised Learning**: Data is labeled and the model learns to predict outputs based on input features.

---


![center w:85%](images/c07f004.png)

---

### 13.2.2. Deep Neural Network (DNN)

* **Deep Neural Networks (DNNs)**: ANNs with multiple hidden layers.
* **Definition**: Increased depth in neural networks compared to shallow networks.
    * **Layers**: Typically at least two layers between input and output.
* **Abbreviation**: DNN or _deep net_.

---


![center w:85%](images/c07f005.png)

---

### 13.2.3. Convolutional Neural Network

* **Convolutional Neural Networks (CNNs)**: Designed for image input and excel in image classification.
* **Scope**: Suitable for various image-based tasks beyond just classification.

---

### 13.2.4. Recurrent Neural Network

**Recurrent Neural Networks (RNNs)**: Designed for sequential data, effective in natural language processing.
* **Long Short-Term Memory (LSTM) Networks**: Popular variant used for sequence prediction tasks.

**Neural Network Training**:
- Uses stochastic gradient descent.
- Requires a loss function to evaluate prediction accuracy.
- Goals: Minimize average loss across examples; gradients help update weights.

---

### 13.2.5. What Loss Function to Use

**Loss Function**: Depends on output layer configuration

* **Regression problem**: Mean squared error (MSE) with a linear activation unit in the output layer
* **Binary classification problem**: Binary cross-entropy, categorical hinge loss, and squared hinge loss with a sigmoid activation function
    * **Multiclass classification problem**: Categorical cross-entropy for one-hot encoded data; sparse categorical cross-entropy for integer-encoded labels

**Example Code Snippet**:
```python
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))

---

model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

---

![center w:85%](images/note.png)

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

* Gradient descent: calculates the gradient of the loss curve at the starting point
* Gradient: vector indicating the direction and magnitude of the steepest increase in the loss function
* Algorithm: takes steps in the direction of the negative gradient to minimize loss

---

### 13.2.7. Learning Rate

* Gradient vector: has direction and magnitude
* Gradient descent: multiplies gradient by learning rate (step size) to find next point
    * Example: gradient magnitude 2.5, learning rate 0.01 → next point is 0.025 away

---

### 13.2.8. Batch

* Batch: Total number of examples used to calculate the gradient in one iteration.
    * Large batch: Can make a single iteration computationally expensive.
* Entire dataset: Often assumed as the batch size in gradient descent.

---

### 13.2.9. Batch Size

* **Batch size**: Number of examples in a batch (e.g., SGD = 1, mini-batch = 10-1,000)
* **Dynamic batch size**: Permitted in TensorFlow during training and inference

---

### 13.2.10. Epoch

* **Epoch**: One full iteration through the entire training dataset.
* **Pass**: Consists of a forward pass and a backward pass.
* **Batch**: Comprises part of the data used in an epoch; multiple batches make up an epoch.

---

### 13.2.11. Hyperparameters

**Hyperparameters**: Parameters set before training begins and can be tuned.
* **Learning Rate**: Affects how quickly the model learns; too low = slow learning, too high may overshoot optimal solution.
* **Batch Size**: Influences computation speed; larger sizes reduce per-batch computation time but increase memory usage.

---

## 13.3. Transfer Learning

**Transfer Learning**: A technique in machine learning that involves using knowledge gained from one problem to improve performance on a different but related problem.

**Transfer Learning**: An optimization to save time or get better performance, especially useful when developing models with limited data.
* You can leverage pretrained models as a starting point for your own model training.

---

## 13.4. Semi‐supervised Learning

* **Semi-supervised learning (SSL)**: A machine learning approach combining labeled and unlabeled data.
    * **Labeled data**: Small amount of data with known labels.
    * **Unlabeled data**: Large amount of data without known labels.
* **Approach**: Bridges unsupervised and supervised learning by using both types of data.

---

### 13.4.1. When You Need Semi‐supervised Learning

**Semi-supervised learning**: Increases model accuracy with limited labeled data

- **Application Example**: Detecting fraud in banking by labeling known instances and using a semi-supervised algorithm to label unknown ones, then retraining the model.
    * **Outcome**: More accurate fraud detection but less trustworthy than traditional supervised techniques.

**Use Cases**:
* Fraud detection or anomaly detection
* Clustering
* Speech recognition
* Web content classification
* Text document classification

---

### 13.4.2. Limitations of SSL

* Semi-supervised learning effective with minimal labeled data and abundant unlabeled data in classification tasks.
* Not suitable for all tasks; requires representative labeled data.
* Inadequate if labeled data doesn't reflect the full distribution.

---

## 13.5. Data Augmentation

**Neural networks require many parameters**: Need proportional number of examples for good performance.

**Data requirements**: Large datasets needed; difficult to find relevant, large-scale datasets.

    * **Data augmentation**: Create synthetic data through minor changes (flips, rotations) to existing dataset when limited data is available.

**Augmentation methods**: Apply in two ways—offline (pre-processing) or online (during training)—to increase relevant data.

---

### 13.5.1. Offline Augmentation

* Offline augmentation: Increases dataset size through precomputed transformations.
    * Suitable for smaller datasets as it doubles with image rotations.
* Method preferred: Enhances training data without real-time processing.

---

### 13.5.2. Online Augmentation

**Data augmentation**: Transforming mini-batches before feeding them into a machine learning model, also known as _augmentation on the fly_, which is preferred for large datasets.

* **Techniques for images**: 
    * Flip, rotate, crop, scale, add Gaussian noise, translate
    * Use conditional GANs to transform images between domains
    * Apply `transfer learning` for better performance with limited data

---

## 13.6. Model Generalization and Strategies to Handle Overfitting and Underfitting

**Bias**: Model error rate on training data; high bias results in oversimplified models.

**Variance**: Model error rate on testing data; high variance leads to overfitting.

Training a deep neural network requires balancing capacity to avoid both underfitting (high bias) and overfitting (high variance).

---

### 13.6.1. Bias Variance Trade‐Off

**Bias-Variance Trade-off**: Balancing model complexity to avoid high bias and low variance (too simple) or high variance and low bias (too complex).

* **Underfitting**: Occurs with models that are too simple, requiring increased capacity.

**Overfitting**: Happens with overly complex models, needing specialized techniques to address.

---

### 13.6.2. Underfitting

**Underfit Model**: Performs poorly on both training and test datasets; characterized by high bias.

* **Data Quality Issues**: Training data not cleaned, leading to poor model performance.
* **High Bias**: Model is too simple to capture the underlying pattern in the data.

**Overfitting**: Performance varies widely with unseen examples due to excessive complexity.

* **Mitigate Underfitting**: Increase model complexity, add features through engineering, clean data, and extend training duration.

---

### 13.6.3. Overfitting

**Overfit Model**: Learns training data too well, performs inconsistently with new examples.

**Approaches to Reduce Overfitting**:
* Increase training data.
* Simplify network structure and parameters.

**Techniques to Avoid Overfitting**:
* Regularization.
  * **Dropout**: Remove inputs during training.
  * **Noise**: Add statistical noise to inputs.
* **Early stopping**: Monitor validation performance, stop training if it degrades.
* Data augmentation.
* Cross-validation.

**BigQuery ML Methods**:
* Early stopping.
* Regularization (see documentation).

**Additional Resources**:
* 10 ways to avoid overfitting: <https://www.v7labs.com/blog/overfitting>

---


![center w:85%](images/note.png)

---

### 13.6.4. Regularization

**Regularization**: Shrinks coefficients toward zero to reduce overfitting.

- **L1 Regularization**
    - Combats overfitting by shrinking parameters toward 0, making some features obsolete.
    - Penalizes absolute weight values; robust to outliers.
    - Useful for feature selection and smaller models.

- **L2 Regularization**
    - Forces weights to be small but not zero; improves generalization in linear models.
    - Penalizes squared weight values; less robust to outliers.

**Common Neural Network Issues**: Exploding gradients, dead ReLU units, vanishing gradients.


---

- **Exploding Gradients**: Large gradients from many large terms; handled by batch normalization and lower learning rates.
- **Dead ReLU Units**: Occurs when weighted sum < 0, unit outputs zero; mitigated by lowering learning rate.
- **Vanishing Gradients**: Lower layers get very small gradients; ReLU activation helps.

**Regularization Techniques**:
- **Dropout Regularization**: Randomly drops out units for a single gradient step (useful for neural networks).
- **Gradient Clipping**: Limits the size of weight updates to prevent exploding gradients.
- **Batch Normalization**: Normalizes layer inputs, helping with vanishing/exploding gradients.

**Loss Reduction Tips**:

---

- Increase network depth and width.
- Use different features if current ones are not informative.
- Decrease learning rate; increase model complexity carefully.
- Utilize cross-validation or bootstrapping for small datasets.
- Simplify the model to check predictive power of individual features.

---

![center w:85%](images/tip.png)

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

* **Model Parallelism & Data Parallelism**: Strategies for training TensorFlow models.
* **Training Neural Networks**: Loss functions, gradient descent, learning rate, batch size, epochs, hyperparameters.
    * **Hyperparameters Impact**: Decreasing learning rate or increasing epochs affect model training.
* **Advanced Techniques**:
    * **Transfer Learning**: Advantages and use cases.
    * **Semi-Supervised Learning**: When needed and limitations.
    * **Data Augmentation**: Online and offline techniques like rotation and flipping.
    * **Model Fit & Regularization**: Underfitting, overfitting, and regularization concepts.

---

## 13.8. Exam Essentials

* **Choose parallelism strategy**: Select framework or model parallelism for multinode training.
  * **Multinode training**: Use data or model parallel strategies; know TensorFlow distributed training techniques.

* **Understand modeling techniques**: Choose loss functions (sparse cross-entropy vs. categorical), grasp gradient descent, learning rate, batch size, and epochs as hyperparameters to tune for optimal performance.

* **Transfer learning**: Utilize pretrained models to aid in training with limited data.

* **Semi-supervised learning (SSL)**: Apply when labeled data is scarce; understand its limitations.


---

* **Data augmentation**: Use techniques like flipping, rotation, GANs, and transfer learning for enhanced dataset diversity.

* **Model generalization & overfitting/underfitting strategies**: Handle bias-variance trade-off; apply regularization (L1/L2) to prevent overfitting and underfitting.

---
# 14. Chapter 8Model Training and Hyperparameter Tuning

---

## 14.1. Ingestion of Various File Types into Training

* Data types: structured (tables, CSV), semi-structured (PDFs, JSON), unstructured (chats, emails, images)
* Data flow: batch or real-time streaming
* Data scale: small to petabyte
* Preparation: cleaning and transforming data for ML training
* Tools: Google Cloud analytics portfolio for data management

---


![center w:85%](images/c08f001.png)

---

### 14.1.1. Collect

**Google Cloud Pub/Sub and Lite**: Real-time messaging and analytics with scalable serverless services for global publishing and subscribing; Pub/Sub Lite optimizes for cost over reliability.

**Datastream**: Serverless change data capture (CDC) service for moving on-premises Oracle and MySQL databases to Google Cloud storage, integrating with Dataflow and templates for loading into BigQuery, Cloud Spanner, and Cloud SQL.

**BigQuery Data Transfer Service**: Automates data ingestion from Teradata, Amazon Redshift, S3, and Google SaaS apps like Cloud Storage and Google Ads directly into BigQuery.

---

### 14.1.2. Process

* **Data processing tools**: Required for transforming raw data into a format suitable for ML training.
* **Tool selection**: Varies based on data source and specific needs.

---

### 14.1.3. Store and Analyze

**Google Cloud Storage Options**: 
- **Tabular data**: BigQuery, BigQuery ML
- **Image, video, audio, unstructured data**: Google Cloud Storage
- **Unstructured data**: Vertex Data Labeling
- **Structured data**: Vertex AI Feature Store
- **AutoML image, video, text**: Vertex AI Managed Datasets

* * *

**Storage Recommendations**:
- Avoid block storage like NFS and VMs.
- Avoid direct database reads from Cloud SQL.

* * *

**Data Storage Tips**:
- Use large container formats for image, video, audio on Cloud Storage.
- Combine data into files of at least 100 MB; aim for 100 to 10,000 shards.
- For TensorFlow: Sharded TFRecord files.
- For other frameworks: Avro files in Cloud Storage.

---

- Use TensorFlow I/O for Parquet format management.

---

![center w:85%](images/tip.png)

---


![center w:85%](images/note.png)

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

**Vertex AI Workbench**: Jupyter Notebook-based environment for data science workflow

* **User-managed notebook**
    * Older version with more control and fewer features
    * No automated shutdown, UI integration with Cloud Storage or BigQuery, no automated runs, custom containers not supported
* **Managed notebook**
    * Latest offering; supports automated shutdown, UI integration, scheduled runs, custom containers, Dataproc/Serverless Spark, multiple frameworks
* Both notebooks include pre-installed deep learning packages and integrate with GitHub

---

*Developing Models in Vertex AI Workbench by Using Common Frameworks*
Managed notebook | User‐managed notebook
---|---
**Automated shutdown for idle instances:** Choosing a managed notebook will shut down your Jupyter Notebooks when not in use. This feature helps save costs because the instances will shut down when not in use automatically. | **Automated shutdown for idle instances:** This feature is not supported out of the box. However, you can create a monitor to see when instances are idle using Cloud Monitoring and Cloud Functions and shut them down when not in use.
**UI integration with Cloud Storage and BigQuery:** From within JupyterLab's navigation menu on a managed notebooks instance, you can use the Cloud Storage and BigQuery integration to browse data and other files that you have access to and load data into your notebook. | **UI integration with Cloud Storage and BigQuery:** There is no UI integration. However, you can use the BigQuery connector to connect to BigQuery data using code or you can also use the BigQuery magic (`%%`) command to run BigQuery SQLl commands on a Jupyter Notebook.

<!-- _class: centered -->

---

### 14.2.1. Creating a Managed Notebook

**Enable APIs**: Go to Vertex AI and enable All APIs.

**Create Managed Notebook**: Click Workbench > Managed Notebooks > New Notebook > Create (Figure 8.4).

**Open JupyterLab**: After creation, click Open JupyterLab button (Figure 8.5). 

* **Upgrade Option**: Notice the manual upgrade option for managed notebooks.

---


![center w:85%](images/c08f004.png)

---


![center w:85%](images/c08f005.png)

---


![center w:85%](images/note.png)

---

### 14.2.2. Exploring Managed JupyterLab Features

**Managed Notebook Environment**: Contains Serverless Spark and PySpark for local use.
* **Serverless Spark**: Runs Dataproc cluster within the notebook.
**Tutorials Folder**: Includes pre-made notebooks to facilitate model building and training.
* **Terminal Option**: Allows running terminal commands on the entire notebook.

---


![center w:85%](images/c08f006.png)

---

### 14.2.3. Data Integration

* Click the Browse GCS icon to access cloud storage folders.
* Load data from Google Cloud Storage into a managed notebook.

---


![center w:85%](images/c08f007.png)

---

### 14.2.4. BigQuery Integration

* Click the BigQuery icon to access data from your tables.
* Use the SQL editor directly in JupyterLab for querying BigQuery tables.

---


![center w:85%](images/c08f008.png)

---

### 14.2.5. Ability to Scale the Compute Up or Down

**Modify Jupyter Environment Hardware**: Choose `n1-standard-4` instance and adjust settings.
* **Attach GPU**: Option available directly within the environment.

---

### 14.2.6. Git Integration for Team Collaboration

* Integrate or clone repositories in a managed notebook
    * Click left navigation icon for integration or use `git clone` command
* Scale hardware by managing notebook resources (Fig. 8.9)
* Enable git functionality with managed notebook interface (Fig. 8.10)

---


![center w:85%](images/c08f009.png)

---


![center w:85%](images/c08f010.png)

---

### 14.2.7. Schedule or Execute a Notebook Code

**Python Execution**: Write "hello world," click Run cell, use black triangle arrow.

**Automatic Execution**: Click Execute (Figure 8.11) to submit notebook for scheduling (Figure 8.12).

**Scheduling Notebook**: Navigate to Type option (Figure 8.13) to schedule one-time or timed runs.

---


![center w:85%](images/c08f011.png)

---


![center w:85%](images/c08f012.png)

---


![center w:85%](images/c08f013.png)

---

### 14.2.8. Creating a User‐Managed Notebook

**User-Managed Notebooks**: Choose the execution environment (e.g., TensorFlow) during creation.
* **Execution Environment**: Select from options like Python 3, TensorFlow, R, JAX, Kaggle, PyTorch.
**Advanced Options**: Configure networking with shared VPCs.
**Hardware Considerations**: Use small hardware instances for development; training occurs in separate containers managed by Vertex AI.

---


![center w:85%](images/c08f014.png)

---


![center w:85%](images/c08f015.png)

---


![center w:85%](images/c08f016.png)

---


![center w:85%](images/note.png)

---

## 14.3. Training a Model as a Job in Different Environments

**AutoML**: Enables minimal-effort creation and training of models.

**Custom training**: Offers full control over training applications for tailored outcomes, including algorithm selection, loss function development, and metric definition.

---

### 14.3.1. Training Workflow with Vertex AI

**Training pipelines**: Primary workflow for training AutoML or custom models; orchestrate steps including dataset addition and model upload.

**Custom jobs**: Specify settings for running custom training code, used only with custom-trained models.

**Hyperparameter tuning jobs**: Search for optimal hyperparameters by optimizing metric values across trials, used only with custom-trained models.

---


![center w:85%](images/c08f017.png)

---


![center w:85%](images/note.png)

---

### 14.3.2. Training Dataset Options in Vertex AI

**No Managed Dataset**: Use Cloud Storage or BigQuery data for training via Vertex AI managed notebooks, integrating with Google Cloud Storage FUSE for specifying datasets.

**Managed Dataset**: Centralize dataset management, create labels, use integrated data labeling, track lineage, compare model performance, generate statistics, and automatically split data.

* **Custom Training Jobs**: Mount NFS shares to containers for accessing remote files locally.

---


![center w:85%](images/note.png)

---

### 14.3.3. Pre‐built Containers

* **Vertex AI Training with Prebuilt Containers**: Use scikit-learn, TensorFlow, PyTorch, or XGBoost containers hosted on the container registry.
    * **Code Structure**: Organize code in a root folder with `setup.py` and a trainer folder containing `task.py` (entry point).
    * **Training Setup**: Upload training code as Python source distribution to Cloud Storage; use `gcloud ai custom-jobs create` command for job creation.

* **Custom Job Command**: Builds Docker image based on prebuilt container and local code, pushes to Container Registry.
    * **Parameters**:
        * **LOCATION**: Region where the container will run.
        * **JOB_NAME**: Display name for the CustomJob.

---

        * **MACHINE_TYPE**: Type of machine; refer to available training machine types.
        * **REPLICA_COUNT**: Number of worker replicas (usually 1).
        * **EXECUTOR_IMAGE_URI**: URI of base container image for new Docker image.
        * **WORKING_DIRECTORY**: Local directory containing entry point script.

---

![center w:85%](images/c08f018.png)

---


![center w:85%](images/c08f019.png)

---

### 14.3.4. Custom Containers

**Custom Container Benefits:**
- Faster startup time: Preinstall dependencies to save time on application boot.
- Flexibility in ML framework choice: Use any preferred framework, e.g., PyTorch.
- Distributed training support: Enable distributed training with various frameworks.

**Creating a Custom Container for Vertex AI Training:**
- **Step 1: Setup Files:** Create Dockerfile and `trainer/task.py` in root directory. Dockerfile installs dependencies, copies code, sets entry point.
    * Example Dockerfile:
      ```docker
      FROM image:tag
      WORKDIR /root

      RUN pip install pkg1 pkg2 pkg3
      RUN curl https://example-url/path-to-data/data-filename --output /root/data-filename

---

      COPY your-path-to/model.py /root/model.py
      COPY your-path-to/task.py /root/task.py

      ENTRYPOINT ["python", "task.py"]
      ```
- **Step 2: Build and Push:** Use provided commands to build and push Docker image to Artifact Registry.
    * Commands:
      ```bash
      export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
      export REPO_NAME=REPOSITORY_NAME
      export IMAGE_NAME=IMAGE_NAME
      export IMAGE_TAG=IMAGE_TAG
      export IMAGE_URI=us-central1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}

      docker build -f Dockerfile -t ${IMAGE_URI} ./
      docker push ${IMAGE_URI}
      ```

---

- **Step 3: Start Training:** Create custom job using `gcloud` command.
    * Command:
      ```bash
      gcloud ai custom-jobs create \
           --region=_LOCATION_ \
           --display-name=_JOB_NAME_ \
           --worker-pool-spec=machine-type=_MACHINE_TYPE_ ,replica-count=_REPLICA_COUNT_ ,container-image-uri=_CUSTOM_CONTAINER_IMAGE_URI_
      ```

* * *

By running training jobs in custom containers, you can leverage unsupported ML frameworks and dependencies.

---

![center w:85%](images/c08f020.png)

---


![center w:85%](images/tip.png)

---

### 14.3.5. Distributed Training

**Distributed Training with Vertex AI:**
- **Replica and Worker Pools**: Define multiple nodes (replicas) in a training cluster; worker pools of identical configurations handle different tasks.
    * **Primary Replica**: Manages other replicas, reports job status.
    * **Worker Replicas**: Perform the bulk of the work based on your configuration.
    * **Parameter Servers & Reduction Server**: Store model parameters and manage shared state or increase throughput/reduce latency using all-reduce algorithms.

- **Configuring Distributed Training**:
    - Use ML frameworks like TensorFlow, PyTorch with NCCL.

---

    - Set up worker pools in `workerPoolSpecs[]` for different roles (e.g., primary, workers).
    - For Vertex AI Reduction Server: Follow prerequisites; use Docker container images to configure worker pools.

- **Example Setup**:
    ```sh
    gcloud ai custom-jobs create \
      --region=_LOCATION_ \
      --display-name=_JOB_NAME_ \
      --worker-pool-spec=machine-type=n1-highmem-96,replica-count=1,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=8,container-image-uri=_CUSTOM_CONTAINER_IMAGE_URI_ \
      --worker-pool-spec=machine-type=n1-highmem-96,replica-count=4,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=8,container-image-uri=_CUSTOM_CONTAINER_IMAGE_URI_ \

---

      --worker-pool-spec=machine-type=n1-highcpu-16,replica-count=16,container-image-uri=us-docker.pkg.dev/vertex-ai-restricted/training/reductionserver:latest
    ```

---
*Distributed Training*
Position in workerPoolSpecs[] | Task Performed in Cluster
---|---
First (`workerPoolSpecs[0]`) | Primary, chief, scheduler, or “master.” Exactly ‐one replica is designated the _primary replica_. This task manages the others and reports status for the job as a whole.
Second (`workerPoolSpecs[1]`) | Secondary, replicas, workers.

<!-- _class: centered -->

---

## 14.4. Hyperparameter Tuning

* Hyperparameters: Parameters of the training algorithm set before learning begins.
* **Learning rate**: Key hyperparameter in gradient descent that influences model training.
* *FIGURE 8.21*: Illustrates the distinction between model parameters and hyperparameters.

---


![center w:85%](images/c08f021.png)

---

### 14.4.1. Why Hyperparameters Are Important

**Hyperparameter Selection**: Crucial for neural network success as it influences model behavior.

* **Search Space Optimization**: Vertex AI uses Bayesian optimization to efficiently search through hyperparameters.
    * **Bayesian Search**: Considers past evaluations to choose the next hyperparameter set, reducing dimensionality issues compared to grid and random search.

**Hyperparameter Tuning**: Automates the process of finding optimal settings using Google Cloud's compute infrastructure.

* **Experiment Management**: Facilitates large-scale testing, providing optimized hyperparameters for better model accuracy.

---

### 14.4.2. Techniques to Speed Up Hyperparameter Optimization

**Distributed Training**: Increase speed by parallelizing across multiple machines.

**Reduced Validation Set**: Use a simple validation set for large datasets to speed up optimization by a factor of ~k, but requires sufficient data.

**Pre-computation/Caching**: Avoid redundant computations to boost efficiency.

**Random Search**: Utilize random search for fewer trials and improved performance.

**Bayesian Optimization**: Explore cloud-based tools like Google Cloud Machine Learning Engine for hyperparameter tuning.

---


![center w:85%](images/tip.png)

---

### 14.4.3. How Vertex AI Hyperparameter Tuning Works

**Hyperparameter Tuning**: Runs multiple training sessions with varied hyperparameters to optimize model performance.
* **Communication**: Involves interaction between Vertex AI and the training application, where the latter defines necessary information.
    * **Metrics**: Specifies target variables (e.g., accuracy) to evaluate each trial, ensuring they are numeric.

**Configuration Steps Using gcloud CLI**:
1. Install `cloud-ml hypertune` package in Dockerfile for custom container.
2. Add hyperparameter tuning code in main function and define metrics.
3. Build and push the container to Artifact Registry; configure using a training pipeline or custom job.


---

**Setting Up Hyperparameter Tuning Job with YAML**:
1. Define study specification with metric ID, goal, parameter ID, and value range.
2. Specify trial job details like machine type and Docker image URI in `config.yaml`.
3. Run command to create custom job for hyperparameter tuning.

**Additional Notes**: Can use default Bayesian algorithm or specify a search algorithm; track progress on Vertex AI console.

---

![center w:85%](images/c08f022.png)

---

### 14.4.4. Vertex AI Vizier

**Vertex AI Vizier**: A black-box optimization service for tuning hyperparameters in complex ML models.

* **No known objective function**: Evaluates without a predefined goal.
* **Costly evaluations**: Handles systems too complex or expensive to evaluate frequently.
* **Versatile use cases**: Optimizes hyperparameters, model parameters, and any system that can be evaluated.

- Optimize neural network hyperparameters
- Improve application usability through UI design
- Minimize computing resources for jobs
- Optimize recipe ingredients for best results

---

## 14.5. Tracking Metrics During Training

* **Interactive Shell**: For real-time model debugging
* **TensorFlow Profiler**: To analyze and optimize model performance
* **What-If Tool**: For exploring and explaining model predictions

---

### 14.5.1. Interactive Shell

**Interactive Shell**: Accessible while the job is in the RUNNING state, it allows inspecting the file system and running debugging utilities.

**Web Terminal**: Created for each node during job execution; provides access via links on the job details page after Vertex AI starts running your job.

* **Tools for Metric Tracking & Profiling**:
    * `py-spy`: Visualizes Python program execution without modifying code.
    * `nvidia-smi` and `nvprof`: Monitor GPU usage in GPU-enabled containers.
    * Perf: Analyzes training node performance using Linux profiling with performance counters.

---


![center w:85%](images/c08f023.png)

---


![center w:85%](images/c08f024.png)

---

*Interactive Shell*
Visualize Python Execution with py‐spy | Retrieve Information about GPU Usage | Analyze Performance with Perf
---|---|---
py‐spy is a sampling profiler for Python programs. It lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way. | GPU‐enabled containers running on nodes with GPUs typically have several command‐line tools preinstalled that can help you monitor GPU usage. You can use `nvidia‐smi` to monitor GPU utilization of various processes or use `nvprof` to collect a variety of GPU profiling information. | Perf lets you analyze the performance of your training node. It's a way to do Linux profiling with performance counters.

<!-- _class: centered -->

---

### 14.5.2. TensorFlow Profiler

**Vertex AI TensorBoard**: Enterprise-ready managed version of TensorBoard for monitoring and optimizing model training.

* **Profiler**: Helps understand resource consumption to pinpoint and fix performance bottlenecks, accelerating model training.
    * **Access**: Via custom jobs or experiments page in Google Cloud console.
    * **Capture**: Requires a running training job.

**TF Profiler**: Allows on-demand profiling of remote Vertex AI training jobs, visualizing results in Vertex TensorBoard.

---

### 14.5.3. What‐If Tool

**What-If Tool (WIT)**: Interactive dashboard for inspecting AI Platform Prediction models.

* **Integration**: Supports TensorBoard, Jupyter Notebooks, Colab notebooks, and Vertex AI Workbench user-managed notebooks.
    * **Preinstallation**: Included in Vertex AI Workbench notebooks and TensorFlow instances.

**Usage**:
1. Install `witwidget` library (preinstalled in Vertex AI Workbench).
2. Configure `WitConfigBuilder` to inspect or compare models using project, model name, version, target feature, and label vocabulary.
3. Display WIT widget with specified height:
   ```python
   WitWidget(config_builder, height=800)
   ```


---

**Example**: Explore the tool in this Colab notebook: *[https://colab.research.google.com/github/pair-code/what-if-tool/blob/master/What_If_Tool_Notebook_Usage.ipynb]*.

---
## 14.6. Retraining/Redeployment Evaluation

* Model performance decays over time due to changes in user behavior and training data.
* Decay rates vary among models.
* **Data drift**: change in the distribution of input features.
* **Concept drift**: shift in the relationship between inputs and outputs.

---

### 14.6.1. Data Drift

* Data drift: Change in production data's statistical distribution from training data
    * Detection methods: Monitor feature attribution changes, check for input unit shifts (e.g., Fahrenheit to Celsius)
* Feature distribution: Examine changes in how features are distributed
* Monitoring system: Use to track schema and correlation changes over baseline

---

### 14.6.2. Concept Drift

**Concept Drift**: Change in the statistical properties of the target variable over time.

**Detection**: Requires monitoring of deployed models; can be achieved using Vertex AI Model Monitoring.

* **Vertex AI Model Monitoring**: Tool for detecting concept drift by monitoring deployed models.

---

### 14.6.3. When Should a Model Be Retrained?

**Retraining strategies**: Choose an interval (weekly/monthly/yearly) based on data update frequency for periodic training.

* **Performance-based trigger**: Retrain when model performance falls below predefined threshold, assuming a robust monitoring system is in place.

**Data changes trigger**: Rebuild models if data drift occurs, indicated by changes in model performance.

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

**Machine Learning Testing**: Involves testing code, model, and data.

* **Model Code Testing**: Ensures units of code function as expected through unit tests.
    * **Data Testing**: Checks model output shape, output ranges, gradient steps, dataset assertions, and label leakage between training and validation sets.

---

### 14.7.1. Testing for Updates in API Calls

* Test API updates: Retrain the model, which is resource-intensive.
* Test API updates: Write a unit test for random input generation and one-step gradient descent.
* Simplify testing: Avoid runtime errors during development.

---

### 14.7.2. Testing for Algorithmic Correctness

* Verify model correctness by checking decreasing loss during training
* Train without regularization; expect low training loss if model is complex
* Test individual components like CNN parts for correct operation per input element

---

## 14.8. Summary

* **File types**: Structured, unstructured, semi-structured; ingestion stages: collect, process, store, analyze
    * **Collect**: Pub/Sub, Pub/Sub Lite
    * **Store & Analyze**: BigQuery Data Transfer Service, Datastream, Cloud Dataflow, Cloud Data Fusion, Cloud Dataproc, Cloud Composer, Cloud Dataprep

* **Model training**: Vertex AI training; frameworks: scikit-learn, TensorFlow, PyTorch, XGBoost; prebuilt and custom containers

* **Training validation**: Unit test data and models for machine learning

* **Hyperparameter tuning**: Vertex AI Vizier; search algorithms

* **Model tracking & debugging**: Vertex AI metrics, interactive shell, TensorFlow Profiler, What-If Tool


---

* **Drift management**: Retrain model to avoid data drift or concept drift

---
## 14.9. Exam Essentials

* **Ingest data into Google Cloud**: Use Pub/Sub, BigQuery Data Transfer Service, and Datastream for structured, unstructured, and semi-structured files.
    * **Process data**: Utilize Cloud Dataflow, Cloud Data Fusion, Cloud Dataproc, Cloud Composer, and Cloud Dataprep for ETL jobs.
* **Use Vertex AI Workbench**: Understand managed vs. user-managed notebooks; know how to create and use them with supported frameworks.
* **Train models in Vertex AI**:
    * **Model training options**: AutoML, custom training using prebuilt or custom containers.
    * **Training setup**: Use pipelines or custom jobs; support for scikit-learn, TensorFlow, PyTorch, XGBoost.

---

    * **Distributed training**: Set up using Vertex AI custom jobs.
* **Test models**: Unit test data and models; test APIs after updates.
* **Hyperparameter tuning**:
    * **Search algorithms**: Grid search, random search, Bayesian search.
    * **Setup**: Use custom jobs; understand Vertex AI Vizier.
* **Track training metrics**: Use Interactive shell, Tensorflow Profiler, What-If tool.
* **Evaluate retraining/redeployment**:
    * **Bias variance trade-off**: Strategies for underfitting and overfitting.
    * **Regularization**: L1 vs. L2; when to apply each.

---
# 15. Chapter 9Model Explainability on Vertex AI

---

## 15.1. Model Explainability on Vertex AI

**Model Explainability**: Increases with the impact of predictions on business outcomes.
* **Examples**:
    * Movie recommendations: Low explainability required.
    * Credit loan approval or drug dosage prediction: High explainability required.
**Visibility into Training Process**: Important for developing human-explainable ML models.

---

### 15.1.1. Explainable AI

**Explainability**: The extent to which ML models can be understood by humans.

* **Global Explainability**: Makes the overall ML model transparent.
* **Local Explainability**: Explains individual predictions made by the model.

Debugging complex models like deep neural nets is difficult due to their opacity, whereas linear models and decision trees are more interpretable. Explainable techniques are necessary for understanding and debugging these models.

---

### 15.1.2. Interpretability and Explainability

* **Interpretability**: Accuracy in associating causes with effects in machine learning models.
* **Explainability**: Ability to justify model results using hidden parameters in deep neural networks.
    * **Deep neural nets**: Covered in Chapter 7, "Model Building".

---

### 15.1.3. Feature Importance

* Feature importance: Scores indicating the value of each feature in constructing boosted decision trees.
    * Variable selection: Helps identify unimportant variables for model deployment, reducing costs and time.
* Target/label or data leakage detection: Identifies accidental inclusion of target variable as a feature.

---

### 15.1.4. Vertex Explainable AI

* **Vertex Explainable AI**: Integrates feature attributions to help understand model outputs for classification and regression tasks.
    * **Feature attributions**: Shows the contribution of each data feature to predicted results, aiding in model verification, bias recognition, and improvements.
* **Supported Services**:
    * AutoML image models (classification only)
    * AutoML tabular models (classification and regression only)
    * Custom-trained TensorFlow models (tabular or image data)

---

### 15.1.5. Data Bias and Fairness

* **Data Bias**: Occurs when certain parts of data are not collected or misrepresented.
    * **Types**: Surveys, systemic/historical beliefs, non-random/sample size issues.
* **ML Fairness**: Ensures models do not treat individuals unfavorably based on protected characteristics (race, gender, etc.).
* **Detection Tools**:
    * Vertex AI's Explainable AI feature attributions in AutoML tables.
    * Interactive `What-If Tool` dashboard for bias detection in datasets.
    * Open-source `Language Interpretability Tool` for NLP models.

---

### 15.1.6. ML Solution Readiness

**Responsible AI**: Principles and tools to ensure ethical use of AI models.
    * **Explainable AI**: Using Vertex AI offerings for transparent model construction.
    * **Model cards**: Documentation explaining model functionality, audience, and maintenance.

**Model governance**: Processes to implement company AI principles.
    * Human in the loop for sensitive tasks.
    * Responsibility assignment matrix per task.
    * Maintain model cards for versioning and data lineage.
    * Evaluate models on benchmark datasets and validate fairness.
    * Use what-if analysis tools for feature importance.

---

### 15.1.7. How to Set Up Explanations in the Vertex AI

**Custom-trained models**: Configure explanations for custom models (`https://cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based`).

**AutoML models**: No specific configuration required for AutoML tabular classification or regression to use Vertex Explainable AI (`https://cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations`).

* **Online explanations**: Send `explain` requests instead of `predict` requests to get predictions with feature attributions.
* **Batch explanations**: Set the generateExplanation field to true in batch prediction jobs to obtain feature attributions asynchronously.

---

* **Local kernel explanations**: Generate explanations locally using Vertex Explainable AI within a User-Managed Vertex AI Workbench notebook, without deploying the model.

**Explainable AI SDK**: Preinstalled in user-managed notebooks; use `save_model_with_metadata()` for TensorFlow models and `explain()` to visualize feature attributions.

---

![center w:85%](images/note.png)

---

## 15.2. Summary

**Explainable AI**: Technique to make machine learning models understandable

**Feature Importance**: Key factor in explaining model decisions; highlights critical input features

**Data Bias & Fairness**: Essential for ensuring ML models are unbiased and fair

**ML Solution Readiness**: Evaluating if an ML solution is ready for deployment

* **Explainable AI Techniques on Vertex AI Platform**
    * **Sampled Shapley**
    * **XRAI**
    * **Integrated Gradients**

---

## 15.3. Exam Essentials

**Explainability on Vertex AI**: Know global and local explanations, feature importance, and use options like Sampled Shapley, integrated gradients, XRAI.

**Responsible AI & ML Governance**: Cover data bias, fairness, and feature attributions for identifying biases.

**Vertex AI Support**: Explainable AI SDK for TensorFlow prediction container and AutoML tabular/image models.

---

# 16. Chapter 10Scaling Models in Production

---

## 16.1. Scaling Prediction Service

**Saved Model**: A complete TensorFlow program including trained parameters and computation; can be shared or deployed using various tools.

* **Deployment Options**: TensorFlow Lite, TensorFlow.js, TensorFlow Serving, TensorFlow Hub

**TF Model Serving Options**: Represented in Figure 10.1, showing distribution strategies with CPUs, GPUs, and TPUs.

---


![center w:85%](images/c10f001.png)

---

### 16.1.1. TensorFlow Serving

**TensorFlow Serving**: Hosts trained TensorFlow models as API endpoints for model serving and version management.

**API Endpoints**: Supports REST and gRPC.

**Setup Steps**:
1. Install TensorFlow Serving with Docker.
2. Train and save a model with TensorFlow.
3. Serve the saved model using TensorFlow Serving.

* * *

**Installation**: Recommended to install TensorFlow Serving with Docker; managed containers on Vertex AI can also be used for management.

---


![center w:85%](images/note.png)

---

## 16.2. Serving (Online, Batch, and Caching)

* Batch Prediction (Offline Serving): For processing large datasets not requiring real-time responses.
* Online Prediction: For real-time requests needing immediate results.
* Best Practices for Serving and Caching Strategy: To be covered in Chapter 5.

---

### 16.2.1. Real‐Time Static and Dynamic Reference Features

* **Static Reference Features**: Values do not change in real time; typically updated in batches, stored in a data warehouse like Firestore.
* **Dynamic Real-Time Features**: Computed on the fly using event-stream processing pipelines; used for real-time use cases like predicting engine failure or recommending news articles based on current session activity.
    * **Storage and Processing**: Stored in low-latency databases such as Cloud Bigtable, processed via Dataflow streaming pipelines.

---


![center w:85%](images/c10f002.png)

---


![center w:85%](images/c10f003.png)

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

**Offline Batch Scoring**: Pre-compute predictions in batch jobs and store them for quick online serving.

* **Key-Value Store**: Data ingested, processed, and stored with keys.
* **Batch Prediction Job**: Trained model runs on prepared data to produce key-identified predictions.
* **Low-Latency Data Store**: Export predictions to a store optimized for fast singleton reads.
* **Client Request**: Sends prediction request by unique key; ML gateway fetches and returns the prediction.

**Lookup Keys**: 
  * Specific Entity: Use for single-entity IDs (e.g., customer ID, device ID).
  * Feature Combination: Hash input features to create keys for anonymous/new customers.

---


![center w:85%](images/c10f004.png)

---

## 16.3. Google Cloud Serving Options

**Online Predictions**: Deploy models for real-time predictions.

**Batch Predictions**: Process data in batches for predictions.

**Vertex AI**: Use for setting up online and batch prediction jobs for both AutoML and custom models.

---

### 16.3.1. Online Predictions

**Real-time Prediction Endpoint Setup:**

* **Models trained in Vertex AI using Vertex AI training:** AutoML or custom models.
* **Model trained elsewhere (on-premise, on another cloud, or in local device):** Import to Google Cloud before deployment.
    * **Prebuilt container import:** Use specific filenames like `saved_model.pb` for TensorFlow, `model.joblib`/`pkl` for scikit-learn, and `model.bst`, `joblib`, or `pkl` for XGBoost.
* **Custom container import:** Create a container image and push to Artifact Registry using Cloud Build.

**Prediction Setup Steps:**

1. Deploy model resource to an endpoint.
2. Make a prediction.
3. Undeploy if the endpoint is not in use.

---

### 16.3.2. Batch Predictions

**Batch Prediction**: Run model on input data stored in Cloud Storage and save results back to Cloud Storage.
- **Input Data Preparation**: Ensure data is formatted as per AutoML or custom model requirements (JSON Lines, TFRecord, CSV, File list, BigQuery).
    * **Options for Custom-Trained Models**: JSON Lines, TFRecord, CSV, File list, BigQuery.
**Execution**: Use Vertex AI APIs or console to create a batch prediction job; output can be stored in BigQuery or Cloud Storage.
- **Output Options**: Choose between BigQuery table or Google Cloud Storage bucket.
    * **Model Monitoring**: Enable for skew detection (in Preview).

---


![center w:85%](images/c10f007.png)

---


![center w:85%](images/tip.png)

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

**MLflow Tracking**: For experiment tracking and parameter comparison.

**MLflow Projects**: Package ML code for reuse and sharing.

**MLflow Models**: Manage and deploy models across various serving platforms.

**MLflow Model Registry**: Centralized model store with versioning and stage transitions.

* **Google Cloud Setup**: Use PostgreSQL DB for metadata, Cloud Storage bucket for artifacts, Compute Engine or Kubernetes for server installation.  
* **Alternative Installation**: Run MLflow using a Google Cloud plugin (`https://pypi.org/project/google-cloud-mlflow`).

---

## 16.5. Testing for Target Performance

**Model Performance Testing**: Ensure real-time data quality and check for training-serving skew.
* **Numerical Stability**: Verify model weights and outputs are not NaN or null; ensure more than half of layer outputs are non-zero.
**Vertex AI Services**: Use Vertex AI Model Monitoring and Feature Store for detecting skew and monitoring performance.

---

## 16.6. Configuring Triggers and Pipeline Schedules

**Cloud Scheduler**: Schedule Vertex AI training or prediction jobs using a cron job.
* **Cloud Workflows**: Orchestrate multiple HTTP-based services into a durable and stateful workflow, useful for chaining microservices like data cleaning, transformation, and model deployment.

**Vertex AI Pipelines**: Automate, monitor, and govern ML systems by orchestrating ML workflows in a serverless manner and storing artifacts using Vertex ML Metadata.
* **Cloud Composer**: Orchestrate data-driven workflows (particularly ETL/ELT) using Python as DAG definition files, supporting pipelines across multiple cloud platforms.


---

**Cloud Functions & Cloud Pub/Sub**: Use event-based triggers for deploying models or retraining jobs. Consider using an orchestrator like Cloud Workflows for complex workflows involving multiple functions.
* * *

For more information: [Choosing the Right Orchestrator on Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/choosing-right-orchestrator-google-cloud)

---

![center w:85%](images/note.png)

---

*Configuring Triggers and Pipeline Schedules*
Option | Description
---|---
Vertex AI Pipelines | Vertex AI Pipelines helps you to automate, monitor, and govern your ML systems by orchestrating your ML workflow in a serverless manner and storing your workflow's artifacts using Vertex ML Metadata. By storing the artifacts of your ML workflow in Vertex ML Metadata, you can analyze the lineage of your workflow's artifact.
Cloud Composer | Cloud Composer is designed to orchestrate data‐driven workflows (particularly ETL/ELT). It's built on the Apache Airflow project, but Cloud Composer is fully managed. Cloud Composer supports your pipelines wherever they are, including on‐premises or across multiple cloud platforms. All logic in Cloud Composer, including tasks and scheduling, is expressed in Python as directed acyclic graph (DAG) definition files.

<!-- _class: centered -->

---

## 16.7. Summary

**TF Serving**: Enables scalable prediction services using the `predict` function and SignatureDef of saved models.
* **Serving Architecture**: Discussed static and dynamic architectures, focusing on pre-computing and caching for efficiency.
* **Deployment Options**: Covered online and batch deployment with Vertex AI Prediction and Google Cloud serving options.
    * **Performance Considerations**: Addressed performance degradation due to training-serving skew and data quality changes.
* **Automation Tools**: Learned about using Cloud Run, Cloud Build, Cloud Scheduler, Vertex AI managed notebooks, and Cloud Composer for model pipelines.

---

## 16.8. Exam Essentials

**TensorFlow Serving**: Deploy trained TensorFlow models; set up with Docker; understand prediction responses.

**Prediction Services Scaling**: Online vs. batch serving; handle real-time (static/dynamic) and caching strategies.

**Google Cloud Options**: Real-time endpoints via Vertex AI Prediction; use APIs or GCP console; batch predictions setup.

**Performance Testing**: Monitor model performance degradation using Vertex AI Model Monitoring.

**Triggers and Schedules**: Set up triggers to invoke models on Google Cloud; schedule with Cloud Scheduler, managed notebooks, Workflows, Vertex AI Pipelines, and Cloud Composer.

---

# 17. Chapter 11Designing ML Training Pipelines

---

## 17.1. Orchestration Frameworks

**Orchestrator**: Manages steps like data cleaning, transformation, and model training in an ML pipeline; runs sequentially based on defined conditions.

**Orchestration phases**: 
* **Development phase**: Automates ML experiment execution for data scientists.
* **Production phase**: Automates pipeline execution based on schedules or triggers.

**Examples of orchestrators**: Kubeflow Pipelines, Vertex AI Pipelines, Apache Airflow, Cloud Composer.

---

### 17.1.1. Kubeflow Pipelines

**Kubeflow**: ML toolkit for Kubernetes, enabling deployment and management of complex systems.
- **Components**: Supports various ML frameworks (TensorFlow, PyTorch, MXNet) for experimentation and production use.

**Kubeflow Pipelines**: Platform for building, deploying, and managing multistep ML workflows using Docker containers.
- **Pipeline**: Describes ML workflow as a graph with components and their relationships; includes inputs and outputs of each component.

**Platform Components**: 
    * User interface (UI) for managing experiments and runs
    * Scheduling engine for multistep workflows
    * SDK for defining and manipulating pipelines/components

---

    * Notebooks for interacting with the system using the SDK
    * Orchestration, experimentation, and reuse capabilities

* * *

**Installation Options**: 
    - Google Cloud: GKE or managed Vertex AI Pipelines
    - On-premises/local systems for testing

---

![center w:85%](images/c11f003.png)

---


![center w:85%](images/c11f004.png)

---


![center w:85%](images/note.png)

---

### 17.1.2. Vertex AI Pipelines

**Vertex AI Pipelines**: Run Kubeflow or TFX pipelines serverlessly, providing automatic infrastructure management and data lineage.

* **Data Lineage**: Tracks data transformations from source to model consumption, capturing metadata and ML artifacts like models or datasets.
    * **Artifact Lineage**: Describes factors resulting in an artifact (e.g., training data, hyperparameters).

**Components and Steps**: Define pipeline workflow code as self-contained components with inputs, outputs, and container images.

* * *

**Vertex AI Pipelines Capabilities**:
- Automate, monitor, and experiment with ML workflows.
- Portable, scalable, based on containers.

---

- Use custom or pre-built components, including Google Cloud Pipeline Components.

---

![center w:85%](images/c11f005.png)

---


![center w:85%](images/c11f006.png)

---


![center w:85%](images/c11f007.png)

---


![center w:85%](images/c11f008.png)

---


![center w:85%](images/note.png)

---

### 17.1.3. Apache Airflow

**Apache Airflow**: An open-source platform for managing data engineering workflows using DAGs.

* **Workflows in Airflow**: Represented as directed acyclic graphs (DAGs) containing dependent tasks.
* **Key Components**: Includes a UI, scheduler, and executor.

---

### 17.1.4. Cloud Composer

**Cloud Composer**: Fully managed workflow orchestration service based on Apache Airflow with no setup or maintenance.

**Benefits**: 
* Quick creation of Airflow environments.
* Access to Airflow-native tools like the web interface and command-line utilities.
* Ideal for data-driven workflows, especially ETL/ELT processes.

**Use Cases**: Orchestrating batch workloads in data pipelines, triggering jobs in BigQuery or starting Dataflow pipelines.

---

### 17.1.5. Comparison of Tools

**Orchestrator Management and Support**: Kubeflow Pipelines supports ML workflows in any framework like TensorFlow; Vertex AI Pipelines offers serverless, managed Kubernetes with no infrastructure management needed; Cloud Composer is a managed Apache Airflow for ETL/ELT pipelines.

* **Failure Handling**: Kubeflow Pipelines requires custom failure handling; Vertex AI Pipelines leverages Kubeflow's failure management; Cloud Composer handles GCP metrics to act on failures or successes.

---

*Comparison of Tools*
****|  Kubeflow Pipelines | Vertex AI Pipelines | Cloud Composer
---|---|---|---
**Management and support for frameworks** | Kubeflow Pipelines is used to orchestrate ML workflows in any supported framework such as TensorFlow, PyTorch, or MXNet using Kubernetes.
It can be set up on‐premises or in any cloud. | Managed serverless pipeline to orchestrate either Kubeflow Pipelines or TFX Pipeline. No need to manage the infrastructure. | Managed way to orchestrate ETL/ELT pipelines using Apache Airflow. It's a Python‐based implementation.

<!-- _class: centered -->

---

## 17.2. Identification of Components, Parameters, Triggers, and Compute Needs

* **Triggers for MLOps pipelines**: Automate retraining of ML models with new data or changes in model performance.
    * **Data availability**: Execute existing continuous training (CT) pipeline to train a new model; no new components are deployed.
    * **New implementation**: Deploy a new pipeline through CI/CD when implementing an updated model.

**FIGURE 11.9** Continuous training and CI/CD

---


![center w:85%](images/c11f009.png)

---

### 17.2.1. Schedule the Workflows with Kubeflow Pipelines

**Kubeflow Pipelines SDK**: Use kfp.Client for programmatic pipeline operations.
- **Trigger Methods**: 
  * Cloud Scheduler for scheduled runs
  * Pub/Sub and Cloud Functions for event-based triggers
  * Cloud Composer or Cloud Data Fusion for larger workflows
  * Built-in Argo scheduler for recurring tasks
- **Alternative Build Systems**: Jenkins (via Google Cloud Marketplace) or Apache Airflow with Cloud Composer
- **Cloud Build Customization**: Skip triggers for documentation or experimentation notebook changes

---


![center w:85%](images/c11f010.png)

---


![center w:85%](images/tip.png)

---

### 17.2.2. Schedule Vertex AI Pipelines

**Schedule pipeline execution with Cloud Scheduler**: Use Cloud Scheduler and an HTTP-triggered Cloud Function to schedule pipeline runs.
**Trigger a pipeline run with Cloud Pub/Sub**: Utilize a Cloud Pub/Sub trigger in a Cloud Function to execute pipelines in response to messages.

---

## 17.3. System Design with Kubeflow/TFX

**Kubeflow DSL**: Discuss system design using Kubeflow Domain-Specific Language.
**TFX**: Cover system design using TensorFlow Extended.

---

### 17.3.1. System Design with Kubeflow DSL

* **Kubeflow Pipelines**: Stores pipelines as YAML files executed by Argo.
    * **Argo Workflows**: Default runtime environment for Kubeflow Pipelines.
* **Python DSL**: Used to author pipelines; represents ML workflow operations and supports simple Python functions in containers.
* **Pipeline Definition**:
    * Create container: As a Python function or Docker image.
    * Define operation: Container, command-line arguments, data mounts, variables.
    * Sequence operations: Define parallelism and dependencies.
    * Compile to YAML: Convert Python-defined pipeline into a format Kubeflow can use.

---

### 17.3.2. System Design with TFX

**TFX**: Google’s production-scale ML platform based on TensorFlow, providing a configuration framework and shared libraries for building and managing ML workflows.

* **TFX Pipelines**: Orchestrate ML workflows across platforms like Apache Airflow, Apache Beam, and Kubeflow Pipelines.
    * **Components**: ExampleGen (ingests data), StatisticsGen (calculates dataset stats), SchemaGen (creates schema), ExampleValidator (detects anomalies), Transform (feature engineering), Trainer (model training), Tuner (hyperparameter tuning), Evaluator (model validation), Model Validator (checks model suitability), Pusher (deploys model).


---

**TFX Libraries**: Provide base functionality for standard components like TFDV.

* **Orchestration Systems**: Use Apache Airflow, Cloud Composer, or Vertex AI Pipelines to run TFX stages.
    * **Kubeflow Pipelines**: Run on GKE with TFX Pipeline DSL and CLI compiling Python code to a YAML file.

---

![center w:85%](images/c11f012.png)

---


![center w:85%](images/note.png)

---

## 17.4. Hybrid or Multicloud Strategies

**Multicloud**: Interconnection between at least two public cloud providers.

* **GCP AI APIs**: Can be integrated anywhere or in applications; AWS Lambda can call GCP ML APIs.
    * **BigQuery Omni**: Runs BigQuery analytics on data from S3 or Azure Blob Storage; `LOAD DATA` SQL statement transfers data into BigQuery for analysis and BigQuery ML.

**Hybrid cloud**: Combines private (on-premises) and public cloud environments.

* **Anthos features**: Supports hybrid ML development with:
    * **BigQuery Omni**: Managed by Anthos, simplifies querying data.
    * **Speech-to-Text On-Prem**: Generally available on Anthos through Google Cloud Marketplace.

---

    * **GKE on-premises**: Sets up Kubeflow Pipelines for ML workflows.
    * **Cloud Run on-premises**: Runs API-based pretrained AI services.

---
## 17.5. Summary

**Orchestration Tools**: 
- **Kubeflow**: Runs ML workflows on GCP Kubernetes Engine.
- **Vertex AI Pipelines**: Managed serverless way to run Kubeflow and TFX workflows; uses Cloud Function event triggers for scheduling.
- **Apache Airflow/Cloud Composer**: For complex, custom workflow automation.

**ML Workflow Scheduling**: 
- **Kubeflow**: Uses Cloud Build for deployment.
- **Vertex AI Pipelines**: Uses Cloud Functions or can be run manually.

**System Design with Kubeflow & TFX**: 
- **Components**: Create tasks as components in Kubeflow Pipelines; visualize with TensorBoard.

---

- **TFX**: Three core components and libraries to define ML pipelines; supports various orchestrators including Cloud Composer, Kubeflow, and Vertex AI Pipelines.

**Hybrid & Multicloud**: 
- Use BigQuery Omni for data from AWS S3 and Azure storage.
- Set up Kubeflow Pipelines on GKE with Anthos.

---
## 17.6. Exam Essentials

**Orchestration Frameworks**: Kubeflow Pipelines and Vertex AI Pipelines (on GCP), Apache Airflow, Cloud Composer  
    * **Kubeflow Pipelines/Vertex AI Pipelines**: Run ML workflows; use Cloud Build for deployment triggers, Cloud Functions for event-based scheduling.  
* **TFX/Kubeflow System Design**: Components, tasks orchestrated as components in Kubeflow; TFX pipelines on Kubeflow or Vertex AI Pipelines using any orchestrator.

---

# 18. Chapter 12Model Monitoring, Tracking, and Auditing Metadata

---

## 18.1. Model Monitoring

**Deployment**: Transition from Jupyter Notebook experimentation to production with serverless architecture.
- **Model Performance Uncertainty**: Post-deployment, evaluate model performance on real-time data; consider external factors like pandemics or subtle input changes.
    * **Drift**: Models may become less relevant over time due to environmental changes; detect concept and data drift for recovery.

---


![center w:85%](images/tip.png)

---

### 18.1.1. Concept Drift

* **Concept drift**: Relationship between input variables and predicted outcomes changes over time.
    * **Adversarial behavior**: Spammers modify email content to evade spam filters, causing concept drift in models trained on historical data.
* **Model assumptions changing**: Underlying conditions affecting model predictions alter, leading to decreased accuracy.

---

### 18.1.2. Data Drift

* **Data drift**: Change in input data distribution or schema compared to training data.
    * **Statistical distribution changes**: Model performance degrades if demographic shifts occur.
* **Input schema changes**: New data (e.g., SKUs) or altered column meanings affect model accuracy.
* **Model monitoring**: Continuously assess input data and re-evaluate models using training metrics to detect drift.

---

## 18.2. Model Monitoring on Vertex AI

* **Training-serving skew**: Input feature distribution difference between production and training data impacts model performance.
    * **Original data access required**: Enable this feature if you have the original data.
* **Prediction drift**: Statistical input distribution changes in production over time impact model performance.
    * **No original data needed**: Use for monitoring inputs without original training data.
* **Data types monitored**: Both skew and drift detection are available for categorical and numerical features.

---


![center w:85%](images/c12f001.png)

---


![center w:85%](images/c12f002.png)

---

### 18.2.1. Drift and Skew Calculation

**Baseline Distribution:**
- **Skew detection baseline:** Statistical distribution of feature values in training data.
- **Drift detection baseline:** Statistical distribution of feature values seen in production recently.

**Distribution Calculation:**
- **Categorical features:** Count or percentage of each value.
- **Numerical features:** Count or percentage within equal-sized buckets.

**Comparison Method:**
- **Categorical:** L-infinity distance between baseline and latest production distribution.
- **Numerical:** Jensen-Shannon divergence for distance score.

---

### 18.2.2. Input Schemas

**Input Values**: Part of prediction request payloads, parsed by Vertex AI for monitoring.
* **Schema**: Required for custom-trained models; provided automatically for AutoML models.

---


![center w:85%](images/tip.png)

---

## 18.3. Logging Strategy

**Model Monitoring**: Track input trends and request logging.
* **Logging Requirements**: Mandatory in regulated domains; useful for updating training data.
**Enabling Prediction Logs in Vertex AI**: Available for AutoML tabular, image models, and custom-trained models; can be set during deployment or endpoint creation.

---

### 18.3.1. Types of Prediction Logs

* Enable three independent log types for prediction nodes
* Logs include:独立启用三种不同类型的日志以从预测节点获取信息。这些类型互不影响，可以单独启用或禁用。

---

### 18.3.2. Log Settings

**Log settings**: Configurable during endpoint creation or model deployment.

**Logging considerations**: 
* Undeploy and redeploy models to change log settings after initial deployment.
* High QPS can lead to increased logging costs; consider scaling and cost management together.

**Example gcloud command**:
```gcloud ai endpoints deploy-model _1234567890_ \
--region=_us-central1_ \
--model=_model_id_12345_ \
--display-name=_image_classification_ \
--machine-type=_a2-highgpu-2g_ \
--accelerator=count=2,type=nvidia-tesla-t4 \
---disable-container-logging \
---enable-access-logging```

---

### 18.3.3. Model Monitoring and Logging

**Model Monitoring and Request-Response Logging**: Use shared backend infrastructure (BigQuery table) but have overlapping restrictions.

  * Enabling Model Monitoring after Request-Response Logging is not possible.
  * Modifying Request-Response Logging after enabling Model Monitoring is restricted.

---

## 18.4. Model and Dataset Lineage

**Metadata**: Recordings of experiment parameters and observations.

* **Tracking Model Performance**: Detect degradation post-deployment; compare hyperparameters.
    * **Lineage Management**: Trace datasets/models, identify sources and descendants.
* **Reproducibility**: Rerun workflows with identical settings.
* **Audit Trail**: Monitor artifact usage for compliance and impact analysis.

---

### 18.4.1. Vertex ML Metadata

* **Metadata store**: Top-level container for all metadata resources, regional and project-specific.
* **Metadata resources**:
    * **Artifacts**: Entities or data pieces created/consumed by ML workflows (e.g., datasets, models).
    * **Context**: Group of artifacts and executions (e.g., experiments with parameters and metrics).
    * **Execution**: Step in ML workflow annotated with runtime parameters.
* **Event**: Connects artifacts and executions, capturing relationships like origin lineage.
* **Metadataschema**: Specifies schema for data types using OpenAPI YAML.

---


![center w:85%](images/c12f003.png)

---

## 18.5. Vertex AI Experiments

**ML Model Development**: Find the best model for your use case by experimenting with different libraries, algorithms, architectures, and hyperparameters.

**Vertex AI Experiments**:  
- Track experiment steps (preprocessing, embedding, training)
- Monitor inputs (algorithms, hyperparameters, datasets)
- Record outputs (models, metrics, checkpoints)

**Google Cloud Console**: View experiments in a single pane, analyze runs, and explore results.

**Vertex AI SDK for Python**: Access experiments, runs, parameters, metrics, and artifacts; track lineage with Vertex ML Metadata.

---

## 18.6. Vertex AI Debugging

**Access Training Container**: Connect to the container where training is running.

* **Install Bash Shell**: Pre-built containers come with this installed.
* **Enable Interactive Shells**: Set `enableWebAccess` API field to true.
* **Debugging Tools**: Use interactive shell to check permissions, visualize Python execution with py-spy, analyze performance using perf, and check CPU/GPU usage.

---

## 18.7. Summary

* **Model Monitoring**: Detect performance degradation post-deployment
* **Logging Strategies**: Utilize various methods in Vertex AI for logging
    * **Vertex ML Metadata & Vertex AI Experiments**: Track model lineage and experiments when building multiple models

---

## 18.8. Exam Essentials

* **Model Monitoring**: Continuously watch for data drift and concept drift in deployed models.
* **Logging Strategies**: Implement logging to track deployment performance and generate new training data using Vertex AI.
    * **Vertex ML Metadata**: Utilize managed GCP solution for storing and accessing model lineage and artifacts, including creating and querying metadata.

---

# 19. Chapter 13Maintaining ML Solutions

---

## 19.1. MLOps Maturity

**MLOps**: Application of DevOps principles to machine learning.
* **Phases of ML journey**: Experimentation → Automation → Transformation
    * **Experimentation**: Manual model training using pipelines; reflects initial AI readiness.
    * **Automation**: Full automation of ML processes, using CI/CD; marks advanced AI maturity.
* **ML steps**:
    * **Data**
        * Extraction: Collect and aggregate data.
        * Analysis: Perform EDA, identify feature engineering needs.
        * Preparation: Transform data, split into train/test/validation sets.
    * **Model**
        * Training: Experiment with algorithms and hyperparameters.

---

        * Evaluation: Assess model quality using metrics.
        * Validation: Ensure model meets performance criteria before deployment.
    * **Deployment**
        * Serving: Deploy for online or batch predictions; manage scaling.
        * Monitor: Continuously monitor for anomalies, drift, and skew.

---
### 19.1.1. MLOps Level 0: Manual/Tactical Phase

* **Experimentation Phase**: Focus on building proof of concepts and testing AI/ML use cases.
    * **Outputs**: Model developed and handed off to release/deployment team via model registry.
* **Model Deployment**: Deployment team deploys the model to serve predictions.

---


![center w:85%](images/c13f001.png)

---

### 19.1.2. MLOps Level 1: Strategic Automation Phase

**Organizations**: Identified business objectives; prioritized ML for problem-solving  
**MLOps Level 1/Strategic Phase**: Automated continuous training & delivery of model predictions  
    * **Pipelines**: Automate data and model validation, triggers, Feature Store, metadata management  
**Development Environment**: Central repository for source code; orchestrated model training  
**Artifacts Sharing**: Infrastructure to share between teams; clear distinction between dev & production environments

---


![center w:85%](images/c13f002.png)

---

### 19.1.3. MLOps Level 2: CI/CD Automation, Transformational Phase

**Transformational Phase**: Uses AI for innovation and agility; ML experts in product teams across business units.

* **Data Access**: Datasets accessible across silos; projects shared between groups.

* **CI/CD Automation**: Entire pipeline automated, including model updates (e.g., TensorFlow version changes).

---


![center w:85%](images/c13f003.png)

---

## 19.2. Retraining and Versioning Models

**Model Monitoring**: Tracks drift and training-serving skew; collects data for performance evaluation and new training datasets.
    * **Retraining Frequency**: Determined based on collected data to ensure model performance remains high.
* **Data Collection**: Essential for creating fresh training and test datasets when enabling monitoring.

---


![center w:85%](images/tip.png)

---

### 19.2.1. Triggers for Retraining

**Retraining Pipeline:** Triggered based on policies like absolute threshold or rate of degradation.
    * **Absolute Threshold**: Retrain when accuracy falls below a set percentage (e.g., 90%).
    * **Rate of Degradation**: Retrain if performance drops by more than 2% in a day.
**Considerations:**
    * **Training Costs:** Avoid frequent retraining to minimize expenses.
    * **Training Time:** Account for varying training times (minutes to weeks) and potential degradation during this period.
    * **Delayed Training:** Ensure thresholds prevent significant performance loss before new models are deployed.

---

    * **Scheduled Retraining:** A simpler option is regular retraining on a fixed schedule.

---

![center w:85%](images/tip.png)

---

### 19.2.2. Versioning Models

**Model Versioning**: Allows deploying multiple versions of a model with distinct version IDs.

**Version Selection**: Users can choose between versions when accessing models via API, ensuring backward compatibility and maintaining expected performance.

**API Access**: Models are accessible using REST endpoints, providing convenience for users to monitor different versions.

---

## 19.3. Feature Store

**Feature Engineering**: A critical but time-consuming process in building effective ML models.

* **Non-reusable**: Features created for specific projects are often not designed to be shared, leading to redundant effort.
    * **Training vs. Serving Differences**: Ad hoc feature creation results in inconsistencies between training and serving data, impacting model performance.
* **Governance and Collaboration Issues**: Lack of shared features complicates data governance and fosters siloed team structures.
* **Productization Challenges**: Ad hoc features are difficult to automate and integrate into production systems requiring low-latency access.

---

### 19.3.1. Solution

**Central Location for Features**: Stores features and metadata, facilitating sharing between data engineers and ML engineers.

**Key Features of Feature Stores**: 
* Process large feature sets quickly.
* Access features with low latency for real-time prediction and batch access for training and predictions.

**Feast**: An open-source Feature Store by Google and Gojek, available as a software download. 

**Google Cloud Managed Service - Vertex AI Feature Store**: Provides dynamic scaling based on needs.

---

### 19.3.2. Data Model

**Vertex AI Feature Store**: Uses a time-series model for data storage, enabling temporal management.
- **Hierarchy**: Featurestore → EntityType → Feature
* **Featurestore**: Top-level container holding one or more entity types.
* **EntityType**: Represents a type of feature with associated features like player_id, team, batting_avg, and age.

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

* **Vertex AI Feature Store**: Supports batch and streaming ingestion; features can be stored in BigQuery.
    * **Ingestion Methods**: Batch (for model training) and online (for real-time inference).
* **Feature Retrieval**:
    * **Batch Method**: Used during model training, retrieves values up to time t.
    * **Online Method**: Used for real-time inference, returns values at or before time t.

---

## 19.4. Vertex AI Permissions Model

**Identity and Access Management (IAM)**: Enforces access control to resources and operations like training, deploying, and monitoring.

**Least privilege**: Restrict users and applications to only necessary actions.

* **Manage service accounts and keys**: Periodically check security assets.
* **Auditing**: Enable audit logs using cloud logging roles.

**Vertex AI specific best practices**: Follow general IAM guidelines tailored for ML pipelines.

---


![center w:85%](images/tip.png)

---

### 19.4.1. Custom Service Account

* **Service Accounts**: Automatically created by Google for accessing resources in a project.
* **Permission Management**: Prefer using custom service accounts with minimal necessary permissions (e.g., not granting access to BigQuery and GCS if not needed).

---

### 19.4.2. Access Transparency in Vertex AI

**Logs**: Capture user access and actions.
* **Cloud Audit logs**: Record actions by users from your organization.
* **Access Transparency logs**: Document actions by Google personnel.

For a full list of supported services, see: [https://cloud.google.com/vertex-ai/docs/general/access-transparency](https://cloud.google.com/vertex-ai/docs/general/access-transparency)

---

## 19.5. Common Training and Serving Errors

**Common Errors**: Frequently encountered issues during training and serving.

**Debugging**: Understanding these errors helps in effective problem resolution.

* **TensorFlow Specific**: Examples and focus will be given using TensorFlow.

---

### 19.5.1. Training Time Errors

**Training Errors**: Occur during `Model.fit()` execution.

* **Input Data Issues**: Not transformed or encoded.
* **Tensor Shape Mismatch**: Incorrect dimensions.
* **Memory Overload**: Due to large instance sizes on CPU/GPU.

---

### 19.5.2. Serving Time Errors

**Serving Time Errors**: Seen only during deployment; different from training errors.

* **Input Data Issues**: Not transformed or encoded.
* **Signature Mismatch**: Occurs during deployment.

---

### 19.5.3. TensorFlow Data Validation

**TensorFlow Data Validation (TFDV)**: Analyzes training and serving data to compute statistics, infer schema, and detect anomalies.

* **Full Documentation**: Available at <https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell>

---

### 19.5.4. Vertex AI Debugging Shell

**Interactive Shell**: Allows debugging of training in both pre-built and custom containers.

* **Tracing and Profiling Tools**: Run to diagnose issues.
* **GPU Utilization Analysis**: Monitor GPU use during training.
* **IAM Permission Validation**: Ensure correct permissions for the container.

---

## 19.6. Summary

**ML Operations (MLOps)**: Based on CI/CD principles for maintaining ML applications through automation.
* **Automation**: Involves training, deployment, and monitoring processes.
* **Retraining Policy**: Balances model quality with training cost.
    * **Feature Store**: Enables sharing of features across departments using open-source software or Vertex AI Feature Store.

---

## 19.7. Exam Essentials

**MLOps Maturity**: Different levels from experimental to fully mature CI/CD‐inspired architecture.

**Model Versioning & Retraining Triggers**: Trigger retraining based on model degradation or time; manage new versions in the model repository.

**Feature Store Usage**: Share engineered features using managed (Vertex AI Feature Store) or open-source (Feast) solutions.

---

# 20. Chapter 14BigQuery ML

---

## 20.1. BigQuery – Data Access

* **Web Console**: Write SQL queries directly and view results.
* **Jupyter Notebook (Magic Command)**: Use `%%bigquery` to run BigQuery queries in Vertex AI Workbench.
    * **Python API**: Import BigQuery library, create client, execute query using Python, capture results in Pandas DataFrame.

---


![center w:85%](images/c14f001.png)

---


![center w:85%](images/c14f002.png)

---

## 20.2. BigQuery ML Algorithms

**BigQuery ML**: Allows creating machine learning models using standard SQL queries without writing Python code.

**BigQuery ML**: Completely serverless for training and prediction.

---


![center w:85%](images/tip.png)

---

### 20.2.1. Model Training

**CREATE MODEL**: Statement used to create machine learning models in BigQuery.

* **Options**: 
    * `model_type`: Specifies the type of model (e.g., logistic regression, linear regression).
    * `input_label_cols`: Identifies the target column for training.
    
**Training Data**: SELECT statement specifying the table and columns to use for training.

**Model Types in BigQuery ML**:
* Regression: LINEAR_REG, BOOSTED_TREE_REGRESSOR, DNN_REGRESSOR, AUTOML_REGRESSION
* Classification: LOGISTIC_REG, BOOSTED_TREE_CLASSIFIER, DNN_CLASSIFIER, DNN_LINEAR_COMBINED_CLASSIFIER, AUTOML_CLASSIFIER
* Clustering: KMEANS

---

* Deep and Wide Models: DNN_LINEAR_COMBINED_REGRESSOR, DNN_LINEAR_COMBINED_CLASSIFIER
* Time-series Forecasting: ARIMA_PLUS
* Dimensionality Reduction: PCA, AUTOENCODER
* General: TENSORFLOW

**DNN Model Options**: Fully configurable using TensorFlow estimators.

---

![center w:85%](images/c14f003.png)

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

**Model Evaluation**: Use separate dataset via `ML.EVALUATE` function  
**Query Example**: 
```sql
SELECT * FROM ML.EVALUATE(MODEL `projectid.test.creditcard_model1`, ( SELECT * FROM `test.creditcardtable`))
```
**Evaluation Results**: Shown in **FIGURE 14.4**

---


![center w:85%](images/note.png)

---


![center w:85%](images/c14f004.png)

---

### 20.2.3. Prediction

* **ML.PREDICT function**: Used to make predictions with a BigQuery ML model, adding predicted labels and probabilities as new columns.
    * **Output**: Includes original input columns plus `_predicted_<label_column_name>` and `_predicted_<label_column_name>_probs`.
* **Example SQL (full output)**: 
    ```sql
    SELECT * FROM ML.PREDICT(MODEL `dataset1.creditcard_model1`, 
                             (SELECT * FROM `dataset1.creditcardpredict` LIMIT 1))
    ```
* **Example SQL (selected predictions only)**:
    ```sql
    SELECT predicted_defaultpaymentnextmonth, 
           predicted_defaultpaymentnextmonth_probs 
    FROM ML.PREDICT(MODEL `dataset1.creditcard_model1`, 

---

                    (SELECT * FROM `dataset1.creditcardtable` LIMIT 1))
    ```
* **Query results**: Shows predictions and their probabilities for each label.

---

![center w:85%](images/c14f005.png)

---

## 20.3. Explainability in BigQuery ML

**Explainability in BigQuery**: Enhances model transparency and is required in certain domains.

- **Global Feature Importance**: Set `enable_global_explain=TRUE` during training; returned as a table showing input features and their importance values.
- **Predictive Explanations**: Use `ML.EXPLAIN_PREDICT` to get feature attributions for individual predictions, shown in the form of top-k features impacting the model.

* **Model Explainability Methods**:
    * Linear and logistic regression: Shapley values, standard errors, p-values
    * Boosted Trees: Tree SHAP, Gini-based importance
    * Deep Neural Network: Integrated gradients
    * Arima_PLUS: Time-series decomposition

---


![center w:85%](images/c14f006.png)

---


![center w:85%](images/c14f007.png)

---


![center w:85%](images/c14f008.png)

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

**BigQuery ML**: Designed for SQL experts handling complex tables and queries; used by analysts and business users.

**Vertex AI**: Targets data scientists and machine learning engineers proficient in Python/Java, using Jupyter Notebooks and Pandas DataFrames; offers fine-grained control over data flow and training process.

* * *

For **analysts or business users**, use BigQuery ML. For **machine learning engineers**, consider Vertex AI.

---


![center w:85%](images/tip.png)

---

## 20.5. Interoperability with Vertex AI

* **Interoperability**: Designed for seamless use of Vertex AI and BigQuery ML throughout the machine learning pipeline
    * **Integration Points**: At least six distinct areas where the two products work together easily

---

### 20.5.1. Access BigQuery Public Dataset

* **BigQuery Public Datasets**: Over 200 datasets available through Google Cloud Public Datasets Program.
    * **Access**: Free storage provided by Google, pay only for queries run.
* **Usage with Vertex AI**: Enhance ML models by combining private data with public datasets.
    * **Example**: Improve traffic prediction model using combined weather data.

---

### 20.5.2. Import BigQuery Data into Vertex AI

**Vertex AI Dataset Creation**: Provide a BigQuery URL directly to create a Vertex AI dataset.
* **Python Code Example**: 
    * ```python
       from google.cloud import aiplatform
       dataset = aiplatform.TabularDataset.create(
           display_name="my-tabular-dataset",
           bq_source="bq://project.dataset.table_name",
       )
       ```
**Integration with BigQuery**: Directly connect to and utilize data in BigQuery without exporting it.

---

### 20.5.3. Access BigQuery Data from Vertex AI Workbench Notebooks

* **Jupyter Notebook in Vertex AI Workbench**: Allows direct browsing of BigQuery datasets, SQL query execution, and DataFrame download.
* **Usefulness for Data Scientists**: Facilitates exploratory analysis, visualization creation, machine learning model experimentation, and feature engineering with various datasets.

---

### 20.5.4. Analyze Test Prediction Data in BigQuery

* Reverse integration with BigQuery: Export model test predictions directly to BigQuery.
* Facilitates further analysis: Use SQL methods for detailed examination of test dataset predictions.
* Simplifies workflow: Streamline the process of moving model output into data analytics pipelines.

---

### 20.5.5. Export Vertex AI Batch Prediction Results

* Batch predictions in Vertex AI can use BigQuery tables as input.
* Predictions can be stored back into BigQuery as new tables.
* Useful for MLOps workflows where data is managed in BigQuery.

---

### 20.5.6. Export BigQuery Models into Vertex AI

**Model Export**: Export BigQuery ML models to GCS for import into Vertex AI.

**Direct Registration**: Use Vertex AI Model Registry to register BigQuery ML models directly, bypassing GCS export.

**Support and Limitations**: Supports both BigQuery built-in models and TensorFlow models; ARIMA_PLUS, XGBoost, and transform-based models cannot be exported.

---

## 20.6. BigQuery Design Patterns

* **Design patterns**: Repeated problem-solution pairs in data science and machine learning.
* **BigQuery ML**: Innovative approach to machine learning with novel solutions for common problems.
* **Elegant solutions**: New, efficient methods addressing traditional challenges in BigQuery ML.

---

### 20.6.1. Hashed Feature

**Incomplete vocabulary**: Data might lack some categorical values, leading to issues in ML models.

**High cardinality**: Variables like zip code have many categories (high cardinality), causing scaling problems.

**Cold start problem**: New values can appear that weren't in the training data, requiring handling of unknowns.

* **Hashing solution**: Convert high-cardinality variables using FarmHash in BigQuery:
  * `ABS(MOD(FARM_FINGERPRINT(zipcode), numbuckets))`

---

### 20.6.2. Transforms

**TRANSFORM clause**: Applies transformations to input features before feeding them into a model.

* **Example usage**: 
    * `ML.FEATURE_CROSS(STRUCT(f1, f2)) as cross_f`
    * `ML.QUANTILE_BUCKETIZE(f3) OVER() as buckets`

**Available transforms in BigQuery ML**: POLYNOMIAL_EXPAND, FEATURE_CROSS, NGRAMS, QUANTILE_BUCKET, HASH_BUCKETIZE, MIN_MAX_SCALER, STANDARD_SCALER

**Caveat**: Models with transformations using the `TRANSFORM` clause may not work outside BigQuery ML.

---

## 20.7. Summary

**BigQuery**: Cloud service that democratized machine learning for SQL users.

**BigQuery ML**: A part of BigQuery that enables performing all stages of a machine learning pipeline using SQL, reducing model creation time through direct input value transformations.

**Interoperability with Vertex AI**: BigQuery ML can be seamlessly integrated with Google’s Vertex AI, offering extended functionality.

---

## 20.8. Exam Essentials

* **BigQuery and ML**: Data warehouse with integrated machine learning using SQL.
    * **BigQuery ML vs Vertex AI**: BigQuery ML for analysts, Vertex AI for engineers; seamless integration between services.

* **BigQuery design patterns**: Elegantly solves common ML problems like hashing, transforms, and serverless predictions.

---

# 23. Online Test Bank

---

## 23.1. Register and Access the Online Test Bank

**Registering for Online Test Bank Access:**

* Go to `www.wiley.com/go/sybextestprep` and click "here to register," then select your book.
* Complete registration by providing security verification; an email with a pin code will be sent.
* Use the pin code to activate access on the test bank site.
    * Log in with username and password or create a new account.
* Ensure you see your test bank listed; refresh the page if necessary.

---


![center w:85%](images/logo.png)

---

# 24. WILEY END USER LICENSE AGREEMENT

---

