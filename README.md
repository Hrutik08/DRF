# DRF
Django Rest Framework

Till gs19 superuser login is admin - admin
gs20: 
superuser login is superuser - superuser
user1 - superuser
admin - superuser


gs22 : superuser - superuser

gs24 : superuser - superuser
user1 - superuser

gs28 : 
get : http http://127.0.0.1:8000/studentapi/ "Authorization: Token 26a96d65b053dc9e80c8377e21e38451c8226b3f"

post : http -f POST http://127.0.0.1:8000/studentapi/ name=Amit roll=2 city=Thane "Authorization: Token 26a96d65b053dc9e80c8377e21e38451c8226b3f"

put : PUT http://127.0.0.1:8000/studentapi/3/ name=Amir roll=3 city=Thane "Authorization: Token 
26a96d65b053dc9e80c8377e21e38451c8226b3f"


gs30 :
http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"

http POST http://127.0.0.1:8000/verifytoken/ token="token string"

http POST http://127.0.0.1:8000/refreshtoken/ refresh="refesh token string"