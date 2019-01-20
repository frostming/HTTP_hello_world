package main

import (
	"fmt"
	"net"
)

func handleRequest(conn net.Conn) {
	defer func() {
		err := conn.Close()
		if err != nil {
			fmt.Println(err)
		}
	}()
	response := "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 11\r\n\r\nhello world\r\n"
	_, err := conn.Write([]byte(response))
	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	var server net.Listener
	server, err := net.Listen("tcp", net.JoinHostPort("localhost", "8002"))
	if err != nil {
		panic("listen error!")
	}
	fmt.Println("start listening...")
	for {
		conn, err := server.Accept()
		if err != nil {
			continue
		}
		go handleRequest(conn)
	}
}
