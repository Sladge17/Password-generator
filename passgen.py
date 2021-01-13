import random

letter_1 = 'abcdefghijklmnopqrstuvwxyz'
letter_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numb = '1234567890'
spec = '!@#$%^&*()-+'
symb = (letter_1, letter_2, numb, spec)

def gen_pas(count):
	if count < len(symb):
		return ("Unsafe length")
	password = [''] * count
	for i in range(len(symb)):
		r_symb = symb[i][random.randint(0, len(symb[i]) - 1)]
		r_pos = random.randint(0, count - 1)
		while password[r_pos] != '':
			r_pos = random.randint(0, count - 1)
		password[r_pos] = r_symb
	for i in range(len(password)):
		if password[i] != '':
			continue
		r_pos = random.randint(0, len(symb) - 1)
		password[i] = symb[r_pos][random.randint(0, len(symb[r_pos]) - 1)]
	password = ''.join(password)
	return (password)

def set_passlen():
	while True:
		passlen = input(f"Enter password length (min length {len(symb)}): ")
		try:
			passlen = int(passlen)
		except:
			print("Password length should be a number")
			continue
		if passlen < len(symb):
			print("Input length less than min length")
			continue
		break
	return passlen

def main():
	print("Your password:", gen_pas(set_passlen()))


if __name__ == "__main__":
	main()

