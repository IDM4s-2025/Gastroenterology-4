from experta import KnowledgeEngine, Fact, Rule, DefFacts

symptoms = ['heartburn', 'regurgitation', 'dysphagia', 'upper_abdominal_pain',
    'nausea', 'vomiting', 'diarrhea', 'constipation', 'blood_in_stool',
    'weight_loss', 'jaundice', 'abdominal_distension', 'fever', 'fatigue']

def user_symptoms(possible_symptoms):
    print("Enter your symptoms one at a time. When finished, type 'done'.")
    print("Valid symptoms:")
    for symptom in possible_symptoms:
        print("- " + symptom)
    confirmed = set()
    while True:
        user = input("Symptom: ").strip().lower()
        if user == "done":
            break
        if user in possible_symptoms:
            confirmed.add(user)
        else:
            print("Invalid symptom, choose from the list.")
    return confirmed

def new_diagnosis():
    answer = input("Start new diagnosis? (yes/no): ").strip().lower()
    return answer in ("yes", "y")

class GastroEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnosed = False 

    @DefFacts()
    def _initial_action(self):
        yield Fact(possible_symptoms=symptoms)

    def _set_diagnosed(self):
        self.diagnosed = True

    @Rule(Fact(symptom='heartburn'), Fact(symptom='regurgitation'))
    def diagnose_gerd(self):
        self._set_diagnosed()
        print("Diagnosis: Gastroesophageal Reflux Disease (GERD)")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='vomiting'))
    def diagnose_gastritis(self):
        self._set_diagnosed()
        print("Diagnosis: Gastritis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='weight_loss'), Fact(symptom='blood_in_stool'))
    def diagnose_peptic_ulcer(self):
        self._set_diagnosed()
        print("Diagnosis: Peptic Ulcer Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='abdominal_distension'), Fact(symptom='weight_loss'))
    def diagnose_crohns(self):
        self._set_diagnosed()
        print("Diagnosis: Crohn’s Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='blood_in_stool'))
    def diagnose_ulcerative_colitis(self):
        self._set_diagnosed()
        print("Diagnosis: Ulcerative Colitis")

    @Rule(Fact(symptom='constipation'), Fact(symptom='abdominal_distension'), Fact(symptom='blood_in_stool'))
    def diagnose_colon_cancer(self):
        self._set_diagnosed()
        print("Diagnosis: Colon Cancer")

    @Rule(Fact(symptom='jaundice'), Fact(symptom='fatigue'), Fact(symptom='abdominal_distension'))
    def diagnose_hepatitis(self):
        self._set_diagnosed()
        print("Diagnosis: Hepatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='fever'))
    def diagnose_pancreatitis(self):
        self._set_diagnosed()
        print("Diagnosis: Pancreatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fatigue'), Fact(symptom='nausea'))
    def diagnose_celiac(self):
        self._set_diagnosed()
        print("Diagnosis: Celiac Disease")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fever'), Fact(symptom='vomiting'))
    def diagnose_diverticulitis(self):
        self._set_diagnosed()
        print("Diagnosis: Diverticulitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='regurgitation'), Fact(symptom='dysphagia'))
    def diagnose_esophagitis(self):
        self._set_diagnosed()
        print("Diagnosis: Esophagitis")

    @Rule(Fact(symptom='fatigue'), Fact(symptom='weight_loss'), Fact(symptom='diarrhea'))
    def diagnose_ibs(self):
        self._set_diagnosed()
        print("Diagnosis: Irritable Bowel Syndrome (IBS)")

    @Rule(Fact(possible_symptoms=symptoms))
    def no_diagnosis(self):
        if not self.diagnosed:
            print("No diagnosis could be made based on the given symptoms.")

def main():
    print("Welcome to the Gastroenterology Diagnostic Expert System!")
    while True:
        engine = GastroEngine() 
        engine.reset()
        syms = user_symptoms(symptoms)
        for s in syms:
            engine.declare(Fact(symptom=s))
        engine.run()
        if not new_diagnosis():
            print("Thank you for using the system. Goodbye!")
            break
main()
