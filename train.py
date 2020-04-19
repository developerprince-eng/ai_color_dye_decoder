import model.main as model
import dataset.main as dataset
from keras.models import model_from_json, model_from_yaml


import os 
os.getcwd()
os.listdir(os.getcwd())

def main():
    create_dataset = dataset.DATASET()

    train_features, test_features   = create_dataset.__image_pass__("input/features/", "png", test_size=0.2, random_state=0)

    train_labels, test_labels = create_dataset.__read__lb_csv__('input/labels.csv', test_size=0.2, random_state=0)

    train_features.drop(train_features.tail(1).index,inplace=True)

    print(len(train_features))

    print(len(test_features))

    print(len(train_labels))

    print(len(test_labels))

    #Initiate Generate Model Object
    classifier = model.MODEL() 

    #Model Generation and Metric Evaluation
    metric = classifier.kr_train_DNN_Seq_03(1, train_features, test_features, train_labels, test_labels, batch_size=4)

    print(f'\nAccuracy of your XENTE FRAUD DETECTION AI Model is : \033[1m \033[92m{metric}%')

if __name__ == "__main__":
    main()
