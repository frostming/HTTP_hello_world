HTTP Hello World
================

This repo is a collection of Hello world HTTP servers implemented by multiple languages. Contributions are welcomed.

Benchmark
---------

### Environment Setup

macOS Mojave 10.14.2
CPU: 2.7GHz Intel Core i5
Memory: 8GB 1867MHz DDR3

Threads: 50, Loops: 100

### Result

| Implementation | TPS | Error% | Received KB/s | Sent KB/s |
| ---- | ---- | ---- | ---- | ---- |
| cpp_socket | 4463.3 | 0 | 340.05 | 514.44 |
| go_goroutine | 4638.2 | 0 | 348.77 | 543.48 |
| py_threaded | 2844.1 | 0 | 213.87 | 327.74 |
| py_async | 4098.4 | 0 | 308.18 | 472.27 |
| node_normal |  3623.2 | 272.45 | 417.52 |
