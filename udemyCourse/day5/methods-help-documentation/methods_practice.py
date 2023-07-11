text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

text1 = text.lstrip(',')
text2 = text1.lstrip(':')
text3 = text2.lstrip('_')
text4 = text3.lstrip('#')
text5 = text4.lstrip(',')
text6 = text5.lstrip(':')
text7 = text6.lstrip('_')
text8 = text7.lstrip('#')
print(text8)

textx = text.lstrip(',').lstrip(':').lstrip('_').lstrip('#').lstrip(',').lstrip(':').lstrip('_').lstrip('#')

print(textx)

# for i in range(len(text)):
#     if text[i] == 'P':
#         break
#     else:
#         if text[i] == text[i+1]:
#             continue
#         else:
#             a_list.append(text[i])

# new_text = text.lstrip(a_list[0]).lstrip(a_list[1])

# print(new_text)
