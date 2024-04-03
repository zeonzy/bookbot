def words_in_text(text):
    text = text.split()
    return len(text)

def count_characters(text):
    text = text.lower()
    new_dict = {}
    for i in text:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    return new_dict

def bookreport(text):
    chars = count_characters(text)
    output_list = []

    for i in chars:
        if i.isalpha():
            output_list.append({"letter": i, "amount": chars[i]})
    #print(output_list)

    def sort_on(dict):
        return dict["amount"]
    
    output_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_in_text(text)} words found in the document")
    print("")
    for i in output_list:
        print(f"The '{i["letter"]}' character was found {i["amount"]} times")
    print("--- End report ---")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(f"Words in text: {words_in_text(file_contents)}")
    #print(f"characters in text: {count_characters(file_contents)}")
    bookreport(file_contents)
    

main()