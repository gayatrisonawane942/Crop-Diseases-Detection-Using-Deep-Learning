# -*- coding: utf-8 -*-
import os
import tensorflow as tf 

from keras.preprocessing import image
import numpy as np

classes_citrus = ['Citrus___Black spot', 'Citrus___Canker', 'Citrus___Greening', 'Citrus___healthy',
            'Citrus___Melanose']
classes_corn = ['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
            'Corn_(maize)___Common_rust_', 'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight']
classes_tomato = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 
            'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
            'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
              'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']
classes_wheat = ['Wheat___healthy', 
              'Wheat___septoria', 'Wheat___stripe_rust']              


suggest_corn = [
    'Spray azoxystrobin or propiconazole to control Cercospora leaf spot. Ensure good air circulation by proper spacing and pruning. Rotate crops to reduce pathogen buildup.',
    'Use tebuconazole-based fungicides to manage common rust. Apply at early infection stages and repeat every 10-14 days. Remove infected leaves to prevent spread.',
    'The crop is healthy. Maintain regular monitoring and follow proper irrigation and nutrient management to sustain crop health.',
    'Apply mancozeb or pyraclostrobin to prevent Northern Leaf Blight. Avoid overhead irrigation and practice crop rotation to minimize disease recurrence.'
]

suggest_tomato = [
    'Use copper-based fungicides to control bacterial spot. Avoid working in wet fields to prevent bacterial spread. Use disease-resistant varieties if possible.',
    'Apply chlorothalonil or mancozeb for early blight prevention. Ensure proper air circulation and remove affected leaves immediately.',
    'The crop is healthy. Regularly monitor for pest activity and ensure balanced fertilization for optimal growth.',
    'Spray metalaxyl or copper oxychloride to manage late blight. Destroy infected plants and avoid planting tomatoes near potatoes to reduce disease risk.',
    'Use thiophanate-methyl to prevent leaf mold. Keep humidity levels low in greenhouses and remove infected leaves promptly.',
    'Apply chlorothalonil or azoxystrobin to control Septoria leaf spot. Ensure proper crop rotation and use mulch to prevent soil splash.',
    'Use abamectin or spiromesifen to manage spider mites. Spray neem oil as an organic alternative and introduce predatory mites for biological control.',
    'Spray boscalid or azoxystrobin to prevent target spot. Improve air circulation through pruning and avoid excessive nitrogen application.',
    'Use imidacloprid or neem oil to control tomato mosaic virus. Disinfect tools regularly and remove infected plants immediately to prevent spread.',
    'Apply pymetrozine or acetamiprid to manage Tomato Yellow Leaf Curl Virus. Control whiteflies with insecticidal soap and plant virus-resistant varieties.'
]

suggest_citrus = [
    'Spray copper oxychloride or mancozeb to control black spot. Ensure proper drainage and avoid overhead irrigation to reduce leaf wetness.',
    'Use streptomycin or copper hydroxide to manage citrus canker. Prune infected branches and apply sprays at regular intervals.',
    'Apply imidacloprid or spirotetramat to control citrus greening. Use certified disease-free planting material and control psyllid vectors.',
    'The crop is healthy. Maintain soil fertility, monitor for pests, and ensure timely irrigation to support tree health.',
    'Use thiophanate-methyl or copper fungicides to prevent melanose disease. Remove dead twigs and ensure proper air circulation around the trees.'
]

suggest_wheat = [
    'The crop is healthy. Continue regular field scouting and maintain proper nitrogen levels for healthy growth.',
    'Spray tebuconazole or propiconazole to control Septoria. Improve drainage to prevent excessive moisture, which favors disease development.',
    'Use triadimefon or azoxystrobin to manage stripe rust. Plant resistant wheat varieties and avoid excessive nitrogen fertilization, which can increase susceptibility.'
]




directory="C:/Users/Admin/OneDrive/Desktop/Multi_Crop/input" #Path of input folder to store uploaded image
def predict(image,crop):
  model = 'model-tomato.h5'
  class_ = classes_tomato
  suggest_= suggest_tomato
  if crop=="tomato":
    model = 'model-tomato.h5'
    class_ = classes_tomato
    suggest_= suggest_tomato
  elif crop=='citrus':
    model = 'model-citrus.h5'
    class_ = classes_citrus
    suggest_= suggest_citrus
  elif crop=='corn':
    model = 'model-corn.h5'
    class_ = classes_corn
    suggest_= suggest_corn
  elif crop=='wheat':
    model = 'model-wheat.h5'
    class_ = classes_wheat
    suggest_= suggest_wheat
  classifierLoad = tf.keras.models.load_model(model)
  stage_detected=""

  test_image = tf.keras.utils.load_img(directory+"/"+image, target_size = (200,200))
#test_image = image.img_to_array(test_image)
  test_image = np.expand_dims(test_image, axis=0)
  result = classifierLoad.predict(test_image)
  arr = np.array(result[0])
  index = np.where(arr == 1)[0][0]
  disease = class_[index]
  suggestion = suggest_[index]
  print(suggestion,disease)
  return {"Suggestion":suggestion},{"Disease":disease}
