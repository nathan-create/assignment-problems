def convert_to_base_10(binum):
    decimal_num = 0
    binum_str = str(binum)
    binum_list = list(binum_str)
    for i in range(len(binum_list)):
        num=binum_list.pop()
        if num == "1":
            decimal_num+=2**i
    return decimal_num
print("Testing convert_to_base_10...")
assert convert_to_base_10(10011)==19,"actual output:{}".format(convert_to_base_10(10011))
print("Passed")
  