---
name: init-theme
description: "Khởi tạo nhánh và worktree Shopify theme từ base, ánh xạ Figma style guide và homepage desktop/mobile bằng section/block có sẵn, cấu hình Theme Settings local trong config/settings_data.json, hoàn thiện preset và content/media từng section mà không custom implementation."
---

# Init Theme

Khởi tạo theme từ base hiện tại rồi dựng Header → template homepage → Footer theo Figma. Khảo sát toàn trang trước; sau đó hoàn thiện layout, content/media và đối chiếu desktop/mobile của từng section trước khi chuyển section tiếp theo. Đây là workflow cấu hình bằng khả năng hiện có, tuyệt đối không custom implementation.

## Đầu vào bắt buộc

Khi được yêu cầu **chạy** init theme, hỏi người dùng tên theme nếu chưa cung cấp và yêu cầu đủ ba link Figma có node/frame cụ thể: style guide, homepage desktop, homepage mobile. Tái sử dụng dữ liệu đã cung cấp, không hỏi lại. Xác định repo base và store domain đích cho content/media; không suy store từ profile minh họa. Thiếu store vẫn có thể khảo sát Figma/repo và cấu hình local; chưa được mutation store. Thiếu một trong ba nguồn Figma thì yêu cầu phần thiếu, không tự coi desktop là bằng chứng mobile.

Yêu cầu tạo/sửa **skill này** không phải yêu cầu chạy init: không hỏi tên theme, tạo branch/worktree hay upload store trong lúc bảo trì skill.

## Skill phụ thuộc và giới hạn ưu tiên

Đọc đúng skill trước tác vụ tương ứng, giải quyết đường dẫn từ thư mục skill này:

- [theme-style-guide](../theme-style-guide/SKILL.md): ánh xạ style guide vào Theme Settings.
- [build-preset](../build-preset/SKILL.md): chọn section/block, dựng preset và composition.
- [store-content-media](../../../setup-store/store-content-media/SKILL.md): upload/tái sử dụng media, tạo content/resource cần thiết và gắn reference local.

Nếu đang dùng bản cài phẳng, tìm các skill cùng tên trong `.agents/skills/`; không dùng đường dẫn tương đối nhóm nguồn cho bản phẳng. Nếu thiếu dependency, báo đường dẫn thiếu; không tự viết workflow thay thế. Đọc reference con theo tác vụ, không tải toàn bộ reference mặc định. Trước mỗi công cụ Figma có prerequisite, đọc skill Figma tương ứng, gồm `figma-design-to-code` trước `get_design_context`.

**Giới hạn của init-theme chặt hơn ngoại lệ của các skill phụ thuộc:**

- Được sửa `current` trong `config/settings_data.json` local bằng các Theme Settings hiện có để khớp Figma; quyền này thuộc phạm vi init/tiếp tục theme, không cần xin phép riêng cho từng giá trị. Chỉ sửa preset trong schema và composition/settings của template/section group thuộc trang đích. Được tạo color scheme bằng definition hiện có.
- Không sửa Liquid/HTML implementation, CSS, JS, snippet, SVG icon implementation hoặc custom CSS; không tạo section/block, setting, option hay sửa allow-list, range, mapping runtime, placement hoặc limits. Không áp dụng ngoại lệ height-option calibration của build-preset hoặc range/runtime mapping của theme-style-guide.
- Giá trị Figma không biểu diễn được bằng control hiện có: dùng giá trị hợp lệ gần nhất nếu vẫn phù hợp và báo sai lệch; không thay schema để khớp. Icon thiếu cũng là gap, không gọi build-theme để bù.
- Không có section/block phù hợp thì bỏ qua vùng đó và ghi rõ lý do; không tạo placeholder giả như đã xong, không tự chuyển sang custom build. Nếu chỉ lệch chi tiết nhỏ, dùng composition hiện có phù hợp và ghi sai lệch.
- Content/media ở store; preset/template chỉ chỉnh file local. Không save Theme Editor hay mutation cấu hình theme bằng API/bot. Upload content không cấp quyền deploy/publish theme. Không tự commit/push các thay đổi cấu hình sau init nếu chưa được yêu cầu; commit khởi tạo bắt buộc của lệnh repo là ngoại lệ thuộc bước tạo theme.

## 1. Tạo nhánh và worktree

Đọc AGENTS.md repo base, trạng thái Git, remotes, `main`, danh sách branch và `git worktree list` trước mutation. Giữ mọi thay đổi có sẵn; base bẩn thì dừng bước tạo theme và báo đường dẫn, không stash/reset hoặc mang diff sang theme mới.

