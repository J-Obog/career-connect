
class HashedGraph:
    def __init__(self):
        self._edges = {}
        self._nodes = {}

    def edges(self):
        return self._edges

    def nodes(self):
        return self._nodes

    def add_node(self, hash, node):
        if hash not in self._nodes:
            self._edges[hash] = node

    def link(self, hash1, hash2):
        if hash1 in self._nodes and hash2 in self._nodes:
            if f'{hash1}:{hash2}' in self._edges:
                self._edges[f'{hash1}:{hash2}'] += 1
                self._edges[f'{hash2}:{hash1}'] += 1
            else:
                self._edges[f'{hash1}:{hash2}'] = 0
                self._edges[f'{hash2}:{hash1}'] = 0
