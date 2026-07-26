class Node:
    def __init__(self, name):
        self.name = name
        self.buffer = []

    def receive_packet(self, packet):
        print(f"{self.name} received packet: {packet}")
        self.buffer.append(packet)

    def forward_packet(self, next_node):
        if self.buffer:
            packet = self.buffer.pop(0)
            print(f"{self.name} forwarding packet: {packet} to {next_node.name}")
            next_node.receive_packet(packet)
        else:
            print(f"{self.name} has no packets to forward")

class PacketSwitchingNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def send_packet(self, start_node_name, end_node_name, packet):
        if start_node_name in self.nodes and end_node_name in self.nodes:
            
            start_node = self.nodes[start_node_name]
            
            end_node = self.nodes[end_node_name]
            
            start_node.receive_packet(packet)
            start_node.forward_packet(end_node)
        else:
            print("Invalid node names")

# Example usage
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

network = PacketSwitchingNetwork()
network.add_node(node_a)
network.add_node(node_b)
network.add_node(node_c)

network.send_packet("A", "B", "Packet1")
network.send_packet("B", "C", "Packet2")
