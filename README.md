# fbphup - Facebook Photo upload script

## Requirements

* python3
* [Facebook Python SDK](https://github.com/mobolic/facebook-sdk)
* Facebook Developer account

## Install

- (optional) Create a *fbphup* python virtual environment, i.e.: `python3 -m venv fbphup`
- (optional) Activate the virtualenv environment: `source fbphup/bin/activate`
- Install the script dependencies: `pip install -r requirements`
- Run the *fbphup.py* script

## Usage

### Upload photos to Facebook Album
1. Create a Facebook Developer account
2. Create Facebook Album in your Facebook profile manually
3. Find out the new Album ID. You can use `fbphup.py -a list_albums` feature to display all your albums and its IDs.
4. Generate YAML file describing your album. Read attached Album YAML file example.
5. Generate a temporary Facebook User Access token
6. Run the upload script: `fbphup.py -a upload_photos -c myalbum.yml`

### Album YAML file example
```
fb_album_id: '1234567890'
fb_album_name: 'Album name'
fb_album_path: 'Full path to the directory containing photos'
fb_album_desc: 'Album description text'
fb_album_photos:
  - name: Photo001.jpg
    desc: Photo001 Description text
  - name: Photo002.jpg
    desc: Photo 002 Description text
```
### Create a Facebook Developer account

Follow the steps on the [Facebook App Development portal](https://developers.facebook.com/docs/apps/register#developer-account). Basically following is needed:
1. Login to your personal Facebook account
2. Register your Facebook account as a developer account using https://developers.facebook.com/docs/apps/register#

### Generate Facebook User Access token

Generate new User Access token using [Graph API explorer](https://developers.facebook.com/tools/explorer):
- Application: *Graph API Explorer*
- Click on *Get Token* -> *Get User Access Token*
- Select *User Data Permissions*:
  - *publish_actions*
  - *user_photos*
- Click *Get Access Token*
- Copy the token from *Access Token* field into a local *secret.yml* file in following format:
  - `fb_access_token: 'abcedfghijklmnopqrstuvwxyz'`

## TODO
* ability to create a facebook album
* error handling
* logging

# Author

* Stanislav Bocinec
* svacko@gmail.com

# License

The software is licensed under [BSD-2-Clause license](https://opensource.org/licenses/BSD-2-Clause)
