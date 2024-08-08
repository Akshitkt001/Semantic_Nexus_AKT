db = db.getSiblingDB("my_database");  // Use your database name

// Create a new collection with sample data
db.my_collection.insertMany([
  { name: "Item 1", value: "Value 1" },
  { name: "Item 2", value: "Value 2" },
  { name: "Item 3", value: "Value 3" }
]);

// Create an index if necessary
db.my_collection.createIndex({ name: 1 });
