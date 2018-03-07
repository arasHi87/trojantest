import os

def run(**args):
    print "[*] In envirnoment module"
    return str(os.environ)