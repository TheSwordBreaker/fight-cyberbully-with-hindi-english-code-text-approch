# use_text_to_vertor= pickle.load(open("./pickel/tfidf_vector_vocabulary.pkl", "rb"))
import argparse
import os
import pickle
from cleanner import comment_cleaner_updated
from sklearn.feature_extraction.text import TfidfVectorizer


def string_argument(value):
    if not isinstance(value, str):
        raise argparse.ArgumentTypeError('Msg must be a string')
    return value

# Create a new ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument to the parser
parser.add_argument('msg', type=string_argument, help='pass text to check if it is bullying')

# Parse the arguments from the command line
args = parser.parse_args()

path =  os.path.dirname(os.path.abspath(__file__))
# Get the path of the file
folder_name = 'pickel'
voc_name = 'tfidf_vector_vocabulary.pkl'
voc_path = os.path.join(path,folder_name, voc_name)

model_name = 'LinearSVC.pkl'
model_path = os.path.join(path,folder_name, model_name)

use_text_to_vertor = TfidfVectorizer( lowercase = True,vocabulary=pickle.load(open(voc_path, "rb")))


data = args.msg
print("Msg is : {}\n".format(data))
data = comment_cleaner_updated(data)
data= use_text_to_vertor.fit_transform([data])

trained_model=pickle.load(open(model_path, 'rb'))


if(trained_model.predict(data)==1):
  print('bullying')
else:
  print('non-bullying')