Chuẩn hóa tên thành slug chữ thường, số và gạch ngang; không lặp hậu tố `-theme`. Người dùng nhập `a` → slug `a-theme`, branch `theme/a-theme`, worktree `<thư mục cha repo base>/a-theme`. Nếu tên không chuyển thành slug rõ ràng hoặc trùng branch/path, hỏi phần mơ hồ; không ghi đè, xóa hoặc tái sử dụng theme khác. Với yêu cầu tiếp tục theme đã init, xác minh đúng branch/worktree/hồ sơ trước khi tiếp tục, không tạo lại.

Theo repo có `node theme-base new-theme`, đọc implementation/help trước khi chạy. Từ base sạch trên `main`, chạy `node theme-base new-theme <slug>` **không `--push`**, để lệnh tạo hồ sơ và loại log base khỏi theme theo quy tắc repo. Lệnh hiện tại có thể switch checkout base sang branch theme và tạo commit khởi tạo; sau thành công, switch checkout base trở lại `main`, rồi chạy `git worktree add <đường dẫn tuyệt đối> theme/<slug>` bằng branch vừa có, không dùng `-b` tạo lại. Nếu lệnh thất bại, kiểm tra trạng thái thực tế và báo lỗi; không tiếp tục chuỗi hoặc tự rollback phá hủy dữ liệu. Nếu repo không có lệnh/quy trình tạo theme tương ứng, báo thiếu thay vì bỏ qua hợp đồng khởi tạo.

Xác minh checkout base ở `main`, worktree mới ở `theme/<slug>`, hồ sơ theme tồn tại và theme không mang log base cá nhân. Từ đây mọi thao tác theme dùng workdir của worktree mới. Không đọc/ghi nội dung log base từ skill này; để lệnh repo xử lý. Không tự cập nhật upstream/base khi init.

## 2. Khảo sát toàn bộ trước khi build

Áp dụng flow đọc reference của `build-preset`: xác minh node và kích thước, đọc cấu trúc/control, rồi đối chiếu screenshot ở cả hai viewport trước khi ghi cấu hình. Không coi lỗi một công cụ là bằng chứng thiết kế không thể truy cập.

### Đọc Figma và xử lý công cụ bị chặn

- Ưu tiên `get_design_context` kèm screenshot sau khi đọc prerequisite Figma. Với phản hồi sparse, đọc các node con nhìn thấy trước khi cấu hình; không dùng metadata tổng quan làm bằng chứng đầy đủ.
- Nếu công cụ báo quota/quyền hoặc không trả thiết kế, ghi lỗi và không lặp cùng lời gọi cho mọi node. Có thể thử `use_figma` ở chế độ chỉ đọc sau khi đọc `figma-use`: xác minh ID/page/frame, lấy cây con, text/style, layout, fills và screenshot bằng API được hỗ trợ. Không sửa file Figma để phục vụ khảo sát.
- Nếu MCP cùng bị chặn, tìm tab Figma đúng file trong các phiên trình duyệt/app hiện có trước khi mở phiên mới; ưu tiên phiên đã đăng nhập có Inspect. Phiên in-app chưa đăng nhập không chứng minh mọi phiên đều bị chặn. Đọc canvas, layer tree và bảng thuộc tính của frame/section ở desktop/mobile; ghi nguồn UI và giá trị đã xác minh. Không đọc token/credential hoặc gọi endpoint nội bộ để vượt quota/quyền.
- Tiếp tục khảo sát và các bước độc lập bằng bằng chứng đã có. Chỉ cấu hình phần đủ bằng chứng và phù hợp prerequisite của công cụ/skill đang áp dụng; không suy font, màu, spacing hoặc media từ thumbnail. Nếu thiếu bằng chứng bắt buộc, đánh dấu phần đó `blocked` và yêu cầu đúng phần thiếu (quyền truy cập hoặc bản export/thuộc tính), không báo hoàn tất.
- Ghi node ID, kích thước frame, nguồn đọc (design context/API/UI), screenshot và thông số còn thiếu vào tài liệu init. Screenshot toàn trang dùng khảo sát; cần xem rõ từng section trước khi dựng. Asset cuối vẫn theo `store-content-media`, không dùng screenshot toàn frame làm ảnh thay thế thiết kế.
- Nếu Figma báo chủ file đã tắt export/copy/sharing, dừng lấy asset qua mọi đường khác; không coi timeout là lý do tìm cách vượt quyền. Hỏi một lần về khả năng bật quyền hoặc cung cấp asset hợp lệ. Khi người dùng xác nhận không thể cấp quyền, tiếp tục phần Inspect/layout độc lập; lưu instance phụ thuộc media/catalog dưới dạng draft bị tắt và ghi rõ nguồn còn thiếu, không upload thumbnail/screenshot thay ảnh hay báo section đã hoàn tất.

### Tối ưu thao tác có bằng chứng

