# Sheet QA theo cây thành phần

## Bảng chính: 10 cột vật lý, header hai tầng

`STT | Section | Thiết bị | Thành phần | Tiêu chí | Figma | Hiện tại | Hướng xử lý | Lần fix | Trạng thái`

F1:G1 gộp nhãn **Nội dung**; F2 là **Figma**, G2 là **Hiện tại**. Các header còn lại gộp dọc qua hai hàng. Hướng xử lý đứng sát bên phải nhóm Nội dung; tiếp theo là Lần fix; Trạng thái giữ dropdown ở cuối theo yêu cầu đã có, chưa bị người dùng bỏ. Đây là mẫu mặc định hiện hành để khởi tạo ngay ở bước QA đầu trên tab mới/trống đã được giao; có thể tiếp tục cập nhật theo hướng dẫn người dùng.

Mẫu định dạng tái sử dụng nằm tại [sheet-style.json](../assets/sheet-style.json). Khi khởi tạo báo cáo, ghi snapshot định dạng vào tài liệu QA của page; giữ chỉnh sửa giao diện riêng đã được người dùng chấp nhận cho báo cáo đang có. JSON mô tả cột/width, font, màu, merge theo nhóm, wrap và dropdown, không phải kết quả kiểm. Mẫu hiện hành đã được chấp nhận để khởi tạo QA, vẫn có thể được người dùng huấn luyện và sửa tiếp. Theo dõi yêu cầu style tại `docs/qa/sheet-style-tracker.md` trong repo theme, tách style đang quan sát, yêu cầu đã hướng dẫn và giá trị còn chờ chốt. Áp dụng mẫu hiện hành ngay khi bắt đầu QA trên tab mới/trống đã được giao; không chờ chốt lại các lựa chọn đã được chấp nhận. Khi người dùng chốt hoặc yêu cầu áp dụng bản hiện hành, đọc lại tracker và JSON rồi render đồng bộ; bản đang huấn luyện phải ghi rõ chưa chốt cuối. Font phần dữ liệu phải thống nhất giữa Tổng quan và section; không lặp lại lệch 11pt/10pt của bản nháp Kinetra. Header có thể khác nếu được chốt riêng.

Các section nối liền nhau ngay sau Tổng quan, không chèn nguồn hoặc ghi chú giữa các nhóm. Phạm vi, link Figma desktop/mobile và preview nằm một cụm ở cuối bảng. Khi bổ sung section, chèn trước cụm cuối này và giữ nguồn ở cuối. Trong tài liệu chi tiết cũng đặt cụm nguồn ở cuối sau kết quả/checkpoint.

- Nhận xét tiếng Việt; tên section đúng tiếng Anh từ tên instance hoặc schema của theme. Không có cột Link đối chiếu. Nguồn Figma/preview và bằng chứng giữ trong hồ sơ local; cụm nguồn trên Sheet nằm ở cuối bảng theo yêu cầu.
- Nhóm theo **Section → Desktop → Mobile → Thành phần → Tiêu chí**. Gộp dọc STT/Section theo instance, Thiết bị theo breakpoint trong section và Thành phần theo các dòng tiêu chí của nó. Không gộp Figma/Hiện tại/Hướng xử lý/Trạng thái qua các thuộc tính khác nhau. Cùng tên nhưng khác instance/template vẫn là nhóm riêng.
- Không lặp nhãn Desktop/Mobile ở từng dòng; gộp ô theo nhóm. Không gộp qua hai thiết bị làm mất khác biệt; cho phép nhóm Chung khi một thay đổi giải quyết cả hai theo quy tắc bên dưới.

## Cây thành phần thực tế

### Nhóm Tổng quan của page

