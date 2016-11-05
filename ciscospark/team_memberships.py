import requests
import json
import re
import common


# GET Requests
def list(token, teamId, max=0):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {}
    if teamId: payload['teamId'] = teamId
    if max: payload['max'] = max
    resp = requests.get(common._sparkurl('/team/memberships'), params=payload, headers=headers)
    team_membership_dict = json.loads(resp.text)
    team_membership_dict['statuscode'] = str(resp.status_code)
    return team_membership_dict


def get_details(token, membershipId):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/team/memberships/{:s}'.format(membershipId)), headers=headers)
    team_membership_dict = json.loads(resp.text)
    team_membership_dict['statuscode'] = str(resp.status_code)
    return team_membership_dict


# POST Requests
def create(token, teamId, personId='', personEmail='', isModerator=False):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'teamId': teamId}
    if personId: payload['personId'] = personId
    if personEmail: payload['personEmail'] = personEmail
    if isModerator: payload['isModerator'] = isModerator
    resp = requests.post(url=common._sparkurl('/team/memberships'), json=payload, headers=headers)
    team_membership_dict = json.loads(resp.text)
    team_membership_dict['statuscode'] = str(resp.status_code)
    return team_membership_dict


# PUTS
def update(token, membershipId, isModerator):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'isModerator': isModerator}
    resp = requests.put(url=common._sparkurl('/team/memberships/{:s}'.format(membershipId)), json=payload, headers=headers)
    team_membership_dict = json.loads(resp.text)
    team_membership_dict['statuscode'] = str(resp.status_code)
    return team_membership_dict


# DELETES
def delete(token, membershipId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/team/memberships/{:s}'.format(membershipId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