- Tái sử dụng brief, link, store, branch/worktree và evidence đã xác minh trong phiên hoặc tài liệu init; không hỏi lại hay init lại. Sau reconnect, tìm lại browser theo profile/tab URL, không coi ID browser tạm thời là ổn định.
- Khảo sát layer cấp section và kích thước/padding desktop/mobile theo nhóm đọc độc lập; lưu kết quả gọn theo node. Sau đó chỉ đào sâu block/control còn ảnh hưởng routing hoặc còn thiếu bằng chứng. Không dump toàn bộ file/template lớn khi chỉ cần schema/preset của ứng viên.
- Trong Figma UI, tên accessible của layer đang hover/selected có thể thêm hậu tố khóa tạm thời; đọc lại snapshot rồi chọn locator duy nhất. Với canvas quá nhỏ, chọn zoom có sẵn rồi double-click layer để xem đúng vùng; đợi render rõ qua observation trước khi đọc ảnh. Không dùng thumbnail còn pixelated để đo thiết kế.
- Dùng manifest chung theo nguồn node/checksum → store resource → các instance sử dụng. Audit/reuse trước upload; preset mặc định và từng instance vẫn phải nhận đúng reference, không tải/upload lặp cho cùng media.
- Trong cây layer Dev Mode, có thể dùng menu ngữ cảnh `Expand all children` để đọc một section thay vì mở từng cấp. Khi chọn layer lồng sâu, ưu tiên click đúng nhãn tên bên trong row; click giữa row có thể trúng caret và chỉ đóng/mở cây. Xác minh tên layer và node URL trong Inspect đã đổi trước khi ghi kích thước hoặc tải asset. Không lấy trạng thái hover của row làm bằng chứng selection.
- Khi người dùng yêu cầu học hỏi trong lúc init, cập nhật skill ở checkout dùng chung bằng bài học đã kiểm chứng và có thể tái dùng; giữ chi tiết theme/node trong tài liệu init. Thay đổi hẹp, kiểm tra link/frontmatter và hành vi liên quan; không tự nới giới hạn implementation, deploy hoặc quyền store. Không tự commit/push skill.

Đọc ba nguồn Figma, screenshot và kích thước frame; phân tách toàn trang thành Header (kể cả announcement/navigation), từng section trong homepage, Footer. So sánh thứ tự, vùng ẩn/hiện và cách chuyển layout ở mobile. Inventory section/block/schema, preset, placement, template và section group thực tế của worktree; không đoán control từ hình ảnh.

Lập bản đồ theo thứ tự trang: node desktop/mobile → section type → cây block dự kiến → setting layout responsive → preset/instance local → content/media cần dùng → mức phù hợp hoặc gap. Xem cả block lồng nhau, giới hạn và dependency. Chọn section đúng ngữ nghĩa hỗ trợ cả hai viewport. Chỉ dùng `Custom section` nếu section chứa và block của nó **đã tồn tại**, theo routing/naming của build-preset; không tạo implementation custom.

Đối chiếu tài nguyên dùng chung toàn trang (product, collection, logo, ảnh/video, navigation) để tránh tạo trùng về sau. Ghi bản đồ và tiến độ vào tài liệu init riêng của theme, ví dụ `docs/theme-init/<slug>.md`; không dùng log base hoặc bịa mục custom implementation. Bản đồ phải hoàn tất trước khi dựng section đầu tiên. Section không có ứng viên phù hợp được đánh dấu `skipped` kèm chi tiết thiếu và báo lại, vẫn làm phần phù hợp.

## 3. Áp dụng style guide

