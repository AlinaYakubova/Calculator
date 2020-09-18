

def greetings():
	greetings_str = "Hey! Welcome to calculator"
	print(greetings_str)
	available_commands = "You can use one of following operations: +, -, /, *"
	print(available_commands)

def sum_two_numbs(a, b):
	return a + b

def mul_two_numbs(a, b):
	return a * b

def sub_two_numbs(a, b):
	return a - b

def div_two_numbs(a, b):
	return a / b

def exit_and_warning_func(user_input):
	if str(user_input) == "exit":
		error_code = -1
	else:
		error_code = 1
	return error_code

def convert_to_proper_type(user_input):
	if "." in user_input:
		user_input = float(user_input)
	else:
		user_input = int(user_input)
	return user_input


def main():
	greetings()
	while True:
		while True:
			first_numb = input("Enter first number: ")
			error_code = exit_and_warning_func(first_numb)
			if error_code == -1:
				break
			elif error_code == 1:
				try:
					first_numb = convert_to_proper_type(first_numb)
					break
				except ValueError:
					print("Please enter a number")
					continue
		
		while True:
			second_numb = input("Enter second number: ")
			error_code = exit_and_warning_func(second_numb)
			if error_code == -1:
				break
			elif error_code == 1:
				try:
					second_numb = convert_to_proper_type(second_numb)
					break
				except ValueError:
					print("Please enter a number")
					continue
		
		while True:
			operation = input("Enter an operator: ")
			if operation != "+" or operation != "+" or operation != "+" or operation != "+":
				print("Please enter valid operation")
				continue
			else:
				break

		if operation == "+":
			result = sum_two_numbs(first_numb, second_numb)
		elif operation == "*":
			result = mul_two_numbs(first_numb, second_numb)
		elif operation == "-":
			result = sub_two_numbs(first_numb, second_numb)
		elif operation == "/":
			result = div_two_numbs(first_numb, second_numb)
		else:
			result = "Oops! Please enter valid operation."
		print(result)
	return 0

if __name__ == "__main__":
	if main() != 0:
		print("Something goes wrong")