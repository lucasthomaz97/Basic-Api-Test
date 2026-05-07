from requests import get
import pytest
import json

NAME = 'name'

def make_request(item, name):
    r = get(f"https://zelda.fanapis.com/api/{item}?name={name}")
    qdata = json.loads(r.text)
    response = qdata.get('data') 
    return qdata, response

@pytest.mark.parametrize("item,name",[("games","Zelda"),("staff","Shigeru Miyamoto")])
def test_validate_return(item, name):
    qdata, response = make_request(item, name)
        
    if qdata.get('success') == False:
        pytest.fail("Error:"+ str(qdata))
    
    if qdata.get('count') > 0:
        for i in response:
            if name not in i.get(NAME):
                pytest.fail('Inconsistent Data: '+NAME+':'+i.get(NAME)+'\n Expected: '+item+':'+name+' ')
    else:
        pytest.fail("No results returned"+ str(qdata))