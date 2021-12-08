import pandas as pd
import os,inspect
from sqlalchemy import create_engine

file_name = inspect.getfile(inspect.currentframe())
path_name=os.path.dirname(os.path.abspath(file_name))

df = pd.read_csv(path_name+'/credit_train_edited_version.csv')
engine = create_engine('sqlite:///'+path_name+'/LoanPrediction/site.db', echo=False)
df.to_sql('Loanee', con=engine)