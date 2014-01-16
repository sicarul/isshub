
import requests
import json

def get_token():
    with open ("mytoken.txt", "r") as myfile:
        token=myfile.read().replace('\n', '')
    return token


def create_issue(reponame, issname, issdesc):

  token = get_token()

  payload = {'title': issname, 'body': issdesc}

  try:
    r = requests.post('https://api.github.com/repos/' + reponame + '/issues',
        headers={'Authorization': 'token ' + token},
        data=json.dumps(payload),
            timeout=45
        )

    if r.status_code == 200:
      return 'Ok'
    else:
      return r.text['message']
  except requests.exceptions.RequestException as e:
    return "Connection error"