import math

def dec_to_any_list(n,radix):
    val_list = []
    over_list = ["A","B","C","D","E","F"]
    while n//radix != 0 :
        rest = n % radix
        n = n // radix
        ## 여기서 한 것 처럼
        if rest>=10 :
            rest = over_list[rest - 10]
        val_list.append(str(rest))
        # print(n , rest)
    ## 여기서도 똑같이 해주면 될 것 같습니다
    if n >= 10:
        n = over_list[n - 10]
    val_list.append(str(n))
    
    val_list.reverse()
    new_num = "".join(val_list)
    # print(new_num)

    return new_num
    
# dec_to_any_list(140,8)


def dec_to_any_string(n, radix):
    val_str = ""
    over_list = ["A","B","C","D","E","F"]
    while n//radix != 0 :
        rest = n % radix
        if rest >= 10 :
            rest = over_list[rest - 10]
        n = (n // radix)
        val_str = val_str + str(rest)
        # print(n , rest)
    if n >= 10:
        n = over_list[n - 10]
    val_str = val_str + str(n)
    
    new_num = val_str[::-1]
    # print(new_num)
    return new_num


def main():

    print("[evaluate dec_to_any.py]")
    num = int(input("Enter a number : "))
    if num < 0 :
        print("Wrong Input!!!")
        return
    radix = int(input("Enter a radix : "))
    if not(2<=radix<=16) :
        print("Wrong Input!!!")
        return
    new_num = dec_to_any_list(num, radix)
    #new_num = dec_to_any_string(num, radix)

    print("%s in base 10 is %s in base %s \n" %(num, new_num, radix ))

main()