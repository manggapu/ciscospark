from ciscospark import people,rooms,memberships,messages,teams,team_memberships,webhooks

token = "INSERT YOUR USER AUTH TOKEN"

# get details of the basic Sparky bot entity
print people.get_details(token, email='devsupport@ciscospark.com')

# format the returned response
resp_dict = rooms.list(at, max=2)['items']
for x in resp_dict:
    for y in x:
        print y + " = " + str(x[y])
    print ""
