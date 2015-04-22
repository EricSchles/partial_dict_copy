def partial_copy(dicter,ignored_keys=[],ignored_values=[]):
    if ignored_keys == [] and ignored_values == []:
        return dicter.copy()
    elif ignored_keys != [] and ignored_values == []:
        copied_dict = dicter.copy()
        for key in ignored_keys:
            del copied_dict[key]
        return copied_dict
    else:
        copied_dict = dicter.copy()
        for key in ignored_keys:
            del copied_dict[key]
        for key in copied_dict.keys():
            for value in ignored_values:
                if value == copied_dict[key]:
                    del copied_dict[key]
        return copied_dict
