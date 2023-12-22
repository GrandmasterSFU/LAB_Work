# TODO Найдите количество книг, которое можно разместить на дискете
number_of_pages = 100
number_of_lines = 50
number_of_simbol = 25
disk_size = 1.44 * 1024 * 1024
number_of_book = disk_size // (4 * number_of_simbol * number_of_lines * number_of_pages)
print("Количество книг, помещающихся на дискету:", int(number_of_book))
