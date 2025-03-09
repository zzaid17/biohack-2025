import pickle
import pandas as pd

def create_sorted_df(input_dict):
    # Sort keys alphabetically
    sorted_keys = sorted(input_dict.keys())

    # Create DataFrame with sorted columns
    df = pd.DataFrame([input_dict], columns=sorted_keys)
    
    return df


def load_models():
    """ 
    Load all five disease prediction models from .pkl files 

    Args:
    None
    
    Returns:
    models (dict): a dictionary of disease models
    """
    models = {}
    diseases = ["cancer", "diabetes", "heart", "liver", "stroke"]
    
    for disease in diseases:
        try:
            with open(f"models/{disease}_model.pkl", "rb") as file:
                models[disease] = pickle.load(file)
        except FileNotFoundError:
            print(f"Warning: Model file for {disease} not found.")
            models[disease] = None
    
    return models



def prepare_data(inputs: dict) -> dict:
    """ 
    Convert input data into a np array suitable for model prediction 
    
    Args:
    inputs (dict): a dictionary of input data

    Returns:
    disease_dfs (dict): a dictionary of ready input dataframes
    """

    try:

        # sort keys 
        sorted_keys = sorted(inputs.keys())

        # base df with sorted cols
        base_df = pd.DataFrame([inputs], columns=sorted_keys)
        base_df = create_sorted_df(inputs)

        # cols to keep for each dataset
        disease_columns = {
        'cancer': ['activity', 'age', 'alcohol', 'bmi', 'cancer_history', 'gender', 'genetic_risk', 'smoking'],
        'diabetes': ['age', 'bmi', 'gender', 'heart_disease', 'hypertension', 'smoking'],
        'heart': ['activity', 'age', 'alcohol', 'bmi', 'diabetes', 'gender', 'genetic_risk', 'hypertension', 'smoking'],
        'liver': ['activity', 'age', 'alcohol', 'bmi', 'diabetes', 'gender', 'hypertension', 'genetic_risk', 'smoking'],
        'stroke': ['age', 'bmi', 'gender', 'heart_disease', 'hypertension', 'smoking']
        }

        # new df for each disease
        disease_dfs = {disease: base_df[cols].copy() for disease, cols in disease_columns.items()}
        
        return disease_dfs
    except Exception as e:
        print(f"Error in preparing data: {e}")
        return None

def predict_diseases(inputs: dict, models: dict) -> dict:
    """ 
    Use the trained models to predict the risk of each disease based on input data 
    
    Args:
    inputs (dict): a dictionary of input data
    models (dict): a dictionary of disease models

    Returns:
    results (dict): a dictionary of disease risk predictions
    """
    results = {}
    input_data = prepare_data(inputs)
    
    if input_data is None:
        return {disease: "Error in input data" for disease in models.keys()}
    
    for disease, model in models.items():
        if model is not None:
            prediction = model.predict(input_data)[0]
            results[disease] = "High Risk" if prediction == 1 else "Low Risk"
        else:
            results[disease] = "Model not available"
    
    return results

# load models when module is imported
models = load_models()

def get_disease_risk(user_inputs: dict) -> dict:
    """ 
    Public function to get disease risk predictions based on user input 

    Args:
    user_inputs (dict): a dictionary of user input data

    Returns:
    results (dict): a dictionary of disease risk predictions
    """

    results = predict_diseases(user_inputs, models)
    return results


if __name__ == "__main__":
    # Test the functions
    
    # unique_non_numeric_cols = ['activity', 'age', 'alcohol', 'bmi', 'cancer_history', 'diabetes', 'gender', 'genetic_risk', 'heart_disease', 'hypertension', 'smoking']