Đặt trước các section chi tiết: **STT 0**, **Section: Tổng quan**, **Thiết bị: Desktop, Mobile**. Tạo ba dòng Thành phần: **Số lượng section**, **Thứ tự section**, **Width / Padding**; mỗi dòng có tiêu chí, nội dung đối chiếu và dropdown Trạng thái riêng. Gộp dọc STT/Section/Thiết bị cho nhóm tổng quan. Ngoại lệ gộp hai thiết bị này chỉ dành cho bước tổng quan; trong nội dung phải phân biệt kết quả/giới hạn desktop và mobile, không suy bằng chứng giữa thiết bị. Ghi rõ phạm vi chỉ homepage khi mới kiểm homepage.

Quy ước chấp nhận do người dùng hướng dẫn phải có trong nội dung đối chiếu, không giữ kết luận lỗi hoặc Chưa xác minh cho tiêu chí mà người dùng đã xác nhận là Khớp. Với Kinetra homepage, người dùng đã chấp nhận cả dòng **Width / Padding** ở STT 0 là **Khớp**, theo quy ước tại bước 0 trong SKILL.md. Ghi rõ cơ sở là xác nhận theo quy ước, không biến thành tuyên bố đã đo đầy đủ. Khi chưa có xác nhận cho cả dòng kết hợp và một thuộc tính còn chưa xác minh, ghi giới hạn đó và dùng Chưa xác minh. Không tạo nhãn dropdown ghép.

Tên thành phần lấy đúng tên block tiếng Anh từ schema/locale trong repo; thêm ngữ cảnh cha trong ngoặc khi cần, ví dụ `Title (Blog card)` nếu block thực sự là Title trong Blog card. Không dùng nội dung hiển thị để đặt tên block: `Eva Johnson` chỉ nằm ở tiêu chí Nội dung; nếu source là block Heading trong Slide thì ghi `Heading (Slide)`, lời đánh giá là `Text (Slide)`. Không đổi Heading thành Title theo suy đoán. Thành phần không có block riêng và nhóm kiểm tổng quan vẫn ghi đúng vai trò thực tế.

Quét thiết kế và theme để biết cấu trúc cần kiểm, không áp một danh sách block phẳng giống nhau cho mọi section. Kiểm tổng quan đủ/thiếu/thừa, bố cục, thứ tự, grouping và căn lề trước; sau đó duyệt từng thành phần và thành phần con trong group.

Ví dụ **Hero của một theme** có thể gồm:

| Thành phần (ô gộp dọc) | Các dòng tiêu chí bên cạnh |
| --- | --- |
| Tổng quan layout | Đủ/thiếu thành phần; bố cục, vị trí, thứ tự và căn chỉnh cụm Header theo Figma |
| Ảnh nền | Ảnh; Crop; Position; Overlay nếu có |
| Group: Icon + Eyebrow | SVG icon; Content eyebrow; Màu icon/eyebrow; Typo eyebrow; Gap giữa icon và eyebrow |
| Heading | Content; Typo; Màu; Kích thước chỉ khi typography đã khớp nhưng box vẫn lệch |
| Button | Content; Typo; Màu nền/chữ/viền; Kích thước/padding |

Đây là ví dụ cách suy ra checklist từ cây thành phần, **không phải danh sách cố định để chèn vào mọi Hero hoặc section**. Chỉ kiểm/hiển thị thành phần và thuộc tính áp dụng với nguồn thực tế. Không có overlay hoặc Navigation/pagination thì bỏ mục đó, không tạo dòng placeholder/N/A. Phân biệt thiếu control so với thiết kế (lỗi) với cả thiết kế và layout đều không có control (không áp dụng). Tabs chỉ là tab thì ghi Tab bộ sưu tập; thao tác vuốt thuộc Grid/slide nếu không có navigation/pagination riêng.

Nhóm thuộc tính cùng loại dưới Typo, nhưng chỉ mỗi thuộc tính lệch/chưa xác minh có một hàng so sánh Figma/Hiện tại; có thể gộp dọc nhãn Typo qua nhóm. Với group, nêu rõ tiêu chí của con nào. Với card lặp, nhóm mẫu giống nhau và giữ khác biệt theo item/biến thể khi có. Không xuất log từng lần click/swipe.

