import json


memory_file="memory.json"


def load_memory():

    with open(memory_file,"r",encoding="utf-8") as file:

        return json.load(file)



def save_memory(memory):

    with open(memory_file,"w",encoding="utf-8") as file:

        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=4
        )



def add_memory(user,reply):

    memory=load_memory()


    memory["conversation"].append(
        {
            "user":user,
            "reply":reply
        }
    )


    save_memory(memory)


def get_recent_memory():

    memory=load_memory()

    return memory["conversation"][-5:]