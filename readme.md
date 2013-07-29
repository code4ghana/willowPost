Hello peeps,


Here is the sample post project very simple in nature.
It utilizes the django-rest-framework to make extending/adding and exposing new models via rest easier.

lemme know if you have any questions



sample requests

curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/posts


curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/posts/

curl -X POST -d '{"title":"booyaaaa","content":"testing","author":1}' -H 'Content-Type:application/json'  http://127.0.0.1:8000/posts/



curl -X POST -d '{"title":"booyaaaa","content":"testing","author":1}' -H 'Content-Type:application/json'  http://127.0.0.1:8000/


curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/authors/
