class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self):
        return f"{self.node_id}: {self.children}"


def BuildTree(records):
    root = None
    trees = []
    records.sort(key=lambda x: x.record_id)
    sorted_record_id = sorted([i.record_id for i in records])
    for i in range(len(records)):
        if i in sorted_record_id and sorted_record_id[-1] == len(records) - 1:
            for j, k in [(i.record_id, i.parent_id) for i in records]:
                if j < k:
                    raise ValueError ("Node record_id should be smaller than it's parent_id.")
                elif j == k and (j!= 0 or k!=0):
                    raise ValueError ("Only root should have equal record and parent id.")
        else:
            raise ValueError("Record id is invalid or out of order.")

    for i in records:
        node = Node(i.record_id)
        trees.append(node)
        if i.record_id != 0:            
            trees[i.parent_id].children.append(node)
    print(trees)
    if len(trees) > 0:
        root = trees[0]
    return root


records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 1),
            Record(4, 1),
            Record(5, 1),
            Record(6, 2),
        ]
root = BuildTree(records)
print(root)
