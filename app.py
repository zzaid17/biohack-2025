# app.py
from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import os

# If your existing code is in a separate file, you can import it:
# from backend_code import get_disease_risk, load_models
# But here, I'll just inline the essential parts from your snippet.

app = Flask(__name__)

############################################################
# 1) Reuse your existing code in app.py (or import from separate file)
############################################################
def load_models():
    models = {}
    diseases = ["cancer", "diabetes", "heart", "liver", "stroke"]
    
    for disease in diseases:
        path = os.path.join("models", f"{disease}_model.pkl")
        if os.path.exists(path):
            with open(path, "rb") as file:
                models[disease] = pickle.load(file)
        else:
            print(f"Warning: Model file for {disease} not found.")
            models[disease] = None
    return models

def prepare_data(inputs: dict) -> dict:
    """
    Convert input data into DataFrames suitable for each model’s prediction.
    This is your original logic. 
    """
    try:
        # You have a function create_sorted_df, etc. in your original code
        # For brevity, I skip certain details. The important part:
        
        # We’ll build a base DataFrame from the user inputs. 
        # Then produce separate subsets for each disease model.
        
        base_df = pd.DataFrame([inputs])  # simplistic approach
        
        disease_columns = {
            'cancer': ['activity', 'age', 'alcohol', 'bmi', 'cancer_history',
                       'gender', 'genetic_risk', 'smoking'],
            'diabetes': ['age', 'bmi', 'gender', 'heart_disease', 'hypertension', 'smoking'],
            'heart': ['activity', 'age', 'alcohol', 'bmi', 'diabetes', 'gender',
                      'genetic_risk', 'hypertension', 'smoking'],
            'liver': ['activity', 'age', 'alcohol', 'bmi', 'diabetes', 'gender',
                      'hypertension', 'genetic_risk', 'smoking'],
            'stroke': ['age', 'bmi', 'gender', 'heart_disease', 'hypertension', 'smoking']
        }
        
        disease_dfs = {}
        for disease, cols in disease_columns.items():
            # Some columns might not be present if you haven't mapped them
            # so let's fill missing ones with 0 or "none" as needed
            for c in cols:
                if c not in base_df.columns:
                    base_df[c] = 0  # or some default
            disease_dfs[disease] = base_df[cols].copy()
        
        return disease_dfs
    except Exception as e:
        print(f"Error in preparing data: {e}")
        return None

def predict_diseases(inputs: dict, models: dict) -> dict:
    results = {}
    input_data = prepare_data(inputs)
    
    if input_data is None:
        return {d: "Error in input data" for d in models.keys()}
    
    for disease, model in models.items():
        if model is not None:
            prediction = model.predict(input_data[disease])[0]
            results[disease] = "High Risk" if prediction == 1 else "Low Risk"
        else:
            results[disease] = "Model not available"
    
    return results

models = load_models()

def get_disease_risk(user_inputs: dict) -> dict:
    results = predict_diseases(user_inputs, models)
    return results


############################################################
# 2) Serve your front-end
############################################################
@app.route('/', methods=['GET'])
def index():
    # Renders templates/index.html
    return render_template('index.html')


############################################################
# 3) Form submission endpoint
############################################################
@app.route('/predict', methods=['POST'])
def predict():
    """
    This route receives form data from your big HTML form. 
    We'll parse the fields, build the dictionary, and call get_disease_risk().
    Then we return JSON or a rendered result page.
    """
    # 1) Collect the form data
    form = request.form
    
    # Example: your front-end fields (some are toggles, some are numeric, etc.)
    # We'll parse them as strings, then convert to int/float where needed.
    
    age = form.get('age', type=int)
    sex = form.get('sex')  # "male" or "female"
    bmi = form.get('bmi', type=float)
    smoking = form.get('smoking')  # "never", "former", "current"
    alcohol = form.get('alcohol-intake')  # "low", "medium", "high"
    hypertension = form.get('hypertension')  # "yes" or "no"
    physical_activity = form.get('physical-activity')  # "low", "medium", "high"
    
    # The toggles for family/personal disease come as "0" or "1"
    family_cancer = form.get('family_cancer', '0')
    personal_cancer = form.get('personal_cancer', '0')
    # etc. for diabetes, heart, liver, stroke...
    
    # 2) Map them to the keys your model code expects
    # For example, your original code expects:
    #    "cancer_history", "genetic_risk", "heart_disease", "diabetes", ...
    # But you now have toggles for personal/family. You decide how to interpret.
    # Let's do a silly example where "personal_cancer" => "cancer_history" = 1 if toggled
    # "family_cancer" => "genetic_risk" = 1 if toggled. 
    # This is just an example - adapt logic as you prefer.
    
    user_inputs = {
        "age": age,
        "gender": 1 if sex == "male" else 0,    # Example numeric
        "bmi": bmi,
        
        "smoking": 0,   # We'll code it: never=0, former=1, current=2
        "alcohol": 0,   # low=0, medium=1, high=2
        "activity": 0,  # low=0, medium=1, high=2
        
        "cancer_history": 1 if personal_cancer == "1" else 0,
        "genetic_risk": 1 if family_cancer == "1" else 0,
        "heart_disease": 0,
        "diabetes": 0,
        "hypertension": 1 if hypertension == "yes" else 0,
    }
    
    # We'll do a quick map:
    if smoking == "never":
        user_inputs["smoking"] = 0
    elif smoking == "former":
        user_inputs["smoking"] = 1
    else:
        user_inputs["smoking"] = 2
    
    if alcohol == "medium":
        user_inputs["alcohol"] = 1
    elif alcohol == "high":
        user_inputs["alcohol"] = 2
    
    if physical_activity == "medium":
        user_inputs["activity"] = 1
    elif physical_activity == "high":
        user_inputs["activity"] = 2
    
    # If personal_diabetes == "1", let's set user_inputs["diabetes"] = 1, for instance
    personal_diabetes = form.get('personal_diabetes', '0')
    if personal_diabetes == "1":
        user_inputs["diabetes"] = 1
    
    # Similarly, if personal_heart == "1":
    personal_heart = form.get('personal_heart', '0')
    if personal_heart == "1":
        user_inputs["heart_disease"] = 1
    
    # Add logic for personal/family stroke, liver, etc. as needed.
    # For example, there's no direct place in your code for "liver_disease" or "stroke",
    # so you'd have to decide how you want them to be used or if they're placeholders for
    # the final predictions.

    # 3) Get predictions from your model
    results = get_disease_risk(user_inputs)  # returns dict { "cancer": "High Risk", ... }

    # 4) Return the results.
    # Option A: Return JSON for an AJAX request
    # return jsonify(results)
    #
    # Option B: Render a simple results page
    # For a quick approach, we'll just return the JSON text:
    return jsonify(results)


############################################################
# 4) Run the app
############################################################
if __name__ == "__main__":
    app.run(debug=True)