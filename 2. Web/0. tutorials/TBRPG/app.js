const http = require('http');
const fs = require('fs');
http.createServer((request, response) => {
    response.statusCode = 200;
    var url = request.url;
    if(request.url == '/') {
        url = '/index.html';
    }
    response.writeHead(200);
    response.end(fs.readFileSync(__dirname + url));
}).listen(3000);

console.log('Server running at http://localhost:3000/');
