import os
import uuid
import tflearn
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
import scipy
import tensorflow
from tensorflow.python.lib.io import file_io
import numpy as np

class Classsifier(object):
    
    def __init__(self):
        checkpoint_dir = os.getenv("CHECKPOINT_DIR"),
        # checkpoint_dir = '/Users/wayne/Downloads/check_point'
        # Real-time data preprocessing
        img_prep = ImagePreprocessing()
        img_prep.add_featurewise_zero_center()
        img_prep.add_featurewise_stdnorm()

        # Real-time data augmentation
        img_aug = ImageAugmentation()
        img_aug.add_random_flip_leftright()
        img_aug.add_random_rotation(max_angle=25.)

        # Convolutional network building
        network = input_data(shape=[None, 32, 32, 3],
                            data_preprocessing=img_prep,
                            data_augmentation=img_aug)
        network = conv_2d(network, 32, 3, activation='relu')
        network = max_pool_2d(network, 2)
        network = conv_2d(network, 64, 3, activation='relu')
        network = conv_2d(network, 64, 3, activation='relu')
        network = max_pool_2d(network, 2)
        network = fully_connected(network, 512, activation='relu')
        network = dropout(network, 0.5)
        network = fully_connected(network, 10, activation='softmax')
        network = regression(network, optimizer='adam',
                            loss='categorical_crossentropy',
                            learning_rate=0.001)

        # Train using classifier
        model = tflearn.DNN(network, tensorboard_verbose=0)

        model_path = os.path.join(checkpoint_dir, "model.tfl")
        print(model_path)
        model.load(model_path)
        self.model = model
        
classsifier = Classsifier()

def classify(image_data):
    file_name = str(uuid.uuid1())
    file_io.write_string_to_file(file_name, image_data)
    img = scipy.ndimage.imread(file_name, mode="RGB")
    # Scale it to 32x32
    img = scipy.misc.imresize(img, (32, 32), interp="bicubic").astype(
        np.float32, casting='unsafe')

    # Predict
    prediction = classsifier.model.predict([img])
    print(prediction[0])
    #print (prediction[0].index(max(prediction[0])))
    num = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    result = "This is a %s" % (num[prediction[0].tolist().index(max(prediction[0]))])
    file_io.delete_file(file_name)
    return result

if __name__ == '__main__':
    import os
    data = tensorflow.gfile.FastGFile(
        '/Users/wayne/Documents/Aliyun/PAI/bird_bullocks_oriole.jpg', 'rb').read()
    print(classify(data))
