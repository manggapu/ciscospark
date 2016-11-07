from ciscospark import people
from ciscospark import rooms
from ciscospark import memberships
from ciscospark import messages
from ciscospark import teams
from ciscospark import team_memberships
from ciscospark import webhooks
import json


# set your user auth token
token = "INSERT YOUR USER AUTH TOKEN"


# sample request to Cisco Spark API
resp = people.list (token, email='devsupport@ciscospark.com')


# pretty format returned response
print json.dumps(resp, sort_keys=True, indent=4, separators=(',', ': '))
