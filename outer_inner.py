def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
outer_function("Hi everyone!!!")