import networkx as nx
from queue import PriorityQueue
import matplotlib.pyplot as plt

def route_packets(G, packets):
    paths = {}

    for packet in packets:
        src = packet['src']
        dest = packet['dest']
        size = packet['size']
        deadline = packet['deadline']

        # Find k shortest paths
        K = 5
        kpaths = list(nx.shortest_simple_paths(G, src, dest, K))

        if not kpaths:
            print(f"No valid path found for packet {packet}.")
            continue

        # Priority queue to hold path score
        pq = PriorityQueue()

        # Score each path
        for path in kpaths:
            score = 0
            residual_bw = float('inf')

            for u, v in zip(path, path[1:]):
                bw = G[u][v]['bw']
                residual_bw = min(residual_bw, bw)
                delay = G[u][v]['delay']

                # Calculate score
                score += residual_bw
                score += 1 / delay

            # Deadline penalty
            if delay > deadline:
                score -= 100

            # Add score to pq
            pq.put((-score, tuple(path)))

        # Get best path
        best_path = pq.get()[1]
        paths[tuple(packet.items())] = best_path 

        print("Selected path for packet from src:", packet['src'], 'dest:', packet['dest'], 'size:', packet['size'], 'deadline:',  packet['deadline'], "is: ", best_path)

        # Update residual bandwidth
        for u, v in zip(best_path, best_path[1:]):
            G[u][v]['bw'] -= size

    return paths

G = nx.Graph()
G.add_edges_from([
    (1, 2, {'bw': 10, 'delay': 2}),
    (1, 3, {'bw': 10, 'delay': 5}),
    (2, 3, {'bw': 20, 'delay': 1}),
    (3, 4, {'bw': 15, 'delay': 3}),
    (2, 4, {'bw': 12, 'delay': 2}),
    (4, 5, {'bw': 18, 'delay': 1}),
    (3, 5, {'bw': 14, 'delay': 4}),
    (1, 6, {'bw': 8, 'delay': 3}),
    (2, 6, {'bw': 15, 'delay': 2}),
    (3, 6, {'bw': 12, 'delay': 4}),
])


packets = [
    {'src': 1, 'dest': 4, 'size': 5, 'deadline': 15},
    {'src': 2, 'dest': 5, 'size': 8, 'deadline': 20},
    {'src': 3, 'dest': 4, 'size': 10, 'deadline': 25},
    {'src': 1, 'dest': 5, 'size': 6, 'deadline': 18},
    {'src': 2, 'dest': 4, 'size': 7, 'deadline': 22},
]

paths = route_packets(G, packets)

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
edge_labels = {(u, v): f'BW: {G[u][v]["bw"]}, Delay: {G[u][v]["delay"]}' for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

plt.show()

for i, (packet, path) in enumerate(paths.items()):
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

    edges_in_path = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    edge_labels = {(u, v): f'BW: {G[u][v]["bw"]}, Delay: {G[u][v]["delay"]}' for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

    plt.title(f"Path for Packet {i + 1}")
    plt.savefig(f"path_packet_{i + 1}.png")
    plt.close()