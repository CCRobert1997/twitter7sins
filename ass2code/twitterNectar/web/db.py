import couchdb
couch = couchdb.Server('http://admin:admin@103.6.254.57:5984')
db = couch['tweets_data']
rows = db.view('_all_docs', include_docs=True)
data = [row['doc'] for row in rows]
print(data)




def samplefunction():
    output = [{
        'name': 'John',
        'data': [5, 3, 4, 7, 2]
    }, {
        'name': 'Jane',
        'data': [2, 2, 3, 2, 1]}]
    return output
