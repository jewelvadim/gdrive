from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


SECRETS_FILE = '/path/to/secrets.json'
CREDENTIALS_FILE = '/path/to/credentials.json'


gauth = GoogleAuth()
gauth.DEFAULT_SETTINGS['client_config_file'] = SECRETS_FILE

gauth.LoadCredentialsFile(CREDENTIALS_FILE)

if gauth.credentials is None:

    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:
    gauth.Refresh()

else:
    gauth.Authorize()

gauth.SaveCredentialsFile(CREDENTIALS_FILE)

gdrive = GoogleDrive(gauth)
