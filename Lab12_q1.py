class FirstSystem:
    def foo(self, data: int) -> str:
        return str(data)

class SecondSystem:
    def bar(self, text: str) -> int:
        return int(text)
    
class SystemAdapter(FirstSystem):
    def __init__(self) -> None:
        self.__obj = SecondSystem()

    def foo(self, data: int) -> str:
        return str(self.__obj.bar(str(data)))
    
class Factory:
    @staticmethod
    def get_system() -> FirstSystem:
        return SystemAdapter()
    
def main():
    system = Factory.get_system()
    print(system.foo(1234))


if __name__ == "__main__":
    main()