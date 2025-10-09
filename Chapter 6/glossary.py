glossary = {
    'dictionary': 'a built-in data type that stores data in key-value pairs, allowing fast and efficient access to values using unique keys',
    'lists': 'an ordered, changeable collection that can store multiple items in a single variable. It allows duplicates and supports indexing',
    'variables': 'a name that refers to a value stored in memory — like a label on a container that holds data',
    'booleans': 'a data type that can only have one of two values: True or False',
    'statements': 'a complete instruction that the interpreter can execute — like assigning a value, printing something, or running a loop',
}
for word in glossary:
    print(f"{word.upper()}:\n{glossary[word]}\n")
