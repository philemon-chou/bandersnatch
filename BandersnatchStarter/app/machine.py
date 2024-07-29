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

class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        probability, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(probability)

    def save(self, filepath):
        # dump(self.model, filepath)
        pass

    @staticmethod
    def open(filepath):
        # return load(filepath)
        pass

    def info(self):
        return f"We are currently running {self.name} at {self.timestamp}."



