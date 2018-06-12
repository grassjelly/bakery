var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
//either use cloud service port or local port:3000
var port = process.env.PORT || 8000;
var bodyParser = require("body-parser");

server.listen(port, function() {
    console.log('Server listening at port %d', port);
});

io.sockets.on('connection', function(socket) {
    socket.emit("hello", "Hello from Server");
    socket.on("hello", function(data) {
        console.log(data);
    });
});

app.use(express.static(__dirname));

app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(bodyParser.json());

app.post('/sensors', function(req, res) {
    /*
    http://localhost:8000/sensors
    {
    "sensor" : 1,
    "value" : 256
    }
    */
    var sensor = req.body.type;
    var value = req.body.value;

    io.emit("sensors", req.body);

    console.log(req.body);

    res.end("ok");
});