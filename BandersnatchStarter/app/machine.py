from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib
import datetime
from joblib import dump, load
'''
This portion of the code is meant to display the modeling using RandomForestClassifier to 
predict the rarity of the monster. Within the class, we have the init function to target (y)
and Feature the rarity (X). We have also included the timestamp function to be able to display
what modeling was used and at what time. Call Function is meant to display the Prediction bias and the probability
of the monster along with the prediciton rank and confidence level.
'''
#machine.py connecting to main.py function.
#each variable is supposed to reflect values set according to main.py
#added timestamp for datetime so model name and datetime can be displayed appropirately when webpage is generated
class Machine:

    def __init__(self, df: DataFrame):
        #name of model
        self.name = "Random Forest Classifier"
        #setting target
        target = df["Rarity"]
        #setting feature
        features = df.drop(columns=["Rarity"])
        #model for ML model
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        #added timestamp code
        self.timestamp = datetime.datetime.now()

    #call function
    def __call__(self, pred_basis: DataFrame):
        #prediction number *_ calls for the digits
        prediction, *_ = self.model.predict(pred_basis)
        probability, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(probability)

    def save(self, filepath):
        ## below code for machine not on mac
        # dump(self.model, filepath)
        pass

    @staticmethod
    def open(filepath):
        ## below code for machine not on mac
        # return load(filepath)
        pass

    def info(self):
        # function calls for info including name and timestamp
        return f"We are currently running {self.name} at {self.timestamp}."



