#   importing responsories

class TruthorFalsehood():

    '''
        #   Author : krigjo25
        #   Date   :

        #   Calibration of truth based on David R. Hawkings Calibration system
        #   
    '''

    def __init__(self): pass

    def MapofthescaleofConsciousness(self, calibration):

        if calibration >= 0 and calibration < 30: pass
        elif calibration > 249 and calibration < 50: pass
        elif calibration >= 310 and calibration < 75: pass
        elif calibration >= 350 and calibration < 100: pass
        elif calibration >= 400 and calibration < 125: pass
        elif calibration >= 500 and calibration < 150: pass
        elif calibration >= 540 and calibration < 175: pass
        elif calibration >= 600 and calibration < 700: pass
        elif calibration > 199 and calibration < 250: arg = ["Permitting", "Feasible", "Courage", "200", "Affirmation", "Empowerment"]
        elif calibration > 249 and calibration < 310: pass
        elif calibration >= 310 and calibration < 350: pass
        elif calibration >= 350 and calibration < 400: pass
        elif calibration >= 400 and calibration < 500: pass
        elif calibration >= 500 and calibration < 540: pass
        elif calibration >= 540 and calibration < 600: pass
        elif calibration >= 600 and calibration < 700: pass
        elif calibration >= 700 and calibration < 1001: arg = ["Self", "Is", "Enlightment", "700-1000", "Ineffable", "Pure Consciousness"]

        else:
            print("something went wrong with the calculation of calibration")
        return arg

    def CalculationofCalibration(self, string): pass

    def main(self):

        try:
            #   Prompting the user for a input
            prompt = input("Input a sentence")

        except Exception as e: print(e)
        else: 

            n = self.CalculationofCalibration(prompt)
            answer = self.MapofthescaleofConsciousness()

        return print(f"The statement {prompt} calibrates  {n}{answer}")

