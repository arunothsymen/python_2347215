def string_split(stringsplit):
  
  print("The format want to be like: name ___ domain_namem ___ regno")
  stringsplit=input("Enter the details like given above: ")
  name = ""
  domain_name = ""
  regno = ""

  split_string = stringsplit.split("___")
  for item in split_string:
    if item != "":
      if name == "":
        name = item
      elif domain_name == "":
        domain_name = item
      elif regno == "":
        regno = item

  dictionary = {
    "name": name,
    "domain_name": domain_name,
    "regno": regno
  }
  return dictionary

dictionary = string_split('stringsplit')

print(dictionary)