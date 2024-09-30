class _Node:
    def __init__(self, cnt: int) -> None:
        self.cnt: int = cnt
        self.keys: set[str] = set()
        self.prev: _Node = None
        self.next: _Node = None


class AllOne:
    def __init__(self):
        self.__map: dict[str, _Node] = dict()
        self.__head: _Node = _Node(cnt=0)
        self.__tail: _Node = _Node(cnt=0)

        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def inc(self, key: str) -> None:
        if self.__map.get(key) is not None:
            node: _Node = self.__map.get(key)
            cnt: int = node.cnt
            next_node: _Node = node.next

            node.keys.remove(key)

            if next_node is self.__tail or next_node.cnt != cnt + 1:
                new_node: _Node = _Node(cnt=cnt + 1)
                node.next = new_node
                new_node.prev = node
                new_node.next = next_node
                next_node.prev = new_node
                new_node.keys.add(key)
                self.__map[key] = new_node
            else:
                next_node.keys.add(key)
                self.__map[key] = next_node

            if len(node.keys) == 0:
                self.__remove_node(node)
        else:
            next_node: _Node = self.__head.next

            if next_node is self.__tail or next_node.cnt > 1:
                new_node: _Node = _Node(1)
                self.__head.next = new_node
                new_node.prev = self.__head
                new_node.next = next_node
                next_node.prev = new_node
                new_node.keys.add(key)
                self.__map[key] = new_node
            else:
                next_node.keys.add(key)
                self.__map[key] = next_node

        # print(f"{key} {self.__map[key].keys} {self.__map[key].next is self.__tail}")

    def dec(self, key: str) -> None:
        if self.__map.get(key) is None:
            return

        node: _Node = self.__map.get(key)
        cnt: int = node.cnt
        prev_node: _Node = node.prev

        node.keys.remove(key)

        if cnt == 1:
            self.__map[key] = None
            
            if len(node.keys) == 0:
                self.__remove_node(node)
            return

        if prev_node is self.__head or prev_node.cnt != cnt - 1:
            new_node: _Node = _Node(cnt=cnt - 1)
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = node
            node.prev = new_node
            new_node.keys.add(key)
            self.__map[key] = new_node
        else:
            prev_node.keys.add(key)
            self.__map[key] = prev_node

        if len(node.keys) == 0:
            self.__remove_node(node)

        # print(f"{key} {self.__map[key].keys} {self.__map[key].next is self.__tail}")

    def getMaxKey(self) -> str:
        if self.__tail.prev is self.__head:
            return ""

        return next(iter(self.__tail.prev.keys))

    def getMinKey(self) -> str:
        if self.__head.next is self.__tail:
            return ""

        return next(iter(self.__head.next.keys))

    def __remove_node(self, node: _Node) -> None:
        prev_node: _Node = node.prev
        next_node: _Node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
