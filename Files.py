import csv
import os
import json

# # open and read a file
# with open('README.md') as text_file:
#     text_data = text_file.read()
#     print(text_data)
#
# # write a new file
# with open('bad_bands.txt', 'w') as bad_bands_doc:
#     bad_bands_doc.write('This is a bad band')
#
# # read a csv file to a dictionary
# cool_csv_list = []
# with open('cool_csv.csv', newline='') as cool_csv_file:
#     cool_csv_dict = csv.DictReader(cool_csv_file)
#     for row in cool_csv_dict:
#         print(row["Cool Fact"])
#         cool_csv_list.append(row)
#
# print(cool_csv_list)
#
# # read a csv file with a different type of delimiter
# isbn_list = []
# with open('books.csv', newline='') as books_csv:
#     books_reader = csv.DictReader(books_csv, delimiter='@')
#     for row in books_reader:
#         isbn_list.append(row['ISBN'])
# print(isbn_list)
#
# # open a file from a different directory
# script_dir = os.path.dirname(os.path.realpath('__file__'))
# print(script_dir)
# file_name = os.path.join(script_dir, 'Test_files/text1.txt')
# print(file_name)
# with open(file_name) as text_file:
#     text_data = text_file.read()
#     print(text_data)
#
# # write csv file
# access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
# fields = ['time', 'address', 'limit']
# with open('logger.csv', 'w') as logger_csv:
#     log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
#
#     log_writer.writeheader()
#     for item in access_log:
#         log_writer.writerow(item)
#
# # open json file
# with open('message.json') as message_json:
#     message = json.load(message_json)
# print(message['secret text'])
#
# # write json file
# data_payload = [
#   {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
#    'follow up': 'But enough talk!'}
# ]
# with open('data.json', 'w') as data_json:
#     json.dump(data_payload, data_json)

# Project - Hacking the Fender
compromised_users = []

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)

with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
    json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = ''' _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/'''
    new_passwords_obj.write(slash_null_sig)






