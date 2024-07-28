def slice_me(family: list, start: int, end: int) -> list:
    # Check if family is a list of lists and if all inner lists have the same length
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise TypeError("Input must be a 2D list.")
    
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("All inner lists must have the same length.")
    
    rows = len(family)
    cols = len(family[0]) if rows > 0 else 0
    print(f"My shape is : ({rows}, {cols})")
    
    sliced_family = family[start:end]
    
    new_rows = len(sliced_family)
    new_cols = len(sliced_family[0]) if new_rows > 0 else 0
    print(f"My new shape is : ({new_rows}, {new_cols})")
    
    return sliced_family
