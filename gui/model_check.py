import os
import pickle

path = 'models/'

def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_all_models():
    model_files = [
        f"{path}cancer_model.pkl", 
        f"{path}diabetes_model.pkl",
        f"{path}heart_model.pkl",
        f"{path}liver_model.pkl",
        f"{path}stroke_model.pkl"
    ]
    models = {}
    for model_file in model_files:
        models[model_file] = load_model(model_file)
    return models

unique_non_numeric_cols = ['activity', 'age', 'alcohol', 'bmi', 'cancer_history', 'diabetes', 'gender', 'genetic_risk', 'heart_disease', 'hypertension', 'smoking']

def calculate_outcome(data):
    all_models = load_all_models()
    
    return model.predict([input_data])



if __name__ == "__main__":
    all_feature_names = set()
    models = load_all_models()
    print("Model input requirements:")
    for name, model in models.items():
        print(name)
        print(model.n_features_in_)  # Prints the number of features the model expects
        print(model.feature_names_in_)
        # Add feature names to the set (will automatically handle duplicates)
        all_feature_names.update(model.feature_names_in_)

    sorted_feature_names = sorted(all_feature_names)

    # Print the set of all unique feature names
    print("All unique feature names:", sorted_feature_names)

