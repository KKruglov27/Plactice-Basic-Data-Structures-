#3nd program
num_ber1 = "{}{}".format(1234 % 90 // 30, 1234 % 100 // 10)
num_ber2 = "{}{}".format(5678 % 100 // 12, 5678 % 100 // 10)

num_ber1 = int(num_ber1)
num_ber2 = int(num_ber2)

print(num_ber1 + num_ber2)