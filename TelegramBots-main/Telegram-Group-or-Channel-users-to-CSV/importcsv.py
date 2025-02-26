import pandas as pd
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio

# Your API ID and Hash
api_id = '22485485'
api_hash = 'dc5093ab19672d777465be2f82e70091'
phone = '+972559889800'

# Create the client and connect
client = TelegramClient(phone, api_id, api_hash)

# Read the CSV file
users = pd.read_csv('members--official-the-sandbox.csv')

async def main():
    # Connect to the client
    await client.start()

    # Get the entity of the group
    group = await client.get_entity('https://t.me/LETSTOPChat')


    # Iterate over the users and add them to the group
    for index, row in users.iterrows():
        try:
            if 'username' in row and pd.notna(row['username']):
                user = await client.get_entity(row['username'])
            else:
                print(f"Skipping row {index} due to missing username.")
                continue

            print(f"Adding {user.username}")
            await client(InviteToChannelRequest(group, [user]))
            print(f"Added {user.username}")
            await asyncio.sleep(100)  # Sleep for 60 seconds to avoid hitting rate limits
        except FloodWaitError as e:
            print(f"Flood wait error: sleeping for {e.seconds} seconds.")
            await asyncio.sleep(e.seconds)
        except UserPrivacyRestrictedError:
            print(f"User {row['username']} has privacy settings that prevent you from adding them.")
        except Exception as e:
            print(f"Unexpected error: {e}")

async def run_with_retries():
    while True:
        try:
            await main()
            break
        except FloodWaitError as e:
            print(f"Flood wait error caught at top level: sleeping for {e.seconds} seconds.")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Unexpected error at top level: {e}")
            break

with client:
    client.loop.run_until_complete(run_with_retries())
