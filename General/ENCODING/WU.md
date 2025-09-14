# Encoding
- Bài 1: ASCII
    Dựa vào định dạng kết quả là crypto{} và dùng bảng mã ASCII với hệ thập phân, đối chiếu được kết quả là crypto{ASCII_pr1nt4bl3}

- Bài 2: Hex
    Dựa vào định dạng kết quả là crypto{} và dùng bảng mã ASCII với hệ thập lục phân, đối chiếu được kết quả là crypto{ASCII_pr1nt4bl3}

- Bài 3: Base64
     Để chuyển chuỗi hex thành byte, lấy từng cặp của chuỗi hex rồi chuyển thành nhị phân (0x72 <=> 01110010)
     1 ký tự của chuỗi Base64 tương đương 6 bit, t nhóm chuỗi nhị phân trên thành mỗi nhóm 6 bit rồi tra bảng Base64
            
- Bài 5: Encoding Challenge
    Đọc file server 13377.py, em thấy:
        - Mỗi level sẽ chọn ngẫu nhiên 3 từ và ghép bằng _
        - Chọn ngẫu nhiên 1 trong 5 loại mã hóa và trả về JSON chứa thông tin của type và encoded
    Suy ra file pwntool cần bổ sung code để decode đúng với từng trường hợp:
        - Hàm nhận và gửi JSON
        - If elif cho các loại type và cách decode
        - Loop cho đến khi nhận được flag