def count_vowel(st):
  count = 0
  for i in st.lower():
    if i in ['a','e','i','o','u']:
      count += 1
  return count

st = input("enter a string: ")

print(count_vowel(st))