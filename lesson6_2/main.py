# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.
import json
import pickle

with open('../lesson6_1/group.json', 'r', encoding='utf-8') as f_json:
    my_favourite_group = json.load(f_json)
    print('from_json => ', my_favourite_group)

with open('../lesson6_1/group.pickle', 'rb') as f_pickle:
    my_favourite_groups = pickle.load(f_pickle)
    print('from_pickle => ', my_favourite_groups)
