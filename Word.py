
# Dictionary


import http.client
import json
import random
import time
from win10toast import ToastNotifier


def word():
    conn = http.client.HTTPSConnection("svnweb.freebsd.org")
    conn.request("GET", "/csrg/share/dict/words?view=co&content-type=text/plain")
    response = conn.getresponse()
    
    if response.status == 200:
        words = response.read().decode('utf-8').splitlines()
        random_word = random.choice(words)
        return random_word.strip()
def Dictionary():
    Words = word()
    conn = http.client.HTTPSConnection("api.dictionaryapi.dev")
    conn.request("GET", f"/api/v2/entries/en/{Words}")
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read().decode('utf-8')
        json_data = json.loads(data)
        

        random_entry = random.choice(json_data)
        random_word = random_entry['word']
        

        meanings = random_entry['meanings']
        if meanings:
            meaning = random.choice(meanings)['definitions'][0]
            
            return random_word, meaning
    
    return "Error", "No definition found"

# Running here :
if __name__ == "__main__":
    running = True
    while running:
        random_word, meaning = Dictionary()
        

        print(f"Random Word: {random_word}")
        print(f"Meaning: {meaning['definition']}")
    
        
    # notify
        notify = ToastNotifier()
        notify.show_toast(title=f"{random_word}",
                        msg=f"{meaning['definition']}",
                        icon_path="icon.ico",
                        duration=10)
        with open(file="Dictionary.txt",mode="+a") as Wordpad:
            Wordpad.write("\n\n")
            Wordpad.write("%s:%s\n" % (random_word,meaning['definition']))
            
        time.sleep(120) # You can Set The Time Here









# Contributions are Allowed ! 




