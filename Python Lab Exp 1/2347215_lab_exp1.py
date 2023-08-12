intro="Hii, I'm Symen. I'm from Sivakasi, Tamilnadu and I'm currently I'm persuading my Master Of Computer Application in Christ(Deemed to be)University, with a roll number of 2347215. In the year 2023, Symen have choosen the domain of Football Management Systems using Python."

def frequency_word_count(paragraph, target_word):
    words = paragraph.split()
    word_count = 0
    for word in words:
        word = word.strip('.,!?()[]{}"\'')
        if word.lower() == target_word.lower():
            word_count += 1
    return word_count
paragraph = input("Enter the para to find the word count:")
target_word = input("Enter the word that you want to count:")
frequency = frequency_word_count(paragraph, target_word)
print(f"The word '{target_word}' appears {frequency} times in the paragraph.")

num=["0","1","2","3","4","5","6","7","8","9"]
spl_word=intro.split(" ")
for i in spl_word:
    for j in i:
        if j in num:
            if "." in i:
                print(i," is float")
                break
            else:
                print(i,"is int")
                break
        else:
            print(i,"is string")
            break
def char_count(paragraph):
    alphabets = 0
    numerics = 0
    specials = 0

    for char in paragraph:
        if char.isalpha():
            alphabets += 1
        elif char.isnumeric():
            numerics += 1
        else:
            specials += 1

    return alphabets, numerics, specials
paragraph = "I'm Symen scored 8.9 GPA in BCA"

alphabets, numeric, specials = char_count(paragraph)

print(f"Alphabets: {alphabets}")
print(f"Numeric characters: {numeric}")
print(f"Special symbols: {specials}")

def set_oper_eg():
    string_set = {"Soprano", "Alto", "Tenor", "Bass", "Baritone"}
    print("Initial Set:", string_set)
    sorted_set = sorted(string_set, reverse=True)
    print("Sorted Set (Descending Order):", sorted_set)
set_oper_eg()

def tuple_oper_eg():

    football = ("Player", "Goal", "Coach", "Cards", "Referee")
    print("Original Tuple:", football)

    first, second, third, fourth, fifth = football
    print("\nUnpacked Variables:")
    print("First attribute:", first)
    print("Second attribute:", second)
    print("Third attribute:", third)
    print("Fourth attribute:", fourth)
    print("Fifth attribute:", fifth)
tuple_oper_eg()

dmn_name=("f","o","o","t","b","a","l","l")
count=0
for i in dmn_name:
    count=count+1
print("count of o",count)

def slicing_and_negative_indexing(dom_name):
    print("Original Domain Name:", dom_name)
    print("\nPositive Slicing:")
    print("1) Slicing from index 3 to 12:", dom_name[3:13])
    print("2) Slicing from index 0 to 7:", dom_name[:8])
    print("3) Slicing from index 5 to the end:", dom_name[5:])
    print("4) Slicing from index 2 to 11 with step 2:", dom_name[2:12:2])
    print("\nNegative Slicing:")
    print("1) Slicing from the end -8 to the end -3:", dom_name[-8:-2])
    print("2) Slicing from the end -11 to the end -1 with step 2:", dom_name[-11:-1:2])
    print("\nNegative Indexing:")
    print("Last character:", dom_name[-1])
    print("Second to last character:", dom_name[-2])
dom_name = "Football management system"
slicing_and_negative_indexing(dom_name)
