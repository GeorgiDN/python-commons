info = {"Sofia": {
    "coffee": 0.50,
    "water": 0.80,
    "beer": 1.20,
    "sweets": 1.45,
    "peanuts": 1.60,
    },
    "Plovdiv": {
        "coffee": 0.40,
        "water": 0.70,
        "beer": 1.15,
        "sweets": 1.30,
        "peanuts": 1.50,
    },
    "Varna": {
        "coffee": 0.45,
        "water": 0.70,
        "beer": 1.10,
        "sweets": 1.35,
        "peanuts": 1.55,
    }
}

print("The original dictionary")
print(info)
print()


print("Sorted by key alphabetically")
sorted_by_key = dict(sorted(info.items()))
print(sorted_by_key)
print()


print("Sorted by key alphabetically - reversed")
sorted_by_key = dict(sorted(info.items(), reverse=True))
print(sorted_by_key)
print()


print("Sorted by nested key alphabetically")
sorted_dictionary_by_nested_key = {}
for key, data in info.items():
    sorted_by_nested_key = dict(sorted(data.items()))
    sorted_dictionary_by_nested_key[key] = sorted_by_nested_key
print(sorted_dictionary_by_nested_key)
print()


print("Sorted by nested key alphabetically - reversed")
sorted_dictionary_by_nested_key_reversed = {}
for key1, data1 in info.items():
    sorted_by_nested_key_reversed = dict(sorted(data1.items(), reverse=True))
    sorted_dictionary_by_nested_key_reversed[key1] = sorted_by_nested_key_reversed
print(sorted_dictionary_by_nested_key_reversed)
print()


print("Sorted by specific key - coffee")
sorted_by_specific_nested_key_coffe = dict(sorted(info.items(), key=lambda x: x[1]["coffee"]))
print(sorted_by_specific_nested_key_coffe)
print()


print("Sorted by specific nested key - beer")
sorted_by_specific_nested_key_beer = dict(sorted(info.items(), key=lambda x: x[1]["beer"]))
print(sorted_by_specific_nested_key_beer)
print()


print("Sorted by specific nested key - beer")
sorted_by_specific_nested_key_beer = dict(sorted(info.items(), key=lambda x: x[1]["beer"]))
print(sorted_by_specific_nested_key_beer)
print()


print("Sorted by specific nested key - peanuts - reversed")
sorted_by_specific_nested_key_peanuts_reversed = dict(sorted(info.items(), key=lambda x: x[1]["peanuts"], reverse=True))
print(sorted_by_specific_nested_key_peanuts_reversed)
print()


print("Sorted by specific nested keys - first water then beer")
sorted_by_specific_nested_keys_water_then_beer = dict(sorted(info.items(), key=lambda x: (x[1]["water"], x[1]["beer"])))
print(sorted_by_specific_nested_keys_water_then_beer)
print()


print("Sorted by specific nested keys - first water then beer - reversed")
sorted_by_specific_nested_keys_water_then_beer_reversed = dict(sorted(info.items(), key=lambda x: (x[1]["water"], x[1]["beer"]), reverse=True))
print(sorted_by_specific_nested_keys_water_then_beer_reversed)
print()
