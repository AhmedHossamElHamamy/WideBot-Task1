# WideBot-Task1:
Using this dictionary, implement a spell checker class that takes this dictionary as input, this 
class has three main operations:
• Store this dictionary in a suitable data structure.
• Take an input word and return the nearest 4 words if this word is not in the dictionary
• Take an input word and add this word to the dictionary
For each operation specify the time and space complexity
Note: You could assume that the nearest 4 words from a word are the 2 words before and 
after this word in lexicographic order if they exist.
# Why Binary tree:
1)Efficient Lookup: Bintrees provide fast lookup time for words in the dictionary. Since it uses binary search tree-based data structures, the time complexity for lookup (searching for a word) is O(log n)
2)Sorted Order: Bintrees naturally maintain words in sorted order, making it easy to find nearest words before and after a given word.
3)Memory Efficiency: Bintrees can be more memory-efficient compared to some other data structures like hash tables since they do not require a fixed-size array for storing elements
