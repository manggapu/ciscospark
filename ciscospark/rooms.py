import requests
import json
import re
import common


# GET Requests
def list(token, teamId='', max=0, type=''):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {}
    if teamId: payload['teamId'] = teamId
    if max: payload['max'] = max
    if type: payload['type'] = type
    resp = requests.get(common._sparkurl('/rooms'), params=payload, headers=headers)
    room_dict = json.loads(resp.text)
    room_dict['statuscode'] = str(resp.status_code)
    return room_dict


def get_details(token, roomId):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {'showSipAddress': 'true'}
    resp = requests.get(common._sparkurl('/rooms/{:s}'.format(roomId)), params=payload, headers=headers)
    room_dict = json.loads(resp.text)
    room_dict['statuscode'] = str(resp.status_code)
    return room_dict


# POST Requests
def create(token, title, teamId=''):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'title': title}
    if teamId: payload['teamId'] = teamId
    resp = requests.post(url=common._sparkurl('/rooms'), json=payload, headers=headers)
    room_dict = json.loads(resp.text)
    room_dict['statuscode'] = str(resp.status_code)
    return room_dict


# PUTS
def update(token, roomId, title):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'title': title}
    resp = requests.put(url=common._sparkurl('/rooms/{:s}'.format(roomId)), json=payload, headers=headers)
    room_dict = json.loads(resp.text)
    room_dict['statuscode'] = str(resp.status_code)
    return room_dict


# DELETES
def delete(token, roomId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/rooms/{:s}'.format(roomId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
