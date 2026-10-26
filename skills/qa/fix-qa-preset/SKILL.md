---
name: fix-qa-preset
description: "Sửa lỗi từ bảng QA Shopify theo vòng fix và hướng xử lý được người dùng ghi; Fix lần 1 chỉ preset, các lần sau theo phạm vi được giao; QA hồi quy, giữ lịch sử, tách cột Lần fix khỏi Trạng thái."
---

# Fix từ bảng QA theo vòng sửa

Kích hoạt khi người dùng nói **Fix lần N**, **fix từ bảng QA**, hoặc gọi `$fix-qa-preset`. Yêu cầu QA đơn thuần không cấp quyền sửa theme. Lần1 chỉ preset hoặc global settings hiện có trong `config/settings_data.json` local. Lần2 trở đi đọc ghi chú **Fix lần N** trong Hướng xử lý làm danh sách được giao; chỉ custom khi hướng dẫn của người dùng cho phép rõ việc đó, không suy quyền custom từ số vòng. Nếu người dùng đang chỉnh Sheet, đọc mới trước khi ghi và không ghi đè ghi chú của họ.

## Nguồn và ranh giới

- Đọc file tổng quan QA hiện có (`docs/qa/<page>-qa.md` hoặc `check-perfect-<page>.md`), các file section liên kết từ đó, Sheet được chỉ định và manifest QA hiện hành. Lấy lỗi từ **Sheet mới nhất**, không ghi đè chỉnh sửa của người dùng bằng snapshot local cũ. Xác nhận theme/template/instance và nguồn Desktop/Mobile; chỉ hỏi khi thông tin thật sự thiếu.
- Dùng [build-preset](../../build/preset/build-preset/SKILL.md) để map setting/composition, và [qa-theme-pixel-perfect](../qa-theme-pixel-perfect/SKILL.md) để kiểm và xuất báo cáo. Bản cài phẳng tìm các dependency trong `.agents/skills/<name>/SKILL.md`. Thiếu dependency thì báo đúng phần thiếu.
- **Lần 1 chỉ preset/config local**: setting đã có, composition bằng section/block hiện có, template/section-group JSON và global Theme Settings hiện có trong **config/settings_data.json local** đã xác minh. Không thêm control, đổi schema ngoài preset, sửa Liquid/CSS/JS/snippet, custom CSS, SVG hay hiệu chỉnh implementation/height. Các ngoại lệ custom/icon của build-preset **không áp dụng** cho lần này.
- Không đổi dữ liệu sản phẩm/media ở store, save Theme Editor, push/publish, commit hoặc cài thêm công cụ chỉ vì được yêu cầu fix preset. Giữ thay đổi người dùng và phạm vi ngoài lỗi được giao.

## 1. Chốt danh sách lỗi trước sửa

Lưu snapshot Sheet và checkpoint local trước mutation. Mỗi lỗi có key ổn định: page/template + instance ID + breakpoint + component + criterion + vòng QA; số hàng chỉ là vị trí hiện tại. Ghi nguyên giá trị Figma, hiện tại, hướng xử lý và trạng thái ban đầu.

Phân loại từng lỗi đã QA: sửa được bằng setting/composition nào; setting dùng riêng hay chung; không sửa được bằng preset; chưa đủ bằng chứng. Không sửa mục Khớp/Figma làm tròn/Không áp dụng hoặc Chưa xác minh theo suy đoán. Lỗi cần custom giữ nguyên dòng và trạng thái chưa giải quyết, ghi lý do giới hạn preset trong MD/hướng xử lý; không đổi thành Khớp chỉ vì đã xem xét.

## 2. Fix lần 1

Sửa các lỗi đã xác minh bằng preset hiện có. Với setting global, lập danh sách consumer trước khi đổi, ưu tiên control riêng nếu có; kiểm lại cả Desktop/Mobile và các consumer bị ảnh hưởng. Không đổi setting đúng để bù lỗi font, constraint, làm tròn hoặc khác viewport. Không dùng preset để lách thay đổi hành vi/dữ liệu ngoài yêu cầu.

