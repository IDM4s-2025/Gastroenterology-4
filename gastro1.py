from experta import *

class Symptom(Fact):
    """Info about the symptoms."""
    pass
class diagnosis(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        print("Welcome to the medical diagnosis system.")
        print("Please answer the following questions with 'y' for yes, or 'n' for no, no other input is available.")
        symptom = {}
        symptom['A']= input("Do you have a nausea? (y/n): ").strip().lower()== 'y'
        symptom['B']= input("Do you have a bloated stomach? (y/n: ").strip().lower() == 'y'
        if symptom['A'] and symptom['B']:
            symptom['E']= input("Do you have abdominal pain? (y/n): ").strip().lower()== 'y'
            if symptom['E']:
                symptom['D']= input("Do you have a diharrea? (y/n): ").strip().lower()== 'y'
                if symptom['D']:
                    symptom['H']= input("Do you have a gurgling stomach? (y/n): ").strip().lower()== 'y'
                else:
                    symptom['H']= False
            else:
                symptom['H']=input("Do you have a gurgling stomach? (y/n): ").strip().lower()== 'y'
                if symptom['H']:
                    symptom['P']= input("Do you have acid reflux? (y/n): ").strip().lower()== 'y'
                else:
                    symptom['P']= False
        elif symptom['A'] and not symptom['B']:
            symptom['G']= input("Do you have chest pain? (y/n): ").strip().lower()== 'y'

        yield Symptom(**symptom)
    
    @Rule(Symptom(A=True, B=True, E=True, D=True, H=True))
    def lactose_intolerance(self):
        print("\nDiagnóstico: Tienes Lactose intolerance (e4)")

    @Rule(Symptom(A=True, B=True, E=True, D=True, H=False))
    def diverticular_disease(self):
        print("\nDiagnóstico: Tienes Diverticular disease (e3)")

    @Rule(Symptom(A=True, B=True, E=True, D=False))
    def colon_cancer(self):
        print("\nDiagnóstico: Tienes Colon cancer (e5)")

    @Rule(Symptom(A=True, B=True, E=False, H=False))
    def gastritis(self):
        print("\nDiagnóstico: Tienes Gastritis (e9)")

    @Rule(Symptom(A=True, B=True, E=False, H=True, P=True))
    def ibs_e2(self):
        print("\nDiagnóstico: Tienes Irritable bowel syndrome (e2)")

    @Rule(Symptom(A=True, B=True, E=False, H=True, P=False))
    def constipation(self):
        print("\nDiagnóstico: Tienes Constipation (e7)")

    @Rule(Symptom(A=False, B=True))
    def ibs_e1(self):
        print("\nDiagnóstico: Tienes IBS (e1)")

    @Rule(Symptom(A=True, B=False, G=True))
    def barretts(self):
        print("\nDiagnóstico: Tienes Barrett’s (e10)")

    @Rule(Symptom(A=True, B=False, G=False))
    def gastroenteritis(self):
        print("\nDiagnóstico: Tienes Gastroenteritis (e6)")

    @Rule(Symptom(A=False, B=False))
    def hemorroides(self):
        print("\nDiagnóstico: Tienes Hemorroides (e8)")

questions = diagnosis()
while True:
    questions.reset() 
    questions.run()
    again = input("Do you want to do another diagnosis? (y/n): ").strip().lower()
    if again != 'y':
        break  