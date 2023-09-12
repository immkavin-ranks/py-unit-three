def main():
  infile = open('grandmasters.txt', 'r')
  line1 = infile.readline()
  line2 = infile.readline()
  line3 = infile.readline()
  infile.close()
  print(line1 + line2 + line3)
main()
