
def ladder_gcd_steps(a, b):
        original_a, original_b = a, b
        steps = []
        d = 2

        while d <= min(a, b):
            if a % d == 0 and b % d == 0:
                steps.append((a, b, d))
                a //= d
                b //= d
            else:
                d += 1

        # چاپ مراحل
        print(f"Steps for {original_a} and {original_b}: \n")
        for x, y, d in steps:
            print(f"{x:4}   {y:4}  |  {d}")

        # چاپ مرحلهٔ آخر (بدون مقسوم‌علیه مشترک)
        print(f"{a:4}   {b:4}  |  -")

        # محاسبهٔ ب‌م‌م
        gcd_value = 1
        for _, _, d in steps:
            gcd_value *= d

        print(f"\n GCD = {gcd_value}")
        return gcd_value


ques = "Y"
while ques != "N":
    a = int(input("Please Enter Your First Number in Integer: "))
    b = int(input("Please Enter Your Second Number in Integer: "))
    
    ladder_gcd_steps(a, b)
    
    ques = input("Wanna Do That Again: (Y or N) ").strip().upper()
    




