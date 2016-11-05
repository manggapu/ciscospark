import requests
import json
import re
import common


# GET Requests
def list(token, roomId='', personId='', personEmail='', max=0):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {}
    if roomId: payload['roomId'] = roomId
    if personId: payload['personId'] = personId
    if personEmail: payload['personEmail'] = personEmail
    if max: payload['max'] = max
    resp = requests.get(common._sparkurl('/memberships'), params=payload, headers=headers)
    membership_dict = json.loads(resp.text)
    membership_dict['statuscode'] = str(resp.status_code)
    return membership_dict


def get_details(token, membershipId):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/memberships/{:s}'.format(membershipId)), headers=headers)
    membership_dict = json.loads(resp.text)
    membership_dict['statuscode'] = str(resp.status_code)
    return membership_dict


# POST Requests
def create(token, roomId, personId='', personEmail='', isModerator=False):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'roomId': roomId}
    if personId: payload['personId'] = personId
    if personEmail: payload['personEmail'] = personEmail
    if isModerator: payload['isModerator'] = isModerator
    resp = requests.post(url=common._sparkurl('/memberships'), json=payload, headers=headers)
    membership_dict = json.loads(resp.text)
    membership_dict['statuscode'] = str(resp.status_code)
    return membership_dict


# PUTS
def update(token, membershipId, isModerator):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'isModerator': isModerator}
    resp = requests.put(url=common._sparkurl('/memberships/{:s}'.format(membershipId)), json=payload, headers=headers)
    membership_dict = json.loads(resp.text)
    membership_dict['statuscode'] = str(resp.status_code)
    return membership_dict


# DELETES
def delete(token, membershipId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/memberships/{:s}'.format(membershipId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
