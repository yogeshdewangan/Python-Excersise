from pip._vendor.distlib.compat import raw_input



if __name__=="__main__":
    image_list=[]
    dict={}

    opr_count=int(raw_input())

    for _ in range(opr_count):
        inp=raw_input().split()
        dict[int(inp[0])]=inp[1]

    for key,value in dict.items():
        print(str(key) + " " + value)