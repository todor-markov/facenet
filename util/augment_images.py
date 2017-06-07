from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.15,
        horizontal_flip=True,
        fill_mode='nearest')


# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow_from_directory('../../data/SFEW_2/Train/Train_For_Augmentation/Surprise', (160,160), class_mode=None, batch_size=1, 
                                         save_to_dir='../../data/SFEW_2/Train/Train_Augmented_Faces/Surprise', save_prefix='aug', save_format='png'):
    i += 1
    if i > 10000:
        break  # otherwise the generator would loop indefinitely