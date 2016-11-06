from ciscospark import people
from ciscospark import rooms
from ciscospark import memberships
from ciscospark import messages
from ciscospark import teams
from ciscospark import team_memberships
from ciscospark import webhooks


# set your user auth token
token = "INSERT YOUR USER AUTH TOKEN"


# sample request to Cisco Spark API
resp = people.list (token, email='devsupport@ciscospark.com')


# pretty format returned response
for k, v in resp.iteritems():
    if isinstance(v, dict):
        print ("%s = " % k)
        for k in v:
            print ("\t" + k + " = " + str(v[k]))
    else:
            print (k + " = " + str(v))
