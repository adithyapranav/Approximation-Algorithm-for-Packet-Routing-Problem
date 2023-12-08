# Approximation-Algorithm-for-Packet-Routing-Problem
We create an Approximation Algorithm which will solve the NP-complete Packet routing problem.

We have created the following graph as a sample graph to test our algorithm:
![Graph](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/8131a356-8d5c-4e9e-add5-2a462f3891f4)

We have defined 5 packets with the following properties to be sent through the network defined by the graph:
````
packets = [
    {'src': 1, 'dest': 4, 'size': 5, 'deadline': 15},
    {'src': 2, 'dest': 5, 'size': 8, 'deadline': 20},
    {'src': 3, 'dest': 4, 'size': 10, 'deadline': 25},
    {'src': 1, 'dest': 5, 'size': 6, 'deadline': 18},
    {'src': 2, 'dest': 4, 'size': 7, 'deadline': 22},
]
````
The following are the results generated from the program:
Output:
````
Selected path for packet from src: 1 dest: 4 size: 5 deadline: 15 is:  (1, 2, 6, 3, 5, 4)
Selected path for packet from src: 2 dest: 5 size: 8 deadline: 20 is:  (2, 3, 4, 5)
Selected path for packet from src: 3 dest: 4 size: 10 deadline: 25 is:  (3, 1, 6, 2, 4)
Selected path for packet from src: 1 dest: 5 size: 6 deadline: 18 is:  (1, 2, 3, 4, 5)
Selected path for packet from src: 2 dest: 4 size: 7 deadline: 22 is:  (2, 3, 5, 4)
````
The paths visualized:
Packet 1
![path_packet_1](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/9447e6a5-93dd-4d51-8c29-ce7558ac4f84)
Packet 2
![path_packet_2](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/051ad8e1-14bf-480a-b1d7-4dacb11350f2)
Packet 3
![path_packet_3](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/6d1ab705-a1ef-42e4-a459-8067837eec37)
Packet 4
![path_packet_4](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/e9d9413f-1f63-4764-801a-79242f487feb)
Packet 5ṭ
![path_packet_5](https://github.com/adithyapranav/Approximation-Algorithm-for-Packet-Routing-Problem/assets/30080510/171617ec-e187-487b-b8ed-907cd1adae84)
