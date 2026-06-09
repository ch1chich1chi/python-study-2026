USER_ROLE = "user"
ASSISTANT_ROLE = "assistant"


def create_user_message(content):
    return {"role": USER_ROLE, "content": content}


def create_assistant_message(content):
    return {"role": ASSISTANT_ROLE, "content": content}
