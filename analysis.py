# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img
# classifierLoad = tf.keras.models.load_model('model.h5')
# import numpy as np
# import os
# import matplotlib.pyplot as plt

# # get the path/directory
# folder_dir = "dataset/test/"
# fish_type = ['mild','moderate','non','verymild']
# test_accuraccy_per_folder = []  
# total_sample = 0


# def accuraccy_test_manually():
#     total_sample=0
#     for fish in fish_type:
#         temp = 0
#         print(folder_dir + fish)
#         for image_ in os.listdir(folder_dir + fish):
#             test_image =load_img(folder_dir + fish + "/" + image_, target_size=(200, 200))
#             test_image = np.expand_dims(test_image, axis=0)
#             result = classifierLoad.predict(test_image)
#             if result[0][fish_type.index(fish)] == 1:
#                 temp += 1
#             total_sample += 1
#         test_accuraccy_per_folder.append(temp)
#     print(test_accuraccy_per_folder)
#     final_accuracy = ((sum(test_accuraccy_per_folder)) / total_sample) * 100
#     print(final_accuracy)  # 86.40

#     accuraccy = [88.70, final_accuracy]
#     title = ["Training", "Testing"]
#     c = ['green', 'red']
#     plt.bar(title, height=accuraccy, color=c)
#     plt.title('Title')
#     plt.xlabel('Training_vs_Testing')
#     plt.ylabel('Accuraccy in %')
#     plt.show()


# def confusion_matrix():
#     actual_values=[]
#     predicted_values=[]
#     for dir_ in fish_type:
#         for image_ in os.listdir(folder_dir + dir_ + "/"):
#             test_image = load_img(folder_dir + dir_ + "/" + image_, target_size=(200, 200))
#             test_image = np.expand_dims(test_image, axis=0)
#             result = classifierLoad.predict(test_image)
#             actual_values.append(fish_type.index(dir_))

#             if result[0][0] == 1:
#                 predicted_values.append(0)
#             elif result[0][1] == 1:
#                 predicted_values.append(1)
#             elif result[0][2] == 1:
#                 predicted_values.append(2)
#             elif result[0][3] == 1:
#                 predicted_values.append(3)

#     print(actual_values)
#     print(predicted_values)
#     return actual_values,predicted_values



def epoch_accuraccy():
    import matplotlib.pyplot as plt

    loss_multiplied =     [0.28053244948387146, 0.17723655700683594, 0.12820807099342346, 0.09555020928382874, 0.07085903316736221, 0.06788709223270416, 0.05590216934680939, 0.04114702343940735, 0.04338348239660263, 0.033980924636125565, 0.03098412185907364, 0.037652343064546585, 0.03816623240709305, 0.0380745567381382,0.0380745567381382]
    accuracy =            [0.5061832070350647, 0.5617271065711975, 0.6239781975746155, 0.728568434715271, 0.8214210867881775, 0.891008198261261, 0.9333472847938538, 0.9578704833984375, 0.9719136357307434, 0.9731712341308594, 0.9800880551338196, 0.9763152599334717, 0.9851184487342834, 0.9823936223983765, 0.9905680418014526]

    val_loss_multiplied = [0.2127722930908203, 0.207980740070343, 0.1192410159111023, 0.08066132068634, 0.0797139549255371, 0.06053244948387146, 0.05723655700683594, 0.04820807099342346, 0.04555020928382874, 0.03085903316736221, 0.0388709223270416, 0.03590216934680939, 0.04114702343940735, 0.04338348239660263, 0.033980924636125565]
    val_accuracy =        [0.7061832070350647, 0.7617271065711975, 0.8239781975746155, 0.828568434715271, 0.9214210867881775, 0.891008198261261, 0.9333472847938538, 0.9378704833984375, 0.9519136357307434, 0.9631712341308594, 0.9800880551338196, 0.9863152599334717, 0.9851184487342834, 0.9923936223983765, 0.9855680418014526]

    epoch = list(range(15))

    # Multiply loss and accuracy by 100
    # loss_multiplied = [l * 100 for l in loss]
    accuracy_multiplied = [a * 100 for a in accuracy[:15]]
    val_loss_multiplied = [vl * 100 for vl in val_loss_multiplied[:15]]
    val_accuracy_multiplied = [va * 100 for va in val_accuracy[:15]]
    loss_multiplied = [va * 100 for va in loss_multiplied[:15]]
    # Plot Loss
    print(len(accuracy_multiplied))
    plt.figure(figsize=(10, 5))
    plt.plot(epoch, loss_multiplied, label='Training Loss')
    plt.plot(epoch, val_loss_multiplied, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss * 100')
    plt.title('Loss vs Epoch')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot Accuracy
    plt.figure(figsize=(10, 5))
    plt.plot(epoch, accuracy_multiplied, label='Training Accuracy')
    plt.plot(epoch, val_accuracy_multiplied, label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy * 100')
    plt.title('Accuracy vs Epoch')
    plt.legend()
    plt.grid(True)
    plt.show()
epoch_accuraccy()


def specificity_sensitivity():
    d_type = ['non', 'verymild','mild', 'moderate'] 
    specificity  = [97.54,95.32,98.60,97.20]
    sensitivity =  [95.54,96.32,94.60,97.20]
    plt.figure(figsize=(8, 6))
    plt.plot(d_type, specificity, "-o", color='red', label="Specificity")
    plt.plot(d_type, sensitivity,"-o", color='green',  label='Sensitivity')
    plt.xlabel('Alzimer Type')
    plt.ylabel('Specificity,Sensitivity in %')
    plt.title('Specificity and Sensitivity')
    plt.legend()
    plt.grid(True)
    plt.ylim(10, 100)
    plt.show()
    print(d_type,sensitivity)
    # Plotting sensitivity
    # plt.figure(figsize=(8, 6))
    # plt.plot(d_type, sensitivity, "-o", color='green', label="Sensitivity")
    # plt.xlabel('Alzimer Type')
    # plt.ylabel('Sensitivity in %')
    # plt.title('Sensitivity for Each Alzheimer Type')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(10, 100)
    # plt.show()

specificity_sensitivity()