from experta import KnowledgeEngine, Fact, Rule, DefFacts

# Lista global de síntomas permitidos
POSSIBLE_SYMPTOMS = [
    'heartburn', 'regurgitation', 'dysphagia', 'upper_abdominal_pain',
    'nausea', 'vomiting', 'diarrhea', 'constipation', 'blood_in_stool',
    'weight_loss', 'jaundice', 'abdominal_distension', 'fever', 'fatigue'
]

def get_user_symptoms(possible_symptoms):
    """
    Prompt the user to enter symptoms one at a time. Validate input and return a set of confirmed symptoms.
    """
    print("Enter your symptoms one at a time. When finished, type 'done'.", flush=True)
    print(f"Valid symptoms: {', '.join(possible_symptoms)}\n", flush=True)
    confirmed = set()
    while True:
        s = input("Symptom: ").strip().lower()
        if s == "done":
            break
        if s in possible_symptoms:
            confirmed.add(s)
        else:
            print("  → Invalid symptom, choose from the list.", flush=True)
    return confirmed

def new_diagnosis():
    """
    Ask user if they wish to start a new diagnosis. Returns True if yes.
    """
    ans = input("\nStart new diagnosis? (yes/no): ").strip().lower()
    return ans in ("yes", "y")

def main():
    """
    Main loop: welcome user, run expert engine, display result(s), allow restart.
    """
    print("Welcome to the Gastroenterology Diagnostic Expert System!", flush=True)
    engine = GastroEngine()
    while True:
        engine.reset()
        syms = get_user_symptoms(POSSIBLE_SYMPTOMS)
        for s in syms:
            engine.declare(Fact(symptom=s))
        engine.run()
        if not new_diagnosis():
            print("Thank you for using the system. Goodbye!", flush=True)
            break

class GastroEngine(KnowledgeEngine):
    """
    The Experta engine: defines initial facts and 12 diagnosis rules.
    """
    @DefFacts()
    def _initial_action(self):
        # Provide possible symptoms fact (not used for logic, only reference)
        yield Fact(possible_symptoms=POSSIBLE_SYMPTOMS)

    @Rule(Fact(symptom='heartburn'), Fact(symptom='regurgitation'))
    def diagnose_gerd(self):
        """GERD: heartburn & regurgitation"""
        print("\nDiagnosis: Gastroesophageal Reflux Disease (GERD)")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='vomiting'))
    def diagnose_gastritis(self):
        """Gastritis: epigastric pain, nausea, vomiting"""
        print("\nDiagnosis: Gastritis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='weight_loss'), Fact(symptom='blood_in_stool'))
    def diagnose_peptic_ulcer(self):
        """Peptic ulcer: epigastric pain, weight loss, GI bleeding"""
        print("\nDiagnosis: Peptic Ulcer Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='abdominal_distension'), Fact(symptom='weight_loss'))
    def diagnose_crohns(self):
        """Crohn’s disease: diarrhea, distension, weight loss"""
        print("\nDiagnosis: Crohn’s Disease")

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='blood_in_stool'))
    def diagnose_ulcerative_colitis(self):
        """Ulcerative colitis: bloody diarrhea"""
        print("\nDiagnosis: Ulcerative Colitis")

    @Rule(Fact(symptom='constipation'), Fact(symptom='abdominal_distension'), Fact(symptom='blood_in_stool'))
    def diagnose_colon_cancer(self):
        """Colon cancer: change in bowel habits, bleeding"""
        print("\nDiagnosis: Colon Cancer")

    @Rule(Fact(symptom='jaundice'), Fact(symptom='fatigue'), Fact(symptom='abdominal_distension'))
    def diagnose_hepatitis(self):
        """Hepatitis: jaundice, fatigue, distension"""
        print("\nDiagnosis: Hepatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='nausea'), Fact(symptom='fever'))
    def diagnose_pancreatitis(self):
        """Pancreatitis: epigastric pain, nausea, fever"""
        print("\nDiagnosis: Pancreatitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fatigue'), Fact(symptom='nausea'))
    def diagnose_celiac(self):
        """Celiac disease: dyspepsia, fatigue, nausea"""
        print("\nDiagnosis: Celiac Disease")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='fever'), Fact(symptom='vomiting'))
    def diagnose_diverticulitis(self):
        """Diverticulitis: pain, fever, vomiting"""
        print("\nDiagnosis: Diverticulitis")

    @Rule(Fact(symptom='upper_abdominal_pain'), Fact(symptom='regurgitation'), Fact(symptom='dysphagia'))
    def diagnose_esophagitis(self):
        """Esophagitis: dysphagia & heartburn"""
        print("\nDiagnosis: Esophagitis")

    @Rule(Fact(symptom='fatigue'), Fact(symptom='weight_loss'), Fact(symptom='diarrhea'))
    def diagnose_ibs(self):
        """Irritable Bowel Syndrome: fatigue, weight change, diarrhea"""
        print("\nDiagnosis: Irritable Bowel Syndrome (IBS)")

if __name__ == "__main__":
    main()
