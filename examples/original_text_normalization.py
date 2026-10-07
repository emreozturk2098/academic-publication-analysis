# Selected original functions; file IO and full script omitted.
import re

def convert_to_english_characters(text):
    conversion_table = {
        'ç': 'c', 'Ç': 'C', 'ş': 's', 'Ş': 'S', 'ı': 'i', 'I': 'i', 
        'ğ': 'g', 'Ğ': 'G', 'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 
        'ı': 'i', 'İ': 'i'
    }
    for key, value in conversion_table.items():
        text = text.replace(key, value)
    return text

def remove_numbers_in_parentheses(text):
    # Sadece string değerlerle işlem yapılacak
    if isinstance(text, str):
        return re.sub(r'\(\d+\)', '', text)  # \(\d+\) -> parantez içindeki rakamlar
    return text
