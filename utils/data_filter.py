def remove_Duplicates(data, key):

    # Stores already encountered values to quickly detect duplicates
    seen_data = set()

    # Stores the final list containing only unique items
    unique_data = []

    # Iterate through each dictionary in the input list
    for item in data:

        # Extract the value associated with the specified key
        val = item.get(key)

        if val not in seen_data:
            seen_data.add(val)
            unique_data.append(item)

    return unique_data


def keyword_Filter(data,key, keywords):
    filtered_data = []

    for item in data:
        text = str(item.get(key,"")).lower()

        for word in keywords:
            if word.lower() in text:
                filtered_data.append(item)
                break
        
    return filtered_data


def clean_empty_values(data, key):
    clean = []

    for item in data:
        val = item.get(key)
        if val is not None and val!="":
            clean.append(item)

    return clean
