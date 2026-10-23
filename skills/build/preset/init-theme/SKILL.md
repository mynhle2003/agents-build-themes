---
name: init-theme
description: "Khởi tạo Shopify theme mới từ main hoặc theme biến thể kế thừa theme nguồn; lập plan Figma, áp dụng Style Guide, dựng preset và content/media bằng section/block hiện có, kiểm chứng preview; cho phép căn chỉnh token, range/runtime mapping hiện hữu theo Style Guide, không tạo implementation mới."
---

# Init Theme

Khởi tạo theme mới từ base hoặc theme biến thể từ theme đã có rồi dựng Header → template homepage → Footer theo Figma. Khảo sát toàn trang trước; sau đó hoàn thiện layout, content/media và đối chiếu desktop/mobile của từng section trước khi chuyển section tiếp theo. Đây là workflow cấu hình bằng khả năng hiện có; được kế thừa implementation của theme nguồn, không tạo implementation mới trong init. Riêng Style Guide được căn chỉnh giá trị CSS token, range và runtime mapping hiện hữu theo contract dùng chung bên dưới.

## Truy cập Figma

Khi cần dữ liệu Figma, bắt buộc áp dụng [Figma MCP và cấp quyền tài khoản](../theme-style-guide/references/figma-access.md) trước khi đọc thiết kế/asset. Với bản cài phẳng, đọc `.agents/skills/theme-style-guide/references/figma-access.md`; thiếu dependency thì báo thiếu, không tự chọn cách truy cập khác.

## Chọn flow trước khi khởi tạo

Khi gọi skill để khởi tạo, **hỏi rõ “Tạo theme mới hay theme biến thể từ theme đã có?” trước khi tạo branch/worktree** nếu người dùng chưa chọn. Không tự suy từ tên theme hoặc độ giống thiết kế. Nếu yêu cầu đã nói rõ một lựa chọn, dùng lựa chọn đó, không hỏi lại. Với yêu cầu tiếp tục, đọc mode đã lưu trong plan và tiếp tục đúng checkpoint. Khi chỉ bảo trì skill, không chạy câu hỏi khởi tạo.

- **Theme mới:** nguồn là `main` của base cá nhân; Style Guide → đối chiếu layout với preset/instance hiện có → tái sử dụng và chỉnh delta từ trên xuống; không reset toàn bộ homepage.
- **Theme biến thể:** hỏi theme nguồn nếu chưa có; tạo branch và worktree mới từ code mới nhất của theme nguồn tại thời điểm tạo, lấy y hệt section/block, logic, preset, template và Theme Settings. **Không đọc lại Style Guide, không hỏi link Style Guide, không áp lại token và không reset composition.** Ghi SHA hiện tại làm checkpoint, không dùng checkpoint cũ lúc theme nguồn mới init. Không tạo từ `main` rồi chép vài file. Ví dụ Essen–Arche và Elara–Malandra là các cặp biến thể theo yêu cầu chủ repo; cặp tên không quyết định chiều kế thừa, phải xác định nguồn → đích.
- Các section/logic giống nhau tiếp tục dùng implementation đã kế thừa, không nhân bản hoặc đổi tên để tạo phiên bản riêng. Khác biệt design ưu tiên cấu hình hiện có. Nếu cần logic mới, ghi gap để xử lý bằng yêu cầu implementation riêng. Nhánh biến thể là snapshot độc lập; đăng ký quan hệ và mốc cập nhật hai chiều theo [Hồ sơ cập nhật biến thể](references/variant-updates.md). Khi tiếp tục build/sửa lỗi, đọc hồ sơ để phát hiện fix cần chuyển giữa các theme; không tự merge hoặc đưa custom vào `main`.

Đọc [Plan và checkpoint](references/execution-plan.md) trước mutation. Lưu mode, nguồn và phạm vi một lần; cập nhật plan khi có evidence hoặc yêu cầu mới.

## Đầu vào bắt buộc

