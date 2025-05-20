
# Q5: Static method vs Class method
class MyClass:
    @staticmethod
    def static_method():
        print("Static method called")

    @classmethod
    def class_method(cls):
        print(f"Class method called from {cls}")

MyClass.static_method()
MyClass.class_method()
