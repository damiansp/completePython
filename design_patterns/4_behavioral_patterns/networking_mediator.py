def main():
    med = NetworkMediator()
    n1 = NetworkNode('Node1', med)
    n2 = NetworkNode('Node2', med)
    n3 = NetworkNode('Node3', med)
    med.add_node(n1)
    med.add_node(n2)
    med.add_node(n3)
    n1.send('Node2', 'Hello, n2!')
    n2.send('Node3', 'Yo, n3!')
    n3.send('Node1', 'What up, n1?')
    

class NetworkMediator:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def send_message(self, sender, receiver, msg):
        if receiver in self.nodes:
            self.nodes[receiver].receive_message(sender, msg)
        else:
            print(f'Node {receiver} not found')


class NetworkNode:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, receiver, msg):
        print(f'{self.name} sending message to {receiver}: {msg}')
        self.mediator.send_message(self.name, receiver, msg)

    def receive_message(self, sender, msg):
        print(f'{self.name} received message from {sender}: {msg}')


if __name__ == '__main__':
    main()
