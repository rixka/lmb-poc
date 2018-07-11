use development;
db.createCollection('ratings')
db.cupcakes.createIndex({ name: 'text', artist: 'text' });
