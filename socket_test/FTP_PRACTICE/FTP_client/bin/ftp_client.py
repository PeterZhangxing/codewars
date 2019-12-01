#!/usr/bin/python3.5

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import client

if __name__ == "__main__":
    client_obj = client.FTPClient()
    client_obj.inter_active()