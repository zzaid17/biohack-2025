# Authors

**Zaid Hoda, Noah Elsayed, Tolani Olatunji, Mutaz Abu-Khader**

# Summary

This repository contains the winning submission for BioHacks 2025, a two-day hackathon at the University of Calgary.

Our group developed a data-driven tool that aims to simplify medical diagnoses by implementing a suite of machine learning models that can accurately analyze and interpret patient data for disease detection. The project is complete with a fully functional user-friendly interface that allows the user to input their symptoms and provide any other relevant information, returning a diagnosis based on our models' predictions.

We used one dataset for each major condition - cancer, diabetes, heart disease, liver disease, and stroke. Our initial data analysis consisted of data cleaning, min-max normalization, and calculating the correlation values for each dataset. We then used scikit-learn to evaluate Random Forest, LDA, Logistic Regression, QDA, Native Bayes, Decision Tree, and KNN models using 10-fold cross validation. Upon determining the ideal model for each dataset, final models were trained and dumped to `.pkl` files for later use in the GUI when predicting on new data.

# Prerequisites

This project was created using Python, and as such the user must have it installed. Once Python is installed, run the following command to ensure all prerequisites are met:
```
pip install tensorflow pandas scikit-learn numpy matplotlib flask
```

# File Structure

```
BIOHACK-2025/
├── data/                        # all data files
│   ├── cleaned-files/           # processed and cleaned data files
│   ├── input-files/             # input data ready for use
│   └── original-files/          # raw files
├── gui/                         # old tkinter UI components [abandoned]
├── models/                      # trained models 
├── static/                      # static files 
├── templates/                   # HTML templates
├── app.py                       # app entry
├── data-cleaning.ipynb          # data processing notebook
├── neural-nets.ipynb            # neural network evaluation
├── scikit-learn-modelling.ipynb # tradition machine learning evaluation
└── README.md                    # this file
```

# How To Run
1. Ensure all prerequisites are met.
2. Download and clone this repository.
3. Navigate to the local clone of the repository.
4. Run any of the below files depending on what you would like to view:
    - `data-cleaning.ipynb`: A jupyter notebook where the raw datasets were cleaned and re-saved.
    - `neural-nets.ipynb`: A brief analysis into the effectiveness of neural networks on the datasets.
    - `scikit-learn-modelling.ipynb`: An in-depth analysis of the data, evaluation of models, and eventual saving of models.
    - `python app.py`: This launches the final GUI web app.

# Results

It should be noted that most of the predictors yielded high correlation values except in the case of the heart disease dataset. Correlation does not always align with model prediction accuracy. For example, the correlation values represent the linear relationship between the predictor and classification, and this may not be accurate in the case of non-linear relationships.

For the diabetes and stroke datasets, logistic regression resulted in the highest prediction accuracy. For cancer and liver disease, random forest proved most effective. For heart disease, logistic regression, LDA, QDA, and Native Bayes, tied for first place. It should be noted that despite the extremely low correlation factors, these four models were able to classify heart disease with 79.68% accuracy.

**Final App**

![Gif](https://raw.githubusercontent.com/zzaid17/biohack-2025/main/images/GUI-working.gif)

**Final Prediction Accuracies:**

| **Dataset**       | **Best Model**           | **Accuracy** |
|-------------------|--------------------------|-------------:|
| Cancer            | Random Forest            | 86.33%       |
| Diabetes          | Logistic Regression      | 91.47%       |
| Heart Disease     | Tie                      | 79.68%       |
| Liver Disease     | Random Forest            | 76.00%       |
| Stroke            | Logistic Regression      | 94.75%       |

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

# Appendix
## Correlation Values

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

**Liver Disease:**

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

## Models

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

