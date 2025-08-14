from pyrogram import Client
import time

# Assistant account's string session
STRING_SESSION = "BQAf70YATsjv3hYTvQpa6Mm5mnP2pUWyzUjVR4M7HhIIbvSUxqXfi1vmWf61M9OdssH8OyZLIC2ZhjfKKsaAESGStJCex1XhDMA6NEANvGr0X8i6Fv7-HzwpaffeVSY9Ub15xgutcgXC2Nr39vst2HpuXiFtztfXAs8LqcO5xdKxq1dFDe-HjPFVPWQta7Ypr5dapqnVBqSnmBP_aIda4_v4jkBq6oIibWOmR8b4tWkw56soT2tyRLOQ69vHAqScJ3reN4fk2vHnSFKDO78rCp-TxC7O5gEgSvJGmhi5Y1K_n8pLUZeHtuNtKLZPQnxNrWneUaiMppoVzfmbYBLBlx6uHHd8kAAAAAGRn950AA"

# Owner's Telegram user ID
OWNER_ID = 6663845789

# Message you want to forward (replace with actual chat_id and message_id)
SOURCE_CHAT_ID = -1001234567890
SOURCE_MESSAGE_ID = 42

app = Client("assistant", session_string=STRING_SESSION)

@app.on_message()
def broadcast(_, message):
    if message.from_user and message.from_user.id != OWNER_ID:
        return
    
    start_time = time.time()
    total_chats = 0
    success_count = 0
    fail_count = 0
    
    for dialog in app.get_dialogs():
        chat_id = dialog.chat.id
        total_chats += 1
        try:
            app.forward_messages(
                chat_id=chat_id,
                from_chat_id=SOURCE_CHAT_ID,
                message_ids=SOURCE_MESSAGE_ID
            )
            success_count += 1
        except Exception as e:
            print(f"Failed to send to {chat_id}: {e}")
            fail_count += 1
    
    elapsed_time = round(time.time() - start_time, 2)
    print(
        f"📢 Broadcast Summary\n"
        f"Total Chats: {total_chats}\n"
        f"Successful: {success_count}\n"
        f"Failed: {fail_count}\n"
        f"Time Taken: {elapsed_time} sec"
    )

app.run()
