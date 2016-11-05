from ciscospark import people
from ciscospark import rooms
from ciscospark import memberships
from ciscospark import messages
from ciscospark import teams
from ciscospark import team_memberships
from ciscospark import webhooks


# set your user auth token
token = "INSERT YOUR USER AUTH TOKEN"


# list people with a certain email address
resp = people.list (token, email='devsupport@ciscospark.com')


# pretty format returned response
resp_dict = resp['items']
for x in resp_dict:
    for y in x:
        print y + " = " + str(x[y])
    print ""
