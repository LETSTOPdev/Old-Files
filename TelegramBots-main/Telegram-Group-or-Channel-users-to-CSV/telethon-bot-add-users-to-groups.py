from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import re

api_id = 22485485        # YOUR API_ID
api_hash = 'dc5093ab19672d777465be2f82e70091'        # YOUR API_HASH
phone = '+972559889800'        # YOUR PHONE NUMBER, INCLUDING COUNTRY CODE
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

def add_users_to_group():
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            try:
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
            except IndexError:
                print('Users without id or access_hash')
            users.append(user)

    chats = []
    last_date = None
    chunk_size = 10
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup:
                groups.append(chat)
        except:
            continue

    print('Choose a group to add members:')
    for i, group in enumerate(groups):
        print(f"{i} - {group.title}")

    g_index = input("Enter a Number: ")
    target_group = groups[int(g_index)]
    print(f'\n\nSelected Group:\t{target_group.title}')

    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    mode = int(input("Enter 1 to add by username or 2 to add by ID: "))

    error_count = 0

    for user in users:
        try:
            print(f"Adding {user['username']}")
            if mode == 1:
                if not user['username']:
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                sys.exit("Invalid Mode Selected. Please Try Again.")
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            print("Waiting 60 Seconds...")
            time.sleep(60)
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        except UserPrivacyRestrictedError:
            print("The user's privacy settings do not allow you to do this. Skipping.")
        except:
            traceback.print_exc()
            print("Unexpected Error")
            error_count += 1
            if error_count > 10:
                sys.exit('Too many errors')
            continue

def list_users_in_group():
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            print(chat)
            groups.append(chat)
        except:
            continue

    print('Choose a group to scrape members from:')
    for i, g in enumerate(groups):
        print(f"{i} - {g.title}")

    g_index = input("Enter a Number: ")
    target_group = groups[int(g_index)]

    print(f'\n\nSelected Group:\t{target_group.title}')

    print('Fetching Members...')
    all_participants = client.get_participants(target_group, aggressive=True)

    print('Saving in file...')
    with open(f"members-{re.sub('-+', '-', re.sub('[^a-zA-Z]', '-', target_group.title.lower()))}.csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
        for user in all_participants:
            username = user.username if user.username else ""
            first_name = user.first_name if user.first_name else ""
            last_name = user.last_name if user.last_name else ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
    print('Members scraped successfully.')

def printCSV():
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            users.append(user)
            print(row)
            print(user)
    sys.exit('FINITO')

print('What do you want to do:')
mode = int(input("Enter \n1-List users in a group\n2-Add users from CSV to Group (CSV must be passed as a parameter to the script)\n3-Show CSV\n\nYour option:  "))

if mode == 1:
    list_users_in_group()
elif mode == 2:
    add_users_to_group()
elif mode == 3:
    printCSV()