**Kích thước Text phụ thuộc typography:** khi typography chưa khớp, không tạo dòng Kích thước, N/A hoặc Chưa xác minh chỉ để lặp lại hệ quả về width/height chữ. Nếu đã có dòng lỗi phụ thuộc, bỏ cả dòng và hướng xử lý tương ứng ở Sheet/Markdown. Chỉ khi typography đã khớp mà kích thước vẫn lệch mới thêm tiêu chí Kích thước; kiểm constraint/width/padding trước khi quy cho browser. Trường hợp xác minh do render/làm tròn của trình duyệt dùng đúng dropdown **Browser render không khớp**, giữ delta, viewport/zoom và bằng chứng trong tài liệu chi tiết. Chưa chứng minh nguyên nhân thì ghi Chưa xác minh hoặc lỗi constraint đã chứng minh, không đoán browser. Quy tắc này không miễn kiểm kích thước section, Button hoặc layout độc lập.

## Nội dung và trạng thái

Mỗi thuộc tính sai lệch/chưa xác minh dùng **một hàng Sheet riêng**. Hai ô Figma/Hiện tại chứa giá trị tương ứng, cùng đơn vị và nhãn ngắn nếu cần, ví dụ `Weight: 500` / `Weight: 400`. Nhóm Typo có thể chứa nhiều hàng Font, Weight, Size, Line-height, Tracking; gộp dọc Tiêu chí nếu cùng nhóm, không gom nhiều thuộc tính thành list trong một ô. Wrap chỉ phục vụ hiển thị câu dài, không dùng xuống dòng để nhét nhiều điểm vào một ô. Chi tiết truy nguyên giữ trong Markdown.

- **Khớp:** trong section, gom thành phần đạt vào dòng xác nhận theo quy tắc rút gọn; Tổng quan giữ nội dung từng tiêu chí. Không highlight phần so sánh. Hướng xử lý trống. Quy ước đã được người dùng chấp nhận giữ trạng thái Khớp, giải thích cơ sở ngắn trong ô/Markdown, không tô đỏ lại chênh lệch đã chấp nhận.
- **Chưa khớp:** chỉ các ô của thuộc tính khác đã xác minh mới highlight: **Figma xanh**, **Hiện tại đỏ**. Không tô toàn group/section hay mọi ô Figma; các thuộc tính giống nhau vẫn bình thường. Không dùng nhãn `Chưa khớp:` và list nhiều lỗi trong một ô nữa.
- **Chưa xác minh:** ghi giá trị đã biết và phần thiếu bằng chứng; không tô như lỗi chắc chắn. Sai lệch đã đo và nguyên nhân chưa rõ phải phân biệt trong Markdown.
- **Không áp dụng:** chỉ dùng khi thật sự cần ghi ngoại lệ, không tạo hàng cho thành phần không có trong thiết kế.
- **Browser render không khớp:** chỉ dành cho text còn lệch sau khi typo/constraint khớp và có bằng chứng renderer/làm tròn; không đoán browser vì chưa biết nguyên nhân. Không ép width để che khác biệt.

Trạng thái tiếp tục dùng dropdown ở cột cuối: Khớp xanh lá, Chưa khớp đỏ, Chưa xác minh vàng, Không áp dụng xám, Browser render không khớp xanh lam. Màu dropdown độc lập với highlight so sánh; yêu cầu “giống nhau không highlight” áp dụng Figma/Hiện tại. Rule phủ vùng dữ liệu, không gồm hai hàng header. Có thể sao chép chỉ xác thực dữ liệu từ mẫu, giữ nguyên giá trị, kiểm lại mở được và đúng nhãn/màu.

## Hướng xử lý

Cột Hướng xử lý nằm **ngay sau nhóm Nội dung**, trước Trạng thái. Mỗi hàng có tối đa một hướng xử lý cho đúng thuộc tính sai trên hàng đó; không dùng list nhiều hành động không liên quan. Mục Khớp để trống. Chưa xác minh/Không áp dụng không tự tạo phương án sửa; bước xác minh có thể ghi riêng trong tài liệu. Khi lỗi hết hoặc được chấp nhận, cập nhật cả hai giá trị/trạng thái và bỏ hướng sửa cũ.

