def decode_int(value, index):
    end_index = value.find('e', index)

    return int(value[index + 1:end_index], 10), end_index + 1


def decode_array(value, index):
    parsed_array = []

    index += 1
    while value[index] != 'e':
        parsed_content, index = decode_content(value, index)
        parsed_array.append(parsed_content)

    return parsed_array, index + 1


def decode_dict(value, index):
    parsed_dict = {}

    index += 1
    while value[index] != 'e':
        key, index = decode_string(value, index)
        parsed_value, index = decode_content(value, index)
        parsed_dict[key] = parsed_value

    return parsed_dict, index + 1


def decode_string(value, index):
    colon_index = value.find(':', index)
    value_length = int(value[index:colon_index])

    end_index = colon_index + value_length + 1

    parsed_value = value[colon_index + 1:end_index]

    return parsed_value, end_index


def decode_content(content, index):
    value = content[index]

    if value == 'i':
        return decode_int(content, index)

    if value == 'l':
        return decode_array(content, index)

    if value == 'd':
        return decode_dict(content, index)

    if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return decode_string(content, index)

    raise Exception('Content type unknown.')


def decode(content):
    if content is None:
        return None

    value, _ = decode_content(content, 0)

    return value
