import os
import pickle

models_dir = "C:\Users\olatu\Desktop\Desktop\WINTER 2025\biohack-2025\models"  # Path to the folder containing .pkl files
models = {}

for filename in os.listdir(models_dir):
    if filename.endswith(".pkl"):
        model_name = filename.replace("_model.pkl", "")  # Extract the disease name
        model_path = os.path.join(models_dir, filename)
        
        with open(model_path, "rb") as file:
            models[model_name] = pickle.load(file)  # Load model into dictionary

# Print loaded models
print(models.keys())  # Should output: dict_keys(['cancer', 'diabetes', 'heart', 'liver', 'stroke'])

'''
cancer_model = models["cancer"]
diabetes_model = models["diabetes"]
'''
