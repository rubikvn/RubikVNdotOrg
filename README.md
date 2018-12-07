# RubikVN.org

Source code for https://rubikvietnam.org/

## Getting involved
--------------------

Shoot me an email at <vttrung12@gmail.com> and tell me which part of the project you'd be interested in. Or simply clone this repo, make some changes, create a pull request. If approved, you will be invited to the team.

## Current progress
-------------------

* The website is temporarily unavailable for front-end remake and further development of our back-end. Any progress will be announced on this repository.
  * At the moment, our main focus is to design a user-friendly front-end.

### Implemented functions
-------------------------

* Ranking display of speedcubers from Vietnam for all categories.
* Login system via OAuth integration with WCA website.
* TravisCI has been set up for this repository, which means we need more testing!

## Running the server locally
-----------------------------

Make sure that your 8000 and 3306 port are clear (i.e no service on your computer is using it). Have [Docker and Docker compose](https://www.docker.com/) ready, whatever OS you're using. Clone this repository to your machine, cd into it, then run:

```bash
docker-compose up -d --build
```

Installation may take a while depending on your internet connection. After everything is done and you see 2 containers have been set up. Open your favorite browser and visit "localhost:8000/", you should see the index page of the website.
