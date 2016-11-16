import requests
import json
import re
import common


# GET Requests
def list(token, max=0):
    headers = {'Authorization': common._sparktoken(token)}
    payload = {}
    if max: payload['max'] = max
    resp = requests.get(common._sparkurl('/webhooks'), params=payload, headers=headers)
    webhook_dict = json.loads(resp.text)
    webhook_dict['statuscode'] = str(resp.status_code)
    return webhook_dict


def get_details(token, webhookId):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/webhooks/{:s}'.format(webhookId)), headers=headers)
    webhook_dict = json.loads(resp.text)
    webhook_dict['statuscode'] = str(resp.status_code)
    return webhook_dict


# POST Requests
def create(token, name, targetUrl, resource, event, secret, filter=''):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'name': name, 'targetUrl': targetUrl, 'resource': resource, 'event': event, 'secret': secret}
    if filter: payload['filter'] = filter 
    resp = requests.post(url=common._sparkurl('/webhooks'), json=payload, headers=headers)
    webhook_dict = json.loads(resp.text)
    webhook_dict['statuscode'] = str(resp.status_code)
    return webhook_dict


# PUTS
def update(token, webhookId, name, targetUrl):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'name': name, 'targetUrl': targetUrl}
    resp = requests.put(url=common._sparkurl('/webhooks/{:s}'.format(webhookId)), json=payload, headers=headers)
    webhook_dict = json.loads(resp.text)
    webhook_dict['statuscode'] = str(resp.status_code)
    return webhook_dict


# DELETES
def delete(token, webhookId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/webhooks/{:s}'.format(webhookId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