Ưu tiên preset/settings đúng thuộc tính đã kiểm trong schema/config; ghi control/đích cụ thể. Chỉ custom sau khi xác minh preset không đáp ứng, nêu giới hạn và ảnh hưởng global. Không đề xuất thay global chỉ để sửa một section. Với min-width/min-height đã chứng minh gây khung sai khi line-height/padding đúng, nhắm đúng constraint/selector và giữ giá trị đã khớp; xem cách truy nguyên trong qa-section. Ghi báo cáo không cấp quyền sửa theme.

## Phạm vi chưa kiểm và bằng chứng local

Áp dụng [hồ sơ QA theo section](../../qa-section/references/qa-report-files.md), bản cài phẳng đọc `qa-section/references/qa-report-files.md`: mỗi section có một file cập nhật qua các lượt, kết quả mới nhất ở đầu; file tổng quan của page giữ mục lục/nguồn/checkpoint chung. Sheet giữ nội dung ngắn gọn; Markdown giữ số đo, nguồn, nguyên nhân, bằng chứng, cơ sở chấp nhận và hướng xử lý chi tiết. Cùng STT/Section/Thiết bị/Thành phần/Tiêu chí phải có kết luận, trạng thái và từng thuộc tính/hướng xử lý tương ứng ở cả hai nơi. Cập nhật cả hai ngay sau mỗi bước hoặc hướng dẫn mới, không chỉ hứa viết tài liệu cuối lượt. Khóa nhận diện vẫn dựa trên instance/breakpoint/thuộc tính; số hàng Sheet có thể đổi. Không dùng báo cáo khác theme hoặc trang làm tài liệu thay thế.

Trang/template thiếu thiết kế hoặc preview: một ghi chú phạm vi cuối bảng với các trang còn thiếu, không đổ hàng trăm dòng placeholder. Manifest local vẫn giữ đủ từng instance; không loại khỏi mẫu số.

Giữ local: run/thời điểm, theme/revision, page → instance → node → preview, viewport/zoom, cây thành phần, checklist thuộc tính, expected/actual/delta/status, screenshot/số đo và phần đã xuất. Key là resource/template + instance ID + breakpoint + thành phần/tiêu chí, không phải số dòng hoặc tên section. Khi đổi bố cục phải giữ các vấn đề còn hiệu lực và phần chưa xác minh. Không gọi bằng chứng cũ là render mới; không tự suy toàn section đạt từ vài tiêu chí khớp.

## Ghi và xác minh Sheet

Đọc đúng file/tab/gid và vùng hiện có trước khi ghi; chỉ sửa báo cáo được yêu cầu, giữ dữ liệu khác. Khi rút gọn/thay bố cục, lưu bản chi tiết local hoặc bản sao rõ tên trước; dọn các cột/hàng dư thuộc báo cáo cũ. Không đổi sharing, gửi thông báo hay sửa theme.

Ưu tiên API Google Sheets theo [sheet-api-workflow.md](sheet-api-workflow.md) để đọc, ghi, merge, format và dropdown. Computer Use dùng kiểm tra giao diện/phần API không hỗ trợ khi được phép. Ghi text literal để nội dung không thực thi như công thức. Gộp ô sau khi nhóm đúng instance, chỉ đặt nhãn ở ô đầu nhóm. Không áp filter trên vùng merge dọc nếu ứng dụng không hỗ trợ.

Xác minh lại từng giá trị, các nhóm gộp, dropdown/màu, số section/breakpoint và vùng đã xuất; xem ở zoom đọc được, wrap và căn giữa theo chiều dọc, không thu nhỏ font để ép nội dung. Thiếu quyền/công cụ thì giữ local và nói rõ phần chưa xuất; không tự commit/push. Bàn giao ngắn kèm link Sheet trong chat, không đưa link thành cột bảng chính.

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

