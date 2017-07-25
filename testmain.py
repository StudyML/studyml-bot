# simple test codes

import json

result = json.loads('{"update_id":828873537,"message":{"message_id":21,"from":{"id":205357200,"first_name":"Cheong","last_name":"Lee","language_code":"ko-KR"},"chat":{"id":205357200,"first_name":"Cheong","last_name":"Lee","type":"private"},"date":1500854858,"text":"ASDF"}}')

print(result['update_id'])