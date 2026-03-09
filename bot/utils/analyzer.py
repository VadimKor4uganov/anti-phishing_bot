from data import loader
import re

def analyze_message(text):
    if not text:
        return None
    text = text.lower()
    
    for word in loader.SUSPICIOUS_WORDS:
        if word in text:
            return f"подозрительное слово: {word}"
    
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    for url in urls:
        domain = url.split('/')[2] if '://' in url else url
        if not any(site in domain for site in loader.WHITELIST):
            return f"подозрительная ссылка: {url}"
    
    return None
