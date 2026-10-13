# Ghi doc và cập nhật giữa các theme biến thể

## Hiểu yêu cầu

- “Ghi doc update cho biến thể” nghĩa là tạo hoặc cập nhật tài liệu chuyển thay đổi từ theme nguồn sang theme đích, chia theo phần có mã ổn định và trạng thái riêng. Chỉ ghi doc không tự cho phép sửa, push hoặc publish theme đích.
- “Update cho biến thể theo doc/mã” nghĩa là đọc tài liệu, xác định nguồn/đích và các mã được yêu cầu, kiểm tra trạng thái đã áp dụng, rồi thực hiện các mã còn thiếu trong phạm vi người dùng cho phép. Thiếu nguồn/đích hoặc phần cần cập nhật thì hỏi phần thiếu; vẫn chuẩn bị audit độc lập. Không đoán đích từ tên biến thể.

- Chỉ ghi và áp dụng những phần người dùng chọn chia sẻ giữa biến thể. Khi người dùng nói “chỉ note fix X/Y”, loại các feature, preset, media hoặc layout riêng của theme nguồn khỏi danh sách chuyển; sửa cả dependency và trạng thái liên quan. Fix độc lập phải được điều chỉnh theo DOM/token của theme đích, không kéo theo custom nguồn chỉ vì nằm cùng file. Giữ mã/trạng thái/bằng chứng của fix còn trong scope; không sửa code theme đích chỉ vì yêu cầu thu hẹp doc.

## Một nguồn theo dõi

Lưu doc trong repo theme nguồn tại `docs/variant-updates/<source>-to-<target>.md`, liên kết từ customization record nếu phần đó đổi implementation. Khi cập nhật theme đích, ghi cùng mã và link/đường dẫn nguồn trong record đích; không tạo mã khác cho cùng thay đổi. Giữ nội dung doc có sẵn.

Mỗi phần độc lập có mã `<SOURCE>-<TARGET>-<SURFACE>-NNN`; giữ mã khi sửa nội dung, thêm revision nếu thay đổi sau khi đích đã nhận. Không tái sử dụng mã cho việc khác. Ghi: ngày, source/target repo và branch, source revision/commit hoặc trạng thái chưa commit, phạm vi file/setting, lý do, hành vi và điều kiện option, dependencies, cách áp dụng, acceptance/QA, trạng thái đích và bằng chứng. Không ghi token hoặc signed upload URL.

Trạng thái mỗi mã: `pending` (chưa áp dụng), `applied` (đã sửa đích, chưa đủ QA), `verified` (đã áp dụng và kiểm tra), `skipped` (có lý do), `conflict` (cần giải quyết). Lưu lịch sử áp dụng theo ngày và commit/revision đích; upload preview và publish là trạng thái riêng. Không đánh dấu verified chỉ vì đã ghi doc, copy file hoặc push.

## Áp dụng an toàn

1. Audit mã và thay đổi thực tế trong cả hai repo; mã verified đúng revision thì không áp dụng lại. Trước mọi update, theme variant phải kiểm tra lại lỗi/gap ở chính theme đích với đúng option, viewport và điều kiện gây lỗi; chỉ áp dụng khi lỗi/gap còn tồn tại. Nếu đã hết hoặc upstream đã có fix/contract tương đương, ghi skipped kèm bằng chứng. Nếu chưa kiểm chứng được, giữ pending và nêu QA còn thiếu, không áp dụng mù.
2. So sánh contract/schema/snippet và diff nguồn/đích. Chuyển patch theo phần, không chép cả file làm mất custom riêng, setting merchant hoặc worktree đang sửa. Ghi conflict nếu contract không tương thích.
3. Phân biệt implementation với preset/content/media; thay đổi nội dung hay upload Files chỉ khi phạm vi người dùng bao gồm phần đó. Mã phụ thuộc chỉ được verified sau dependency.
4. Chạy kiểm tra đúng phần: schema/JSON, Theme Check, option gating, responsive, accessibility và editor/runtime chịu tác động. Ghi rõ phần chưa kiểm tra.
5. Cập nhật trạng thái và lịch sử từng mã trong doc nguồn/record đích; báo mã đã nhận, pending hoặc conflict. Không tự commit, push hoặc publish khi chưa được yêu cầu.
