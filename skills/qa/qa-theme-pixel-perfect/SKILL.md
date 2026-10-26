---
name: qa-theme-pixel-perfect
description: "Kiểm toàn theme Shopify với Figma theo từng section: đủ/thiếu thành phần, bố cục rồi nội dung, typography, màu, kích thước, grid/slide và navigation/pagination. Nhóm tiêu chí dưới ô thành phần gộp dọc, xuất báo cáo tiếng Việt gọn vào Google Sheet được chỉ định; không tự sửa theme."
---

# QA pixel-perfect toàn theme

Kiểm tuần tự từng section trên desktop/mobile: **quét tổng quan → kiểm từng thành phần → kiểm grid/slide và control → ghi Sheet**. Kiểm chi tiết nhưng báo cáo gọn; không đổ dữ liệu kỹ thuật thành hàng trăm dòng. “Pixel-perfect” là mục tiêu kiểm, không phải kết luận mặc định.

## Tab và group Google Chrome

Khi dùng Chrome cho task, bắt buộc áp dụng [vòng đời tab/group dùng chung](../../../references/browser-session.md). Bản cài phẳng đọc `references/browser-session.md` trong chính thư mục skill này.

## File Figma tạm để đọc giá trị cụ thể

Chủ dự án cho phép copy đúng section/layer cần QA sang [Layouthub-copy](https://www.figma.com/design/GUJw3Y8gUBn8C5rISC5FPV/Layouthub-copy) để inspect giá trị px thực khi nguồn chỉ hiện token/instance hoặc khó đọc. Đây là ngoại lệ có phạm vi cho quy tắc chỉ đọc Figma bên dưới: không sửa file thiết kế gốc. Trước khi paste, ghi nhận page/nội dung có sẵn ở file tạm; theo dõi đúng node/page mới tạo trong lượt và nguồn gốc, mode Desktop/Mobile. Với radius: sau khi copy đúng layer sang file tạm, số px hiển thị trực tiếp là giá trị chốt để đối chiếu theme. Không tiếp tục để “Chưa xác minh” chỉ vì nguồn hiện token như lg hoặc tên tag/breakpoint không khớp; designer có thể gắn sai nhãn. Không tự đổi mode để ép số theo tên Desktop/Mobile. Ghi số đọc được và node nguồn/bản copy làm bằng chứng; không tự đặt một con số khi chưa inspect. Nếu phải detach/unbind, chỉ thao tác trên bản tạm và ghi rõ thao tác.

Ví dụ do người dùng cung cấp để học cách đọc radius (không thay nguồn thiết kế Kinetra): [Skinora — node nguồn](https://www.figma.com/design/U93PY3yeu6sZbQLnF7LJTt/?node-id=52576-17716) → [Layouthub-copy — node tham chiếu](https://www.figma.com/design/GUJw3Y8gUBn8C5rISC5FPV/Layouthub-copy?node-id=9994-292). Đây là node có sẵn, không thuộc phạm vi cleanup của lượt QA mới.

Sau khi QA và lưu đủ bằng chứng local, reset bằng cách xóa đúng phần đã copy/tạo trong lượt, xác nhận không còn node tạm và nội dung có sẵn vẫn nguyên. Không xóa cả file hoặc dọn nội dung không do lượt QA tạo. Nếu copy bị chặn bởi quyền nguồn thì báo đúng chỗ vướng, không vượt hạn chế copy/export. Nếu cleanup bị chặn, ghi rõ phần còn lại để tiếp tục dọn, không báo đã reset. Link này là nơi QA tạm của dự án hiện tại, không mặc định dùng cho dự án khác.

## Phạm vi và nguồn

- Tái sử dụng [qa-section](../qa-section/SKILL.md) cho cách đọc nguồn, đo viewport/computed style, truy nguyên typography/màu và lưu bằng chứng. Trước khi đọc Figma, áp dụng [contract Figma dùng chung](../../build/preset/theme-style-guide/references/figma-access.md). Bản cài phẳng tìm các dependency `qa-section` và `theme-style-guide` trong `.agents/skills/`; thiếu dependency thì báo đúng phần thiếu, tiếp tục phần độc lập.
- Tái sử dụng theme/preview, Figma desktop/mobile, Style Guide và Sheet đã được người dùng cung cấp. Active file IDE không quyết định theme đích. Khi chỉ tạo/bảo trì skill, không cần hỏi link QA mới hoặc tự chạy lại QA.
- Trước khi hỏi nguồn, đọc file tổng quan QA hiện có (`docs/qa/<page>-qa.md` hoặc `check-perfect-<page>.md`) và các file section liên kết từ đó để lấy link Figma, preview, sheet, định dạng báo cáo và checkpoint. Tái sử dụng dữ liệu đã lưu, xác minh còn đúng đích; chỉ hỏi trường còn thiếu, không tự đoán hoặc ghi đè nguồn mới hơn trong hội thoại.
- Chỉ đọc theme, Figma, storefront và Theme Editor; chỉ ghi báo cáo QA vào file Sheet được chỉ định. Không sửa code/config/media, Save Theme Editor, commit/push/publish, đổi sharing hay gửi thông báo.
- “Toàn theme” gồm các section instance trên các template/page hiện có, kèm Header/Footer và overlay có trong thiết kế. Một instance không đại diện mọi preset hoặc instance cùng loại. Không tự mở rộng thành QA release/editor/checkout hay tạo đơn.
- Giữ manifest local: page/template → resource preview thực → instance ID/type/order → node desktop/mobile → trạng thái cần kiểm. Trang thiếu thiết kế/preview vẫn phải có trong phạm vi chưa kiểm; không tự đoán URL hoặc loại khỏi mẫu số. Chỉ tóm tắt các trang thiếu nguồn ở cuối bảng chính.

## Khởi tạo Sheet ngay khi bắt đầu QA

Đọc [sheet-style.json](assets/sheet-style.json) làm mẫu mặc định đã ghi nhớ và áp dụng [workflow API](references/sheet-api-workflow.md) ngay ở bước0 trên tab mới/trống đã được giao. Lưu style version/path trong hồ sơ page; không chờ cuối page hoặc hỏi lại các lựa chọn đã chấp nhận. Tab có dữ liệu phải đọc live và giữ chỉnh sửa người dùng.

## 1. Quét tổng quan section

### Bước 0: Tổng quan page/template

Trước khi đi sâu từng section, đối chiếu danh sách section của page với Figma trên desktop/mobile: số lượng, thứ tự, width và padding. Giới hạn theo page người dùng yêu cầu; QA homepage không đại diện toàn theme. Ghi ngay nhóm **STT 0 · Section: Tổng quan · Thiết bị: Desktop, Mobile** với ba thành phần **Số lượng section**, **Thứ tự section**, **Width / Padding** theo [quy tắc báo cáo](references/sheet-report.md). Bao gồm announcement bar/header/footer khi thiết kế có; phân biệt với số section nội dung.

Nếu người dùng đang huấn luyện từng bước, hoàn thành và ghi Sheet bước hiện tại rồi dừng trao đổi trước khi chuyển bước/section. Hỏi đúng điểm mắc khi gặp, không tự chạy tiếp toàn bộ checklist. Sau mỗi hướng dẫn mới, cập nhật quy tắc vào skill nguồn và reference sở hữu quy tắc đó ngay trong lượt; giữ phạm vi/điều kiện của hướng dẫn, không biến ngoại lệ tạm thời thành chuẩn chung.

**Quy ước tạm thời được chủ dự án chấp nhận cho Kinetra homepage:** lấy width theo section lớn nhất trong Figma làm chuẩn đối chiếu ở bước tổng quan. Không báo lỗi chỉ vì container con của Confidence in every move rộng 1600px trong Figma và 1805px trên theme. Người dùng đã xác nhận cả tiêu chí **Width / Padding** của **STT 0 — Tổng quan**, thiết bị **Desktop, Mobile**, là **Khớp**; cập nhật dropdown và nội dung Sheet tương ứng, không tiếp tục giữ Chưa xác minh cho mục đã được xác nhận. Ghi đây là chấp nhận theo quy ước QA của người dùng, không mô tả thành kết quả đo đầy đủ từng section/breakpoint. Không áp mặc định sang dự án hoặc tiêu chí khác.

Lấy Figma làm danh sách gốc rồi đối chiếu giao diện, không lấy DOM hiện tại làm danh sách chuẩn.

| Cần xác nhận | Cách kiểm |
| --- | --- |
| Đủ thành phần chưa? | Liệt kê Eyebrow, Heading, Text, Button, icon, ảnh/video, card, badge, navigation, pagination… Xác nhận đủ/thiếu/thừa, số lượng, thứ tự và nội dung chính. Loại trừ trường hợp nằm ở slide khác, bị ẩn theo breakpoint hoặc chưa tải trước khi kết luận thiếu. |
| Bố cục tổng thể đúng chưa? | So thứ tự, vị trí, hướng xếp, full/page width, bố trí content/media, số cột, căn lề, padding/gap giữa các cụm. Không chỉ kiểm chiều cao section. |
| Cụm Header đúng chưa? | Nếu Figma có cụm eyebrow/heading/text/button, kiểm có nhóm bọc phù hợp theo contract theme; thường là Header. So cả căn giữa/trái/phải, chiều rộng và thứ tự trong cụm. Ví dụ Figma căn giữa thì cả cụm và text phải căn giữa tương ứng; chỉ có block Header chưa đủ kết luận đúng layout. |
| Desktop/mobile có đổi layout không? | So đúng thiết kế từng breakpoint về thứ tự, alignment, số item và thành phần ẩn/hiện; không suy mobile từ desktop. |

Header là composition thường dùng, không bắt buộc cho mọi section. Khi kiểm cấu trúc Header phải có bằng chứng source/editor; chỉ nhìn giao diện chưa chứng minh được block tree. Không tự rebuild khi thiếu bằng chứng.

Ghi **một dòng Tổng quan layout** cho section/breakpoint: vừa xác nhận đủ/thiếu thành phần, vừa nêu bố cục/căn chỉnh khớp hay lệch. “Đủ thành phần” không đồng nghĩa layout đúng hoặc section đã pixel-perfect.

## 2. Đi sâu từng thành phần, từ nhỏ đến lớn

Duyệt danh sách đã lập ở bước 1. Với **mỗi block/thành phần**, kiểm các thuộc tính áp dụng rồi **gộp dọc ô tên thành phần**, cạnh đó là các dòng tiêu chí như Nội dung, Typo, Màu, Kích thước. Nhóm font/weight/size/line-height/tracking dưới tiêu chí Typo, nhưng chỉ xuất thuộc tính lệch/chưa xác minh thành một hàng Sheet để so Figma và Hiện tại; không dùng list nhiều thuộc tính trong cùng ô.

Đặt tên thành phần theo tên block tiếng Anh đã xác minh trong schema/locale của repo, thêm ngữ cảnh cha trong ngoặc khi cần theo [quy tắc tên thành phần](references/sheet-report.md#cây-thành-phần-thực-tế). Nội dung như tên người hoặc nhãn nút chỉ ghi trong tiêu chí Nội dung.

| Thành phần | Nội dung cần đối chiếu |
| --- | --- |
| Eyebrow / Heading / Text | Đúng câu và dấu câu; font thực đã tải, weight/style, size, line-height, tracking, case, xuống dòng; màu; căn lề, width/height và khoảng cách. |
| Button | Đủ và đúng nhãn/icon; typography, màu chữ/nền/viền; width/height, padding, border/radius, kích thước và gap icon. |
| Icon / badge/tag | Đúng hình/nhãn; màu nền/chữ/stroke, kích thước, vị trí và khoảng cách. Sale và Sold out cần kiểm riêng khi thiết kế có cả hai. |
| Ảnh/video | Đúng media desktop/mobile; crop/focal point, tỷ lệ, object-fit, overlay, kích thước và vị trí. |
| Product card / card khác | Đủ ảnh, tên, giá, badge và nút theo thiết kế; kiểm từng thành phần bên trong rồi so khung thẻ và gap. Với card lặp, nêu rõ item/biến thể đã kiểm, không suy toàn bộ từ card đầu. |

- Đọc thông số Figma thật và CSS/box thực tế; không suy HEX hoặc px từ thumbnail. Chờ font/media và entrance animation ổn định trước khi đo. Đo vị trí tương đối với section ở viewport phù hợp; phân biệt scrollbar, zoom, padding của block và padding section theo `qa-section`.
- Với kích thước Text, kiểm typography trước. Nếu font family/variant, weight, size, line-height hoặc letter-spacing chưa khớp thì không kiểm/báo thêm dòng Kích thước chỉ do chữ lệch theo typography; bỏ dòng và hướng xử lý kích thước phụ thuộc đã tạo. Chỉ bổ sung Kích thước khi typography đã khớp mà box vẫn lệch. Nếu có bằng chứng sai khác do trình duyệt render/làm tròn, dùng trạng thái **Browser render không khớp**, ghi số đo/bằng chứng và kiểm trình duyệt trước khi đề xuất custom. Không gán nguyên nhân browser chỉ vì chưa tìm ra lỗi.
- Khi typography theo trục đang đo và padding đã khớp mà khung vẫn lệch, áp dụng bước truy nguyên min/max/fixed constraint trong `qa-section`; không đề xuất sửa padding đã đúng để bù min-width/min-height cứng.
- Giữ đầy đủ checklist và bằng chứng local. Lập cây thành phần thực tế từ Figma/theme: một group có thể chứa icon + eyebrow; phải kiểm cả thành phần con và gap của group, không chỉ phân loại thành Text/Icon độc lập. Bảng chính gộp dọc tên thành phần, cạnh đó là tiêu chí và trạng thái riêng; hai cột Figma/Hiện tại đặt cùng thuộc tính trên cùng hàng; giá trị khớp không highlight, giá trị lệch highlight Figma xanh và Hiện tại đỏ.
- Giữ hai nhóm Desktop/Mobile rõ ràng trong mỗi section; không xen kẽ nhãn thiết bị giữa các tiêu chí. Không gộp các block Text độc lập thành một dòng chung nếu chúng có kết quả khác nhau.
- Thiếu nguồn/công cụ thì nêu đúng thành phần, thuộc tính và lý do chưa xác minh. Không kết thúc ở lượt quét layout hoặc dùng placeholder “typography/color chưa kiểm” thay cho việc kiểm chi tiết khi vẫn có thể tiếp tục.

## 3. Grid/slide, navigation và pagination

- Grid/slide: kiểm số cột, số item trên hàng/trong viewport, gap, kích thước card, alignment và thứ tự sản phẩm/media theo thiết kế. Quan sát các item/trạng thái cần thiết, không chỉ card đầu.
- Navigation/pagination: kiểm đủ và đúng loại arrows/dots/fraction/progress; màu, vị trí/inset, kích thước nút và icon, stroke, gap, border/radius; active/inactive/disabled khi có nguồn. Thao tác để xác nhận đổi đúng item và trạng thái đầu/cuối.
- Gộp thành dòng `Grid/slide` và `Navigation/pagination` của section/breakpoint. Không xuất mỗi lần bấm/vuốt thành một dòng. Chức năng chạy đúng không chứng minh kiểu hiển thị đã khớp.
- Hover/focus chỉ đối chiếu khi có thiết kế hoặc được yêu cầu; không tự tạo lỗi vì Figma không có state đó.

### Ngoại lệ mobile có item kế tiếp ló ra

Nếu Figma có **1 item đầy đủ + một phần item thứ 2**, chỉ xác minh giao diện cũng có **1 item đầy đủ + preview item kế tiếp** ở đúng viewport. Nếu nguồn có 2 item đầy đủ + một phần item thứ 3 thì kiểm đúng mẫu đó.

Trong trường hợp này **không cần đo chính xác %/px item ló ra, kích thước card hay kích thước section**. Ghi ngoại lệ trong dòng Grid/slide; không tạo dòng lỗi hoặc hàng N/A cho từng kích thước được miễn. Vẫn kiểm gap, số item/cột, nội dung, typo, màu, control và overflow ngoài chủ đích. Không áp ngoại lệ cho desktop hoặc mobile không có next-item preview. Chưa đọc rõ mẫu từ nguồn thì ghi chưa xác minh, không tự giả định.

## 4. Ghi báo cáo và kết luận

Đọc [sheet-report.md](references/sheet-report.md) trước khi xuất. Bảng chính dùng tiếng Việt, tên section đúng tiếng Anh trong theme, có STT riêng, nhãn Desktop/Mobile và nhóm các dòng cùng section. Không có cột link đối chiếu; giữ nguồn ở hồ sơ local. Mỗi nhóm gồm **Tổng quan layout → các thành phần thực có → Grid/slide và Navigation/pagination nếu áp dụng**. Gộp dọc tên thành phần và các cột cha; cạnh đó là các dòng tiêu chí Nội dung/Typo/Màu/Kích thước với nội dung đối chiếu và trạng thái riêng.

Mẫu mặc định hiện có 10 cột vật lý theo reference: STT, Section, Thiết bị, Thành phần, Tiêu chí, **Nội dung (Figma | Hiện tại)**, Hướng xử lý, Lần fix, Trạng thái. Header Nội dung gộp ngang trên hai cột con. Mỗi thuộc tính sai lệch/chưa xác minh là một hàng riêng; không list nhiều lỗi trong một ô. Chỉ phần khác đã xác minh mới highlight: Figma xanh, Hiện tại đỏ; phần giống nhau không highlight. Hướng xử lý đứng ngay sau nhóm Nội dung, ánh xạ đúng thuộc tính trên cùng hàng; Trạng thái vẫn dùng dropdown ở cuối vì yêu cầu này chưa bị hủy. Mục Khớp để trống Hướng xử lý. Style hiện hành được áp dụng ngay bước QA đầu trên tab mới/trống đã được giao; lưu tracker để tiếp nhận các thay đổi sau. Không chờ chốt lại style đã được chấp nhận.

Ưu tiên hướng xử lý bằng preset/settings đã có. Chỉ đưa custom sau khi kiểm schema/config và xác nhận preset không đáp ứng; giải thích giới hạn và ảnh hưởng nếu dùng setting global. Không thực hiện sửa theme chỉ từ đề xuất QA.

Lưu chi tiết vào một file cho mỗi section, gộp các lượt QA/recheck/fix vào cùng file theo [hồ sơ QA theo section](../qa-section/references/qa-report-files.md). Bản cài phẳng đọc `qa-section/references/qa-report-files.md` trong thư mục skills. File tổng quan của page chỉ giữ nguồn chung, mục lục và checkpoint. Đồng bộ STT/thành phần, kết luận, trạng thái và hướng xử lý với Sheet ngay sau mỗi bước; giữ số đo, nguồn và phân tích dài trong tài liệu thay vì nhồi vào ô Sheet.

Ghi kết quả trực tiếp vào Sheet sau mỗi bước/section, không chỉ báo trong chat rồi hỏi lại có ghi hay không khi Sheet đã được chỉ định. Hoàn tất desktop/mobile của section hiện tại rồi chuyển section kế tiếp, trừ chế độ huấn luyện từng bước: ghi Sheet rồi dừng trao đổi theo bước 0. Phần bị chặn ghi Chưa xác minh; trong chế độ huấn luyện hỏi/trao đổi trước khi chuyển tiếp. Giữ key/checkpoint local để resume, không ghi trùng.

**Ưu tiên API Google Sheets** để đọc/ghi dữ liệu, merge, định dạng và dropdown; áp dụng [quy trình khởi tạo/style và API](references/sheet-api-workflow.md). Computer Use dùng để xác minh giao diện hoặc phần chip API không hỗ trợ khi đã được người dùng cho phép. Không suy công cụ Spaces spreadsheet hỗ trợ Google Sheets hoặc tạo file đích thay thế ngầm. Đọc lại nội dung sau khi ghi; thiếu quyền/công cụ thì giữ báo cáo local và nói rõ phần chưa xuất.

Khớp cần bằng chứng cả thiết kế và giao diện; config-only chưa đủ. Sai lệch và chưa xác minh là hai kết quả khác nhau. Một dòng có cả thuộc tính lệch và chưa kiểm phải nêu cả hai; không bỏ phần chưa kiểm khi gom dòng. Chỉ kết luận section đạt hoàn toàn khi mọi tiêu chí áp dụng đã xác minh và không còn sai lệch/chưa xác minh. Trả link Sheet và vài điểm chính; không liệt kê metadata kỹ thuật trong lời bàn giao.

### Rút gọn kết quả đã khớp trong section

Chỉ áp dụng cho section chi tiết, không áp dụng STT 0 Tổng quan page/theme: Tổng quan vẫn giữ từng dòng Số lượng section, Thứ tự section, Width / Padding như hiện tại. Trong mỗi section/breakpoint, gom các thành phần đã khớp hoàn toàn vào một dòng **Đã kiểm và khớp**, chỉ nêu tên, không lặp thông số. Ví dụ Heading đạt toàn bộ thì ghi Heading trong dòng này, không tạo các dòng Content/Typo/Màu riêng. Với thành phần có sai lệch, ví dụ Button chỉ sai line-height, chỉ tách hàng Button · Line-height với Figma/Hiện tại và hướng xử lý tương ứng; không liệt kê lại các thuộc tính Button đã khớp. Các thuộc tính còn lại đã kiểm có thể được xác nhận gọn trong dòng tổng hợp, không làm mất mục chưa xác minh. Mỗi sai lệch hoặc mục chưa xác minh là một hàng riêng; checklist và số đo đầy đủ giữ trong Markdown. Dòng xác nhận khớp có thể gộp ngang Figma/Hiện tại, không highlight so sánh.

### Thành phần lặp trong scroll/marquee

Khi Figma dùng cùng style cho nhiều text/icon/ảnh lặp, nhóm mỗi loại/style thành một mục đại diện trên Sheet; không xuất lại cùng tiêu chí cho từng item. Vẫn đối chiếu các item/biến thể cần thiết, không suy đồng bộ từ một mẫu duy nhất. Chỉ tách các thuộc tính chưa khớp/chưa xác minh. Nếu Figma đồng bộ nhưng các item hiện tại khác style nhau, ghi nội dung **Chưa đồng bộ style** với thuộc tính và vị trí lệch; dropdown dùng **Chưa khớp**, không tự thêm trạng thái mới. Nếu mọi item cùng sai một thuộc tính, ghi một lỗi chung của nhóm, không kết luận thiếu đồng bộ nội bộ. Lưu danh sách mẫu, số đo và vị trí chi tiết trong Markdown. Nội dung khác nhau theo thiết kế không đồng nghĩa style khác nhau.

### Layout: khoảng cách từ trong ra ngoài

Tạo Thành phần riêng **Layout** để báo cáo khoảng cách. Phân biệt tiêu chí **Gap** (giữa các thành phần/cụm) và **Padding** (mép trong của cụm/section), kèm tên cặp thành phần hoặc container để định vị. Kiểm từ trong ra ngoài: gap giữa các con trong một group → gap giữa các group/thành phần cha → padding của group/container/section; đối chiếu riêng Desktop/Mobile. Chỉ liệt kê các Gap/Padding chưa khớp trong nhóm Layout, mỗi chỗ lệch một hàng với Figma/Hiện tại/hướng xử lý. Khoảng cách đã khớp chỉ xác nhận gọn trong Đã kiểm và khớp, không xuất hàng thông số. Mục chưa đủ bằng chứng không được coi là đã khớp; giữ ở ghi chú chưa xác minh khi cần. Tổng quan page/theme STT 0 vẫn giữ cách liệt kê đã thống nhất. Chiều cao, viền, constraint hoặc typography có nguyên nhân riêng không đổi nhãn thành lỗi Gap/Padding để bù sai lệch.

### Border không tạo khác biệt nhìn thấy

Theo quy ước QA được người dùng hướng dẫn: nếu border/stroke trong Figma trùng màu nền, không làm tăng kích thước hoặc thay đổi layout và quan sát tổng thể không thấy đường viền, coi như **không có border về mặt hiển thị**. Không báo thiếu border chỉ vì Figma có stroke còn CSS không có; không đề xuất bật separator hay custom chỉ để sao chép thuộc tính vô hình. Nếu đã báo lỗi, bỏ dòng lỗi và hướng xử lý trên Sheet, ghi cơ sở chấp nhận trong Markdown; phần đã khớp gom vào xác nhận chung. Phải đủ cả ba điều kiện; border còn nhìn thấy hoặc có ảnh hưởng geometry vẫn đối chiếu như bình thường. Không dùng quy ước này để bỏ qua sai lệch chiều cao có nguyên nhân độc lập như min-height. Với Announcement bar Kinetra Desktop/Mobile, người dùng chấp nhận viền dưới theo quy ước này; rút đề xuất bật Show bottom separator, giữ lỗi font family và chiều cao do constraint đã chứng minh.

### Phần Chung cho sửa một chỗ áp dụng cả hai thiết bị

Trong từng section, đặt nhóm Thiết bị **Chung (Desktop, Mobile)** trước Desktop/Mobile. Mọi mục mà đã đối chiếu cả hai thiết bị và xác minh **sửa một chỗ giải quyết cho cả hai** chỉ ghi một lần tại Chung, không lặp lại dưới từng thiết bị. Không giới hạn ở font family: có thể là style, content, constraint hoặc thuộc tính khác nếu cùng một setting/selector/cách sửa chung. Ví dụ font family của Announcement bar do cùng setting; min-height của cùng inner/track trên cả hai; Không dùng line-height Button Primary/Secondary làm ví dụ lỗi chung vì đã được miễn kiểm riêng theo quy tắc cập nhật. Khác số đo hoặc yêu cầu thiết kế chỉ gộp khi biểu diễn rõ cả hai và vẫn cùng một thay đổi xử lý đúng, không che khác biệt. Không suy chung vì tên lỗi giống nhau, không coi hai cấu hình phải sửa riêng là một lỗi chung. Mục chưa xác minh có cùng điểm cần xác minh và bằng chứng hai thiết bị thì gom Chung, giữ Chưa xác minh; không suy cùng nguyên nhân hay tự đề xuất sửa. Desktop/Mobile chỉ giữ mục riêng; xác nhận khớp gom chung, thêm hậu tố thiết bị khi cần; Markdown vẫn giữ bằng chứng hai thiết bị và vị trí tác động. Trạng thái dùng dropdown hiện có. Tổng quan STT0 giữ nguyên.

### Điểm đã khớp chung và nhãn thiết bị riêng

Mỗi section chỉ cần một dòng **Đã kiểm và khớp** trong nhóm Chung. Thành phần/thuộc tính đã xác minh đạt ở cả Desktop/Mobile ghi một lần, không lặp danh sách theo thiết bị. Mục chỉ áp dụng/đạt ở riêng một thiết bị thêm hậu tố **(Mobile)** hoặc **(Desktop)** ngay sau tên trong cùng dòng xác nhận. Không ghi thông số dài hoặc list xuống dòng trong ô. Không biến một thành phần chỉ đạt vài thuộc tính thành đạt toàn bộ: nêu ngắn phạm vi đã khớp, giữ lỗi/chưa xác minh riêng. Markdown vẫn giữ checklist/số đo từng thiết bị. Không áp cách rút gọn này cho Tổng quan STT0.

### Button Primary/Secondary: đánh giá khung tổng thể

Với button có variant Primary hoặc Secondary đã xác minh từ schema/config/DOM, không kiểm/báo line-height của label như một tiêu chí sai lệch riêng. Kích thước đánh giá theo tổng thể button: width/height, padding, border/radius, alignment và bố cục label/icon; vẫn đối chiếu nội dung, font family/weight/size/tracking/case và màu áp dụng. Không suy lỗi kích thước label từ line-height. Bỏ cả dòng lỗi line-height và hướng sửa tương ứng nếu đã báo; chi tiết cũ chỉ giữ như lịch sử được thay thế. Với Hero Kinetra, nút SHOP NOW là Primary, khung56px Desktop/44px Mobile đã khớp: rút đề xuất custom line-height1.5. Quy tắc không tự áp dụng cho menu text, localization hoặc control icon Header; constraint min-height của các control vẫn cần kiểm nếu làm sai khung section.

### STT theo thứ tự section trong thiết kế

STT theo thứ tự section trong Figma/page, không theo thời điểm QA. Khi bỏ sót một section trước đó, chèn đúng vị trí và đổi STT các section phía sau; giữ bằng chứng/checkpoint theo instance, không biến dữ liệu cũ thành lần kiểm mới. Kinetra homepage: 0 Tổng quan, 1 Announcement bar, 2 Header, 3 Hero.

### Chưa xác minh cũng gom Chung khi cùng điểm cần xác minh

Quy tắc chống lặp áp dụng mọi trạng thái. Khi cùng thuộc tính, cùng kết quả quan sát/giá trị đối chiếu và cùng câu hỏi cần xác minh ở cả Desktop/Mobile, ghi một lần tại **Chung (Desktop, Mobile)**; giữ trạng thái **Chưa xác minh**, không bịa nguyên nhân chung hay hướng sửa. Điều kiện vẫn cần bằng chứng từng thiết bị; tên giống nhau nhưng dữ liệu/câu hỏi khác thì tách và gắn thiết bị. Ví dụ Header border dưới Figma0.5px/computed1px ở DPR1 xuất một dòng Chung; không lặp hai dòng Section Desktop/Mobile. Mục metrics cùng câu hỏi ở hai thiết bị ghi Chung; nếu đã được chấp nhận theo quy tắc text width gần sát bên dưới thì cập nhật kết luận thay vì giữ Chưa xác minh.

### SVG: so kích thước hiển thị gồm stroke

Đối chiếu biên hiển thị tổng thể của SVG/icon, tính cả stroke ngoài; không kết luận lệch chỉ từ width/height box hoặc viewBox khác nhau. Ví dụ Figma box12×12px với stroke ngoài1px mỗi phía có tổng14×14px; icon theme hiển thị14×14px tương ứng được coi là **Khớp** về kích thước. Khi đã xác nhận tương đương, bỏ dòng lỗi/chưa xác minh và hướng sửa kích thước, gộp vào “Đã kiểm và khớp” với nhãn thiết bị phù hợp. Vẫn kiểm riêng hình dạng, màu, độ dày stroke và gap nếu chúng khác; không tự giảm icon theme xuống12px để khớp box nội bộ.

### Figma làm tròn khi công thức typography đã khớp

Khi font size và line-height đã khớp, tính chiều cao bằng font-size × line-height%. Nếu kết quả là số lẻ và Figma chỉ hiển thị số nguyên tương ứng sau làm tròn, kết luận **Figma làm tròn**, không để Chưa xác minh hoặc quy lỗi browser render. Ví dụ68px ×120% =81.6px; theme computed81.6px (DOM81.59px do lượng tử hóa), Figma hiển thị82px: dùng trạng thái dropdown **Figma làm tròn**, hướng xử lý “Không cần sửa”. Chỉ áp dụng khi chênh lệch được giải thích bởi phép làm tròn này; không áp dụng cho sai font hoặc constraint; chiều rộng text theo quy tắc riêng bên dưới. Giữ một dòng giải thích ngắn khi cần thể hiện trạng thái này.

### Chiều rộng text gần sát khi typography đã khớp

Với block dạng text, kiểm nội dung/case, font thực đã tải và variant/weight, size, letter-spacing; loại trừ wrap, scale/transform, width constraint hoặc icon/gap tính nhầm vào text. Khi typography đã khớp, chiều rộng render gần sát Figma và không làm đổi xuống dòng/alignment/bố cục, có thể suy luận khác biệt do Figma làm tròn hoặc font metrics; không mặc định giữ Chưa xác minh và không custom font-size/tracking/width để bù. Dùng trạng thái **Figma làm tròn** theo quy ước QA người dùng, ghi rõ **suy luận làm tròn/metrics**, không tuyên bố là phép làm tròn số học đã chứng minh hay lỗi browser render. Ví dụ Eyebrow148px/149.11px với typography khớp được chấp nhận. Không đặt ngưỡng px/% chung từ ví dụ; nếu chênh đáng kể, ảnh hưởng layout hoặc chưa chắc font thì kiểm thêm font file/variant, shaping/metrics và constraint, giữ Chưa xác minh đúng chỗ. Chiều cao68×120%=81.6→82px là trường hợp chứng minh bằng công thức, khác suy luận chiều rộng.

### Box cha: truy phần tử con và không lặp sai số làm tròn

Trước khi báo lệch chiều cao/rộng của box Layout, kiểm từ con ra cha: Text, Button, ảnh/media → group → section. Với ảnh, kiểm đúng kích thước theo trục đã chốt và đúng tỷ lệ/crop; tính trục còn lại theo tỷ lệ. Nếu kết quả lẻ nhưng Figma hiển thị số nguyên làm tròn tương ứng, kết luận **Figma làm tròn** tại ảnh. Với Text, khi các thuộc tính ảnh hưởng chiều cao đã khớp, tính line-height × số dòng (cộng paragraph spacing nếu có); kết quả lẻ được Figma hiển thị làm tròn thì kết luận ngay tại Text. Button Primary/Secondary vẫn xét tổng khung, không quay lại báo line-height label riêng.

Tính tổng các box con cùng gap/padding/border thực. Khi chênh lệch box cha được giải thích bởi các phần tử con đã ghi **Figma làm tròn**, bỏ qua phần chênh kế thừa đó: không tạo thêm dòng Layout/section, không lặp trạng thái làm tròn ở mọi cấp cha, không sửa gap/padding đúng để bù. Chỉ giữ một dòng ở phần tử/nguyên nhân gốc; chi tiết phép cộng giữ trong Markdown. Nếu còn sai số không được giải thích, wrap/crop sai hoặc constraint độc lập thì vẫn kiểm và báo phần dư đó. Khác viewport/scrollbar là sai điều kiện đo, không tự đổi tên thành Figma làm tròn hoặc lỗi theme.

### Marquee/scroll Mobile: ưu tiên vùng hiển thị trong viewport

Đối chiếu gap giữa các ảnh/text/icon thực sự nhìn thấy trong vùng clip của frame Mobile (ví dụ ảnh mép trái → heading chính → ảnh mép phải). Không dùng gap của outline/cycle/ảnh nằm ngoài viewport để kết luận chưa khớp hoặc đề xuất custom khi vùng nhìn thấy đã đúng; thiết kế có thể giữ lại gap Desktop ở phần ẩn. Bản copy bỏ clip chỉ giúp inspect/nắm cấu trúc, không mở rộng phạm vi visual QA. Với chuyển động, so cùng nhóm phần tử/phase tương ứng; chỉ báo gap ngoài vùng ban đầu nếu quan sát nó đi vào viewport và có sai lệch hiển thị thực tế. Không suy lệch từ vị trí marquee ở hai thời điểm khác nhau. Nội dung lặp cùng style chỉ báo đại diện theo quy tắc hiện hành.

### QA lại phải cập nhật báo cáo ngay

Mỗi lượt QA lại, đồng bộ mọi mục vừa xác minh vào Sheet và MD trong cùng lượt, kể cả chỉ kiểm một phần section. Xóa lỗi đã sửa và gộp thuộc tính đạt vào summary; giữ riêng mục còn lệch/chưa xác minh đúng bằng chứng mới. Đọc lại sau ghi. Tab Sheet cũ đóng/mất không phải blocker: mở lại đúng URL/tab đã lưu, dùng connector nếu có hoặc CUA hợp lệ. Chỉ báo chưa ghi khi đã thử đường truy cập hợp lệ và có lỗi cụ thể; lưu checkpoint, không gọi lượt QA hoàn tất khi Sheet chưa đồng bộ. Không lấy số cũ làm kết quả đo mới.

### Scroll/marquee: chấp nhận gap bù padding Heading

Khi Heading không có option padding, đánh giá **khoảng cách hiển thị thực tế** giữa các biên nội dung nhìn thấy trong viewport, không yêu cầu riêng CSS gap và padding trùng Figma. Khoảng đích = padding phía cuối của phần tử trước + gap Figma + padding phía đầu của phần tử sau (chỉ cộng phía thực sự nằm giữa hai nội dung). Có thể đặt toàn bộ khoảng đích vào gap preset của theme. Ví dụ padding10px + gap12px + padding10px =32px: gap theme32px được chấp nhận nếu biên hiển thị khớp. Không tự suy padding hoặc chốt gap12px chỉ từ container; phải đọc padding của các wrapper liên quan, tránh cộng trùng. Kiểm riêng từng breakpoint, các cặp lặp và chỗ nối chu kỳ khi nhìn thấy. Nếu khoảng nhìn thấy khớp, gộp vào Đã kiểm và khớp, rút lỗi gap/padding và không đề xuất custom thêm option chỉ để giống cấu trúc Figma. Chỉ báo phần chênh khoảng thực tế còn lại; MD lưu phép cộng và bằng chứng. Nếu chưa đo đủ, ghi chưa xác minh, không giữ kết luận lỗi dựa riêng vào gap. Quy tắc này áp dụng scroll/marquee, không dùng bù lỗi typography hay constraint độc lập.

### Style báo cáo hiện hành

Áp dụng quy tắc trong references/sheet-report.md: mọi ô căn giữa chiều dọc, header center/middle; cột Trạng thái chỉ có màu chip dropdown, không tô màu nền ô dữ liệu. Giữ highlight Figma/Hiện tại và các nhóm merge.

### Khi người dùng yêu cầu Fix lần 1

Chuyển sang [fix-qa-preset](../fix-qa-preset/SKILL.md): chỉ preset/config local, sau đó QA lại toàn phạm vi và ghi Sheet/MD. Chu kỳ này giữ dòng lỗi và số đo gốc; gắn nhãn Lần 1–Lần 5/Bỏ qua ở cột **Lần fix**, Trạng thái chỉ đổi **Khớp** sau QA đạt. Lỗi mới chèn đúng section với **Chưa khớp**, vòng phát hiện lưu MD. Không áp quy tắc xóa lỗi đã sửa/gộp summary cho lịch sử lỗi trong chu kỳ fix. Yêu cầu QA đơn thuần vẫn chỉ đọc theme.

## Gắn cờ xử lý ngay lượt QA đầu

Sau khi có Hướng xử lý cụ thể và xác minh có thể sửa lỗi bằng preset/composition hiện có hoặc config/settings_data.json local, gắn dropdown Lần fix = **Lần 1**, giữ Chưa khớp đến khi fix và QA đạt. Đây là cờ vòng xử lý, không chứng minh đã sửa và không cấp quyền sửa theme trong QA. Không tự gắn cờ cho mục đã khớp, làm tròn, chưa xác minh hay lỗi cần custom chưa được giao vòng. Dropdown Lần fix dùng **Lần 1–Lần 5, Bỏ qua**, không số trần; Bỏ qua chỉ theo quyết định người dùng. Chi tiết [fix-qa-preset](../fix-qa-preset/SKILL.md).

## File output/test và commit

Bắt buộc áp dụng [quy tắc loại trừ và dọn file kiểm tra](../../../references/task-artifacts.md) khi tạo output/test hoặc chuẩn bị commit. Bản cài phẳng đọc `references/task-artifacts.md` trong chính thư mục skill này.
