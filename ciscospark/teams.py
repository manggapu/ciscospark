import requests
import json
import re
import common


# GET Requests
def list(token, max=0):
    headers = {'Authorization': common._sparktoken(token)}
    if max: payload = {'max': max}
    resp = requests.get(common._sparkurl('/teams'), params=payload, headers=headers)
    team_dict = json.loads(resp.text)
    team_dict['statuscode'] = str(resp.status_code)
    return team_dict


def get_details(token, teamId):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {'showSipAddress': 'true'}
    resp = requests.get(common._sparkurl('/teams/{:s}'.format(teamId)), params=payload, headers=headers)
    team_dict = json.loads(resp.text)
    team_dict['statuscode'] = str(resp.status_code)
    return team_dict


# POST Requests
def create(token, name):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'name': name}
    resp = requests.post(url=common._sparkurl('/teams'), json=payload, headers=headers)
    team_dict = json.loads(resp.text)
    team_dict['statuscode'] = str(resp.status_code)
    return team_dict


# PUTS
def update(token, teamId, name):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'name': name}
    resp = requests.put(url=common._sparkurl('/teams/{:s}'.format(teamId)), json=payload, headers=headers)
    team_dict = json.loads(resp.text)
    team_dict['statuscode'] = str(resp.status_code)
    return team_dict


# DELETES
def delete(token, teamId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/teams/{:s}'.format(teamId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
