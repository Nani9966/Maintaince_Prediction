import pymongo 
import pandas as pd 
import json 

#Provide the mongoDB local host url to connect Python to mongo db

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

TRAIN_DATA_PATH="/config/workspace/Turbo_jet_data/train_FD001.txt"
TEST_DATA_PATH='/config/workspace/Turbo_jet_data/test_FD001.txt'
RUL_DATA_PATH='/config/workspace/Turbo_jet_data/RUL_FD001.txt'


DATABASE_NAME="PREDICTION"
COLLECTION_NAME1="PREDICTION_TRAIN"
COLLECTION_NAME2="PREDICTION_TEST"
COLLECTION_NAME3="RUL"

if __name__=="__main__":
    
 
####   TRAIN_DATA_SET_EXPORT ############# 
    index_names = ['unit_nr', 'time_cycles']
    setting_names = ['setting_1', 'setting_2', 'setting_3']
    sensor_names = ['s_{}'.format(i) for i in range(1,22)] 
    col_names = index_names + setting_names + sensor_names
    train_df= pd.read_csv(TRAIN_DATA_PATH, sep='\s+', header=None, names=col_names)
    train_df.reset_index(drop=True,inplace=True)
    train_df=train_df.dropna(axis=1,how='all') 

 ## converting the data into json format   
    json_record=list(json.loads(train_df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME1].insert_many(json_record)



####   TEST_DATA_SET_EXPORT ############# 

    index_names = ['unit_nr', 'time_cycles']
    setting_names = ['setting_1', 'setting_2', 'setting_3']
    sensor_names = ['s_{}'.format(i) for i in range(1,22)] 
    col_names = index_names + setting_names + sensor_names
    test_df= pd.read_csv(TEST_DATA_PATH, sep='\s+', header=None, names=col_names)
    test_df.reset_index(drop=True,inplace=True)
    test_df=test_df.dropna(axis=1,how='all')


 ## converting the data into json format   
    json_record=list(json.loads(test_df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME2].insert_many(json_record)



### RUL_DATA_EXPORT #################


    RUL_df= pd.read_csv(RUL_DATA_PATH,sep='\s+', header=None, names=['RUL'])
    RUL_df.reset_index(drop=True,inplace=True)
    RUL_df=RUL_df.dropna(axis=1,how='all') 
 ## converting the data into json format   
    json_record=list(json.loads(RUL_df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME3].insert_many(json_record)


    print(f"Rows and columns of RUL : {RUL_df.shape} ")
    print(f"Rows and columns of test_data is :{test_df.shape}")
    print(f"Rows and columns of train_data is:{train_df.shape}")


################## change the data ######

    print(sss)

