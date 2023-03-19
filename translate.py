from googletrans import Translator


def translate_to_en(text: str) -> str:
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='ru', dest='en')
    return translation.text


def translate_to_ru(text: str) -> str:
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='ru')
    return translation.text
