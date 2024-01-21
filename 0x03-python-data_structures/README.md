# 0x03. Python - Data Structures: Lists, Tuples

# Lists

A list in Python is an ordered collection of items which can be of any type. Lists are mutable, meaning the values in a list can be changed.

### Creating a List

```Python
my_list = [1, 2, 3, 'Python', 'Data Structures']
```
## Accessing List Elements

```Python
first_element = my_list[0]  # Output: 1
last_element = my_list[-1]  # Output: 'Data Structures'
```
## Modifying a List

```Python
my_list[3] = 'Java'  # The fourth element is now 'Java'
```

# Tuples

A tuple in Python is similar to a list. The main difference is that tuples are immutable, meaning the values in a tuple cannot be changed.

## Creating a Tuple

```Python
my_tuple = (1, 2, 3, 'Python', 'Data Structures')
```

## Accessing Tuple Elements

```Python
first_element = my_tuple[0]  # Output: 1
last_element = my_tuple[-1]  # Output: 'Data Structures'
```

## Trying to Modify a Tuple

```Python
my_tuple[3] = 'Java'  # This will raise a TypeError
```
