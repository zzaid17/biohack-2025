# Summary

This repository is a submission for BioHacks 2025, a two-day hackathon for at the University of Calgary. We developed a data-driven tool that consists of a classification model and user-friendly interface to predict and diagnose various health disorders.

We used one dataset for each major condition - cancer, diabetes, heart disease, liver disease, and stroke. Our initial data analysis consisted of data cleaning, normalization, and calculating the correlation values for each dataset.

# Correlation Values

**Cancer**

| **Predictor**      | **Correlation** |
|--------------------|-----------------|
| activity           | -0.150089       |
| age                | 0.196603        |
| alcohol            | 0.212772        |
| bmi                | 0.187560        |
| cancer_history     | 0.392188        |
| diagnosis          | 1.000000        |
| gender             | -0.250336       |
| genetic_risk       | 0.141599        |
| smoking            | 0.226999        |

**Diabetes**

| **Predictor**   | **Correlation** |
|-----------------|-----------------|
| age             | 0.258008        |
| bmi             | 0.214357        |
| diagnosis       | 1.000000        |
| gender          | 0.037411        |
| heart_disease   | 0.171727        |
| hypertension    | 0.197823        |
| smoking         | 0.092998        |

**Heart Disease**

| **Predictor**   | **Correlation** |
|-----------------|-----------------|
| activity        | -0.008640       |
| age             | -0.007247       |
| alcohol         | 0.007565        |
| bmi             | 0.019876        |
| diabetes        | -0.002389       |
| diagnosis       | 1.000000        |
| gender          | -0.005758       |
| genetic_risk    | -0.001833       |
| hypertension    | -0.005096       |
| smoking         | 0.006163        |

**Liver**

| **Predictor**   | **Correlation** |
|-----------------|-----------------|
| activity        | -0.116689       |
| age             | 0.156099        |
| alcohol         | 0.349610        |
| bmi             | 0.167655        |
| diabetes        | 0.107480        |
| diagnosis       | 1.000000        |
| gender          | -0.189558       |
| hypertension    | 0.170683        |
| genetic_risk    | 0.118292        |
| smoking         | 0.200071        |

**Stroke**

| **Predictor**   | **Correlation** |
|-----------------|-----------------|
| age             | 0.242495        |
| bmi             | 0.011673        |
| diagnosis       | 1.000000        |
| gender          | 0.012167        |
| heart_disease   | 0.138553        |
| hypertension    | 0.143647        |
| smoking         | 0.034922        |
