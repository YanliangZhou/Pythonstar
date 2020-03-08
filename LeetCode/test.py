# l1 = ["eat", "sleep", "repeat"]
#
# # printing the tuples in object directly
# for ele in enumerate(l1):
#     print (ele)
#
# # changing index and printing separately
# for count, ele in enumerate(l1):
#     print (count, ele)

favorite_languages = {
jen: python,
sarah: c,
}
for name in favorite_languages.keys():
    print(name.title())