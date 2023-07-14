#FCS Assignment 2, question 2.b
#Name: Shivam Agarwal
#Roll number: 2020123
import jwt

def get_secret(payload, signature):
  alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyz'

  for i in alphanumeric:
    for j in alphanumeric:
      for k in alphanumeric:
        for l in alphanumeric:
          for m in alphanumeric:

            key = i+j+k+l+m
            key='p1gzy'
            b = jwt.encode(payload, key, algorithm='HS256').split('.')[2]
            # print(key)
            # print(b)
            if b == signature:
              return key

payload = {
              "sub": "fcs-assignment-1",
              "iat": 1516239022,
              "exp": 1672511400,
              "role": "user",
              "email": "arun@iiitd.ac.in",
              "hint": "lowercase-alphanumeric-length-5"
            }

key = get_secret(payload,'LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI')
print(key)

a = jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI" , key, algorithms='HS256')
print(a)
a['role'] = 'admin'
print(a)
c = jwt.encode(a, key,algorithm='HS256')
print(c)

