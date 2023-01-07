# checks if a valid configuration .yaml exists
# if not found, creates a config file with default values

import os
import json

class configcheck:

    def __init__(self):
        return

    def check(*args):

        cfgfile = 'config.json'

        if not os.path.exists(cfgfile):
            print(' : config.yaml not found, creating new file with default values \n')

            default = {
                "currency": "dollars",
            }
            with open (cfgfile, "w") as outfile:
                json.dump(default, outfile)
        else:
            print(' : config.json exists \n')