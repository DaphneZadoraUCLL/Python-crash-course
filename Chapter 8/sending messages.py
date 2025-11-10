messages = [
    "Hello! How can I assist you today?",
    "Don't forget to check out our new features.",
    "Your account has been updated successfully.",
    "Thank you for your feedback!",
    "Please let us know if you need any further assistance."]
sent_messages = []


def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending following message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
