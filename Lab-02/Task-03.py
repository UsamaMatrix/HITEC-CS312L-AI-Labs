banner = r"""
██████╗ ██╗ ██████╗
██╔══██╗██║██╔════╝
██████╔╝██║██║  ███╗
██╔══██╗██║██║   ██║
██████╔╝██║╚██████╔╝
╚═════╝ ╚═╝ ╚═════╝
"""
watermark = "github.com/UsamaMatrix"
borders = "="

print(banner)
print(borders.center(40, "="))
print(watermark.center(40, " "))
print(borders.center(40, "="))

nums = [1, 2, 4, 2, 6]
print("Largest:", max(nums))  # 6
