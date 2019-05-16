if __name__ == "__main__":
    fine_sum = 0  # money
    v, num = input().split()  # speed and number of car
    v = int(v)
    while (num[0] != "A" and
           num[1] != "5" and
           num[2] != "5" and
           num[3] != "5" and
           num[4] != "A" and
           num[5] != "A"):

        if v > 60:

            if (num[1] == num[2]
                or num[2] == num[3]
                    or num[1] == num[3]):

                if num[1] == num[2] == num[3]:
                    fine_sum += 1000
                else:
                    fine_sum += 500
            else:
                fine_sum += 100

        v, num = input().split()
        v = int(v)

    print(fine_sum)
