def is_valid(driver, registered):
    for i in range(2):
        if driver[i] != registered[i]:
            return False
    return True


def check(driver, registered_list, arrested_list, num_suspects):
    for i in registered_list:
        if is_valid(driver, i):
            return False
        else:
            arrested_list.append(driver)
    if len(arrested_list) == num_suspects:
        return True
    else:
        return False