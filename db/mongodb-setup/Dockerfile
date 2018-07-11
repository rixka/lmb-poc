FROM mvertes/alpine-mongo

RUN apk add --no-cache mongodb-tools

COPY cupcakes.json /cupcakes.json
COPY init.sh /init.sh
COPY init.js /init.js
#CMD mongoimport --host mongodb --db development --collection cupcakes --type json --file /cupcakes.json --jsonArray
CMD sh /init.sh
