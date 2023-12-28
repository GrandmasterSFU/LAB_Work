# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, g = ","):
    participants_first_group = participants_first_group.split(g)
    participants_second_group = participants_second_group.split(g)
    common_participance = list(set(participants_first_group).intersection(participants_second_group))
    common_participance.sort()
    return common_participance
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"{find_common_participants(participants_first_group, participants_second_group, g = "|" )}")


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
