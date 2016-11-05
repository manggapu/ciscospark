import requests
import json
import common

# GET Requests
def list(token, email='', displayName='', max=0):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {} 
    if email: payload['email'] = email
    if displayName: payload['displayName'] = displayName
    if max: payload['max'] = max
    resp = requests.get(common._sparkurl('/people'), params=payload, headers=headers)
    people_dict = json.loads(resp.text)
    people_dict['statuscode'] = str(resp.status_code)
    return people_dict


def get_details(token, personId):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/people/{:s}/'.format(personId)), headers=headers)
    person_detail_dict = json.loads(resp.text)
    person_detail_dict['statuscode'] = str(resp.status_code)
    return person_detail_dict


def get_me(token):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/people/me'), headers=headers)
    # print (resp.text)
    me_dict = json.loads(resp.text)
    me_dict['statuscode'] = str(resp.status_code)
    return me_dict
