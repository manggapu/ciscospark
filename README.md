# ciscospark
Welcome to the Python SDK for Cisco Spark API

Build notes:
- Tested on Python 2.7
- Requires pip install requests
- Requires pip install requests-toolbelt

Features:
- Maps exactly to all functions and parameters of the 7 main APIs 
- These include people, rooms, messages, teams, memberships, team memberships, webhooks
- To check if a parameter is mandatory / optional, go to each API Reference link below

sample.py shows you how to start using ciscospark today!

------------------------------------------------------------

https://developer.ciscospark.com/resource-people.html  
- people.get_details (token, personId)  
- people.get_me (token)  
- people.list (token, email='', displayName='', max=0)  

https://developer.ciscospark.com/resource-rooms.html  
- rooms.create (token, title, teamId='')  
- rooms.delete (token, roomId)  
- rooms.get_details (token, roomId)  
- rooms.list (token, teamId='', max=0, type='')  
- rooms.update (token, roomId, title)  

https://developer.ciscospark.com/resource-memberships.html  
- memberships.create (token, roomId, personId='', personEmail='', isModerator=False)  
- memberships.delete (token, membershipId)  
- memberships.get_details (token, membershipId)  
- memberships.list (token, roomId='', personId='', personEmail='', max=0)  
- memberships.update (token, membershipId, isModerator)  

https://developer.ciscospark.com/resource-messages.html  
- messages.create (token, roomId='', toPersonId='', toPersonEmail='', text='', markdown='', files='')  
- messages.delete (token, messageId)  
- messages.get_details (token, messageId)  
- messages.list (token, roomId, mentionedPeople='', before='', beforeMessage='', max=0)  

https://developer.ciscospark.com/resource-teams.html  
- teams.create (token, name)  
- teams.delete (token, teamId)  
- teams.get_details (token, teamId)  
- teams.list (token, max=0)  
- teams.update (token, teamId, name)  

https://developer.ciscospark.com/resource-team-memberships.html  
- team_memberships.create (token, teamId, personId='', personEmail='', isModerator=False)  
- team_memberships.delete (token, membershipId)  
- team_memberships.get_details (token, membershipId)  
- team_memberships.list (token, teamId, max=0)  
- team_memberships.update (token, membershipId, isModerator)  

https://developer.ciscospark.com/resource-webhooks.html  
- webhooks.create (token, name, targetUrl, resource, event, secret, filter='')  
- webhooks.delete (token, webhookId)  
- webhooks.get_details (token, webhookId)  
- webhooks.list (token, max=0)  
- webhooks.update (token, webhookId, name, targetUrl)  
