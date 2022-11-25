""""import required libraries"""
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# creating an instance of the IBM Watson Language translator

# authenticate
authenticator = IAMAuthenticator(apikey)

# setup service
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

lt.set_service_url(url)


def english_to_french(english_text):
    """translating to French"""
    french_text = lt.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """translating to English"""
    english_text = lt.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text

# # calling function for e2f translation
# french_translation = englishToFrench('Hello')
# print(french_translation)

# # calling function for f2e translation
# english_translation = frenchToEnglish('Bonjour')
# print(english_translation)
