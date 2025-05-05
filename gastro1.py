import csv
from experta import KnowledgeEngine, Fact, Rule, FIELD

def load_symptoms(csv_path):
    diseases = {}
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            disease = row['disease']
            symptoms = [s.strip() for s in row['symptoms'].split(',')]
            diseases[disease] = symptoms
    return diseases

class GastroExpert(KnowledgeEngine):
    def __init__(self, disease_symptoms):
        super().__init__()
        self.disease_symptoms = disease_symptoms
        self.user_symptoms = set()

    def ask(self, symptom):
        answer = ''
        while answer.lower() not in ('y', 'n'):
            answer = input(f"Do you experience {symptom.replace('_', ' ')}? (y/n): ")
        if answer.lower() == 'y':
            self.declare(Fact(symptom=symptom))
            self.user_symptoms.add(symptom)

    def reset(self):
        super().reset()
        self.user_symptoms.clear()

    @Rule(Fact(symptom=MATCH.s1), Fact(symptom=MATCH.s2))
    def rule_template(self, s1, s2):
        pass

    @Rule(Fact(symptom='heartburn'), Fact(symptom='regurgitation'))
    def diagnose_gerd(self):
        print("Diagnosis: Gastroesophageal Reflux Disease (GERD)")
        self.halt()

    @Rule(Fact(symptom='abdominal_pain'), Fact(symptom='bloating'), Fact(symptom='altered_bowel_habits'))
    def diagnose_ibs(self):
        print("Diagnosis: Irritable Bowel Syndrome (IBS)")
        self.halt()

    @Rule(Fact(symptom='chronic_diarrhea'), Fact(symptom='weight_loss'), Fact(symptom='ulcers_on_colonoscopy'))
    def diagnose_crohns(self):
        print("Diagnosis: Crohn's Disease")
        self.halt()

    @Rule(Fact(symptom='bloody_diarrhea'), Fact(symptom='cramping'), Fact(symptom='mucus_in_stools'))
    def diagnose_uc(self):
       
        print("Diagnosis: Ulcerative Colitis")
        self.halt()

    @Rule(Fact(symptom='epigastric_pain'), Fact(symptom='ulcer_on_endoscopy'))
    def diagnose_peptic_ulcer(self):
      
        print("Diagnosis: Peptic Ulcer Disease")
        self.halt()

    @Rule(Fact(symptom='jaundice'), Fact(symptom='right_upper_quadrant_pain'))
    def diagnose_hepatitis(self):
        
        print("Diagnosis: Hepatitis")
        self.halt()

    @Rule(Fact(symptom='severe_abdominal_pain'), Fact(symptom='high_amylase'))
    def diagnose_pancreatitis(self):
        print("Diagnosis: Acute Pancreatitis")
        self.halt()

    @Rule(Fact(symptom='diarrhea'), Fact(symptom='post_prandial_bloating'))
    def diagnose_lactose_intolerance(self):
        print("Diagnosis: Lactose Intolerance")
        self.halt()

    @Rule(Fact(symptom='gluten_sensitivity'), Fact(symptom='villous_atrophy_on_biopsy'))
    def diagnose_celiac(self):
        print("Diagnosis: Celiac Disease")
        self.halt()

    @Rule(Fact(symptom='right_lower_quadrant_pain'), Fact(symptom='fever'))
    def diagnose_diverticulitis(self):
        print("Diagnosis: Diverticulitis")
        self.halt()

    @Rule(Fact(symptom='nausea'), Fact(symptom='vomiting'), Fact(symptom='diarrhea'), Fact(symptom='recent_travel'))
    def diagnose_gastroenteritis(self):
        print("Diagnosis: Gastroenteritis")
        self.halt()

    @Rule()
    def no_diagnosis(self):
        print("No clear diagnosis. Please consult a specialist.")
        self.halt()

if __name__ == '__main__':
    print("Welcome to the Gastroenterology Diagnostic Expert System!")
    print("Please answer the following questions to help diagnose your condition.")
    diseases = load_symptoms('Symptoms.csv')  # ensure CSV in same directory
    engine = GastroExpert(diseases)
    while True:
        # Ask about all possible symptoms
        for symptom_list in diseases.values():
            for symptom in symptom_list:
                if symptom not in engine.user_symptoms:
                    engine.ask(symptom)
        engine.run()
        again = input("\nWould you like to start a new diagnosis? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the system. Goodbye!")
            break
        
