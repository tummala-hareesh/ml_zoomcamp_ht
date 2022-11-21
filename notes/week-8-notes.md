# Week 8
These notes were prepared during week-8 of ML Zoomcamp. The topic for this week is `Neural Networks and Deep Learning`.

# 1 Fashion classification
- Tabluar data in previous lessons. 
- Use Images -> Multi-class classification 
- **Usecase**: User comes to website -> Upload a picture -> Fashion Classification Service (T-shirt) -> Selection of category faster
- Goal is to suggest a category to make it easier for user
- Sub-set of Fashion dataset 
- 10 categories of clothes ~ 5000 images
- Train, test and Validation is already present
- Practical application of neural network
- Not theoritical - Go to `CS231n Stanford` for more theory 


# 1b Setting up the Environment on Saturn Cloud
- Saturn cloud for using GPUs
- Configure SSH to push Saturn notebook to Github (if needed)
- `clothes-classsification-mlzoomcamp`

# 2 TensorFlow and Keras
- Framework for doing deep-learning
- Keras is higher-level abstract on top of Tensorflow
- Load image with a target_size as a neural network expect image with a specific size.
- `PIL` - Processing image library in python 
- Image = Numpy array with 3 channels
    - RED: 0-255
    - GREEN: 0-255
    - BLUE: 0-255
- Each numpy array element is a pixel with (R,G,B) values


# 3 Pre-trained convolutional neural networks
- Imagenet is a huge dataset with ~1000 object classes 
- keras has pre-trained models for us to use
- Different models with different architectures
    - Xception model 
    - preprocesing input from xception
    - decode_prediction from xception 


# 4 Convolutional neural networks
- Type of NN used for Images 
- Convolutional layer 
- Xception model is a CNN
    - multiple layers
    - Convoluation layers   
        - Filters 
        - simple images 
        - aceoss the image - similarity of pixel with simple image
        - Outputs: Set of Feature Maps
        - 2nd CNN will create feature maps using feature map1
        - Finally, extract vector representation 
    - Dense layers 
        - Vector representation is passed to Dense layer
        - We get predictions from dense layer
- `Pooling` for making NN smaller with less no. of features. 

# 5 Transfer learning
- Take already trained models 
- Use Convolution layer 
- Retrain Kense layer 
- Use a lower target size of train faster E,g: `target_size=(150,150)` 
- `OneHot Encoding` for multi-class classification
- `include_top=False` avoids Denselayers in Keras
- Pooling, Optimizer, Losses, Activation/Softwmax 


# 6 Adjusting the learning rate
- How fast we can read. - `Learning Rate`

# 7 Checkpointing
- Way of saving model after each iteration of after certain iterations are met. 


# 8 Adding more layers
- Adding more Dense layers
- Activation functions - softmax, sigmoid, ReLu, etc.,

# 9 Regularization and dropout
- Many EPOCS, NN might look at trends
- Hide a part of an image -> Model will see different inputs every time we train

# 10 Data augmentation
- Creating new data from actual
- Different approach w.r.t Dropout, 
- generate more images from existing ones
    - Tranformations to create diffeerente images 
    - flip 
    - resize etc., 
- 

# 11 Training a larger model
- Train on 299x299 images instead of 150x150 sized images

# 12 Using the model
- Loading and Predictions
- test dataset

# 13 Summary
- pre-Trained models 
- Convolutional layer 
- Dense layer 
- Use Convolutional layer and create your own dense layer/s
- Test on (150x150) and then train on (299x299) dataset
- Learning rate, Callbacks, checkpoints, dropout
- Data Augumentation etc., 

# 14 Explore more
- Using PyTorch instead of TensorFlow/Keras
- Try other architectures, in addition to Xception 

# 15 Homework
- [Link to week-8 homework](../ipynb/08_homework.ipynb)
