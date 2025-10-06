banner = r"""
██╗    ██╗██╗  ██╗██╗██╗     ███████╗    ██╗      ██████╗  ██████╗ ██████╗
██║    ██║██║  ██║██║██║     ██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
██║ █╗ ██║███████║██║██║     █████╗      ██║     ██║   ██║██║   ██║██████╔╝
██║███╗██║██╔══██║██║██║     ██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝
╚███╔███╔╝██║  ██║██║███████╗███████╗    ███████╗╚██████╔╝╚██████╔╝██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝
"""

watermark = "github.com/UsamaMatrix"
borders = "="

print(banner)
print(borders.center(40, "="))
print(watermark.center(40, " "))
print(borders.center(40, "="))

# Code: While loop print numbers 1 to 10
i = 1
print("\nNumbers from 1 to 10:")
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")
print(borders.center(40, "="))
print(borders.center(40, "="))

# Code: Modify to print even numbers between 1 and 20
print("\nEven numbers between 1 and 20:")
j = 2
while j <= 20:
    print(j, end=" ")
    j += 2
print("\n")
print(borders.center(40, "="))
