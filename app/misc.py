import requests
import cfg
from zipfile import ZipFile
import os

def download_csv(url, filename):

    with requests.Session() as s:
        with open( filename, 'wb') as fd:
            r = s.get(url)
            fd.write( r.content )
 
    return r.status_code

def unzip_file(zipped_file, dest_dir=os.getcwd()):

    with ZipFile(zipped_file, 'r') as z:
        z.extractall(dest_dir)

    return dest_dir

