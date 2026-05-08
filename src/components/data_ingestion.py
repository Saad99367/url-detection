import os 
import sys 
import pandas as pd
from sklearn.model_selection import train_test_split 
from src.config.constants import (
    DATA_FILE_PATH,
    ARTIFACTS_DIR
)
from src.utils.logger import logging 
from src.utils.exception import UrlException 



class DataIngestion: 
    """
    Data Ingestion Components 
    """

    def __init__(self): 

        self.raw_path= os.path.join(
            ARTIFACTS_DIR, 
            'raw.csv'
        )

        self.train_path= os.path.join(
            ARTIFACTS_DIR, 
            'train.csv' 
        ) 

        self.test_path= os.path.join(
            ARTIFACTS_DIR, 
            'test.csv'
        )
    

    def init_data_ingestion(self):  

        logging.info('Data ingestion started...') 

        try: 
            df= pd.read_csv(DATA_FILE_PATH) 
            logging.info('Data loaded successfully...') 

            os.makedirs(ARTIFACTS_DIR, exist_ok=True) 

            raw_data= df.to_csv(self.raw_path, index=False)
            logging.info("Raw data saved successfully...") 

            train_set, test_set= train_test_split(
                df, test_size=0.2, random_state=42
            )  

            logging.info("Train test split completed")

            train_set.to_csv(
                self.train_path, 
                index= False
            ) 

            test_set.to_csv(
                self.test_path, 
                index= False
            )
            logging.info("Train/Test data loaded successfully..")
        
            return(
                self.raw_path, 
                self.train_path, 
                self.test_path 
            )
        
        except Exception as e : 
            raise UrlException(e, sys)





if __name__ == "__main__": 
    obj= DataIngestion() 
    obj.init_data_ingestion() 
    print(obj.train_path, obj.raw_path, obj.test_path)