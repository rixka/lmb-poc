# Little Mama’s Bakery

[![Build Status](https://travis-ci.org/rixka/lmb-poc.svg?branch=master)](https://travis-ci.org/rixka/lmb-poc)

### Customer Overview
Little Mama’s Bakery [LMB] is a British multinational bakery company headquartered in Edinburgh, United Kingdom.
It has about 33 million customers across 16 countries. In the United Kingdom, LMB  is the largest general bakery
and a leading cupcakes provider. In addition, LMB has a focus on five markets in Europe and in Asia, the company
is focused on the growth markets of China and South-East Asia. LMB is also the second largest general bakery in Canada.


### Customer Background
Their applications are currently constantly prone to outages due to lack of redundancy and high-availability.
The software is also very slow to run. Mama’s Little Bakery has been going through a period of significant growth
and transformation, and as part of the expansion a significant IT budget has been allocated to ramp up the company IT presence.

They enlisted Cloudreach’s help to help guide them during this transformation and provide Agile Coaching and best practices.
Initially, we have been tasked to redesign the backend API for their Cupcake service as a proof of concept. If successful,
LMB will support a project for the complete re-architecture. This will be a big win for Cloudreach, never before have
we worked with a customer as globally recognised as Little Mama’s Bakery.

#### Dependencies

_Note: This project assumes **virtualenv**, **docker**, and **docker-compose** are installed locally._

Virtual env can be installed with pip:
```
pip install virtualenv
```

To install [Docker](https://docs.docker.com/install) and [Docker Compose](https://docs.docker.com/compose/install/) please review the appropriate documentation.


### Task List
* Greengrass development project, concept -> deployment
* Python development for applications and scripting
* RESTful API development
* Continuous Delivery and Continuous Integration
* Building and updating deployment pipelines
* Investigate docker or serverless solutions


### Requirements Specification
* Use python with Flask
* Database for storing data provided in the file `cupcakes.json`
* All routes should return a valid json dictionary
* Test Driven Development
* Follow the KISS principle
* Provide all instructions for an easy setup
* Please take into consideration that the number of cupcakes and ratings will grow to millions of documents as well as the number of users using the API


### API Considerations
* GET `/cupcakes`
	* Returns a list of cupcakes with some details on them
	* Add possibility to paginate cupcakes.
* GET `/cupcakes/search`
	* Takes in parameter a 'message' string to search.
	* Return a list of cupcakes. The search should take into account cupcakes flavour and name. The search should be case insensitive.
* POST `/cupcakes/rating`
	* Takes in parameter a "cupcake_id" and a "rating"
	* This call adds a rating to the cupcake. Ratings should be between 1 and 5.
* GET `/cupcakes/rating/<rating_id>`
	* Takes in parameter a "rating_id" and returns the document
* GET `/cupcakes/avg/rating/<cupcake_id>`
	* Returns the average, the lowest and the highest rating of the given cupcake id.


### Quick Start with Docker

```shell
make docker-up
make docker-logs

# Kill with fire
make docker-down
```

Or if preferred:
```shell
docker-compose build
docker-compose up

# Kill with fire
docker-compose down
```

Once the API container is running you can curl requests or navigate with the browser `http://localhost:5000/cupcakes`.

#### Example - curl
```
curl -v http://localhost:5000/cupcakes

# example id
curl -v "http://localhost:5000/cupcakes?last-id=5aae8dd659b58a3eb2973b6c"
```


### Quick testing
```shell
make test
```

Or if preferred:
```shell
python setup.py test
```

All tests are run using pytest:
```shell
pytest -vvra tests
```

### Quick cleaning with Docker
```shell
docker rm `docker ps -aq`
docker volume rm `docker volume ls -q -f dangling=true`
docker rmi `docker images --filter "dangling=true" -q --no-trunc`
```

_Note: More information available [here](https://gist.github.com/bastman/5b57ddb3c11942094f8d0a97d461b430)._

