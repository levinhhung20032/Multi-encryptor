# Multi-encryptor

## I. Lời nói đầu

Đây là sản phẩm của Lê Vĩnh Hưng:

    - MSV: 21011494
    - K15-KHMT
    - Đại học Phenikaa.

Ứng dụng được viết nhằm mục đích phục vụ học phần "An toàn và bảo mật thông tin".

Nếu có góp ý chỉnh sửa vui lòng liên hệ trực tiếp.

## II. Bố cục tập tin

- Controller: Logic chính của ứng dụng.

    - Mỗi chương trình sẽ chứa hàm mã hóa và hàm giải mã của hệ mã hóa cùng tên.
 
- Data: Cơ sở dữ liệu của ứng dụng.

    - text.txt: Chứa nội dung bản rõ.
    - crypt.txt: Chứa nội dung bản mã.
    - input_backup.txt: Tôi đã chuẩn bị một đoạn text sẵn để người dùng có thể thử nghiệm.

- Image: Các tệp hình ảnh phục vụ nhu cầu thẩm mĩ của ứng dụng.

- Model: Các giao thức tương tác với cơ sở dữ liệu.

- View: Giao diện của ứng dụng.

- Multi-encryptor.exe: Ứng dụng chính.

- README.pdf: Giới thiệu và hướng dẫn sử dụng.

## III. Hướng dẫn sử dụng

### Khởi động

Kích đúp vào Multi-encryptor.exe để mở giao diện chính của ứng dụng.

- Hai vùng trắng được sử dụng để nhập hoặc hiển thị thông tin và bản rõ và bản mã của đoạn thông tin đang thao tác.
- Hộp chọn được sử dụng để chọn hệ mã hóa muốn sử dụng.
- Thanh ghi được sử dụng để điền hệ số k phục vụ cho hệ mã hóa đã chọn.
- Nút lệnh "Encrypt" thực hiện lấy thông tin bản rõ và mã hóa.
- Nút lệnh "Decrypt" thực hiện lấy thông tin bản mã và giải mã.

### Thao tác trên ứng dụng

#### Mã hóa

- Điền đoạn văn bản mong muốn vào vùng trắng của bản rõ.
  - Đoạn văn bản này sẽ được lưu vào cơ sở dữ liệu "Data/text.txt".
- Chọn hệ mã hóa phù hợp (Ứng dụng chỉ mới phát triển Caesar Cipher và sẽ thêm
những hệ mã hóa khác trong tương lai).
- Chọn hệ số k phù hợp với hệ mã hóa vừa chọn.
- Nhấn nút lệnh "Encrypt".
- Bản mã sẽ được hiện lên ở vùng trắng của bãn mã.
  - Đoãn mã này sẽ được lưu vào cơ sở dữ liệu "Data/crypt.txt"

> Bạn cũng có thể nhấn "Encrypt" khi chưa có bất kì nội dung nào trong vùng ghi của bản rõ. 
> Việc này sẽ khiến vùng ghi của bản rõ hiển thị thông tin được lưu trong cơ sở dữ liệu từ trước (bản rõ được thao tác gần đây nhất).
> Ngoài ra bạn cũng có nhấn "Encrypt" lần nữa nếu chưa điền khóa k để phần mềm tự tạo một khóa k và điền vào thanh ghi

#### Giải mã

- Điền đoạn văn bản mong muốn vào vùng trắng của bản mã.
  - Đoạn văn bản này sẽ được lưu vào cơ sở dữ liệu "Data/crypt.txt".
- Chọn hệ mã hóa phù hợp (Ứng dụng chỉ mới phát triển Caesar Cipher và sẽ thêm
  những hệ mã hóa khác trong tương lai).
- Chọn hệ số k phù hợp với hệ mã hóa vừa chọn.
- Nhấn nút lệnh "Decrypt".
- Bản rõ sẽ được hiện lên ở vùng trắng của bãn rõ.
  - Bản rõ này sẽ được lưu vào cơ sở dữ liệu "Data/text.txt"

> Bạn cũng có thể nhấn "Decrypt" khi chưa có bất kì nội dung nào trong vùng ghi của bản mã.
> Việc này sẽ khiến vùng ghi của bản mã hiển thị thông tin được lưu trong cơ sở dữ liệu từ trước (bản mã được thao tác gần đây nhất).

#### Thử nghiệm

> Tôi đã chuẩn bị một đoạn văn bản được lưu trong "Data/input_backup.docx" nhằm mục đích thử nghiệm.
> Người dùng có thể sao chép đoạn văn bản này để thử nghiệm mã hóa.
