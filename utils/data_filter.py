def remove_Duplicates(data, key):

    # Stores already encountered values to quickly detect duplicates
    seen_data = set()

    # Stores the final list containing only unique items
    unique_data = []

    # Iterate through each dictionary in the input list
    for item in data:

        # Extract the value associated with the specified key
        val = item.get(key)

        # Add the item only if its key value has not been seen before
        if val not in seen_data:
            seen_data.add(val)           # Mark the value as seen
            unique_data.append(item)     # Preserve the first occurence

    # Return the list with duplicate entries removed
    return unique_data



def keyword_Filter(data,key, keywords):

    # Stores items that match at least one of the specified keywords
    filtered_data = []

    # Iterate through each dictionary in the input list
    for item in data:

        
        # Get the value for the given key, convert it to lowercase for case-insensitive keyword matching
        text = str(item.get(key,"")).lower()

        # Check if any keyword exists in the text
        for word in keywords:
            if word.lower() in text:

                # Add the matching item to the result list
                filtered_data.append(item)
                break

    # Return all items that matched at least one keyword
    return filtered_data



def clean_empty_values(data, key):

    # Stores items that contain valid (non-emoty) values for the given key
    clean = []

    # Iterate through each dictionary in the input list
    for item in data:

        # Get the value associated with the specified key
        val = item.get(key)
        if val is not None and val!="":
            clean.append(item)

    return clean
