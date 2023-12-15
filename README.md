Find movie commentary/reviews through YouTube API, full descriptions and in different languages.

(Issue 2: Currently, program should accept movie title as input,
 and output a list of 10 YouTube videos of review/commentary on the movie.
 The information about the video should be id, title, and description for each.)

To run:
* Clone repository.
* In terminal, install fastapi, uvicorn, google-api-python-client
* In terminal, type: uvicorn main:app --reload
* Open in browser, and change url to http://127.0.0.1:8000/docs

To test:
* Install pytest, pytest-mock, pytest-cov
* Type pytest --cov=.