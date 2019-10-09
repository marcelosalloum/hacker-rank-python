# hacker-rank-python
A few HackerRank solutions, written in Python3

## Cheatsheet

### Hashtables

* `is_key_on_dict = key in dict.keys()`

### Array
* `count_grather_than_5 = sum(i > 5 for i in j)`

```python
def upper_bound(list, number):
    base_list = [x for x in list if x > number]
    return min(base_list) if len(base_list) > 0 else None

def lower_bound(list, number):
    base_list = [x for x in list if x < number]
    return max(base_list) if len(base_list) > 0 else None
```