str_1 = "hello"
str_2 = "12345"
str_3 = "##abc123##"
str_4 = " "
str_1_num = str_1.isnumeric()
print(str_1_num)
str_1_alpha = str_1.isalpha()
print(str_1_alpha)
str_2_alphanum = str_2.isalnum()
print(str_2_alphanum)
str_4_empty = str_4.isspace()
print(str_4_empty)
str_3_start = str_3.startswith("abc")
print(str_3_start)
str_3_end = str_3.endswith("3")
str_1_he = str_1.startswith("he") and str_1.endswith("lo")
print(str_1_he)
str_3_remove = str_3.strip("#")
print(str_3_remove)
str_3_remove_leading = str_3.lstrip("#")
print(str_3_remove_leading)