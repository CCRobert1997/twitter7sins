from searchtweets import ResultStream, gen_rule_payload, load_credentials

premium_search_args=load_credentials(filename="harvest/creds.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)


rule = gen_rule_payload("place:melbourne lang:en",results_per_call=100) # testing with a sandbox account
print(rule)

from searchtweets import collect_results



import couchdb

couch = couchdb.Server('http://admin:admin@127.0.0.1:5984')
print("Connect succeed")

try:
    db = couch['testnew']
except:
    db = couch.create('testnew')


print("Doc create succeed")
#db = couch.create('test')
#db = couch['test']




tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)
print("Tweet collected succeed")
data_to_couch=[]
for i in range(len(tweets)):
    data_to_couch.append({})

i=0
for t in tweets:
    data_to_couch[i]['id']=t.id
    i+=1

for js in data_to_couch:
    db.save(js)

