require('dotenv').config({ path: './w3s-dynamic-storage/.env' })
const path = require('path');
const express = require('express');

const app = express();

app.use(express.static('dist'));
app.use(express.json());

app.get('/api/hello', async (req, res) => {
  res.send('Hello world');
});

const clientApp = express();
clientApp.use(express.static('dist'));
clientApp.use(express.json());

clientApp.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, '../../dist', 'index.html'));
});


app.listen(process.env.PORT || 3000, () => console.log(`Listening on port ${process.env.PORT || 3000}!`));

if (process.env.NODE_ENV !== 'development') {
  clientApp.listen(8000, () => console.log('client listening on port 8000'));
}
