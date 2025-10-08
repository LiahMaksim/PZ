#В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
#(например, в URL-apece http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
#домен выделен полужирным).

import re
def simple_domain_extraction(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    domains = re.findall(r'https?://([^/:\s]+)', text)
    clean_domains = sorted(set(domain.split(':')[0] for domain in domains))
    print("Найдены домены:")
    for domain in clean_domains:
        print(domain)
    print(f"\nВсего: {len(clean_domains)} доменов")
    return clean_domains
if name == "__main__":
    domains = simple_domain_extraction("radio_stations.txt")