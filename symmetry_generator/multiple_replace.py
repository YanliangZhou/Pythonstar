import re
def multiple_replace(text, adict):
     rx = re.compile('|'.join(map(re.escape, adict)))
     def one_xlat(match):
           return adict[match.group(0)]
     return rx.sub(one_xlat, text)


if __name__ == "__main__":
       text = 'X123,X124,X125,X134,X135,X145,X234,X235,X245,X345'
       P = str(text)
       a=str(1)
       b=str(3)
       adict = {
          a : "3",
          b : "1",
         }
       print(multiple_replace(text, adict))
