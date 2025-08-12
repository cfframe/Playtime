#  PCPP1 related code
class TopCodeClass:
    def __init__(self):
        self.name = "TopCodeClass"

    def display(self):
        print(f"TopCodeClass.display: This is '{self.name}'")

    def __str__(self):
        return "TopCodeClass dummy string representation"


def main():
    top_code_instance = TopCodeClass()
    top_code_instance.display()
    print(top_code_instance)
    print(f'__name__: {__name__}')
    print(f'TopCodeClass.__name__: {TopCodeClass.__name__}  ')
    try:
        print(f'top_code_instance.__name__: {top_code_instance.__name__}  ')
    except AttributeError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
