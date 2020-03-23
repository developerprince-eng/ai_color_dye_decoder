import model.main as model
import dataset.main as dataset
from keras.models import model_from_json, model_from_yaml


import os 
os.getcwd()
os.listdir(os.getcwd())

def main():
    create_dataset = dataset.DATASET()

    labels     = create_dataset.__read_csv__('input/labels.csv')

    print(labels)

    #Initiate Generate Model Object
    classifer = model.MODEL() 

    #Model Generation and Metric Evaluation
  
if __name__ == "__main__":
    main()
