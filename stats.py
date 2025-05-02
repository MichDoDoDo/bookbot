
def get_book_text(filepath):
    fileContent = ""
    with open(filepath) as f:
        fileContent = f.read()
    return fileContent

def countWords(text):
    parsedList = text.split()
    return len(parsedList)

def get_num_words(filepath):
    text = get_book_text(filepath)
    count = countWords(text)
    print(f"Found {count} total words")
    
    
def count_all_chars(filepath):
    text = get_book_text(filepath).lower()
    charDict = {}
    for i in range(len(text)):
        charDict[text[i]] = 1 + charDict.get(text[i], 0)
    prettyDisplay(charDict,filepath)
    
def prettyDisplay(charDict,filepath):
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    get_num_words(filepath)
    print("--------- Character Count -------")
    sortedCharDict = dict(sorted(charDict.items(), key=lambda item: item[1], reverse = True))
    for key, value in sortedCharDict.items():
        if key.isalpha():
            print(f"{key}: {value}")
            
        
    print("============= END ===============")
    
    
