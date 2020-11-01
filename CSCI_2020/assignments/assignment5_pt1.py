class Hepatitis():
    def __init__(self, Class = '', Age = 0, Sex = '', Steroid = False, Antivirals = False,
                 Fatigue = False, Malaise = False, Anorexia = False, Liver_Big = False,
                 Liver_Firm = False, Spleen_Palpable = False, Spiders = False,
                 Ascites = False, Varices = False, Bilirubin = 0, Alk_Phosphate = 0,
                 SGOT = 0, Albumin = 0, Protime = 0, Histology = False):

        self.Class = Class
        self.Age = Age
        self.Sex = Sex
        self.Steroid = Steroid
        self.Antivirals = Antivirals
        self.Fatigue = Fatigue
        self.Malaise = Malaise
        self.Anorexia = Anorexia
        self.Liver_Big = Liver_Big
        self.Liver_Firm = Liver_Firm
        self.Spleen_Palpable = Spleen_Palpable
        self.Spiders = Spiders
        self.Ascites = Ascites
        self.Varices = Varices
        self.Bilirubin = Bilirubin
        self.Alk_Phosphate = Alk_Phosphate
        self.SGOT = SGOT
        self.Albumin = Albumin
        self.Protime = Protime
        self.Histology = Hisology


# get methods
    def get_Class(self):
        return(self.Class)
    def get_Age(self):
        return(self.Age)
    def get_Sex(self):
        return(self.Sex)
    def get_Steroid(self):
        return(self.Steroid)
    def get_Antivirals(self):
        return(self.Antivirals)
    def get_Fatigue(self):
        return(self.Fatigue)
    def get_Malaise(self):
        return(self.Malaise)
    def get_Anorexia(self):
        return(self.Anorexia)
    def get_Liver_Big(self):
        return(self.Liver_Big)
    def get_Liver_Firm(self):
        return(self.Liver_Firm)
    def get_Spleen_Palpable(self):
        return(self.Spleen_Palpable)
    def get_Spiders(self):  
        return(self.Spiders)
    def get_Ascites(self):
        return(self.Ascites)
    def get_Varices(self):
        return(self.Varices)
    def get_Bilirubin(self):
        return(self.Bilirubin)
    def get_Alk_phosphate(self):
        return(self.Alk_Phosphate)
    def get_SGOT(self):
        return(self.SGOT)
    def get_Albumin(self):
        return(self.Albumin)
    def get_Portime(self):
        return(self.Protime)
    def get_Histology(self):
        return(self.Histology)


    def set_Class(self, setValue):
        self.Class = setValue
