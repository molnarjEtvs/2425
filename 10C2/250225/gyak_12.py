class Motor:
    def __init__(self,marka:str,cm3:str):
        self.marka = marka
        self.cm3 = cm3
    
    def adatkiiras(self):
        print(f"Márka: {self.marka}, cm3: {self.cm3}")


motor1 = Motor("Suzuki","50")
motor1.adatkiiras()
