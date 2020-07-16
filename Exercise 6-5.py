
# Exercise 6-5

str = 'X-DSPAM-Confidence: 0.8475 '

colon_pos = str.find(":")

num = str[colon_pos+1: ]
num = float(num)

print(num)
