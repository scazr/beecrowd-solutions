while True:
    try:
        INPUT = input(); INPUT = INPUT.split()
        num1 = int(INPUT[0]); num2 = int(INPUT[1]);
        print(num1 ^ num2)
    except EOFError:
        break
def Main(a, b):
  print(a^b)
if __name__ == '__main__':
  while True:
    try:
      a, b = map(int ,input().split())
    except EOFError:
      break
    Main(a, b)
