def time_format_check(time_str):
    import time

    if len(time_str)>5:
        return False

    try:
        time.strptime(time_str, '%H:%M')
        return True
    except:
        return False



print(time_format_check("08:69"))
print(time_format_check("08:59"))
print(time_format_check("45:00"))
print(time_format_check("0:0"))
print(time_format_check("00:1"))
print(time_format_check("39:60"))