Khi được yêu cầu **chạy** init theme, xác định mode ở trên và hỏi tên theme đích nếu chưa cung cấp. **Theme mới** cần đủ ba link Figma có node/frame cụ thể: style guide, homepage desktop, homepage mobile. **Biến thể** hỏi tên đích, theme nguồn và **hai link Figma homepage desktop/mobile** có node/frame cụ thể; không hỏi hoặc đọc Figma Style Guide. Kế thừa nguyên Style Guide đã cấu hình mà không yêu cầu xác nhận dùng chung. Hỏi gộp phần còn thiếu, không hỏi lại dữ liệu đã có. Nếu thiếu link layout, vẫn có thể chuẩn bị branch/worktree từ nguồn đã xác định nhưng chưa build phần thiếu bằng chứng; thiếu store chỉ chặn content/media mutation. Ngoại lệ clone-only chỉ áp dụng khi người dùng nói rõ chỉ sao chép/tạo nhánh, chưa build design. Chỉ rà Style Guide khi có yêu cầu riêng đổi style. Tái sử dụng dữ liệu đã cung cấp, không hỏi lại. Xác định store đích khi có content/media work; không suy store từ profile minh họa. Thiếu store vẫn làm phần local, chưa mutation store. Không tự coi desktop là bằng chứng mobile.

Yêu cầu tạo/sửa **skill này** không phải yêu cầu chạy init: không hỏi tên theme, tạo branch/worktree hay upload store trong lúc bảo trì skill.

## Skill phụ thuộc và giới hạn ưu tiên

Đọc đúng skill trước tác vụ tương ứng, giải quyết đường dẫn từ thư mục skill này:

- [theme-style-guide](../theme-style-guide/SKILL.md): ánh xạ style guide vào Theme Settings.
- [build-preset](../build-preset/SKILL.md): chọn section/block, dựng preset và composition.
- [store-content-media](../../../setup-store/store-content-media/SKILL.md): upload/tái sử dụng media, tạo content/resource cần thiết và gắn reference local.

Nếu đang dùng bản cài phẳng, tìm các skill cùng tên trong `.agents/skills/`; không dùng đường dẫn tương đối nhóm nguồn cho bản phẳng. Nếu thiếu dependency, báo đường dẫn thiếu; không tự viết workflow thay thế. Đọc reference con theo tác vụ, không tải toàn bộ reference mặc định. Trước mỗi công cụ Figma có prerequisite, đọc skill Figma tương ứng, gồm `figma-design-to-code` trước `get_design_context`.

Trước bước Style Guide, đọc [contract config dùng chung](../theme-style-guide/references/config-theme-settings.md), mục 1–4 rồi các mục liên quan. Đường dẫn sibling này dùng được cả cây nguồn và bản cài phẳng; nếu dependency thiếu thì báo, không tự thay bằng workflow khác. Đây là nguồn duy nhất cho quyền token/range/mapping và cách đọc Typography, Colors, Generated, button responsive.

**Giới hạn của init-theme và quyền Style Guide:**

