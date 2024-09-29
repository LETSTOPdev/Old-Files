import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['messages']  # Assuming the messages are under the key 'messages'

def count_messages(data):
    message_count = {}
    for item in data:
        user_id = item.get('from_id', 'Unknown User')
        user_name = item.get('from', 'Anonymous')  # Get the user's name
        user_key = (user_id, user_name)  # Combine user_id and user name into a tuple

        if user_key not in message_count:
            message_count[user_key] = 0
        message_count[user_key] += 1
    return message_count

def get_top_senders(message_count, top_n=1000):
    sorted_senders = sorted(message_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_senders[:top_n]

def main():
    file_path = r'C:\Users\Almog\Desktop\Pythonbots\ChatExport_2024-05-13\result.json'  # Update this path to your actual file path
    data = read_json_file(file_path)
    message_count = count_messages(data)
    top_senders = get_top_senders(message_count)

    for (user_id, user_name), count in top_senders:
        print(f'User {user_name} ({user_id}) sent {count} messages')

if __name__ == '__main__':
    main()