Giữ mapping lỗi → file/instance/setting → trước/sau trong MD. Kiểm cấu trúc JSON/schema và validation theo quy tắc repo, rồi xác minh preview thực sự phản ánh cấu hình mới; preview cũ/chưa cập nhật không chứng minh đã fix. Nếu deploy cần quyền riêng mà chưa có, giữ kết quả chưa xác minh, không push ngầm và không đánh dấu đã fix.

## 3. QA toàn phạm vi sau fix

Sau khi sửa xong, chạy QA lại **toàn phạm vi theme trong manifest**, không chỉ các ô lỗi vừa sửa: tổng quan số lượng/thứ tự, từng section, Desktop/Mobile, typography, layout từ trong ra ngoài, media/crop, grid/scroll/control và các trạng thái có mẫu. Dùng checklist/quy ước đã học trong skill QA, đo mới, lưu ảnh và số đo mới. Đặc biệt rà ảnh hưởng của setting dùng chung lên phần trước đó đã khớp.

“Toàn theme” không được suy từ Homepage: duyệt các page/template hiện có trong manifest; trang thiếu Figma/preview được ghi rõ chưa kiểm, không loại khỏi mẫu số hoặc kết luận đạt. Nếu hồ sơ dự án hiện chỉ có Homepage thì kiểm đầy đủ Homepage và báo giới hạn đó; không tự bịa thiết kế cho trang khác. Có chỗ bị chặn thì tiếp tục phần độc lập, giữ checkpoint và nói rõ phần chưa xác minh.

## 4. Đồng bộ Sheet và MD trong cùng lượt

Áp dụng [hồ sơ QA theo section](../qa-section/references/qa-report-files.md) (bản cài phẳng: `qa-section/references/qa-report-files.md`): cập nhật kết quả hiện hành và thêm lịch sử vòng fix vào đúng file section, không tạo file MD riêng cho mỗi Fix lần N. Bảng nhiều section phải phân bổ về đúng file; nguồn/validation/hồi quy chung nằm ở tổng quan.

Ưu tiên API đọc/ghi/format theo [workflow Sheet QA](../qa-theme-pixel-perfect/references/sheet-api-workflow.md); đọc live trước mutation, chỉ dùng Computer Use cho xác minh/phần API không hỗ trợ khi đã được cho phép.

- **Giữ nguyên dòng lỗi và giá trị Figma/Hiện tại ban đầu**, không xóa hoặc gộp lịch sử vào pass summary. Số đo mới, mapping và vòng QA lưu trong MD.
- Bảng có10 cột: STT, Section, Thiết bị, Thành phần, Tiêu chí, Figma, Hiện tại, Hướng xử lý, **Lần fix**, **Trạng thái**. Lần fix đứng cạnh Trạng thái, dùng dropdown một lựa chọn đúng nhãn **Lần 1, Lần 2, Lần 3, Lần 4, Lần 5, Bỏ qua**; tối đa5 vòng. Không ghi số trần1/2. Khi migrate, chỉ đổi nhãn1→Lần 1,…,5→Lần 5; giữ vòng và trạng thái đã có, không coi đổi nhãn là một lượt fix mới.
- **Lần fix là cờ phân công vòng xử lý, không phải bằng chứng đã sửa.** Ngay lượt QA đầu, sau khi có Hướng xử lý cụ thể và xác minh lỗi có thể sửa bằng preset/composition hiện có hoặc config/settings_data.json, tự gắn **Lần 1**, vẫn giữ Trạng thái Chưa khớp. Cần map rõ setting/control và trước→sau, kiểm ảnh hưởng control dùng chung; một đề xuất chưa đủ bằng chứng/đổi Body làm sai weight không được tự coi là preset-fixable. Chỉ gắn cờ trong QA, chưa tự sửa theme khi chưa được yêu cầu fix.
- Mục Khớp từ đầu, Figma làm tròn, Không áp dụng hoặc Chưa xác minh không tự gắn Lần 1. Lỗi cần custom/thiếu control giữ cờ trống đến khi người dùng giao vòng phù hợp; không tự gắn Bỏ qua vì chưa sửa được. Giữ cờ do người dùng đã giao, không ghi đè bằng phân loại tự động. Khi thực hiện mà chưa đạt, giữ cờ vòng đó và trạng thái chưa giải quyết, lưu tình trạng planned/attempted/verified trong MD.
- **Bỏ qua trong Lần fix** chỉ gán theo quyết định người dùng về việc không đưa tiêu chí vào vòng sửa. Không tự chuyển Trạng thái sang Khớp; Trạng thái Bỏ qua vẫn là lựa chọn riêng cho quyết định bỏ qua tiêu chí, không ngầm đồng bộ hai cột khi người dùng chưa yêu cầu.

