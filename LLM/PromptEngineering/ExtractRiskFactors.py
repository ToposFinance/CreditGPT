import os
import sys
import pandas as pd


sys.path.append(os.path.join(os.path.dirname(__file__), '/Users/marcnunes/PycharmProjects/CreditGPT'))


def get_risk_factors():

    taxonomy=pd.read_pickle('Config/taxonomy.pkl')

    