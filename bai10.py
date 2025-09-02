max_cot = 11  # bề rộng tối đa (cứ để số lẻ sẽ đẹp hơn)

# TỰ CHỌN độ rộng cho từng hàng (bao nhiêu cũng được)
hang_widths = [1, 3, 7, 3, 5, 7, 11]

# in phần lá (theo danh sách trên)
for w in hang_widths:
    space = (max_cot - w) // 2
    print(" " * space + "*" * w)

# in thân cây (ví dụ: rộng 1 cột, cao 3 hàng)
than_rong = 1
than_cao = 3
space = (max_cot - than_rong) // 2
for _ in range(than_cao):
    print(" " * space + "*" * than_rong)
