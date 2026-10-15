my_keys = ["id", "name", "age"]


def get_cats_info(path):
    try:
        cats_list = []
        with open (path, "r", encoding="utf-8" ) as file:            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cats_list.append(dict(zip(my_keys, line.split(","))))
        return cats_list
    except FileNotFoundError:
        return "File not found"
    