import io,json,os
import public_ip as ip
from pushbullet import Pushbullet

class ChangeIPAlert():

    def __init__(self):
        self.load_parameters()

        new_ip = ip.get()
        if new_ip:
            if not new_ip == self._old_ip:
                print("The IP change from {} to {}".format(self._old_ip,new_ip))
                self.update_dns()
                self.send_alert(new_ip)
                self.update_parameters(new_ip)


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

    def update_dns(self):
        import requests
        res = requests.get(self._url)

    def send_alert(self,ip):
        pb = Pushbullet(self._api_key)
        push = pb.push_note('Se actualizo la IP: {}'.format(ip), "Cambio de IP")
        

if __name__ == "__main__":
    alertas = ChangeIPAlert()