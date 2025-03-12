import os
os.system("cls")

class Motor:
    def __init__(self,marka:str,cm3:str):
        self.marka = marka
        self.cm3 = cm3

    def adatkiiras(self):
        print(f"{self.marka}, {self.cm3}")

motor1 = Motor("Suzuki","1328")
motor1.adatkiiras()