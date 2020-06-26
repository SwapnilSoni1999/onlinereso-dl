from requests import Session
import re
from os.path import join

class Client(Session):
    def __init__(self):
        super().__init__()
        self.headers.update({
            'x-csrf-token': 'VxqYmUWJegXRXF71tx6Iwr0D28zwnk2WOJpMM1Lh',
            'x-requested-with': 'XMLHttpRequest'
        })

    def login(self, uid, pswd):
        """ Authenticates with onlinereso.in with your credentials. """
        token = "VxqYmUWJegXRXF71tx6Iwr0D28zwnk2WOJpMM1Lh"
        payload = {
            '_token': token,
            'user_name': str(uid),
            'password': str(pswd)
        }
        res = self.post('https://www.onlinereso.in/ajaxLogin', data=payload)
        if 'coursekart_session' in res.cookies.get_dict():
            print("Login Successful!")
        else:
            print("[WARN] issues with login...")
            exit(-1)

    def __extract_note_id(self, note_url: str):
        try:
            note_id = re.search(r"https?.+onlinereso.in\/note\/(.+)", note_url).group(1)
            if note_id:
                return note_id
            else:
                print("[Err] Not a onlinereso.com url! exiting...")
                exit(-1)
        except:
            print("Not a notes url!! please fix your notes file")
            exit(-1)
            
    def get_note_id(self, note_url: str):
        """ Extracts note id from given url """
        note_id = self.__extract_note_id(note_url)
        return note_id
    
    def download(self, note_id, output_path):
        """ Downloads note (Login credentials are required!) """
        res = self.get('https://onlinereso.in/api/getEbook', params={ 'note_id': note_id })
        filepath = join(output_path, note_id + ".pdf")
        open(filepath, 'wb').write(res.content)
        print("=" * 20)
        print("Download Completed!")
        print(f"Filename: {note_id}.pdf")
        print(f"Saved in: {filepath}")
        print("=" * 20)
