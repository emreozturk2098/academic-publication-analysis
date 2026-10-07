# Selected original functions; file IO and full script omitted.
import re

def remove_numbers_in_parentheses(text):
    if not isinstance(text, str):  # Eğer değer string değilse boş bir string döndür
        return ""
    return re.sub(r"\s*\(.*?\)", "", text).strip()

def parse_full_name(name):
    if not isinstance(name, str):  # Eğer değer string değilse boş bir string döndür
        return ""
    name_parts = name.split(",")  # Soyisim, İsim formatında ayır
    if len(name_parts) == 2:  # Eğer gerçekten soyisim ve isim varsa
        full_name_parts = name_parts[1].strip().split()  # İsimleri ayır
        surname = name_parts[0].strip()
        if len(full_name_parts) == 1:  # Eğer sadece tek bir isim varsa
            return f"{full_name_parts[0]} {surname}"  # Yalnızca 1 isim ve soyisim
        elif len(full_name_parts) == 2:  # Eğer 2 isim varsa
            return f"{full_name_parts[1]} {full_name_parts[0]} {surname}"  # 2. isim ve soyisim, sonra 1. isim
    return name
