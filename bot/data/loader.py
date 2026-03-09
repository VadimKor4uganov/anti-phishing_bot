def load_list(path):
    with open(path, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

SUSPICIOUS_WORDS = load_list("data/suspicious_words.txt")
WHITELIST = load_list("data/whitelist_sites.txt")
