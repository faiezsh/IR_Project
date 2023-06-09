

class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.ids=[]
        self.children = dict()
        self.is_word = False # New code

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def size(self, current = None):
        '''
        Returns the size of this prefix tree, defined
        as the total number of nodes in the tree.
        '''
        # By default, get the size of the whole trie, starting at the root
        if not current:
            current = self.root
        count = 1
        for letter in current.children:
            count += self.size(current.children[letter])
        return count

        
    def insert(self, word,wordId):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True # New code
        current.ids.append(wordId)
        
    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

    def starts_with(self, prefix):
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]

        self.__child_words_for(current, words)
        # if current.is_word:
        #     words=current.ids
        return words
    '''
    def printTrie(self):
        words = list()
        current = self.root
        for char in current.children.values():
            if char.is_word:
                words.append((current.ids,current.text))
            for letter in char.children.values():
                self.__child_words_for(current.children[letter], words)
            self.__child_words_for(current, words)
            return words
    '''
    def __getstate__(self):
        # return a state dictionary that contains the root node and the size of the trie
        return {'root': self.root, 'size': self.size}
    '''
    def __setstate__(self, state):
        # set the root node and the size of the trie from the state dictionary
        self.root = state['root']
        self.size = state['size']
    '''

    def __setstate__(self, state):
        # set the root node and the size of the trie from the state dictionary
        self.root = state.get('root', None)
        self.size = state.get('size', 0)

