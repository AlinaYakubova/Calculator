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
	if str(user_input) == "exit":
		return True
	return False

def convert_to_proper_type(user_input):
	if "." in user_input:
		user_input = float(user_input)
	else:
		user_input = int(user_input)
	return user_input

def handle_user_input_numbers(user_input):
	while True:
		if check_for_exit(user_input):
			return None
			break
		else:
			try:
				user_number = convert_to_proper_type(user_input)
				break
			except ValueError:
				print("Please enter a number")
				continue
	return user_number

def handle_user_input_operation():
	while True:
		operation = input("Enter an operator: ")
		if operation  not in ["+", "-", "*", "/"]:
			print("Please enter valid operation")
			continue
		else:
			break
	return operation

def calculate(first_numb, second_numb, operation):
	if operation == "+":
		result = sum_two_numbs(first_numb, second_numb)
	elif operation == "*":
		result = mul_two_numbs(first_numb, second_numb)
	elif operation == "-":
		result = sub_two_numbs(first_numb, second_numb)
	elif operation == "/":
		try:
			result = div_two_numbs(first_numb, second_numb)
		except ZeroDivisionError:
			result = "You cannot divide by zero!"
	else:
		result = "Oops! Please enter valid operation."
	print(result)
	# return result



def run():
	while True:
		user_input_1 = input("Enter first number: ")
		first_numb = handle_user_input_numbers(user_input_1)
		if first_numb is None:
			break
		user_input_2 = input("Enter second number: ")
		second_numb = handle_user_input_numbers(user_input_2)
		if second_numb is None:
			break
		operation = handle_user_input_operation()
		calculate(first_numb, second_numb, operation)


def main():
	greetings()
	run()
	return 0

if __name__ == "__main__":
	if main() != 0:
		print("Something goes wrong")