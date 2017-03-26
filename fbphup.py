#!/usr/bin/env python

"""
fbphup - Facebook photo uploader
"""

__author__ = "Stanislav Bocinec"
__copyright__ = "Copyright 2017, Stanislav Bocinec, svacko@gmail.com"
__license__ = "BSD 2-Clause"
__version__ = "0.0.1"
__maintainer__ = "Stanislav Bocinec"
__contact__ = "svacko@gmail.com"
__status__ = "Development"


import argparse
import facebook
import os
import requests
import sys
import yaml


class FbAlbum():
    def __init__(self, config):
            self.fb_album_id = None
            self.fb_album_name = None
            self.fb_album_path = None
            self.fb_album_desc = None
            self.fb_album_photos = []

def load_secret():
    with open('./secret.yml', 'r') as secret_file:
        try:
            return yaml.safe_load(secret_file)
        except yaml.YAMLError as exc:
            print(exc)


def load_config(config):
    with open(config, 'r') as config_file:
        try:
            return yaml.safe_load(config_file)
        except yaml.YAMLError as exc:
            print(exc)


def display_album(graph, album):
    print("Album: {}. ID: {}".format(album['name'], album['id']))
    try:
        album_details = graph.get_object(album['id'])['description']
        print("Desc: {}".format(album_details))
    except KeyError:
        print("Desc: --")


def list_albums(graph):
    profile = graph.get_object("me")
    albums = graph.get_connections(profile['id'], 'albums')
    [display_album(graph, album) for album in albums['data']]


def upload_photo(graph, album_id, photo_path, description):
    print("Uploading Foto: {} Album ID: {} Description: {}".format(photo_path, album_id, description))
    graph.put_photo(image=open(photo_path, 'rb'), album_path=album_id + "/photos", message=description)


def main():
    parser = argparse.ArgumentParser(description='Facebook photo uploader')
    parser.add_argument('-a', '--action', choices=['list_albums', 'upload_photos'],
                        help='script action', required=True)
    parser.add_argument('-c', '--config', dest='config_file', action='store',
                        default='./config.yml',
                        help='configuration file path (default: ./config.yml)')
    args = parser.parse_args()


    secret = load_secret()
    if 'access_token' in secret:
        access_token = secret['access_token']
    else:
        print("access_token not defined in secret.yml file. Exiting")
        sys.exit(1)

    graph = facebook.GraphAPI(access_token)
    # Album: UPTEST. ID: 10155163793496952

    if args.action == 'list_albums':
        list_albums(graph)
    elif args.action == 'upload_photos':
        config = load_config(args.config_file)
        for photo in config['fb_album_photos']:
        #album_id = '10155163793496952'
            upload_photo(graph, config['fb_album_id'], os.path.join(config['fb_album_path'], photo['name']), photo['desc'])


if __name__ == "__main__":
    main()
