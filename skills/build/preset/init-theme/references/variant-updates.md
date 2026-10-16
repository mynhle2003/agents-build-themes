# Hồ sơ cập nhật hai chiều giữa các theme biến thể

Mục tiêu: fix section/logic chung tìm thấy khi build B có thể chuyển lại A, và fix mới ở A có thể chuyển sang B; lần sau chỉ rà phần mới và hàng đợi chưa giải quyết. Đây là quy trình theo yêu cầu/phiên build đang chạy, không phải background automation hay quyền tự sửa mọi theme.

## Nơi lưu và quyền sở hữu

Mỗi theme giữ hồ sơ của chính nó tại `docs/variant-updates/<slug>.md`, link từ plan init và hồ sơ customization. Đọc hồ sơ ở **branch/worktree thật của theme đó**, không coi bản sao hồ sơ A kế thừa trong B là trạng thái mới nhất của A. Dùng `git show <ref>:<path>` để đọc nhánh khác khi cần, không switch/reset checkout của người dùng.

- Khi tạo B từ A tại SHA S: hồ sơ B ghi quan hệ A ↔ B, phạm vi section/dependency chung, các khác biệt giữ riêng và mốc A → B = S (đã kế thừa). Chiều B → A bắt đầu từ S vì A đã chứa phần chung đến S; phần thay đổi mới của B sau S chưa được áp dụng vào A.
- Đăng ký B trong hồ sơ A khi quyền tác vụ bao gồm sửa A. Nếu chưa có quyền, ghi `peer-registration-pending` trong B; không ngầm ghi sang A và không báo đăng ký hai bên đã xong. Khi bắt đầu công việc ở A, đối chiếu hồ sơ B và hoàn tất đăng ký nếu nằm trong phạm vi được phép.
- Không ghi marker `theme-base-sync-state` vào hồ sơ variant và không đổi marker base trong customization để đánh dấu cập nhật từ theme anh em. Cập nhật từ `main` và từ biến thể là hai lịch sử khác nhau.

## Nội dung hồ sơ của theme đích

Ghi tên/branch các peer, SHA fork và nguồn gốc; section/logic/dependency được chia sẻ, vùng giữ riêng (preset, media, typography hoặc custom cụ thể). Dùng SHA đầy đủ trong checkpoint, ngày chỉ để người đọc tham khảo.

### Checkpoint nhận theo từng nguồn

| Source branch | Fork SHA | Reviewed through SHA | Last applied source SHA | Target result commit | Pending IDs |
| --- | --- | --- | --- | --- | --- |

`Reviewed through` là đã phân loại hết range đó, **không có nghĩa đã áp dụng hết**. `Last applied` chỉ là mốc tiện tra; danh sách quyết định từng fix bên dưới mới xác định đã nhận gì. Mỗi chiều có checkpoint riêng, không dùng checkpoint A → B cho B → A.

### Quyết định và hàng đợi

| Fix ID / origin branch + SHA | Symptom and shared files | Direction | Decision | Target files / result | Validation | Next action |
| --- | --- | --- | --- | --- | --- | --- |

Decision: `pending`, `applied`, `already-present`, `keep-local`, `not-applicable`, `blocked`. Ghi lý do giữ riêng/bỏ qua và dependency hoặc hunk liên quan. Dùng một Fix ID ổn định cho lỗi, giữ origin ban đầu qua mọi lần chuyển; commit chứa nhiều fix phải tách quyết định theo fix. Nếu chưa commit, ghi `local-pending` cùng file/hành vi; không dùng HEAD làm SHA đại diện cho diff chưa commit.

## Khi build hoặc sửa lỗi một biến thể

1. Đọc phần quan hệ/checkpoint và hàng đợi của theme đang làm; đọc bổ sung hồ sơ peer liên quan. Kiểm tra HEAD và diff chưa commit thực tế. Nếu không có commit mới và không có pending liên quan, bỏ qua việc đọc lại toàn bộ lịch sử.
2. Rà `reviewed-through..source-head` cùng pending IDs cũ, ưu tiên file section/block, snippet, CSS/JS và schema dependency chung. Không chỉ lọc subject commit; lỗi logic chung có thể nằm cùng commit preset. Nếu checkpoint không còn tồn tại/không phải ancestor của nguồn hiện tại, dừng việc nhảy mốc và xác định lại ancestry/patch tương đương, không đánh dấu toàn range đã đọc.
3. Mỗi fix mới xác định: lỗi có xảy ra ở peer không, peer đã có patch tương đương chưa, section/dependency còn chung hay đã đổi cấu trúc. Ghi quyết định kể cả `keep-local`/`not-applicable` để lần sau không phải phân tích lại. Khi thay đổi kiến trúc liên quan, mở lại đúng quyết định bị ảnh hưởng thay vì bỏ qua vĩnh viễn hoặc rà lại tất cả.
4. Sửa lỗi mới ở B thì ghi candidate B → A với nguyên nhân, hành vi mong đợi, file/dependency và evidence tái hiện. Lần làm ở A đọc candidate này. Ngược lại A → B áp dụng đúng cùng quy trình; không ưu tiên cố định theme tạo trước.
5. Chỉ áp dụng trong theme được người dùng cho phép cập nhật. Với implementation, chuyển sang workflow build/update phù hợp; giới hạn preset-only của init vẫn giữ nguyên. Tích hợp có chọn lọc theo trạng thái đích, giữ design/preset/media riêng; không merge toàn branch hoặc chép nguyên file nguồn để lấy một fix. Chồng lấn custom/ý định chưa rõ thì ghi `blocked` và xin quyết định cụ thể theo quy tắc repo.
6. Validate sau tích hợp: schema/composition, hành vi lỗi ban đầu và dependency, Theme Check; cập nhật customization nếu implementation đổi. Chỉ đánh dấu `applied` sau khi phần sửa và kiểm tra liên quan thành công. Trước commit dùng `applied, uncommitted`; sau commit ghi SHA đích thật, không bịa SHA tự tham chiếu trong chính commit. Commit/push chỉ trong quyền đã có.
7. Nâng `reviewed-through` đến source HEAD đã chốt khi mọi fix trong range có quyết định, giữ hàng đợi `pending`/`blocked` để đọc tiếp lần sau. Bổ sung kết quả vào hồ sơ đích; cập nhật trạng thái gửi ở nguồn khi có quyền, hoặc để `ack-pending`. Không đẩy checkpoint chỉ vì đã chạy log/diff hay Theme Check.

## Tránh chuyển fix qua lại vô hạn

Trước chuyển fix, so origin ID, patch/hành vi và hồ sơ đích. Một fix A đã chuyển sang B rồi xuất hiện trong lịch sử B không trở thành fix mới cần gửi về A. Ghi `already-present` khi tương đương đã có. Bản sửa tiếp theo thay đổi hành vi có ID/revision mới, liên kết fix cũ để cả hai theme đánh giá phần delta. Chỉ khác preset/media/design riêng thì ghi giữ riêng, không coi là lỗi logic chung.

Kết thúc phiên ghi gọn: chiều đã rà, range SHA, fix đã nhận/gửi, target result, pending và checkpoint lần tới. Không tuyên bố hai theme đã đồng bộ chỉ vì cả hai cùng chứa một hồ sơ; phải kiểm chứng kết quả code/hành vi ở từng đích.
