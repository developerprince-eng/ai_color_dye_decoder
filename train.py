import model.main as gm
import dataset.main as dt
from keras.models import model_from_json, model_from_yaml


import os 
os.getcwd()
os.listdir(os.getcwd())

def main():
    create_dataset = dt.DATASET()
    data = create_dataset.__read_csv__('input/training.csv')
    input_x, features_train, features_test, label_train, label_test = create_dataset.__obtain_data__csv__el__lbencode__('input/training.csv', 15, 1)
    
    print(input_x)

    print(features_train)

    print(label_train)

    print("-----------------------------Run Test---------------------------")

    print(features_test)

    print(label_test)

        #Initiate Generate Model Object
    classifer = gm.GENERATE_MODEL() 

        #Model Generation and Metric Evaluation
    metric1 = classifer.kr_train_DNN_Seq_03(14, features_train, features_test, label_train,  label_test, batch_size=100)

    print(f'\nAccuracy of your ETA PREDICTOR AI Model is : \033[1m \033[92m{metric1}%')

   
if __name__ == "__main__":
    main()
