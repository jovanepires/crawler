from threading import Thread
from requests import Request, Session
from bs4 import BeautifulSoup
import time
import re

class FindAnswer(Thread):
    def run():
        try:
            s = Session()
            endpoint = 'http://applicant-test.us-east-1.elasticbeanstalk.com/'

            get = Request('GET', endpoint)
            get_prepped = s.prepare_request(get)

            # Merge environment settings into session
            get_settings = s.merge_environment_settings(get_prepped.url, None, None, None, None)
            get_resp = s.send(get_prepped, **get_settings)

            ## Get token value
            soup = BeautifulSoup(get_resp.text, "html.parser")
            token = soup.find("input", {"id": "token"}).get("value")
            new_token = ""
            replacements = {"a": "z","b": "y","c": "x","d": "w","e": "v","f": "u","g": "t","h": "s","i": "r","j": "q","k": "p","l": "o","m": "n","n": "m","o": "l","p": "k","q": "j","r": "i","s": "h","t": "g","u": "f","v": "e","w": "d","x": "c","y": "b","z": "a"}

            for i in range(len(token)):
                if token[i] in replacements.keys():
                    new_token += replacements[token[i]]
                else:
                    new_token += token[i]

            # Get response text of page submit
            post = Request('POST', endpoint, data={ "token" : new_token })
            post_prepped = s.prepare_request(post)

            # Merge environment settings into session
            post_settings = s.merge_environment_settings(post_prepped.url, None, None, None, None)
            post_resp = s.send(post_prepped, **post_settings)

            # Print only response
            answer = re.sub(r'<[/]?(.*?)>', '',   post_resp.text)
            print(answer)

            time.sleep(0.1)

        except: 
            raise Exception('An error occured here.')
 
if __name__ == '__main__':
    FindAnswer.run()
