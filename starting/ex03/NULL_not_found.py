def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"Nothing: None <class 'NoneType'>")
        elif isinstance(object, float) and object != object: 
            print(f"Garlic: nan <class 'float'>")
        elif object == 0 and isinstance(object, int):
            print(f"Zero: 0 <class 'int'>")
        elif object == '':
            print(f"Empty: <class 'str'>")
        elif object is False:
            print(f"Fake: False <class 'bool'>")
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
