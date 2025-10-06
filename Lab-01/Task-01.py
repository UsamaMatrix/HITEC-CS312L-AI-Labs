banner = r"""
████████╗ █████╗ ██████╗ ██╗     ███████╗
╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝
   ██║   ███████║██████╔╝██║     █████╗
   ██║   ██╔══██║██╔══██╗██║     ██╔══╝
   ██║   ██║  ██║██████╔╝███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
"""

watermark = "github.com/UsamaMatrix"
borders = "="

print(banner)
print(borders.center(40, "="))
print(watermark.center(40, " "))
print(borders.center(40, "="))

# Code: Multiplication Table
num = int(input("Enter a number to print its table: "))
print(borders.center(40, "="))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
