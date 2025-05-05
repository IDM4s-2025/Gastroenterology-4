from experta import *


class Symptom(Fact):
    """Info about the symptoms."""
    pass
class diagnosis(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        """Initial action to be performed when the engine starts.
        This method is called automatically when the engine is run.
        It prints a welcome message and prompts the user for input.
        The imputs are stored in a dictionary called symptom.
        The dictionary is then passed to the Symptom class to create a new instance.

        Yields:
            dictionary: containing the user's input for each symptom.
        """
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
        """If the user has nausea, bloated stomach, abdominal pain, diharrea and gurgling stomach,
        the user is diagnosed with lactose intolerance.
        """
        print("\nDiagnóstico: Tienes Lactose intolerance (e4)")

    @Rule(Symptom(A=True, B=True, E=True, D=True, H=False))
    def diverticular_disease(self):
        """If the user has nausea, bloated stomach, abdominal pain, diharrea and no gurgling stomach,
        the user is diagnosed with diverticular disease.
        """
        print("\nDiagnóstico: Tienes Diverticular disease (e3)")

    @Rule(Symptom(A=True, B=True, E=True, D=False))
    def colon_cancer(self):
        """If the user has nausea, bloated stomach, abdominal pain and no diharrea,
        the user is diagnosed with colon cancer.
        """
        print("\nDiagnóstico: Tienes Colon cancer (e5)")

    @Rule(Symptom(A=True, B=True, E=False, H=False))
    def gastritis(self):
        """If the user has nausea, bloated stomach and no abdominal pain and no gurgling stomach,
        the user is diagnosed with gastritis.
        """
        print("\nDiagnóstico: Tienes Gastritis (e9)")

    @Rule(Symptom(A=True, B=True, E=False, H=True, P=True))
    def ibs_e2(self):
        """If the user has nausea, bloated stomach, no abdominal pain, gurgling stomach and acid reflux,
        the user is diagnosed with irritable bowel syndrome.
        """
        print("\nDiagnóstico: Tienes Irritable bowel syndrome (e2)")

    @Rule(Symptom(A=True, B=True, E=False, H=True, P=False))
    def constipation(self):
        """If the user has nausea, bloated stomach, no abdominal pain, gurgling stomach and no acid reflux,
        the user is diagnosed with constipation.
        """
        print("\nDiagnóstico: Tienes Constipation (e7)")

    @Rule(Symptom(A=False, B=True))
    def ibs_e1(self):
        """If the user has no nausea, bloated stomach,
        the user is diagnosed with irritable bowel syndrome.
        """
        print("\nDiagnóstico: Tienes IBS (e1)")

    @Rule(Symptom(A=True, B=False, G=True))
    def barretts(self):
        """If the user has nausea, no bloated stomach and chest pain,
        the user is diagnosed with Barrett's esophagus.
        """
        print("\nDiagnóstico: Tienes Barrett’s (e10)")

    @Rule(Symptom(A=True, B=False, G=False))
    def gastroenteritis(self):
        """If the user has nausea, no bloated stomach and no chest pain,
        the user is diagnosed with gastroenteritis.
        """
        print("\nDiagnóstico: Tienes Gastroenteritis (e6)")

    @Rule(Symptom(A=False, B=False))
    def hemorroides(self):
        """If the user has no nausea and no bloated stomach,
        the user is diagnosed with hemorroides.
        """
        print("\nDiagnóstico: Tienes Hemorroides (e8)")

questions = diagnosis() # Create an instance of the diagnosis class
while True: # Start the loop to ask the user for input in case of wanting to do another diagnosis or an error
    try:
        questions.reset() # Reset the engine to clear previous facts and rules
        questions.run() # Run the engine to process the facts and rules
        again = input("Do you want to do another diagnosis? (y/n): ").strip().lower()
        if again != 'y': # If the user does not want to do another diagnosis, break the loop
            break  
    except Exception as e: # Catch any exceptions that occur during the execution of the engine
        # Print the error message and break the loop
        print(f"An error occurred: {e}")
        break
    finally: # This block will always execute, regardless of whether an exception occurred or not
        # Print a message indicating that the program is ending
        print("Thank you for using the medical diagnosis system.")
        print("Goodbye!")