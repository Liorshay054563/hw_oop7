# hw_oop7

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))

def print_user_info(**kwargs):
    
    user_info =[f"{key}: {value}" for key, value in kwargs.items()]
    print(user_info)

print_user_info(name="Dana", age=30, city="Tel Aviv")

def combine_values(*args, **kwargs):
    total_sum = sum(args)
    print(f"Sum: {total_sum}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def greet_user(**kwargs):
    name = kwargs.get("name", "guest")
    print(f"Hello {name}")

greet_user(name= 'lior')
greet_user()