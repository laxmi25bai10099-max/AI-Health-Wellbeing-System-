"""
AI Health & Wellbeing Awareness System
This poject predicts diseases based on symptoms and provides health and stress awareness. 
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings("ignore")
#  creating dataset with symptoms and disease 
data = {
    'fever':[1,1,0,1,1,1,0,1,0],
    'cough':[1,0,1,1,1,1,0,1,0],
    'fatigue':[1,1,0,1,1,1,1,1,0],
    'chest_pain':[0,0,1,1,1,0,1,1,0],
    'headache':[1,1,0,1,1,1,0,1,0],
    'breathing':[0,0,0,1,1,1,1,1,0],
    'disease': [
        'Flu','Flu','Cold','Heart Disease','COVID-19',
        'Pneumonia','Kidney Disease','Tuberculosis','Healthy'
    ]
}

df = pd.DataFrame(data)
X = df.drop('disease', axis=1)
y = df['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

#  Taking user input
 
print("Enter symptoms (1 = Yes, 0 = No):")
fever = int(input("Fever: "))
cough = int(input("Cough: "))
fatigue = int(input("Fatigue: "))
chest_pain = int(input("Chest Pain: "))
headache = int(input("Headache: "))
breathing = int(input("Breathing Issue: "))

# Checking emergency symptoms or conditions

nose_bleeding = int(input("Nose Bleeding (1/0): "))
mouth_bleeding = int(input("Mouth Bleeding (1/0): "))

# Cancer awareness inputs

weight_loss = int(input("Unexplained Weight Loss (1/0): "))
long_term_fatigue = int(input("Persistent Fatigue (1/0): "))
lump = int(input("Unusual Lump (1/0): "))
blood_cough = int(input("Blood in Cough (1/0): "))
long_term_pain = int(input("Long-term Pain (1/0): "))

# Student stress inputs

study_hours = int(input("Study Hours per day: "))
sleep_hours = int(input("Sleep Hours per day: "))
stress_level = int(input("Stress Level (1-10): "))

#  Emergency symptoms check

def check_emergency(nose_bleeding,mouth_bleeding):
    if nose_bleeding == 1 or mouth_bleeding == 1:
        print("\n EMERGENCY ALERT!")
        print(" Bleeding detected. Please seek medical help immediately.")
        print(" Stay calm and contact a doctor or nearby hospital.\n")

#  Predicting disease 

prediction = model.predict([[fever, cough, fatigue, chest_pain, headache, breathing]])
print("\n Predicted Disease:", prediction[0])
if prediction[0] =="Healthy":
    print(" You seem to be healthy.")
    print(" Maintain a healthy lifestyle.")
else:
    print(" Please consult a doctor for proper diagnosis.")

# Serious diseases

serious = ["Heart Disease","COVID-19","Pneumonia","Tuberculosis","Kidney Disease"]

if prediction[0] in serious:
    print(" Serious condition detected!")
    print(" Please consult a doctor immediately.")
    print(" Early action can protect your health.")
else:
    print(" Condition seems mild.")
    print(" Take care and monitor symptoms.")

#  Cancer symptoms check

cancer_symptoms = [weight_loss, long_term_fatigue, lump, blood_cough, long_term_pain]

if sum(cancer_symptoms) >= 3:
    print("\n High Risk Alert!")
    print(" Multiple serious symptoms detected.")
    print(" Please consult a doctor immediately.")
    print(" Early detection can save lives.")

print("\n Note: This system is for awareness only and not a medical diagnosis.")

#  Student stress level analysis system 

if stress_level >= 8 or sleep_hours < 5:
    print("\n High Stress Detected!")
    print(" Take rest and talk to someone you trust.")
    print(" Your health is more important than anything.")
    print(" Health is Wealth. Take care of yourself.")
elif stress_level >= 5:
    print("\n  Moderate Stress Detected")
    print(" Try relaxation techniques like deep breathing or short breaks.")
    print(" Manage your time effectively and maintain a healthy routine.")
else:
    print("\n Low Stress Detected")
    print(" Keep maintaining a healthy routine.")