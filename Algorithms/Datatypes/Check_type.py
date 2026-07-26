string_variable = "Hello, world"

# type check
def odd(n: int) -> bool:
    return n % 2 != 0


def main() -> None:
    print(type(string_variable))
    print('is_odd: ', odd(3)) # error if used "string variable"

if __name__ == "__main__":
    main()