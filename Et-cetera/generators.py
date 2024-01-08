def main():

  n = int(input("what is N? "))
  for s in sheep(n):
    print(s)

def sheep(n):
  for i in range(n):
    yield "Fuck"* i


if __name__ == "__main__":
 main()
        