### Chưa xác minh cũng gom Chung khi cùng điểm cần xác minh

Quy tắc chống lặp áp dụng mọi trạng thái. Khi cùng thuộc tính, cùng kết quả quan sát/giá trị đối chiếu và cùng câu hỏi cần xác minh ở cả Desktop/Mobile, ghi một lần tại **Chung (Desktop, Mobile)**; giữ trạng thái **Chưa xác minh**, không bịa nguyên nhân chung hay hướng sửa. Điều kiện vẫn cần bằng chứng từng thiết bị; tên giống nhau nhưng dữ liệu/câu hỏi khác thì tách và gắn thiết bị. Ví dụ Header border dưới Figma0.5px/computed1px ở DPR1 xuất một dòng Chung; không lặp hai dòng Section Desktop/Mobile. Hero Eyebrow148px/149.11px cùng câu hỏi metric cũng xuất một dòng Chung, khác Marquee chỉ Desktop vẫn giữ riêng.

SVG/icon: so tổng kích thước hiển thị gồm stroke theo quy tắc “SVG: so kích thước hiển thị gồm stroke” trong SKILL.md. Tổng tương đương thì gộp vào Đã kiểm và khớp, bỏ dòng pending/lỗi box và gợi ý sửa tương ứng.

Dropdown bổ sung **Figma làm tròn**: công thức font-size × line-height% khớp, Figma hiển thị số đã làm tròn. Ghi Không cần sửa; không tô Figma xanh/Hiện tại đỏ như lỗi. Xem quy tắc tương ứng trong SKILL.md.

Chiều rộng text gần sát sau khi typography khớp: dùng Figma làm tròn theo quy tắc text trong SKILL.md, Hướng xử lý ghi Không cần sửa; suy luận làm tròn/metrics. Markdown giữ cơ sở suy luận, không coi là lỗi browser đã chứng minh.

Box Layout/section không xuất thêm dòng khi chênh lệch chỉ kế thừa sai số đã ghi Figma làm tròn ở Text/ảnh/Button con. Đối chiếu tổng box con + gap/padding/border; giữ nguyên nhân gốc một lần, chỉ báo phần dư độc lập. Khác viewport giữ trong bằng chứng phép đo, không gọi là Figma làm tròn.

### QA lại phải cập nhật báo cáo ngay

Mỗi lượt QA lại, đồng bộ mọi mục vừa xác minh vào Sheet và MD trong cùng lượt, kể cả chỉ kiểm một phần section. Xóa lỗi đã sửa và gộp thuộc tính đạt vào summary; giữ riêng mục còn lệch/chưa xác minh đúng bằng chứng mới. Đọc lại sau ghi. Tab Sheet cũ đóng/mất không phải blocker: mở lại đúng URL/tab đã lưu, dùng connector nếu có hoặc CUA hợp lệ. Chỉ báo chưa ghi khi đã thử đường truy cập hợp lệ và có lỗi cụ thể; lưu checkpoint, không gọi lượt QA hoàn tất khi Sheet chưa đồng bộ. Không lấy số cũ làm kết quả đo mới.

### Scroll/marquee: chấp nhận gap bù padding Heading

Khi Heading không có option padding, đánh giá **khoảng cách hiển thị thực tế** giữa các biên nội dung nhìn thấy trong viewport, không yêu cầu riêng CSS gap và padding trùng Figma. Khoảng đích = padding phía cuối của phần tử trước + gap Figma + padding phía đầu của phần tử sau (chỉ cộng phía thực sự nằm giữa hai nội dung). Có thể đặt toàn bộ khoảng đích vào gap preset của theme. Ví dụ padding10px + gap12px + padding10px =32px: gap theme32px được chấp nhận nếu biên hiển thị khớp. Không tự suy padding hoặc chốt gap12px chỉ từ container; phải đọc padding của các wrapper liên quan, tránh cộng trùng. Kiểm riêng từng breakpoint, các cặp lặp và chỗ nối chu kỳ khi nhìn thấy. Nếu khoảng nhìn thấy khớp, gộp vào Đã kiểm và khớp, rút lỗi gap/padding và không đề xuất custom thêm option chỉ để giống cấu trúc Figma. Chỉ báo phần chênh khoảng thực tế còn lại; MD lưu phép cộng và bằng chứng. Nếu chưa đo đủ, ghi chưa xác minh, không giữ kết luận lỗi dựa riêng vào gap. Quy tắc này áp dụng scroll/marquee, không dùng bù lỗi typography hay constraint độc lập.

