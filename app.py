from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

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
        
        base_df = pd.DataFrame([inputs])
        
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
            # Fill missing columns with 0
            for c in cols:
                if c not in base_df.columns:
                    base_df[c] = 0
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

# Serve front-end
@app.route('/', methods=['GET'])
def index():
    # Renders templates/index.html
    return render_template('index.html')

# Form submission endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    form = request.form
    
    # Parse form inputs
    age = form.get('age', type=int)
    sex = form.get('sex')  # male or female
    bmi = form.get('bmi', type=float)
    smoking = form.get('smoking')  # never, former, or current
    alcohol = form.get('alcohol-intake')  # never, sometimes, often
    hypertension = form.get('hypertension')  # yes or no
    physical_activity = form.get('physical-activity')  # low, medium, high
    
    # 0 or 1 for family or personal cancer history
    family_cancer = form.get('family_cancer', '0')
    personal_cancer = form.get('personal_cancer', '0')
    
    # Map inputs to keys for model
    # personal_cancer = 1 --> cancer_history = 1
    # family_cancer = 1 --> genetic_risk = 1
    
    user_inputs = {
        "age": age,
        # We encode male to be 1 and female to be 0. Note that this does NOT match the datasets we used
        # but we encoded it separately in our scikit-learn-modelling notebook.
        "gender": 1 if sex == "male" else 0,
        "bmi": bmi,
        "smoking": 0,   # never=0, former=1, current=1
        "alcohol": 0,   # low=0, medium=0.5, high=1
        "activity": 0,  # low=0, medium=0.5, high=1
        
        "cancer_history": 1 if personal_cancer == "1" else 0,
        "genetic_risk": 1 if family_cancer == "1" else 0,
        "heart_disease": 0,
        "diabetes": 0,
        "hypertension": 1 if hypertension == "yes" else 0,
    }
    
    # Map dropdown inputs to numerical values
    if smoking == "never":
        user_inputs["smoking"] = 0
    elif smoking == "former":
        user_inputs["smoking"] = 1
    elif smoking == "current":
        user_inputs["smoking"] = 1
    
    if alcohol == "never":
        user_inputs["alcohol"] = 0
    elif alcohol == "sometimes":
        user_inputs["alcohol"] = 0.5
    elif alcohol == "often":
        user_inputs["alcohol"] = 1
    
    if physical_activity == "low":
        user_inputs["activity"] = 0
    elif physical_activity == "medium":
        user_inputs["activity"] = 0.5
    elif physical_activity == "high":
        user_inputs["activity"] = 1
    
    # Obviously if the user says they have a condition then output that as 1 or high risk
    personal_diabetes = form.get('personal_diabetes', '0')
    if personal_diabetes == "1":
        user_inputs["diabetes"] = 1

    personal_heart = form.get('personal_heart', '0')
    if personal_heart == "1":
        user_inputs["heart_disease"] = 1
    
    # Note: Though not necessary with our current datasets, we add the option to input other
    # family or personal history even if the model doesn't actually use it. This could be implemented
    # in the future with more data.

    # Get dictionary of predictions
    results = get_disease_risk(user_inputs)

    # Return JSON output as a website popup
    return jsonify(results)

# Run app
if __name__ == "__main__":
    app.run(debug=True)