import re
from nltk.tokenize import WordPunctTokenizer


def comment_cleaner_updated(text):

    # soup = BeautifulSoup(text,  "html.parser")
    # souped = soup.get_text()

     # removes @user
    # text = np.vectorize(remove_pattern)(text,"@[\w]*")

    clean = re.sub(r'@\S+|(https?://[^ ]+)|(RT)|(\\x[a-zA-z0-9]+)|(www.[^ ]+)','',text)
    clean_lower_case = clean.lower()
    clean_letters_only = re.sub("[^a-zA-Z]", " ", clean_lower_case)
  
    #unnecessary white spaces may have been created due to cleaning
    #Therefore it is necessary to tokenize the string and then join them together to eliminate extra spaces
    tokenizer  = WordPunctTokenizer()
    words = [x for x  in tokenizer.tokenize(clean_letters_only) if len(x) > 1]
    return (" ".join(words)).strip()