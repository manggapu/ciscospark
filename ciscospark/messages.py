import requests
import json
import mimetypes
from requests_toolbelt.multipart.encoder import MultipartEncoder
import re
import common


# GET Requests
def list(token, roomId, mentionedPeople='', before='', beforeMessage='', max=0):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {'roomId': roomId}
    if mentionedPeople: payload['mentionedPeople'] = mentionedPeople
    if before: payload['before'] = before
    if beforeMessage: payload['beforeMessage'] = beforeMessage
    if max: payload['max'] = max
    resp = requests.get(common._sparkurl('/messages'), params=payload, headers=headers)
    messages_dict = json.loads(resp.text)
    messages_dict['statuscode'] = str(resp.status_code)
    return messages_dict


def get_details(token, messageId):
    headers = {'Authorization': common._sparktoken(token)}
    resp = requests.get(common._sparkurl('/messages/{:s}'.format(messageId)), headers=headers)
    message_dict = json.loads(resp.text)
    message_dict['statuscode'] = str(resp.status_code)
    return message_dict


# POST Requests
def create(token, roomId='', toPersonId='', toPersonEmail='', text='', markdown='', files=''):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    payload = {}
    if roomId: payload['roomId'] = roomId
    if toPersonId: payload['toPersonId'] = toPersonId
    if toPersonEmail: payload['toPersonEmail'] = toPersonEmail
    if markdown: payload['markdown'] = markdown
    if text: payload['text'] = text
    if files:
        if re.match('.*://.*', files):
            # public URL files message
            payload['files'] = [files]
            resp = requests.post(url=common._sparkurl('/messages'), json=payload, headers=headers)
        else:
            # local files message
            filesbin = open(files, 'rb')
            filestype = mimetypes.guess_type(files)[0]
            payload['files'] = (files, filesbin, filestype)
            m = MultipartEncoder(fields=payload) # all payload dict is packaged and streamed
            headers['content-type'] = m.content_type 
            resp = requests.post(url=common._sparkurl('/messages'), data=m, headers=headers)
    else:
        # text message
        resp = requests.post(url=common._sparkurl('/messages'), json=payload, headers=headers)
    message_dict = json.loads(resp.text)
    message_dict['statuscode'] = str(resp.status_code)
    return message_dict


# DELETES
def delete(token, messageId):
    headers = {'Authorization': common._sparktoken(token), 'content-type': 'application/json'}
    resp = requests.delete(url=common._sparkurl('/messages/{:s}'.format(messageId)), headers=headers)
    del_dict = {'statuscode': str(resp.status_code)}
    return del_dict
