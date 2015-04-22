# partial_dict_copy

this little tool copies over partial dictionaries.  It can either remove keys, values or both!

Here's the use case:

from partial_dict_copy import partial_copy

dicter = {"a":"b","c","d"}
print partial_copy(dicter,ignored_keys=["a"])
print partial_copy(dicter,ignored_values["b"])
print partial_copy(dicter,ignored_keys=["a","c"])
