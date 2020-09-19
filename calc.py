

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

def check_for_exit(user_input):
	if str(user_input) == "exit"
		return True
	return False

def convert_to_proper_type(user_input):
	if "." in user_input:
		user_input = float(user_input)
	else:
		user_input = int(user_input)
	return user_input

def run()
	while True:
		handle_user_input()
		calculate()

def hanlde_user_input()
	[first_numb, second_numb, operation]

def calculate(a, b, operation)

def main():
	greetings()
	while True:
		while True:
			first_numb = input("Enter first number: ")
			if exit_and_warning_func(first_numb):
				return 0
			else:
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
				return 0
			elif error_code == 1:
				try:
					second_numb = convert_to_proper_type(second_numb)
					break
				except ValueError:
					print("Please enter a number")
					continue

		while True:
			operation = input("Enter an operator: ")
			if operation  not in ["+", "-", "*", "/"]:
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