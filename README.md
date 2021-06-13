# Django api for board news


## Running The App

API running as a docker container. Make sure to have Docker and docker compose

```bash
docker-compose up
```

## Viewing The App
## posts
board_api/posts/
## specific post
board_api/posts/{int-number}
## comments
board_api/comments/
## specific comment 
board_api/comments/{int-number} 
## endpoint to upvote (Still under development)
board_api/posts/{specific_post ->int}/upvote  #endpoint to upvote (Still under development)

## Go to locally`http://127.0.0.1:8000`
## Go to on Heroku 'https://django-api-board-news.herokuapp.com/board_api/posts/'

 ## Test app with POSTMAN
 ## local
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/978fa84c22d3b8672b9d?action=collection%2Fimport)
## on heroku
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/978fa84c22d3b8672b9d?action=collection%2Fimport)
