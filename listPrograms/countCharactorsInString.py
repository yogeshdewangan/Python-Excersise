
def count_char_in_string():
    str="yogeshkumardewangan"
    count_dict={}
    for char in str:
        count =str.count(char)
        count_dict[char]=count
    print(count_dict)


if __name__ == "__main__":
    count_char_in_string()