# Project description:

The aim of the project was to take the FaceNet architecture described in Schroff, Kalenichenko and Philbin (2015) (link: https://arxiv.org/pdf/1503.03832.pdf) and try to adapt it for emotion recognition

# Dataset

The dataset used was the Static Facial Expressions in the Wild (SFEW) provided for the Emotion Recognition in the Wild (EmotiW) 2015 challenge. Data consists of 160x160x3 facial crops taken from movies. Each crop is labeled with one of the seven universal emotions (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)

I tested out two different types of data augmentation. The first one was taking the horizontal reflection of each image and adding it to the dataset. The second one was a standard 10-crop augmentation (taking the top-left, top-right, bottom-left, bottom-right, center crops of the image and their horizontal reflections). There was no significant difference in performance between the two augmentations.

# Models and results

I tested two groups of models. The first was simple, shallow CNNs, used as a baseline. The second was models based on the final layers of a pre-trained FaceNet (pre-training done on the CASIA-WebFace dataset). 

The architecture for the two simple models was as follows (nonlinearity used is ReLU, after all Convolutional and fully connected layers (except the FC layer immediately before softmax)):

Model S1:
Convolution - Batch Normalization - Max Pool - Convolution - Batch Normalization - Max Pool - Fully Connected - Fully Connected - Softmax
Both convolutions had 64 filters, kernel size 5, stride 2
The Fully connected layer had 128 units (the second FC layer had 7 units, since we have 7 classes)
Training accuracy - 93% (training was done for 7 epochs, so training accuracy might have gone higher with more training)
Validation accuracy - 23.4%

Model S2:
Convolution - Batch Normalization - Max Pool - Fully Connected - Fully Connected - Softmax
Convolution had 64 filters, kernel size 9, stride 4
Fully connected layer had 128 units
Training accuracy - 93.9% (again with 7 epochs of training)
Validation accuracy - 24.8%

We can see that both models significantly overfit the data. This is not very surprising, as the dataset is small

For the pre-trained FaceNet models, I tested the following combinations: 

For the output of the pre-trained part, taking the output of the average pool layer, of the final FC layer, of the L2 normalization, or all three of these outputs concatenated
For the "new" part of the net that was to be trained, having a hidden fully connected layer of 128/256/512 units (with ReLU nonlinearity) followed by a fully connected layer of 7 units and then softmax; as well as having no hidden layer, i.e. just having a fully connected layer of 7 units followed by softmax

The validation accuracy for these models also ranged from 20% to 28% (training accuracy ran from 28% for the L2 normalization output with no hidden layer to more than 70% for hidden layer models with the average pool layer output (or all three outputs)). The strong overfit that some of these models showed leads me to believe that perhaps the strength of the features is too large compared to the size of the dataset we have - i.e. linear combinations of the features allow us to discriminate the images in the training set because it is not very large, even though the features aren't necessarily useful for recognizing emotion.

These results are somewhat disappointing, since the EmotiW challenge reported achieving 35.96% validation accuracy for a baseline SVM trained on hand-crafted features. 



Original codebase forked from https://github.com/davidsandberg/facenet
