import graphlib as gl


graph = {'D': {'B', 'C'}, 'C': {'A'}, 'B': {'A'}}
ts = gl.TopologicalSorter(graph)
print(tuple(ts.static_order()))

'''
topo_sort = gl.TopologicalSorter()
while topo_sort.is_active():
    for node in top_sort.get_ready():
        task_queue.put(node)
    node = finalized_tasks_queue.get()
    topo_sort.done(node)
'''


ts = gl.TopologicalSorter()
ts.add(3, 2, 1)
ts.add(1, 0)
print([*ts.static_order()])


ts = gl.TopologicalSorter()
ts.add(1, 0)
ts.add(3, 2, 1)
print([*ts.static_order()])
