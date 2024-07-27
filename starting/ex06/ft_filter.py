def ft_filter(function, iterable):
    """
    ft_filter(function or None, iterable) --> iterator

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        # If function is None, return items that are true
        return (item for item in iterable if item)
    else:
        # Otherwise, apply the function to filter the items
        return (item for item in iterable if function(item))

# Example usage:
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = ft_filter(is_even, numbers)

print(list(filtered_numbers))  # Output: [2, 4, 6]