- **Chỉ đổi dropdown Trạng thái thành Khớp sau khi QA mới xác nhận đạt ở đủ thiết bị của dòng đó.** Không đưa số vòng vào nhãn trạng thái mới. Khi migrate bảng cũ, Đã fix (QA 1) → Lần fix “Lần 1” + Khớp dựa trên bằng chứng đã có; không gán vòng1 cho mọi dòng Khớp vốn có.
- Lỗi cũ còn tồn tại giữ nguyên dòng. Lỗi mới/regression sau fix chèn đúng section và nhóm thiết bị/thành phần, Trạng thái Chưa khớp; ghi vòng phát hiện QA trong MD, không dùng cột Lần fix thay vòng phát hiện. Chỉ gắn Lần 1 cho lỗi mới nếu đã có hướng xử lý preset/config được xác minh; vòng khác theo phân công người dùng. Giữ thứ tự tương đối mọi dòng cũ và các section khác.
- Giữ Hướng xử lý người dùng đã viết, nguồn ở cuối, merge và dropdown chip hiện hành. Chỉ chèn cột khi chưa có; không tạo trùng cột mỗi vòng. Chỉ chip có màu, ô thông thường không nền; Sau QA đạt và chuyển **Khớp**, bỏ nền màu cả hai ô **Figma/Hiện tại** nhưng giữ giá trị gốc. Chưa khớp đã xác minh vẫn Figma xanh/Hiện tại đỏ. Toàn bảng middle, header center/middle.
- Dropdown Trạng thái có **Bỏ qua**. Đây là quyết định bỏ qua tiêu chí, không đồng nghĩa Khớp hoặc Không áp dụng; chỉ gán khi người dùng chỉ định/chấp nhận bỏ qua, không tự dùng cho lỗi khó sửa hoặc chưa xác minh.
- Quy tắc giữ lịch sử trong chu kỳ fix ưu tiên hơn quy tắc QA thường xóa lỗi đã sửa/gộp summary. Yêu cầu người dùng mới nhất được ưu tiên hơn format phiên trước.

Đọc lại vùng đã đổi/chèn và các dòng lân cận, kiểm dropdown thật và giao diện. Lưu snapshot sau ghi cùng screenshot. Bàn giao lỗi fix đã QA đạt, lỗi chưa giải quyết, lỗi mới, phạm vi đã kiểm/chưa kiểm, link Sheet và MD; không tuyên bố QA toàn theme khi chỉ kiểm Homepage.

### Màu chip Lần fix

Lần fix dùng chip dropdown, chỉ chọn một giá trị: Lần 1 xanh dương #BFE1F6; Lần 2 tím #E6CFF2; Lần 3 cam #FFC8AA; Lần 4 vàng #FFE5A0; Lần 5 xanh lá #D4EDBC; Bỏ qua xám #E7E6E6. Cột rộng100px, nền ô không màu; giữ màu chip Trạng thái hiện có. Không tô cả ô/hàng theo vòng fix.

## File output/test và commit

Bắt buộc áp dụng [quy tắc loại trừ và dọn file kiểm tra](../../../references/task-artifacts.md) khi tạo output/test hoặc chuẩn bị commit. Bản cài phẳng đọc `references/task-artifacts.md` trong chính thư mục skill này.
