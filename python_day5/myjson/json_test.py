import json

customer = {'id': 12345, 'name':'chacha'}
# encoding
jsonString = json.dumps(customer, indent=4)
# 
print(jsonString)

#decoding
# jsonString = '{"name": "kim", "id": 152352, "history": [{"date":"2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
# dict = json.loads(jsonString)
# print(dict['name'])
# for h in dict['history']:
#     print(h['date'], h['item'])