Dùng theme-style-guide đọc toàn bộ Theme Settings schema và ánh xạ thuộc tính Figma có bằng chứng vào `config/settings_data.json` của worktree: typography, scheme, button, badge và các nhóm có control tương ứng. Xác minh font handle, giá trị và tham chiếu scheme theo skill phụ thuộc. Chỉ chỉnh `current`, giữ comment đầu file, saved presets và giá trị ngoài phạm vi. Áp dụng [quy trình Global Theme Settings của build-preset](../build-preset/SKILL.md#global-theme-settings-trong-configsettings_datajson): đọc schema và nơi setting được sử dụng, kiểm tra kiểu/option/min/max/step, ghi giá trị cũ/mới cùng bằng chứng Figma và ảnh hưởng tới các section/block dùng chung. Không cần xin phép riêng để sửa file local trong phạm vi init đã yêu cầu.

Khi hoàn thiện từng section, được tiếp tục hiệu chỉnh Theme Settings hiện có nếu frame desktop/mobile cung cấp bằng chứng bổ sung, ví dụ product card, swatch hoặc badge. Kiểm tra lại các section đã cấu hình dùng cùng setting; không lấy một chi tiết riêng lẻ làm lý do thay toàn bộ typography/palette khi chưa đủ căn cứ. Validate JSON, schema values và Theme Check; đối chiếu cả hai viewport khi có preview. Quyền sửa local không cấp quyền lưu Theme Editor, ghi cấu hình theme qua API/bot, deploy hay publish.

Với token thiếu control hoặc cần sửa implementation/range, giữ giới hạn init-theme và ghi gap; không mở rộng schema.

## 4. Hoàn thiện tuần tự từng section

Với theme mới, sau khi hoàn tất bước Style Guide và trước khi dựng instance đầu tiên, reset template homepage đích: đặt `sections` thành `{}` và `order` thành `[]`, giữ comment đầu file và metadata ngoài composition. Đây là xóa instance demo trong template, không xóa đăng ký `presets[]` của section, implementation hay template trang khác. Không tự reset lại khi tiếp tục theme đã build; kiểm tra trạng thái và giữ instance đã hoàn thiện. Header/Footer được dựng trong group tương ứng theo bản đồ, không xóa group ngoài phạm vi.

Đi theo bản đồ Header → homepage từ trên xuống → Footer, gồm các section con trong group. Với **mỗi section**:

1. Đọc kỹ node/screenshot desktop và mobile; phân tích hierarchy, thứ tự/cây block, width, columns, spacing, alignment, typography, crop/focal point và responsive. Xác minh lại setting/allowed block của ứng viên trước khi ghi.
2. Dùng build-preset tạo/cập nhật preset và instance trong template/group local đúng đích. Giữ tên/category và quy tắc preset của skill đó, tôn trọng giới hạn init-theme. Không đụng composition trang khác. Nếu một section type xuất hiện nhiều lần, giữ instance riêng với content/layout của từng vùng; không để cập nhật preset mặc định ghi đè instance đã hoàn thiện.
3. Ngay khi layout section đã dựng, dùng store-content-media hoàn thiện đúng ảnh, video, product, collection, blog hoặc resource cần để giống Figma trên store đã xác định. Đọc reference đúng loại; reuse tài nguyên đã xác minh và manifest dùng chung, chỉ tạo phần thiếu. Không biến ảnh trang trí thành product, không bịa giá/thuộc tính thương mại thiếu nguồn. Nếu thiếu quyền/đích/source bắt buộc, hỏi phần thiếu; không tạo dữ liệu phỏng đoán.
4. Chờ processing có giới hạn và readback resource/media; gắn URL lâu dài, handle hoặc file reference đúng kiểu setting vào **preset/instance local**. Áp dụng cùng tham chiếu vào các đích local cần thiết; không để preset còn ảnh rỗng trong khi chỉ instance hoàn thiện. Không lưu Figma/staging URL làm tài nguyên cuối.
5. Validate JSON/schema/block tree, reference và section/group placement. Khi có preview được phép, đối chiếu section tại cả kích thước Figma desktop/mobile, gồm crop, wrapping, overflow và nội dung thật. Preview cần upload theme chỉ chạy khi đã có quyền deploy tương ứng; nếu chưa có, ghi rõ chỉ kiểm tra local và thiếu kiểm chứng storefront, không tự push.
6. Ghi trạng thái và evidence vào tài liệu init: `complete` khi đã kiểm chứng đầy đủ, `configured-unverified` nếu chỉ thiếu preview, `blocked` nếu thiếu resource/quyền/đầu vào, hoặc `skipped` nếu không có khả năng hiện có. Ghi cụ thể mismatch còn lại. Không chuyển sang section tiếp theo khi section hiện tại vẫn còn việc khả thi trong phạm vi. Khi bị chặn bên ngoài, ghi và báo chặn rồi mới tiếp tục section độc lập; không tuyên bố section đó hoàn tất.

## 5. Kiểm tra tổng thể và bàn giao

Kiểm tra toàn trang theo cả desktop/mobile, thứ tự Header/template/Footer, style guide, schema/resource reference và các section lặp. Chạy Theme Check theo AGENTS.md và kiểm tra diff: chỉ cấu hình/preset/composition, tài liệu init và file khởi tạo repo bắt buộc; không có thay đổi implementation ngoài ý muốn. Báo rõ check không thể chạy và nguyên nhân.

Bàn giao branch, đường dẫn worktree tuyệt đối, file thay đổi, section/block đã dùng, content/media đã upload/reuse và trạng thái deploy. Liệt kê riêng từng section bỏ qua, gap, phần bị chặn hoặc chưa xem preview; nêu control/section/block còn thiếu. Không khẳng định khớp Figma hoàn toàn nếu còn gap hoặc chỉ kiểm tra local. Không commit/push/publish thêm nếu chưa có yêu cầu.