- Được sửa `current` trong `config/settings_data.json` local bằng các Theme Settings hiện có để khớp Figma; quyền này thuộc phạm vi init/tiếp tục theme, không cần xin phép riêng cho từng giá trị. Chỉ sửa preset trong schema và composition/settings của template/section group thuộc trang đích. Được tạo color scheme bằng definition hiện có.
- Trong bước Style Guide được sửa giá trị token CSS hiện hữu, min/max/step của range hiện hữu và runtime mapping/binding Liquid/CSS hiện hữu theo mục 1.1 của contract. Ngoại trừ migration control đã duyệt ở mục 1.2, giữ ID/type/unit/ý nghĩa, default và dữ liệu đã lưu hợp lệ; kiểm chứng toàn bộ consumer. Không cần hỏi lại quyền cho các chỉnh sửa này.
- **Ngoại lệ compare-at đã được cho phép:** nếu thiếu option tương ứng, được custom color qua `--price-compare-color`, tỷ lệ `font-size` và `opacity` trong rule `.price__compare-at` hiện hữu để khớp Figma; theo [contract compare-at](../theme-style-guide/references/config-theme-settings.md#642-ngoại-lệ-compare-at-color-font-size-opacity). Đọc fill/alpha/opacity và size, tính em theo size cha thực, audit card/PDP/cart. Không cần hỏi lại cho ba thuộc tính này; không tự thêm setting/token/selector/breakpoint.
- **Ngoại lệ line-height Button Tertiary đã được cho phép:** khi chưa có control phù hợp, được chỉnh riêng `line-height` trong rule Tertiary hiện hữu để khớp label Figma; theo [mục 6.3.1](../theme-style-guide/references/config-theme-settings.md#631-ngoại-lệ-line-height-button-tertiary). Không áp số đo Tertiary lên Primary/Secondary, không thêm setting/token/selector hay đổi height/padding/underline.
- Ngoại lệ nâng cấp Typography đã duyệt: tracking từng cấp Heading, weight riêng Button/Badge, migration schema/data/locale và nạp variant font cùng family theo [mục 1.2](../theme-style-guide/references/config-theme-settings.md#12-bộ-nâng-cấp-typography-đã-được-duyệt); Heading tablet không cần đối chiếu. Ngoài bộ này, không tạo section/block, setting/option mới, markup, JS, SVG, selector/breakpoint/layout mới, custom CSS ngoài ngoại lệ compare-at và line-height Tertiary nêu trên hoặc sửa allow-list/placement/limits. Thêm select value hoặc CSS token phải đề xuất và được người dùng duyệt trước theo mục 9. Không kế thừa ngoại lệ height-option/SVG từ build-preset để mở rộng phạm vi; không viết CSS giá riêng ngoài đúng ba thuộc tính compare-at theo contract.
- Giá trị Style Guide chưa biểu diễn được: ưu tiên config, căn chỉnh token/range/mapping hiện hữu; nếu vẫn thiếu value/token thì hỏi theo contract, không tự chọn gần đúng và báo khớp. Thiếu setting hoặc cần tính năng/layout mới thì ghi gap. Icon thiếu cũng là gap, không gọi build-theme để bù.
- Không có section/block phù hợp thì bỏ qua vùng đó và ghi rõ lý do; không tạo placeholder giả như đã xong, không tự chuyển sang custom build. Nếu chỉ lệch chi tiết nhỏ, dùng composition hiện có phù hợp và ghi sai lệch.
- Content/media ở store; preset/template chỉ chỉnh file local. Không save Theme Editor hay mutation cấu hình theme bằng API/bot. Upload content không cấp quyền deploy/publish theme. Không tự commit/push các thay đổi cấu hình sau init nếu chưa được yêu cầu; commit khởi tạo bắt buộc của lệnh repo là ngoại lệ thuộc bước tạo theme.

## 1. Tạo nhánh và worktree

Chọn đúng quy trình: các đoạn tạo từ `main` bên dưới chỉ dành cho **theme mới**. Với **biến thể**, đọc [Tạo nhánh biến thể](references/variant-theme.md); không chạy `new-theme` từ main. Cả hai flow phải ghi checkpoint nguồn để kiểm chứng và tiếp tục, không tự đồng bộ upstream trong init.

Đọc AGENTS.md repo base, trạng thái Git, remotes, `main`, danh sách branch và `git worktree list` trước mutation. Giữ mọi thay đổi có sẵn; base bẩn thì dừng bước tạo theme và báo đường dẫn, không stash/reset hoặc mang diff sang theme mới.

Chuẩn hóa tên thành slug chữ thường, số và gạch ngang; không lặp hậu tố `-theme`. Người dùng nhập `a` → slug `a-theme`, branch `theme/a-theme`, worktree `<thư mục cha repo base>/a-theme`. Nếu tên không chuyển thành slug rõ ràng hoặc trùng branch/path, hỏi phần mơ hồ; không ghi đè, xóa hoặc tái sử dụng theme khác. Với yêu cầu tiếp tục theme đã init, xác minh đúng branch/worktree/hồ sơ trước khi tiếp tục, không tạo lại.

Theo repo có `node theme-base new-theme`, đọc implementation/help trước khi chạy. Từ base sạch trên `main`, chạy `node theme-base new-theme <slug>` **không `--push`**, để lệnh tạo hồ sơ và loại log base khỏi theme theo quy tắc repo. Lệnh hiện tại có thể switch checkout base sang branch theme và tạo commit khởi tạo; sau thành công, switch checkout base trở lại `main`, rồi chạy `git worktree add <đường dẫn tuyệt đối> theme/<slug>` bằng branch vừa có, không dùng `-b` tạo lại. Nếu lệnh thất bại, kiểm tra trạng thái thực tế và báo lỗi; không tiếp tục chuỗi hoặc tự rollback phá hủy dữ liệu. Nếu repo không có lệnh/quy trình tạo theme tương ứng, báo thiếu thay vì bỏ qua hợp đồng khởi tạo.

Xác minh checkout base ở `main`, worktree mới ở `theme/<slug>`, hồ sơ theme tồn tại và theme không mang log base cá nhân. Từ đây mọi thao tác theme dùng workdir của worktree mới. Không đọc/ghi nội dung log base từ skill này; để lệnh repo xử lý. Không tự cập nhật upstream/base khi init.

## 2. Khảo sát toàn bộ trước khi build

Phần Figma này dành cho theme mới hoặc giai đoạn build design biến thể đã được yêu cầu; **không chạy khi chỉ clone biến thể**. Clone-only hoàn tất sau kiểm chứng bản sao, hồ sơ và branch/worktree mới; không tự reset/build hoặc đòi đủ ba link Figma. Khi build biến thể, khảo sát layout desktop/mobile và delta với composition kế thừa, dùng nguyên Theme Settings hiện tại.

Áp dụng flow đọc reference của `build-preset`: xác minh node và kích thước, đọc cấu trúc/control, rồi đối chiếu screenshot ở cả hai viewport trước khi ghi cấu hình. Không coi lỗi một công cụ là bằng chứng thiết kế không thể truy cập.

### Đọc Figma và xử lý công cụ bị chặn

- Ưu tiên `get_design_context` kèm screenshot sau khi đọc prerequisite Figma. Với phản hồi sparse, đọc các node con nhìn thấy trước khi cấu hình; không dùng metadata tổng quan làm bằng chứng đầy đủ.
- Khi công cụ yêu cầu quyền tài khoản, thực hiện luồng kết nối Figma MCP theo [contract cấp quyền](../theme-style-guide/references/figma-access.md), chờ người dùng Accept rồi đọc lại node. Phân biệt quota, quyền file và OAuth; hết quota thì tự dùng CUA trên Chrome đang mở với profile `minhle@beae.com` theo contract, không dùng fallback này để né yêu cầu cấp quyền.
- Có thể dùng `use_figma` chỉ đọc sau khi đọc `figma-use` nếu công cụ phù hợp và kết nối đã được cấp quyền; không dùng nó để né yêu cầu Accept đang chờ hoặc lỗi quyền/quota. Không sửa file Figma để phục vụ khảo sát. Dùng UI theo fallback hết quota hoặc lựa chọn rõ của người dùng trong contract chung; các mẹo UI bên dưới áp dụng khi đã chọn đúng Chrome/tài khoản.
- Tiếp tục khảo sát và các bước độc lập bằng bằng chứng đã có. Chỉ cấu hình phần đủ bằng chứng và phù hợp prerequisite của công cụ/skill đang áp dụng; không suy font, màu, spacing hoặc media từ thumbnail. Nếu thiếu bằng chứng bắt buộc, đánh dấu phần đó `blocked` và yêu cầu đúng phần thiếu (quyền truy cập hoặc bản export/thuộc tính), không báo hoàn tất.
- Ghi node ID, kích thước frame, nguồn đọc (design context/API/UI), screenshot và thông số còn thiếu vào tài liệu init. Screenshot toàn trang dùng khảo sát; cần xem rõ từng section trước khi dựng. Asset cuối vẫn theo `store-content-media`, không dùng screenshot toàn frame làm ảnh thay thế thiết kế.
- Nếu Figma báo chủ file đã tắt export/copy/sharing, dừng lấy asset qua mọi đường khác; không coi timeout là lý do tìm cách vượt quyền. Hỏi một lần về khả năng bật quyền hoặc cung cấp asset hợp lệ. Khi người dùng xác nhận không thể cấp quyền, tiếp tục phần Inspect/layout độc lập; lưu instance phụ thuộc media/catalog dưới dạng draft bị tắt và ghi rõ nguồn còn thiếu, không upload thumbnail/screenshot thay ảnh hay báo section đã hoàn tất.

### Tối ưu thao tác có bằng chứng

- Tái sử dụng brief, link, store, branch/worktree và evidence đã xác minh trong phiên hoặc tài liệu init; không hỏi lại hay init lại. Khi dùng CUA theo contract, sau reconnect tìm lại browser theo profile/tab URL, không coi ID browser tạm thời là ổn định.
- Khảo sát layer cấp section và kích thước/padding desktop/mobile theo nhóm đọc độc lập; lưu kết quả gọn theo node. Sau đó chỉ đào sâu block/control còn ảnh hưởng routing hoặc còn thiếu bằng chứng. Không dump toàn bộ file/template lớn khi chỉ cần schema/preset của ứng viên.
- Trong Figma UI, tên accessible của layer đang hover/selected có thể thêm hậu tố khóa tạm thời; đọc lại snapshot rồi chọn locator duy nhất. Với canvas quá nhỏ, chọn zoom có sẵn rồi double-click layer để xem đúng vùng; đợi render rõ qua observation trước khi đọc ảnh. Không dùng thumbnail còn pixelated để đo thiết kế.
- Dùng manifest chung theo nguồn node/checksum → store resource → các instance sử dụng. Audit/reuse trước upload; preset mặc định và từng instance vẫn phải nhận đúng reference, không tải/upload lặp cho cùng media.
- Trong cây layer Dev Mode, có thể dùng menu ngữ cảnh `Expand all children` để đọc một section thay vì mở từng cấp. Khi chọn layer lồng sâu, ưu tiên click đúng nhãn tên bên trong row; click giữa row có thể trúng caret và chỉ đóng/mở cây. Xác minh tên layer và node URL trong Inspect đã đổi trước khi ghi kích thước hoặc tải asset. Không lấy trạng thái hover của row làm bằng chứng selection.
- Khi người dùng yêu cầu học hỏi trong lúc init, cập nhật skill ở checkout dùng chung bằng bài học đã kiểm chứng và có thể tái dùng; giữ chi tiết theme/node trong tài liệu init. Thay đổi hẹp, kiểm tra link/frontmatter và hành vi liên quan; không tự nới giới hạn implementation, deploy hoặc quyền store. Không tự commit/push skill.

Đọc nguồn Figma theo mode (theme mới: Style Guide + homepage desktop/mobile; biến thể: chỉ homepage desktop/mobile), screenshot và kích thước frame; phân tách toàn trang thành Header (kể cả announcement/navigation), từng section trong homepage, Footer. So sánh thứ tự, vùng ẩn/hiện và cách chuyển layout ở mobile. Inventory section/block/schema, preset, placement, template và section group thực tế của worktree; không đoán control từ hình ảnh.

Lập bản đồ theo thứ tự trang: node desktop/mobile → section type → cây block dự kiến → setting layout responsive → preset/instance local → content/media cần dùng → mức phù hợp hoặc gap. Xem cả block lồng nhau, giới hạn và dependency. Chọn section đúng ngữ nghĩa hỗ trợ cả hai viewport. Chỉ dùng `Custom section` nếu section chứa và block của nó **đã tồn tại**, theo routing/naming của build-preset; không tạo implementation custom.

Đối chiếu tài nguyên dùng chung toàn trang (product, collection, logo, ảnh/video, navigation) để tránh tạo trùng về sau. Ghi bản đồ và tiến độ vào tài liệu init riêng của theme, ví dụ `docs/theme-init/<slug>.md`; không dùng log base hoặc bịa mục custom implementation. Bản đồ phải hoàn tất trước khi dựng section đầu tiên. Section không có ứng viên phù hợp được đánh dấu `skipped` kèm chi tiết thiếu và báo lại, vẫn làm phần phù hợp.

### Kiểm tra layout và tái sử dụng preset trước khi chỉnh template

Áp dụng cho cả theme mới và biến thể. Trước mutation composition, đối chiếu từng vùng Figma desktop/mobile với **instance đang có trong template/group** và **preset đã đăng ký của section**. So sánh hierarchy/cây block, thứ tự, layout responsive, content/media và setting có thể cấu hình; không kết luận giống chỉ dựa vào tên preset hoặc thumbnail.

- Khớp layout: giữ instance, ID, cây block, setting và reference đã xác minh; chỉ cập nhật delta có bằng chứng.
- Gần khớp và control hiện có đủ đáp ứng: tái sử dụng preset/cây block phù hợp rồi chỉnh phần khác biệt; không dựng lại từ đầu.
- Chưa có instance phù hợp: dùng preset có sẵn phù hợp nhất để thêm instance riêng. Chỉ dựng composition mới từ block hiện có khi không preset nào đáp ứng, vẫn giữ giới hạn không sửa implementation.
- Vùng cũ không có trong thiết kế đích: ghi rõ `remove` trong bản đồ rồi xử lý riêng vùng đó; không xóa hàng loạt để làm trống template. Giữ các vùng chưa khảo sát/chưa đủ bằng chứng.

Ghi preset/instance ứng viên, kết quả `reuse/change/add/remove`, lý do và delta cần chỉnh vào plan trước khi build. Không reset toàn bộ `sections`/`order`, không xóa mọi preset trong template/schema. Khi cùng section type có nhiều consumer, chỉnh instance đích và bảo toàn các instance còn lại; chỉ cập nhật preset mặc định theo quy tắc build-preset sau khi rà consumer.

## 3. Áp dụng style guide

Đây là checkpoint bắt buộc cho **theme mới** trước chỉnh composition/build. **Biến thể bỏ qua bước này**, ghi `inherited` kèm SHA nguồn trong plan; không đọc lại Figma Style Guide hay ghi lại Theme Settings. Chỉ mở lại bước style khi người dùng yêu cầu riêng thay đổi style. Với theme mới, ghi riêng normal/hover của primary, secondary, tertiary, font weight, tracking và underline: thiếu bằng chứng hover thì giữ nguyên và ghi chưa xác minh, không coi màu normal là bằng chứng hover.

Dùng theme-style-guide đọc schema liên quan và contract dùng chung, lập manifest đủ Heading, Text, Eyebrow, Button, Badges, Product card title/price trước khi phân bổ token shared. Family/style/weight của Heading lấy từ Heading, Body từ Body/16 – Body text, Accent từ frame Eyebrow; chọn đúng biến thể font picker và kiểm tra role token/consumer theo mục 6.0 của contract, không hardcode weight riêng. Body/16 – Body text cung cấp base size, line height và tracking; theo mục 6.2/6.4 của contract, bind tracking vào `--font-body-letter-spacing` qua scale chung, Price kế thừa tracking và giữ font/size riêng. Kiểm tra cascade, override cứng và output px/em của mọi consumer Body. Style Guide cung cấp Heading/Text/Button/Badges; hỏi URL frame Eyebrow và URL một product card nếu chưa có, không suy từ trang khác. Thiếu nguồn chỉ chặn phần phụ thuộc và việc chốt scale global, không chặn chuẩn bị worktree hay việc độc lập. Đọc thêm height/padding/gap desktop/mobile và Tertiary Show underline/Underline offset; Colors giữ role/scheme ID, Generated/N và from Generated/N tra đúng cấp từ Heading HEX theo contract; hover thiếu thiết kế được tạo từ màu normal, kiểm tra contrast chữ/nền4.5:1 theo mục 10.4, ghi derived-hover. Sau đó đọc Theme Settings schema và ánh xạ thuộc tính Figma có bằng chứng vào `config/settings_data.json` của worktree: typography, scheme, button, badge và các nhóm có control tương ứng. Xác minh font handle, giá trị và tham chiếu scheme theo skill phụ thuộc. Chỉ chỉnh `current`, giữ comment đầu file, saved presets và giá trị ngoài phạm vi. Áp dụng [quy trình Global Theme Settings của build-preset](../build-preset/SKILL.md#global-theme-settings-trong-configsettings_datajson): đọc schema và nơi setting được sử dụng, kiểm tra kiểu/option/min/max/step, ghi giá trị cũ/mới cùng bằng chứng Figma và ảnh hưởng tới các section/block dùng chung. Không cần xin phép riêng để sửa file local trong phạm vi init đã yêu cầu.

Đọc gap giữa giá bán và giá gạch trên card Figma desktop/mobile, gắn vào `--compare-at-price-spacing` hiện hữu theo [contract Price gap](../theme-style-guide/references/config-theme-settings.md#641-khoảng-cách-giá-bán--compare-at-price); audit consumer dùng chung, không hardcode gap theo card hoặc tự thêm setting/token responsive.

Card Figma còn là nguồn cấu hình **layout nhóm Product cards**, không chỉ title/price. Áp dụng [contract Product cards](../theme-style-guide/references/config-theme-settings.md#67-product-cards-cấu-hình-layout-từ-card-figma): đọc desktop/mobile, phân biệt ba lớp spacing, map style/scheme, ratio, alignment, swatch, badge và quick add/view vào control hiện hữu; kiểm tra các consumer dùng chung và override của từng instance. Với theme mới, thực hiện cùng bước Style Guide; với biến thể, chỉ cập nhật khi yêu cầu phát triển layout đích bao gồm thay đổi card, giữ nguyên Style Guide kế thừa và không tự config lại typography/màu. Thiếu khả năng thì ghi gap; không tạo CSS/layout mới, setting hoặc tự thay catalog.

Khi hoàn thiện từng section, được tiếp tục hiệu chỉnh Theme Settings hiện có nếu frame desktop/mobile cung cấp bằng chứng bổ sung, ví dụ product card, swatch hoặc badge. Kiểm tra lại các section đã cấu hình dùng cùng setting; không lấy một chi tiết riêng lẻ làm lý do thay toàn bộ typography/palette khi chưa đủ căn cứ. Validate JSON, schema values và Theme Check; đối chiếu cả hai viewport khi có preview. Quyền sửa local không cấp quyền lưu Theme Editor, ghi cấu hình theme qua API/bot, deploy hay publish.

Giữ nhãn UI và preset ngoài phạm vi. Chỉ đổi phần chưa khớp; dùng một scale letter spacing/line height cho mọi nhóm. Range/runtime mapping hiện hữu được sửa theo mục 1.1, ghi bảng trước/sau, grid/default/saved values và output consumer. Thiếu select value/token hỏi theo mục 9; thiếu setting hoặc cần implementation mới thì ghi gap, không tự mở rộng schema. Không ghi đè giá trị kế thừa của biến thể khi chưa có yêu cầu riêng đổi style.

## 4. Hoàn thiện tuần tự từng section

Sau khảo sát và bước Style Guide tương ứng mode, lưu backup composition trước chỉnh trong thư mục local ignored. Dùng kết quả đối chiếu preset/instance để chỉnh từng vùng theo bản đồ; **không reset homepage ở cả hai mode**. Giữ ID và cấu hình của instance tái sử dụng, chỉ thêm/xóa/di chuyển vùng có quyết định rõ trong plan. Không xóa preset đăng ký, implementation, template khác hoặc group ngoài phạm vi. Khi tiếp tục, kiểm tra checkpoint và giữ các instance đã hoàn thiện; không tạo lại hoặc reset template.

Đi theo bản đồ Header → homepage từ trên xuống → Footer, gồm các section con trong group. Với **mỗi section**:

1. Đọc kỹ node/screenshot desktop và mobile; phân tích hierarchy, thứ tự/cây block, width, columns, spacing, alignment, typography, crop/focal point và responsive. Xác minh lại setting/allowed block của ứng viên trước khi ghi.
2. Dùng build-preset tạo/cập nhật preset và instance trong template/group local đúng đích. Giữ tên/category và quy tắc preset của skill đó, tôn trọng giới hạn init-theme. Không đụng composition trang khác. Nếu một section type xuất hiện nhiều lần, giữ instance riêng với content/layout của từng vùng; không để cập nhật preset mặc định ghi đè instance đã hoàn thiện.
3. Ngay khi layout section đã dựng, dùng store-content-media hoàn thiện đúng ảnh, video, product, collection, blog hoặc resource cần để giống Figma trên store đã xác định. Đọc reference đúng loại; reuse tài nguyên đã xác minh và manifest dùng chung, chỉ tạo phần thiếu. Không biến ảnh trang trí thành product, không bịa giá/thuộc tính thương mại thiếu nguồn. Nếu thiếu quyền/đích/source bắt buộc, hỏi phần thiếu; không tạo dữ liệu phỏng đoán.
4. Chờ processing có giới hạn và readback resource/media; gắn URL lâu dài, handle hoặc file reference đúng kiểu setting vào **preset/instance local**. Áp dụng cùng tham chiếu vào các đích local cần thiết; không để preset còn ảnh rỗng trong khi chỉ instance hoàn thiện. Không lưu Figma/staging URL làm tài nguyên cuối.
5. Validate JSON/schema/block tree, reference và section/group placement. Khi có preview được phép, đối chiếu section tại cả kích thước Figma desktop/mobile, gồm crop, wrapping, overflow và nội dung thật. Preview cần upload theme chỉ chạy khi đã có quyền deploy tương ứng; nếu chưa có, ghi rõ chỉ kiểm tra local và thiếu kiểm chứng storefront, không tự push.
6. Ghi trạng thái và evidence vào tài liệu init: `complete` khi đã kiểm chứng đầy đủ, `configured-unverified` nếu chỉ thiếu preview, `blocked` nếu thiếu resource/quyền/đầu vào, hoặc `skipped` nếu không có khả năng hiện có. Ghi cụ thể mismatch còn lại. Không chuyển sang section tiếp theo khi section hiện tại vẫn còn việc khả thi trong phạm vi. Khi bị chặn bên ngoài, ghi và báo chặn rồi mới tiếp tục section độc lập; không tuyên bố section đó hoàn tất.

## 5. Kiểm tra tổng thể và bàn giao

Khi có quyền preview, áp dụng [Xác minh local và Editor](references/preview-verification.md). Theme Check pass, cổng mở hoặc CLI in link không chứng minh bản remote đã nhận đủ template/config. Không kết luận lỗi cache hoặc sai theme khi chưa đối chiếu evidence.

Kiểm tra toàn trang theo cả desktop/mobile, thứ tự Header/template/Footer, style guide, schema/resource reference và các section lặp. Chạy Theme Check theo AGENTS.md và kiểm tra diff: chỉ cấu hình/preset/composition, tài liệu init, file khởi tạo repo bắt buộc và phần token/range/runtime mapping và ngoại lệ compare-at Style Guide đã nêu trong contract. Kiểm tra grid range, default/saved values, output resolver và mọi consumer; select value/token mới phải có phê duyệt tương ứng. Không có implementation ngoài phạm vi. Báo rõ check không thể chạy và nguyên nhân.

Bàn giao branch, đường dẫn worktree tuyệt đối, file thay đổi, section/block đã dùng, content/media đã upload/reuse và trạng thái deploy. Liệt kê riêng từng section bỏ qua, gap, phần bị chặn hoặc chưa xem preview; nêu control/section/block còn thiếu. Không khẳng định khớp Figma hoàn toàn nếu còn gap hoặc chỉ kiểm tra local. Không commit/push/publish thêm nếu chưa có yêu cầu.
