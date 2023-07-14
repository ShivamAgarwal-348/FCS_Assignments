#FCS Assignment 2, question 2.a
#Name: Shivam Agarwal
#Roll number: 2020123

import hmac
import base64
import hashlib

def verifyJwt(token, secret):

    signature = token.split('.')[2]
    payload = '.'.join(token.split('.')[:2])
    # print(payload)
    gen_sig_256 = base64.urlsafe_b64encode(hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).digest())
    gen_sig_512 = base64.urlsafe_b64encode(hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha512).digest())

    # print(signature)
    # print(gen_sig_256.decode('utf8').strip('='))
    # print(gen_sig_512.decode('utf8').strip('='))

    if signature == gen_sig_256.decode('utf8').strip('=') or signature == gen_sig_512.decode('utf8').strip('='):
        print('signature is valid')
        # print(token.split('.')[1])
        print(base64.b64decode(token.split('.')[1] + '==').decode('utf-8'))
    else:
        raise Exception("Signature is invalid")

# token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJhZG1pbiIsImVtYWlsIjoiYXJ1bkBpaWl0ZC5hYy5pbiIsImhpbnQiOiJsb3dlcmNhc2UtYWxwaGFudW1lcmljLWxlbmd0aC01In0.XYZudo71U6I_yMP6_qu_EVs-rdF0T9A2Rv8aj4lP-wLLN88-jASxMvSQunFhygiz4H4elM9D7aZZffKM_Dx0xw'
# secret = 'p1gzy'
verifyJwt(token, secret)