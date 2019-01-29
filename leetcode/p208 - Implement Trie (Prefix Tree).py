class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.head
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['\n'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.startsWith(word) and '\n' in self.cur

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        self.cur = self.head
        for c in prefix:
            self.cur = self.cur.get(c)
            if not self.cur:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        cur = self.head
        for c in word:
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        return self.startsWith(word) and self.cur.end

    def startsWith(self, prefix):
        self.cur = self.head
        for c in prefix:
            self.cur = self.cur.children.get(c)
            if not self.cur:
                return False
        return True
