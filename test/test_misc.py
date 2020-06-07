import sys
import os
sys.path.append(os.getcwd() + '/../app/')

from misc import *
import cfg

def test_download_csv():

    status = download_csv(cfg.download_url, cfg.download_file)

    assert status == requests.codes.ok

def test_unzip_file():

    download_csv( cfg.download_url, cfg.download_file )
    r = unzip_file( cfg.download_file)

    assert r == cfg.download_file

def test_load_to_kafka():
