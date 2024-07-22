from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
import pandas as pd

'''This data.py page is to ensure correct enviornment is uploaded and connected to this page.
Setting up the class to load MongoDB through the .env file.Then establish functions of the database.
In this page we have the __init__, seed, reset, count, dataframe, and HTML. Goal of this page is to
be able to display 1000 monsters randomly generated from the Monster library.'''

class Database:
    # Created DB_URL set it in .env.
    # Load dotenv
    # Set and get database from .env through getenv.

    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self):
        # Create init function. Set collection to be pulling from database collection
        self.collection = self.database["Collection"]

    def seed(self, amount=1000):
        # Create seed function where amount is set to 1000
        # Code means insert_many from Monster library, convert to dict and insert it in
        # format of however many monster we decide.
        return self.collection.insert_many([Monster().to_dict() for i in range(amount)]).acknowledged

    def reset(self):

        # Deleting many from dict returning the result
        return self.collection.delete_many({}).acknowledged

    def count(self) -> int:

        # Return the counted number of documents in dict
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # Turning collection in to document then in to dataframe
        # through collection, find diction but exclude id
        documents = self.collection.find({}, {"_id": False})

        # Converting the document and result of line above to dataframe
        df = pd.DataFrame(documents)

        # Return DataFrame
        return df

    def html_table(self) -> str:

        # If the collection is empty, return None
        if self.count() <= 0:
            return "None"
        else:
            return self.dataframe().to_html(index=False)


if __name__ == '__main__':
    db = Database()
    db.reset()
    db.seed()
