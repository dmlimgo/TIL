# 참조: https://blog.ilkyu.kr/entry/파이썬에서-Trie-트라이-구현하기
class Node(object):
    """
    Trie를 구성할 Node
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
    

class Trie(object):
    """
    Trie 구현
    """

    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head

        # tree 형태로 Node들을 구성한다.
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        
        # 마지막 글자에서는 Node의 data에 문자열 전체를 저장한다.
        current_node.data = string

    def search(self, string):
        """
        string이 Trie에 존재하는지 여부를 반환한다.
        """
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        
        # string의 마지막 글자일 때, current_node에 data가 존재한다면 string이 Trie에 존재한다.
        if current_node.data != None:
            return True

    def starts_with(self, prefix):
        """
        주어진 prefix로 시작하는 단어들을 Trie에서 찾아 리스트 형태로 반환한다.
        """
        current_node = self.head
        result = []
        subtrie = None

        # Trie에서 prefix를 찾고, prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
                subtrie = current_node
            else:
                return None
        
        queue = list(subtrie.children.values())

        while queue:
            current = queue.pop()
            if current.data != None:
                result.append(current.data)
            
            queue += list(current.children.values())

        return result

trie = Trie()
trie.insert('Joe')
trie.insert('John')
trie.insert('Johnny')
trie.insert('Jane')
trie.insert('Jack')
print(trie.starts_with('a'))
