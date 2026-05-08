import pickle
import os 
import sys 

from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
)

from src.utils.logger import logging 
from src.utils.exception import UrlException 



def save_object(file_path, obj): 
    """
    Save python objects
    """

    try:

        logging.info('Save object method started...')

        dir_name = os.path.dirname(file_path)

        if dir_name != "":
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as f:

            pickle.dump(obj, f)

        logging.info(f'Object saved successfully in: {file_path}')

    except Exception as e:

        raise UrlException(e, sys)


def load_object(file_path): 
    """
    Load python Objects 
    """
    try: 
        logging.info('Load object method started...') 
        with open(file_path, 'rb') as f: 
           obj = pickle.load(f)
        logging.info('Object loaded successfully')
        return obj


    
    except Exception as e: 
        raise UrlException(e, sys)

def classification_metrics(y_test, y_pred):
    """
    Calculate evaluation metrics 
    """ 
    logging.info('Classification method started...')

    try: 
        acc= accuracy_score(y_test, y_pred) 
        report= classification_report(y_test, y_pred)
        logging.info("Classification method finished")
        return acc, report

    except Exception as e: 
        raise UrlException(e,sys) 
    
