# 8-4 大号T恤 ：修改函数make_shirt() ，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。调用这个函数来制作如下T恤：一件
# 印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size, word="I love Python"):
    """size and word"""
    print("The size of the shirt is " + size + ". And the word on it is " + word + ".")


make_shirt("L")
make_shirt(word="I love Lily", size="M")