# fbphup - Facebook Photo upload script

## Requirements

* python3
* [Facebook Python SDK](https://github.com/mobolic/facebook-sdk)
* Facebook Developer account

## Install

- Create a Facebook developer account using [Facebook developers portal](https://developers.facebook.com/)
- Generate new User Access token using [Graph API explorer](https://developers.facebook.com/tools/explorer):
  - Application: *Graph API Explorer*
  - Click on *Get Token* -> *Get User Access Token*
  - Select *User Data Permissions*:
    - *publish_actions*
    - *user_photos*
  - Click *Get Access Token*
  - Copy the token from *Access Token* field into a local *secret.yml* file in following format:
    - `access_token: 'skdjsaljlejwijwioejwioejqwoejwqioejwoqijewqoiejwqoiejqw'`
  - Run the script

# Author
* Stanislav Bocinec
* svacko@gmail.com

# License
The software is licensed under [BSD-2-Clause license](https://opensource.org/licenses/BSD-2-Clause)
