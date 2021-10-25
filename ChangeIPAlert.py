import io,json,os
import requests
from bs4 import BeautifulSoup
from pushbullet import Pushbullet

class ChangeIPAlert():

    def __init__(self):
        self.load_parameters()

        ip = self.get_ip()
        if ip:
            if not ip == self._old_ip:
                print("The IP change from {} to {}".format(self._old_ip,ip))
                self.send_alert(ip)
                self.update_parameters(ip)


    def load_parameters(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.config_file = __location__+'/config.json'
        if(os.path.exists(self.config_file)):
            with open(self.config_file) as f:
                self.parameters = json.load(f)

                self._old_ip = self.parameters["IP"]
                self._api_key = self.parameters["APIKEY"]
            
            f.close()
        else:
            print("config.json does not exist")
            exit()


    def update_parameters(self,ip):
        self.parameters["IP"] = ip
        with open(self.config_file, "w") as jsonFile:
            json.dump(self.parameters, jsonFile)
        jsonFile.close()


    def get_ip(self):
        url = "https://www.whatsmyip.org/"

        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find_all('span')
            if results:
                ip = results[0].text
                return ip
        except Exception as err:
            print("Can't connect to {}".format(url))
            return
        
    def send_alert(self,ip):
        pb = Pushbullet(self._api_key)
        push = pb.push_note('Se actualizo la IP: {}'.format(ip), "Cambio de IP")

if __name__ == "__main__":
    alertas = ChangeIPAlert()