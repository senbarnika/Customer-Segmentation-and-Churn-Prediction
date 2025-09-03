🌟 **Customer Churn & Segmentation Analysis: A Predictive Framework**

This project leverages a hybrid machine learning approach to address two critical business challenges: customer segmentation and churn prediction. By first segmenting the customer base using unsupervised learning, we gain valuable insights into different customer behaviors. Subsequently, a supervised learning model is trained to predict which customers are most likely to churn, enabling proactive retention strategies.</br>

</br>![shared 1](https://github.com/user-attachments/assets/13818685-3d22-4d92-8607-086d1c9e049d)</br>

🎯 **Project Objectives**

The primary goal of this project is to build an analytical framework that not only identifies at-risk customers but also explains the underlying factors driving churn. The two main objectives are:</br>

Unsupervised Learning: To segment the customer base into distinct groups (clusters) based on their purchasing behavior and demographic data using the K-Means algorithm.</br>
Supervised Learning: To develop a robust XGBoost model for predicting customer churn, providing a quantifiable risk assessment for each customer.</br>

**Customer Segmentation and Churn Rate**

| Cluster | Customer Count (n) | Actual Churn Rate | Insights |
| :--- | :--- | :--- | :--- |
| **0** | 1028 | 14.20% | A significant segment with a moderate churn risk. |
| **1** | 219 | **18.26%** | **Highest churn rate.** This is a high-priority segment for retention efforts. |
| **2** | 523 | 15.11% | A large segment with a churn rate slightly above the average. |
| **3** | 464 | 14.87% | A substantial segment with a churn rate close to the overall average. |

🛠️ **Data Engineering and Preprocessing**

A meticulous data preprocessing pipeline was engineered to prepare the raw data for modeling. This ensured the integrity and quality of the features used in both the clustering and prediction phases.</br>

(i) Feature Engineering: New features like Days_Since_Enrollment and Age were created from existing date and birth year columns. A Children's feature was also synthesized from the sum of Kidhome and Teenhome. </br>
(ii) Missing Value Imputation: Missing Income values were imputed with the median of the column to maintain data integrity.</br>
(iii) Feature Scaling and Encoding: Numerical features were standardized using StandardScaler to normalize their range, while categorical features were converted into a numerical format using OneHotEncoder, which is essential for most machine learning algorithms.</br>

📊 **Unsupervised Learning: Customer Segmentation**

The first phase of the project involved segmenting the customer base to uncover distinct behavioral patterns.

(i) Elbow Method for Optimal K: The Elbow Method was used to determine the optimal number of clusters for the K-Means algorithm.  The plot clearly shows the "elbow" point, indicating that 4 is the optimal number of clusters. This ensures that the segments are meaningful and not overly fragmented.</br>

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/62a7056b-d0d2-4fa3-8dc7-b527661329f8" /></br>

(ii) K-Means Clustering: The K-Means algorithm was applied with the optimal K value to group customers. This resulted in four distinct segments, each with unique characteristics related to their purchasing habits and engagement. </br>

🤖 **Supervised Learning: Churn Prediction with XGBoost**

The second phase focused on building a predictive model to identify at-risk customers. XGBoost was chosen for its high performance and ability to handle complex datasets. </br>

(i) Model Training and Evaluation: The data was split into training and testing sets, and the XGBoost classifier was trained. The model's performance was then evaluated using a comprehensive suite of metrics.</br>
(ii) Feature Importance: The model's feature importance was analyzed to identify the key drivers of churn.  The results revealed that AcceptedCmp5, AcceptedCmp1, and AcceptedCmp3 were the most significant predictors, indicating that customer participation in past marketing campaigns is a strong indicator of future churn.</br>

(iii) Model Performance Metrics:</br>

Confusion Matrix: A confusion matrix was generated to visualize the model's predictions.  It shows that the model successfully identified 40 true churn cases (True Positives) while only misclassifying 44 actual churners as non-churners (False Negatives). This indicates a strong ability to capture at-risk customers.

ROC Curve: The ROC curve provides a visual representation of the model's diagnostic ability.  With an Area Under the Curve (AUC) of 0.89, the model demonstrates excellent performance, significantly better than a random classifier.

**Model Performance and Key Metrics**

| Metric | Value | Significance in Churn Prediction |
| :--- | :--- | :--- |
| **Accuracy** | 94.70% | High overall correctness, but can be misleading in imbalanced datasets. |
| **Precision** | 69% | Of all customers predicted to churn, 69% actually did. This measures the cost of false alarms. |
| **Recall** | 48% | The model correctly identified 48% of all customers who actually churned. This measures how many at-risk customers we captured. |
| **F1-Score** | 57% | A balanced score of precision and recall, providing a reliable measure of the model's overall effectiveness. |
| **ROC AUC** | 0.89 | The model has a strong ability to distinguish between churning and non-churning customers, performing significantly better than a random guess. |

📈 **Combined Analysis & Business Insights**

A powerful aspect of this project is the integration of both unsupervised and supervised learning. By combining the predicted churn data with the customer segments, we can derive actionable business insights.</br>

_Churn Rate by Customer Segment_: A bar chart was created to visualize the actual churn rate for each of the four customer segments.  This analysis reveals that Customer Segment 1 has the highest churn rate at 18.26%, highlighting it as a high-priority segment for targeted retention efforts.</br>

🎨 **Power BI Dashboard for Business Intelligence**

A comprehensive and interactive dashboard was developed using Power BI to provide a user-friendly interface for stakeholders to explore the data and derive business intelligence.</br>

(i) Customer Demographics & Sales: The dashboard provides a high-level overview of the customer base, including the Distribution of Quantity by Gender and the Sum of Quantity by Category and Gender. This allows business users to quickly identify top-selling product categories and key customer demographics.</br>

(ii) Sales & Trends Analysis: Visualizations of sales by Shopping Mall and Invoice Count by Year offer insights into geographical performance and temporal trends. This helps identify underperforming locations and seasonal patterns.</br>

(iii) Comparative Analysis: The dashboard allows for a quick comparison of the average age of customers across different product categories and genders, enabling tailored marketing campaigns.</br>


<img width="1972" height="1104" alt="image" src="https://github.com/user-attachments/assets/bba7ca91-4a99-4a9b-875c-726e352dfab8" /> </br>

This Power BI dashboard complements the machine learning models by translating complex data into actionable business insights, making the project's findings accessible and impactful for business decision-makers.</br>

✅ **Conclusion**

This project successfully demonstrates the power of a combined machine learning approach to solve complex business problems. By first employing unsupervised learning with K-Means, the customer base was intelligently segmented, revealing distinct groups with varying behaviors. This segmentation provided a critical foundation for the subsequent supervised learning phase.</br>

The XGBoost model proved to be highly effective at predicting customer churn, as evidenced by its strong performance metrics, including a high AUC of 0.89. The feature importance analysis provided actionable insights, showing that past campaign responses are the most significant indicators of churn, which is vital for developing targeted retention campaigns.</br>

Finally, the integration of a comprehensive Power BI dashboard transforms these analytical insights into a user-friendly and interactive tool. It allows business stakeholders to effortlessly visualize key performance indicators, understand customer behavior, and make informed decisions to reduce churn and enhance overall business strategy. This project is a complete solution, from raw data to actionable business intelligence.</br>

⚙️ **How the Project Works**

This project functions as a two-part analytical system that combines unsupervised and supervised machine learning to deliver actionable business insights.</br>

(i) Customer Segmentation (Unsupervised Learning): The process begins with unsupervised learning, specifically using the K-Means algorithm. The model analyzes various customer data points (like purchasing behavior, demographics, and spending habits) without any pre-defined labels. Its goal is to identify hidden patterns and group similar customers into distinct clusters. The Elbow Method is used to determine the optimal number of clusters, ensuring the segments are meaningful. This segmentation provides a foundational understanding of the customer base.</br>

(ii) Churn Prediction (Supervised Learning): In the second phase, the project uses supervised learning to predict customer churn. The XGBoost classifier is trained on a labeled dataset where the "churn" status of each customer is known. The model learns the relationships between customer features and their likelihood of churning. It then uses this knowledge to predict whether new or existing customers are at risk.</br>

(iii) Combined Analysis: The real power of the project lies in combining the outputs of these two models. By overlaying the churn prediction results onto the customer segments, you can identify which specific customer groups are most vulnerable to churn. For example, if Segment 1 has the highest churn rate, the business knows exactly where to focus its retention efforts.</br>

🚀 **Future Aspects and Scope for Improvement**

This project provides a strong foundation, but its capabilities can be significantly expanded to provide even greater value.</br>

(a) Real-Time Prediction: The current model could be integrated into a real-time system where it scores a customer's churn probability as soon as their behavior changes (e.g., a sudden drop in engagement or a long period of inactivity). This allows for immediate, proactive interventions.</br>

(b) Integration with Marketing Tools: The model’s output could be directly linked to marketing automation platforms. When a customer is flagged as high-risk, a personalized and targeted retention campaign (e.g., an exclusive discount or a special offer) can be automatically initiated.</br>

(c) Advanced Algorithms: The project could explore more sophisticated algorithms for both clustering and classification. For example, using hierarchical clustering or DBSCAN could reveal more complex customer groups, while trying deep learning models (like Recurrent Neural Networks) could capture sequential purchasing patterns over time, potentially leading to higher prediction accuracy.</br>

(d) Root Cause Analysis: Beyond just predicting churn, the project can be enhanced to perform a deeper root cause analysis. Instead of just identifying "who" is likely to churn, it could use techniques like SHAP or LIME to explain "why" they are churning by highlighting the specific features driving their individual churn probability.</br>

(e) Enhanced Dashboarding: The Power BI dashboard can be made more dynamic. It could include predictive analytics, allowing users to see simulated churn rates based on different business decisions (e.g., "What if we offer a 15% discount to Segment 1?"). This would turn the dashboard from a reporting tool into a powerful strategic decision-making platform.</br>






