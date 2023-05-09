import inspect
import re
class MyClass:
    class_variable = 42

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method1(self):
        return self.a + self.b

    @staticmethod
    def static_method():
        return "Hello, world!"

    @classmethod
    def class_method(cls):
        return cls.class_variable

if __name__ == '__main__':
    # obj = MyClass(3, 6).class_method
    # if isinstance(obj, staticmethod):
    #     print('static')
    # if isinstance(obj, classmethod):
    #     print('class_method')
    # if inspect.ismethod(obj):
    #     print('method')
    # if inspect.isfunction(obj):
    #     print('function')
    # name = 'Oleg'
    # print(f'Hello,{name}!')
    # print(name[1:-1])
    # print(bool('False'))

    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?:[^{}]|(?R))*\}"  # выделить группы в фигурных скобках
    # matches = re.findall(pattern, text)
    # print(matches)  # ['{brown {fox} jumps}', '{lazy {dog}}']

    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?P<group>(?:[^{}]|(?P>group))*)\}"  # выделить группы в фигурных скобках
    # matches = re.findall(pattern, text)
    # print(matches)  # ['brown {fox} jumps', 'lazy {dog}']


    # text = "{foo {bar} baz} qux {quux}"
    # pattern = r'\{(?:[^{}]|(?R))*\}'  # выделить группы в фигурных скобках
    # matches = re.findall(pattern, text)
    # print(matches)  # ['{foo {bar} baz}', '{bar}', '{quux}']

    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?P<group>(?:[^{}]|(?P<group>\{(?:[^{}]|(?P<group>))*\}))*?)\}"
    # matches = re.findall(pattern, text)
    # print(matches)  # ['brown {fox} jumps', 'lazy {dog}']


    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?P<group1>(?:[^{}]|(?P<group2>\{(?:[^{}]|(?P<group2>))*\}))*?)\}"
    # matches = re.findall(pattern, text)
    # print(matches)  # ['brown {fox} jumps', 'lazy {dog}']
    # import re

    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?P<group>(?:[^{}]|(?P<group>.*))*?)\}"
    # matches = re.findall(pattern, text)
    # print(matches)  # ['brown {fox} jumps', 'lazy {dog}']

    # text = "The quick {brown {fox} jumps} over the {lazy {dog}}."
    # pattern = r"\{(?P<group1>[^{}]*(?:\{(?P<group2>[^{}]*(?:\{(?P<group3>[^{}]*)\}|[^{}]*)*)\}[^{}]*)*)\}"
    # matches = re.findall(pattern, text)
    # print(matches)
    #...............

    text = "Some [text] with [multiple [groups]] inside."
    pattern = r"\[(?P<group1>[^\[\]]*(?:\[(?P<group2>[^\[\]]*(?:\[(?P<group3>[^\[\]]*)\]|[^\[\]]*)*)\][^\[\]]*)*)\]"
    matches = re.findall(pattern, text)
    print(matches)
