"""
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True

  return False

print(letter_check("strawberry", "a"))

def common_letters(string_one, string_two):
    common_list = []
    for character in string_one:
        if character in string_two and character not in common_list:
            common_list.append(character)

    return common_list

print(common_letters("treehouse", "treehouse"))

def username_generator(first_name, last_name):
    user_name = first_name[:3] + last_name[:4]
    return user_name

def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
        password = password + user_name[i - 1]
        i += 1
    return password

print(password_generator("AbeSimp"))
"""

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

author_last_name = []

for name in author_names:
    author_last_name.append(name.split()[-1])

print(author_last_name)

python_topics = ["variables", "control flow", "loops", "modules", "classes"]
