const net = require('net');

net.createServer((sock) => {
  sock.on('data', (data) => {
    sock.write('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 11\r\n\r\nhello world\r\n');
    sock.destroy();
  });
}).listen(8002, 'localhost');

console.log('start listening...');
