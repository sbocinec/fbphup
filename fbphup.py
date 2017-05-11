#!/usr/bin/env python

"""
fbphup - Facebook photo uploader
"""

__author__ = "Stanislav Bocinec"
__copyright__ = "Copyright 2017, Stanislav Bocinec, svacko@gmail.com"
__license__ = "BSD 2-Clause"
__version__ = "0.0.2"
__maintainer__ = "Stanislav Bocinec"
__contact__ = "svacko@gmail.com"
__status__ = "Development"


import argparse
import facebook
import os
import requests
import sys
import yaml


def load_secret_file():
    with open('./secret.yml', 'r') as secret_file:
        try:
            return yaml.safe_load(secret_file)
        except yaml.YAMLError as exc:
            print(exc)


def fb_get_token(secret):
    if 'fb_access_token' in secret:
        return secret['fb_access_token']
    else:
        print("ERROR: fb_access_token not defined in secret.yml file. Exiting")
        sys.exit(1)


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


def fb_list_albums(graph):
    profile = graph.get_object("me")
    albums = graph.get_connections(profile['id'], 'albums')
    [display_album(graph, album) for album in albums['data']]


def fb_upload_photo(graph, album_id, photo_path, description):
    print("Facebook: Uploading Photo: {} Album ID: {} Description: {}".format(photo_path, album_id, description))
    graph.put_photo(image=open(photo_path, 'rb'), album_path=album_id + "/photos", message=description)


def main():
    parser = argparse.ArgumentParser(description='Facebook photo uploader')
    parser.add_argument('-a', '--action', choices=['list_albums', 'upload_photos', 'check_config'],
                        help='script action', required=True)
    parser.add_argument('-c', '--config', dest='config_file', action='store',
                        default='./config.yml',
                        help='configuration file path (default: ./config.yml)')
    args = parser.parse_args()

    if args.action == 'list_albums':
        secret = load_secret_file()
        fb_access_token = fb_get_token(secret)
        graph = facebook.GraphAPI(fb_access_token)
        fb_list_albums(graph)
    elif args.action == 'upload_photos':
        config = load_config(args.config_file)
        secret = load_secret_file()
        fb_access_token = fb_get_token(secret)
        graph = facebook.GraphAPI(fb_access_token)
        for photo in config['fb_album_photos']:
            fb_upload_photo(graph, config['fb_album_id'], os.path.join(config['fb_album_path'], photo['name']), photo['desc'])
    elif args.action == 'check_config':
        config = load_config(args.config_file)
        for photo in config['fb_album_photos']:
            photo_abs_path = os.path.join(config['fb_album_path'], photo['name'])
            if os.path.isfile(photo_abs_path):
                print("OK: {}, Desc: {}".format(photo_abs_path, photo['desc']))
            else:
                print("Not Found: {}".format(photo_abs_path))


if __name__ == "__main__":
    main()
