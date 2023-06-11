// I will write here the code to be rendered
const express = require('express');
const app = express(); //instance of the espress app
app.use(express.json());
//define routes for your server like this
app.get('/', (req, res) => {
    res.send('Hello, World!');
  });
  const port = 3000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
