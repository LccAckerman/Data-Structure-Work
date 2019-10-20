def  tower_of_Hanoi(num_disk):
    tower_of_Hanoi_helper(num_disk,'S','A','D')


def tower_of_Hanoi_helper(num_disk, from_rod, to_rod, aux_rod):
    if num_disk == 0:
        return
    if num_disk == 1:
        print("{}{}".format(from_rod, to_rod))
        return
    tower_of_Hanoi_helper(num_disk - 1, from_rod, aux_rod, to_rod)
    print("{}{}".format(from_rod, to_rod))
    tower_of_Hanoi_helper(num_disk - 1,aux_rod, to_rod, from_rod)

tower_of_Hanoi(5)