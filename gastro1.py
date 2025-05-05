from experta import KnowledgeEngine, Fact, Rule, DefFacts

symptoms = [
    'heartburn', 'regurgitation', 'dysphagia', 'upper_abdominal_pain',
    'nausea', 'vomiting', 'diarrhea', 'constipation', 'blood_in_stool',
    'weight_loss', 'jaundice', 'abdominal_distension', 'fever', 'fatigue'
]

def user_symptoms(possible_symptoms):
    print("Enter your symptoms one at a time. When finished, type 'done'.")
    print(f"Valid symptoms: {', '.join(possible_symptoms)}")
    confirmed = set()
    while True:
        s = input("Symptom: ").strip().lower()
        if s == "done":
            break
        if s in possible_symptoms:
            confirmed.add(s)
        else:
            print("  → Invalid symptom, choose from the list.")
    return confirmed

def new_diagnosis():
    ans = input("\nStart new diagnosis? (yes/no): ").strip().lower()
    return ans in ("yes", "y")

def main():
    print("Welcome to the Gastroenterology Diagnostic Expert System!")
    engine = GastroEngine()
    while True:
        engine.reset()
        syms = user_symptoms(symptoms)
        for s in syms:
            engine.declare(Fact(symptom=s))
        engine.run()
        if not new_diagnosis():
            print("Thank you for using the system. Goodbye!")
            break

class GastroEngine(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(possible_symptoms=symptoms)

    @Rule(Fact(symptom='heartburn'), Fact(symptom='regurgitation'))
    def diagnose_gerd(self):
        print("\nDiagnosis: Gastroesophageal Reflux Disease (GERD)")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='vomiting'))
    def diagnose_gastritis(self):
        print("\nDiagnosis: Gastritis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='weight_loss'), Fact(symptom='blood_in_stool'))
    def diagnose_peptic_ulcer(self):
        print("\nDiagnosis: Peptic Ulcer Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='abdominal_distension'), Fact(symptom='weight_loss'))
    def diagnose_crohns(self):
        print("\nDiagnosis: Crohn’s Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='blood_in_stool'))
    def diagnose_ulcerative_colitis(self):
        print("\nDiagnosis: Ulcerative Colitis")

    @Rule(Fact(symptom='constipation'), Fact(symptom='abdominal_distension'), Fact(symptom='blood_in_stool'))
    def diagnose_colon_cancer(self):
        print("\nDiagnosis: Colon Cancer")

    @Rule(Fact(symptom='jaundice'), Fact(symptom='fatigue'), Fact(symptom='abdominal_distension'))
    def diagnose_hepatitis(self):
        print("\nDiagnosis: Hepatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='fever'))
    def diagnose_pancreatitis(self):
        print("\nDiagnosis: Pancreatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fatigue'), Fact(symptom='nausea'))
    def diagnose_celiac(self):
        print("\nDiagnosis: Celiac Disease")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fever'), Fact(symptom='vomiting'))
    def diagnose_diverticulitis(self):
        print("\nDiagnosis: Diverticulitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='regurgitation'), Fact(symptom='dysphagia'))
    def diagnose_esophagitis(self):
        print("\nDiagnosis: Esophagitis")

    @Rule(Fact(symptom='fatigue'), Fact(symptom='weight_loss'), Fact(symptom='diarrhea'))
    def diagnose_ibs(self):
        print("\nDiagnosis: Irritable Bowel Syndrome (IBS)")

main()
