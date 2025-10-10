# ========================== bot_module.py ==========================
import spacy
import random
import warnings


# Remove warnings
def warn(*args, **kwargs):
    pass


warnings.warn = warn

# Load spacy NLP
nlp = spacy.load("en_core_web_sm")

# Features (Symptoms)
feature_names = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
    'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
    'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
    'spotting_urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
    'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
    'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
    'cold'
]


# ========================== NLP Output ==========================
def nltk_output(msg):
    # Tokenize and lemmatize user message
    sentence = [token.lemma_.lower() for token in nlp(msg)]

    # Check which symptoms are mentioned
    matched_symptoms = [sym for sym in feature_names if sym in sentence]

    if matched_symptoms:
        tag = random.choice(matched_symptoms)
        return f"Based on your symptoms, you might be experiencing: {tag.replace('_', ' ')}"

    return "Sorry, I could not understand your symptoms. Could you describe them differently?"


# ========================== GUI Helper Functions ==========================
def get_pridected_value(user_input, outputs):
    """
    Predict disease based on all reported symptoms (outputs list) + latest input
    """
    # Add latest symptom if not already in outputs
    sentence = [token.lemma_.lower() for token in nlp(user_input)]
    for sym in feature_names:
        if sym in sentence and sym not in outputs:
            outputs.append(sym)

    if outputs:
        # Combine all reported symptoms to make prediction
        # Here for demo, just return last symptom reported
        return outputs[-1].replace('_', ' ')

    return "Unknown"


def get_diesese_practions(predicted_disease):
    precautions = [
        "Take proper rest",
        "Drink plenty of water",
        "Eat healthy food",
        "Avoid stress",
        "Consult a doctor if symptoms persist"
    ]
    precautions_text = "\n".join([f"{i + 1}) {p}" for i, p in enumerate(precautions)])
    return f"Precautions for {predicted_disease}:\n{precautions_text}"


def getresponse(msg):
    return nltk_output(msg)
