# Plan và checkpoint init-theme

Lập một plan tại `docs/theme-init/<slug>.md` trước mutation theme. Tái sử dụng tài liệu đã có khi tiếp tục; plan là trạng thái hiện tại, không sao chép mọi log vào đó. Hỏi gộp đầu vào còn thiếu một lần, tiếp tục phần độc lập; câu trả lời mơ hồ không được coi là xác nhận file đã tải hay quyền đã cấp.

## Thông tin điều phối

- Mode: new / variant; theme đích, branch, đường dẫn worktree tuyệt đối.
- Nguồn: branch/ref và SHA chính xác; với variant ghi nguồn → đích, base checkpoint và hồ sơ custom kế thừa.
- Biến thể: liên kết `docs/variant-updates/<slug>.md`, các theme liên quan, checkpoint đã rà từng nguồn và fix còn chờ chuyển/nhận; đọc [quy trình cập nhật hai chiều](variant-updates.md) khi tạo, tiếp tục hoặc sửa lỗi.
- Theme mới: ba nguồn Figma, kích thước desktop/mobile và đường đọc khả dụng. Biến thể: Style Guide = `inherited` từ SHA nguồn, không đọc lại; hỏi đúng hai link homepage desktop/mobile, không hỏi Style Guide. Chỉ bỏ qua hai link khi người dùng yêu cầu rõ clone-only.
- Store canonical; quyền content/media, preview, commit/push đã có trong yêu cầu. Các quyền tách biệt, không suy từ quyền upload ảnh.
- Phạm vi template/group được sửa; các trang khác giữ nguyên. Media manifest/ledger hiện có và nơi lưu backup local.
- Việc đang làm, bước tiếp theo và blocker cụ thể; không dùng báo cáo cũ thay cho trạng thái hiện tại.

## Checkpoint

| Bước | Evidence để chuyển bước |
| --- | --- |
| Chọn mode và nguồn | Người dùng đã chọn new/variant; nguồn và đích không mơ hồ |
| Tạo worktree | Đúng branch/path, SHA nguồn, hồ sơ; variant có diff code/config ban đầu rỗng so với nguồn |
| Khảo sát | Khi build: bản đồ Header → homepage → Footer đủ desktop/mobile; clone-only không cần khảo sát Figma |
| Style Guide | New: manifest đầy đủ nguồn → role/breakpoint → setting/token → trước/sau; shared scale có đủ consumer, range/grid/default/saved values và runtime output đã kiểm tra; thiếu value/token ghi chờ duyệt. Variant: `inherited` từ SHA nguồn, bỏ qua đọc/áp lại style |
| Chuẩn bị composition | Cả hai mode: backup, đối chiếu layout với preset/instance hiện có, ghi ứng viên và quyết định reuse/change/add/remove; không reset toàn bộ template |
| Build tuần tự | Mỗi vùng đã cấu hình preset + instance, media readback, validate; blocker không còn việc khả thi thì chuyển vùng độc lập |
| QA / preview | Theme Check, diff phạm vi, desktop/mobile, local/Editor sync được xác minh hoặc ghi rõ phần chưa kiểm chứng |
| Bàn giao | Trạng thái từng vùng, gap và resource pending; file/branch, preview/theme ID và quyền deploy thực tế |

Mỗi dòng bản đồ section ghi: thứ tự/vùng, node desktop/mobile, section type và block tree, preset/instance ứng viên, reuse/change/add/remove và delta cần chỉnh (cả hai mode), đường dẫn preset và instance, media/resource, trạng thái, evidence cuối và việc tiếp theo. Khi một type dùng nhiều nơi, liệt kê tất cả consumer trước đổi preset; homepage không cấp quyền ghi đè trang collection.

Trạng thái dùng thống nhất: `pending`, `in-progress`, `complete`, `configured-unverified`, `blocked`, `skipped`. `complete` cần đủ cấu hình, resource và kiểm chứng yêu cầu; không gộp “đã viết JSON” với “đã xem preview”.

## Giảm thao tác lặp

- Dùng Figma MCP theo [contract cấp quyền](../../theme-style-guide/references/figma-access.md); lưu trạng thái kết nối/Accept và evidence, không lưu credential. Hết quota thì tự dùng CUA trên Chrome đang mở với profile `minhle@beae.com` đã xác minh theo contract; ghi nguồn UI và evidence. Lỗi quota/quyền không retry cho từng node. Đào sâu riêng section đang build, dùng evidence chung đã xác minh cho token/media lặp.
- Media theo dependency: reuse trước create, lưu ID sau mutation rồi readback; timeout chưa rõ kết quả thì tra ID/ledger trước retry. Video dùng reference video của store, không poster hoặc URL export tạm.
- Export bị chủ file tắt: hỏi một lần, ghi quyết định; không tải qua đường khác. Dựng phần Inspect độc lập, giữ draft bị tắt nếu thiếu media làm kết quả sai.
- Countdown có số mẫu: dùng mode duration nếu người dùng chọn; ghi duration thực tế theo control, không chuyển sang ngày hết hạn giả. Thiếu giá trị duration cần hỏi hoặc giữ default và ghi chưa xác nhận.
- Sau ngắt/reconnect: đọc plan, Git diff và resource pending trước làm tiếp; không tạo lại branch, reset template hay upload lại tài nguyên đã READY.

## Evidence cho Style Guide

Dùng [contract config chung](../../theme-style-guide/references/config-theme-settings.md). Lưu URL Style Guide, frame Eyebrow và một product card khi có xử lý style tương ứng; thiếu URL thì hỏi, không suy dữ liệu hay chốt scale global. Biến thể kế thừa không cần hỏi các nguồn này trừ khi người dùng yêu cầu đổi style.

Ghi raw px/%/em, số chuẩn hóa và số px runtime cho mọi consumer của scale. Với range/mapping hiện hữu, lưu file và trước/sau, grid/default/dữ liệu saved, consumer bị ảnh hưởng và kiểm chứng tương thích. Được căn chỉnh phần này, nhưng thêm select value/token phải có đề xuất và câu trả lời duyệt; không tạo setting mới. Font weight cần node nguồn Heading/Body/Eyebrow → font handle/biến thể picker → role token → computed weight của mọi consumer; thiếu font/variant/control thì ghi gap, không bù CSS. Body cần node Body/16 – Body text → raw tracking/size → primitive chung → `--font-body-letter-spacing` → px runtime của Body và Price kế thừa. Ghi declaration override tracking được sửa nếu có; xác minh font/size riêng của Price vẫn đúng, gồm scope PDP/cart chịu tác động. Tracking khác Figma thì ghi gap, không tự thêm control/scale riêng. Generated cần Heading HEX seed, cấp N, HEX output và field nhận màu. Button cần evidence desktop/mobile của height, padding, gap và underline/offset Tertiary. Thiếu preview thì giữ trạng thái configured-unverified thay vì khẳng định khớp Figma.

Compare-at custom theo mục 6.4.2 phải ghi fill/alpha/opacity, size compare-at/cha, ratio em, token/declaration/file/scope trước–sau và ảnh hưởng card/PDP/cart. Khi thiếu option, ba thuộc tính color/font-size/opacity hiện hữu được phép custom; không thêm setting/token/selector/breakpoint. Variant kế thừa bỏ qua trừ khi có yêu cầu đổi style.
