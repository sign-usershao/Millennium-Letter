import json

from dialogue import get_reply
from memory import add_memory, get_recent_memory
from ai import ask_ai


print("==== 千年回信 ====")


print("""
请选择你想遇见的李白：

1. 少年李白（18岁）
2. 长安李白（42岁）
3. 晚年李白（60岁）

""")


choice=input("请输入编号：")


if choice=="1":

    filename="千年回信/characters/libai_young.json"

elif choice=="2":

    filename="千年回信/characters/libai_changan.json"

elif choice=="3":

    filename="千年回信/characters/libai_old.json"

else:

    print("选择错误")
    exit()



with open(filename,"r",encoding="utf-8") as file:

    libai=json.load(file)



while True:


    question=input("你：")


    if question=="退出":
        break



    #读取历史记忆

    history=get_recent_memory()



    #生成李白人格提示词

    prompt=get_reply(
        question,
        libai,
        history
    )


    #交给AI生成回答

    answer=ask_ai(prompt)



    print(
        libai["name"]+"："
    )

    print(answer)



    #保存真实对话

    add_memory(
        question,
        answer
    )


    print()