import random

def return_user_agent():
    agent_list = ["Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
                  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"]
    choose = random.randint(0, len(agent_list) - 1)
    return agent_list[choose]