## Căn lề và nền ô trạng thái — cập nhật26/10/2026

- Mọi ô trong bảng căn giữa theo chiều dọc (middle), giữ wrap. Nội dung dữ liệu giữ căn ngang hiện hành.
- Tất cả tiêu đề header, kể cả Nội dung/Figma/Hiện tại, căn giữa ngang và dọc (center/middle).
- Ô dữ liệu cột Trạng thái không tô nền theo trạng thái; để nền trắng/không màu. Màu nằm trên chip dropdown, giữ nguyên nhãn, màu chip và xác thực dữ liệu. Header Trạng thái vẫn dùng nền header chung. Highlight so sánh Figma xanh/Hiện tại đỏ giữ nguyên.

### Nền ô thông thường

Ô dữ liệu thông thường không tô nền: bỏ nền nhóm STT/Section/Thiết bị/Thành phần, nền phân biệt Desktop/Mobile và nền khối nguồn cuối bảng. Chỉ giữ nền header, màu chip dropdown và highlight đối chiếu Figma xanh/Hiện tại đỏ tại thuộc tính chưa khớp đã xác minh. Không tô cả hàng theo trạng thái.

## Chu kỳ fix từ bảng QA

Áp dụng [fix-qa-preset](../../fix-qa-preset/SKILL.md). Bảng hiện có10 cột; sau Hướng xử lý là Lần fix rồi Trạng thái. Ghi nhãn vòng được giao vào Lần fix; chỉ chuyển dropdown sang Khớp sau QA đạt. Đã fix (QA 1) cũ migrate thành Lần fix “Lần 1” / Khớp theo bằng chứng đã có. Giữ dòng và giá trị gốc, không gộp lịch sử vào summary; lỗi mới chèn đúng section với Chưa khớp, vòng phát hiện ghi MD. Không đụng ghi chú người dùng trong Hướng xử lý; giữ relative order và chip. Khi Trạng thái là Khớp, bỏ nền màu hai ô Figma/Hiện tại, giữ giá trị lịch sử; lỗi chưa khớp đã xác minh vẫn highlight xanh/đỏ. Cột mới Arial10, middle/wrap, không nền; header center/middle, cùng style các header khác.

Lần fix dùng dropdown **Lần 1, Lần 2, Lần 3, Lần 4, Lần 5, Bỏ qua**, một lựa chọn, tối đa5 vòng. Ngay QA đầu, sau Hướng xử lý đã map và xác minh sửa được bằng preset hoặc config/settings_data.json local, tự gắn Lần 1 và giữ Chưa khớp; cờ không chứng minh đã sửa. Để trống lỗi chưa xác minh/cần custom chưa giao vòng và mục vốn đã khớp. Bỏ qua chỉ theo quyết định người dùng, không tự bỏ qua lỗi khó sửa. Dropdown Trạng thái bổ sung Bỏ qua; không tự coi lỗi ngoài khả năng sửa là Bỏ qua, chỉ gán theo quyết định người dùng.

### Màu chip Lần fix

Lần fix dùng chip dropdown, chỉ chọn một giá trị: Lần 1 xanh dương #BFE1F6; Lần 2 tím #E6CFF2; Lần 3 cam #FFC8AA; Lần 4 vàng #FFE5A0; Lần 5 xanh lá #D4EDBC; Bỏ qua xám #E7E6E6. Cột rộng100px, nền ô không màu; giữ màu chip Trạng thái hiện có. Không tô cả ô/hàng theo vòng fix.
