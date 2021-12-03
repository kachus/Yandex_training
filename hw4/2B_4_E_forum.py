n = int(input())
topics = []
dict_topics = {}
dict_order = {}
order_num = 0
count = 0
for i in range(n):
    number = int(input())
    order_num += 1
    if number ==0:
        topic = input()
        input()
        topics.append(topic)
        dict_topics[topic] = count #заполняем словарь с темами тема - количество сообщений
        dict_order[order_num] = topic
        
    else:
        input()
        dict_order[order_num] = dict_order[number]
        dict_topics[dict_order[number]]+=1
      
max_count = max(dict_topics.values())
for key in dict_topics.keys():
    if dict_topics[key] == max_count:
        print(key)
        break