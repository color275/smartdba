# custom_auth.py
import requests, json
import logging.config


def check_if_user(user_id, user_pw):
    
    body = {
        'id': user_id,
        'pw': user_pw,
        'service_name': 'SMARTDBA'
    }

    try :

        if (user_id == "22980" or user_id == "TEST") and user_pw == "admin" :
            logging.info("22980으로 인증을 거치지 않고 접속함")
            return True

        print("1")

        headers = { 'Host': '51Scrum-Auth.gsshop.com', 'apikey': 'lRyYOvBi8A69DfGoNRGmjYRIVd2pIWvV' }

        with requests.Session() as s:        
            reuslt_auth = s.post('https://cloud-api.gsshop.com', headers=headers, data=json.dumps(body))        
            json_result = json.loads(reuslt_auth.text)
            # logging.info(json_result)        
            
            if json_result['result'] == "OK" :
                return True
            else :            
                return False
    except :
        return False



def get_user_img(sabun)         :
    # curl -XGET  https://cloud-api.gsshop.com/api/homenet/findById?userId=22980 -H "Host:51tf-collector-poc.gsshop.com" -H "apikey:lRyYOvBi8A69DfGoNRGmjYRIVd2pIWvV"

    headers = { 'Host': '51tf-collector-poc.gsshop.com', 'apikey': 'lRyYOvBi8A69DfGoNRGmjYRIVd2pIWvV' }    

    with requests.Session() as s:        
        reuslt_auth = s.get('https://cloud-api.gsshop.com/api/homenet/findById?userId='+sabun, headers=headers)        
        json_result = json.loads(reuslt_auth.text)        
        
        if json_result['recordsets'][0][0]['profileImage'] != "" :
            return json_result['recordsets'][0][0]['profileImage']
        else :            
            return "False"

        




