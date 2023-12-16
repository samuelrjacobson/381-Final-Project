Find movie commentary/reviews through YouTube API, full descriptions and in different languages.

FastAPI program has 4 methods:
* First one accepts no arguments and returns "Hello, world".
* Second accepts movie title as input and outputs a list of 10 YouTube videos of review/commentary on the movie.
 The information about the video should be id, title, and description for each.
* Third accepts YouTube video id and returns the full description of that video.
* Fourth accepts a language code (e.g., 'fr', 'de') and a movie title, converts the movie title to that language,
 and outputs a list of 10 YouTube videos of review/commentary on the movie (presumedly in the specified language)
 The information about the video should be id, title, and description for each.


Instructions:
* Clone repository in terminal and cd into it.
* In terminal, type: python3 -m pip install -r requirements.txt

To run:
* In terminal, type: uvicorn main:app --reload
* Open in browser, and change url to http://127.0.0.1:8000/docs
* Open the method you wish to use, Try it out, enter values, Execute

To test:
* Type pytest --cov=.