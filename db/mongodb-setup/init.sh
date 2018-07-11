#!/bin/bash

mongoimport --host mongodb --db development --collection cupcakes --type json --file /cupcakes.json --jsonArray
mongo --host mongodb < init.js
