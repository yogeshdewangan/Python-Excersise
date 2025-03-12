
def another_way():
    str= "yogeshkumardewangan"
    dict ={}

    for char in str:
        if char in dict.keys():
            dict[char]+=1
        else:
            dict[char]=1
    print(dict)


if __name__ == "__main__":
    another_way()