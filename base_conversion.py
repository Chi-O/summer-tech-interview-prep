def convertDectoBase(n, base):
  if n == 0:
    return "" + str(n % base) 
  else:
    return (convertDectoBase(n // base, base) + str(n % base))

def convert(n, base):
  if n >= 1:
    convert(n // base, base)
  print(n % base, end="") 

def get_binary(n):
  return str(bin(n)).replace("0b", "")

if __name__ == "__main__":
  print(get_binary(17))