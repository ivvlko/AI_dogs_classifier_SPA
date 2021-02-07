import tensorflow as tf
from skimage.transform import resize
import requests




named_labels = {0: 'Chihuahua',
 1: 'Japanese_spaniel',
 2: 'Maltese_dog',
 3: 'Pekinese',
 4: 'Shih_Tzu',
 5: 'Blenheim_spaniel',
 6: 'papillon',
 7: 'toy_terrier',
 8: 'Rhodesian_ridgeback',
 9: 'Afghan_hound',
 10: 'basset',
 11: 'beagle',
 12: 'bloodhound',
 13: 'bluetick',
 14: 'black_and_tan_coonhound',
 15: 'Walker_hound',
 16: 'English_foxhound',
 17: 'redbone',
 18: 'borzoi',
 19: 'Irish_wolfhound',
 20: 'Italian_greyhound',
 21: 'whippet',
 22: 'Ibizan_hound',
 23: 'Norwegian_elkhound',
 24: 'otterhound',
 25: 'Saluki',
 26: 'Scottish_deerhound',
 27: 'Weimaraner',
 28: 'Staffordshire_bullterrier',
 29: 'American_Staffordshire_terrier',
 30: 'Bedlington_terrier',
 31: 'Border_terrier',
 32: 'Kerry_blue_terrier',
 33: 'Irish_terrier',
 34: 'Norfolk_terrier',
 35: 'Norwich_terrier',
 36: 'Yorkshire_terrier',
 37: 'wire',
 38: 'Lakeland_terrier',
 39: 'Sealyham_terrier',
 40: 'Airedale',
 41: 'cairn',
 42: 'Australian_terrier',
 43: 'Dandie_Dinmont',
 44: 'Boston_bull',
 45: 'miniature_schnauzer',
 46: 'giant_schnauzer',
 47: 'standard_schnauzer',
 48: 'Scotch_terrier',
 49: 'Tibetan_terrier',
 50: 'silky_terrier',
 51: 'soft',
 52: 'West_Highland_white_terrier',
 53: 'Lhasa',
 54: 'flat',
 55: 'curly',
 56: 'golden_retriever',
 57: 'Labrador_retriever',
 58: 'Chesapeake_Bay_retriever',
 59: 'German_short',
 60: 'vizsla',
 61: 'English_setter',
 62: 'Irish_setter',
 63: 'Gordon_setter',
 64: 'Brittany_spaniel',
 65: 'clumber',
 66: 'English_springer',
 67: 'Welsh_springer_spaniel',
 68: 'cocker_spaniel',
 69: 'Sussex_spaniel',
 70: 'Irish_water_spaniel',
 71: 'kuvasz',
 72: 'schipperke',
 73: 'groenendael',
 74: 'malinois',
 75: 'briard',
 76: 'kelpie',
 77: 'komondor',
 78: 'Old_English_sheepdog',
 79: 'Shetland_sheepdog',
 80: 'collie',
 81: 'Border_collie',
 82: 'Bouvier_des_Flandres',
 83: 'Rottweiler',
 84: 'German_shepherd',
 85: 'Doberman',
 86: 'miniature_pinscher',
 87: 'Greater_Swiss_Mountain_dog',
 88: 'Bernese_mountain_dog',
 89: 'Appenzeller',
 90: 'EntleBucher',
 91: 'boxer',
 92: 'bull_mastiff',
 93: 'Tibetan_mastiff',
 94: 'French_bulldog',
 95: 'Great_Dane',
 96: 'Saint_Bernard',
 97: 'Eskimo_dog',
 98: 'malamute',
 99: 'Siberian_husky',
 100: 'affenpinscher',
 101: 'basenji',
 102: 'pug',
 103: 'Leonberg',
 104: 'Newfoundland',
 105: 'Great_Pyrenees',
 106: 'Samoyed',
 107: 'Pomeranian',
 108: 'chow',
 109: 'keeshond',
 110: 'Brabancon_griffon',
 111: 'Pembroke',
 112: 'Cardigan',
 113: 'toy_poodle',
 114: 'miniature_poodle',
 115: 'standard_poodle',
 116: 'Mexican_hairless',
 117: 'dingo',
 118: 'dhole',
 119: 'African_hunting_dog'}

model = tf.keras.models.load_model('api/model/saved_model-20210201T203511Z-001/saved_model/resnet_inception')


def give_top_three_candidates(pic, model, named_labels=named_labels):
    picture = resize(pic, (299, 299), preserve_range=True)
    picture = tf.keras.applications.inception_resnet_v2.preprocess_input(picture)
    picture = tf.expand_dims(picture, axis=0)
    predictions = model.predict(picture)
    prediction = max(predictions[0])
    index1 = list(predictions[0]).index(prediction)
    predictions[0][index1] = 0
    first_prediction = f'This is a {named_labels[index1]} with {round((100 * prediction), 2)} % certainty'
    prediction = max(predictions[0])
    index2 = list(predictions[0]).index(prediction)
    second_prediction = f'Second guess is {named_labels[index2]} with {round((100 * prediction), 2)} % certainty'
    predictions[0][index2] = 0
    prediction = max(predictions[0])
    index3 = list(predictions[0]).index(prediction)
    third_prediction = f'Third guess is {named_labels[index3]} with {round((100 * prediction), 2)} % certainty'
    return [first_prediction, second_prediction, third_prediction]


def read_tensor_from_image_url(url,
                               input_height=299,
                               input_width=299,
                               input_mean=0,
                               input_std=255):
 image_reader = tf.image.decode_image(
  requests.get(url).content, channels=3, name="jpeg_reader")

 return image_reader
