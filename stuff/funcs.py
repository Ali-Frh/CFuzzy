import json
import os

settings_path = ".cfuzzy.conf"

## data template
template = {
    "svport":           "2500",
    "cfip":             "162.159.135.42",
    "cfport":           "443",
    "l_fragment":       "77",
    "fragment_sleep":   "0.2",
    "my_socket_timeout":"60",
    "first_time_sleep": "0.01",
    "accept_time_sleep":"0.01",
    "randfrag":         False
}



def load_settings():
    if os.path.exists(settings_path):
        z = open(settings_path,"r")
        data = z.read()
        z.close()

        ## check file corruption
        try:
            loaded_data = json.loads(data)
            return loaded_data
        except:
            print("Corrupted Data")
            return template
    else:
        return template

def save_settings(data):
    z = open(settings_path,"w")
    z.write(json.dumps(data))
    z.close()
    return True
