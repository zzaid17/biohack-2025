# Authors

**Zaid Hoda, Noah Elsayed, Tolani Olatunji, Mutaz Abu-Khader**

# Summary

This repository is a submission for BioHacks 2025, a two-day hackathon at the University of Calgary.

Our group developed a data-driven tool that aims to simplify medical diagnoses by implementing a suite of machine learning models that can accurately analyze and interpret patient data for disease detection. The project is complete with a fully functional user-friendly interface that allows the user to input their symptoms and provide any other relevant information, returning a diagnosis based on our models' predictions.

We used one dataset for each major condition - cancer, diabetes, heart disease, liver disease, and stroke. Our initial data analysis consisted of data cleaning, mix-max normalization, and calculating the correlation values for each dataset. We then used scikit-learn to implement our Random Forest, LDA, Logistic Regression, QDA, Native Bayes, Decision Tree, and KNN models.

# Correlation Values

**Cancer:**

|**Predictor**   | **Correlation** |
|----------------|-----------------|
| activity       | -0.150089       |
| age            | 0.196603        |
| alcohol        | 0.212772        |
| bmi            | 0.187560        |
| cancer_history | 0.392188        |
| diagnosis      | 1.000000        |
| gender         | -0.250336       |
| genetic_risk   | 0.141599        |
| smoking        | 0.226999        |

**Diabetes:**

|**Predictor**   | **Correlation** |
|----------------|-----------------|
| age            | 0.258008        |
| bmi            | 0.214357        |
| diagnosis      | 1.000000        |
| gender         | 0.037411        |
| heart_disease  | 0.171727        |
| hypertension   | 0.197823        |
| smoking        | 0.092998        |

**Heart Disease:**

|**Predictor**   | **Correlation** |
|----------------|-----------------|
| activity       | -0.008640       |
| age            | -0.007247       |
| alcohol        | 0.007565        |
| bmi            | 0.019876        |
| diabetes       | -0.002389       |
| diagnosis      | 1.000000        |
| gender         | -0.005758       |
| genetic_risk   | -0.001833       |
| hypertension   | -0.005096       |
| smoking        | 0.006163        |

**Liver:**

|**Predictor**   | **Correlation** |
|----------------|-----------------|
| activity       | -0.116689       |
| age            | 0.156099        |
| alcohol        | 0.349610        |
| bmi            | 0.167655        |
| diabetes       | 0.107480        |
| diagnosis      | 1.000000        |
| gender         | -0.189558       |
| hypertension   | 0.170683        |
| genetic_risk   | 0.118292        |
| smoking        | 0.200071        |

**Stroke:**

|**Predictor**   | **Correlation** |
|----------------|-----------------|
| age            | 0.242495        |
| bmi            | 0.011673        |
| diagnosis      | 1.000000        |
| gender         | 0.012167        |
| heart_disease  | 0.138553        |
| hypertension   | 0.143647        |
| smoking        | 0.034922        |

It should be noted that most of the predictors yielded significant correlation factors except in the case of the heart disease dataset. **write more about why cuz idk**

# Models

**Heart Disease:**

| **Model**              | **Accuracy** |
|------------------------|-------------:|
| LDA                    | 0.7968       |
| Naive Bayes            | 0.7968       |
| QDA                    | 0.7968       |
| Logistic Regression    | 0.7968       |
| Random Forest          | 0.7824       |
| KNN                    | 0.7678       |
| Decision Tree          | 0.6651       |

**Cancer:**

| **Model**              | **Accuracy** |
|------------------------|-------------:|
| Random Forest          | 0.8633       |
| Logistic Regression    | 0.8300       |
| LDA                    | 0.8267       |
| QDA                    | 0.8067       |
| Decision Tree          | 0.7960       |
| Naive Bayes            | 0.7840       |
| KNN                    | 0.6720       |

**Diabetes:**

| **Model**              | **Accuracy** |
|------------------------|-------------:|
| Logistic Regression    | 0.9147       |
| LDA                    | 0.9093       |
| KNN                    | 0.9064       |
| Random Forest          | 0.8924       |
| Decision Tree          | 0.8786       |
| Naive Bayes            | 0.8686       |
| QDA                    | 0.8665       |

**Liver Disease:**

| **Model**              | **Accuracy** |
|------------------------|-------------:|
| Random Forest          | 0.7600       |
| LDA                    | 0.7506       |
| Logistic Regression    | 0.7494       |
| QDA                    | 0.7394       |
| Naive Bayes            | 0.7318       |
| Decision Tree          | 0.6806       |
| KNN                    | 0.5871       |

**Stroke:**

| **Model**              | **Accuracy** |
|------------------------|-------------:|
| Logistic Regression    | 0.9475       |
| KNN                    | 0.9422       |
| LDA                    | 0.9416       |
| Random Forest          | 0.9352       |
| Decision Tree          | 0.9022       |
| QDA                    | 0.8958       |
| Naive Bayes            | 0.8862       |


# Results

TODO: Insert best model and final accuracy for each dataset

# References

**[1]** Soriano, F. (2021). Stroke Prediction Dataset. Kaggle. Available: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
(Accessed: Mar. 8, 2025)

**[2]** El Kharoua, R. (2025). Cancer Prediction Dataset. Kaggle. Available:  https://www.kaggle.com/datasets/rabieelkharoua/cancer-prediction-dataset  
(Accessed: Mar. 8, 2025)

**[3]** Mustafa, T. (2025). Diabetes Prediction Dataset. Kaggle. Available:  https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset
(Accessed: Mar. 8, 2025)

**[4]** Rdeki, O. (2025). Heart Disease. Kaggle. Available: https://www.kaggle.com/datasets/oktayrdeki/heart-disease 
(Accessed: Mar. 8, 2025)

**[5]** El Kharoua, R. (2024). Predict Liver Disease: 1700 Records Dataset. Kaggle. Available: https://www.kaggle.com/datasets/rabieelkharoua/predict-liver-disease-1700-records-dataset
(Accessed: Mar. 8, 2025)
