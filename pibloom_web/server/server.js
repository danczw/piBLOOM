const axios = require('axios');
const bodyParser = require('body-parser');
const cors = require('cors');
const dotenv = require("dotenv")
const express = require('express');
const morgan = require('morgan');
const path = require('path');

dotenv.config();

const api_url = process.env.API_URL;
const express_port = process.env.EXPRESS_PORT;
const webapp_path = path.join(__dirname, '..', '/dist/');
const app = express();

app.use(bodyParser.json());
app.use(cors());
app.use(express.static(webapp_path));
app.use(morgan('combined'));

// root path serving vue app
app.get('/', (req, res) => {
    res.sendFile(path + 'index.html');
});

// test path
app.get('/hello/', (req, res) => {
    res.json({
        data: 'Hello World'
    });
});

// BLOOM model serving path
app.post('/chat/', (req, res) => {

    const headers = {
        "Content-Type": "application/json",
    };

    axios
        .post(
            api_url + '/chat/', // data POST url
            { content: req.body.content }, // data to be sent,
            { headers }
        )
        .then(function (response) {
            res.json({
                data: response.data.data
            });
        })
        .catch(function (error) {
            res.json({
                data: 'Error! Could not reach the API. ' + error
            });
        });
});

app.listen(express_port, () => {
    console.log(`Server started on port ${express_port}`);
})
