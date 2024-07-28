from typing import List, Union

def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Height list must contain only integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Weight list must contain only integers or floats.")
    
    bmi_list = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = w / (h * h)
        bmi_list.append(bmi)
    return bmi_list

def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI list must contain only integers or floats.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    return [b > limit for b in bmi]
