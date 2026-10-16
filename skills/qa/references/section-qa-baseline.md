# Checklist nền cho skill QA tương lai

Trích từ build-theme local. Đây là tài liệu tham khảo, chưa phải skill hoặc kết quả QA.

## Section QA and release gate

Before handoff, run a matrix across context, breakpoint, content state, and editor/runtime state:

- **Schema/placement:** valid JSON, owner/consumer mapping, preset, guard, defaults, `visible_if`, capacity, translations, and correct resource context.
- **Editor:** add, remove, duplicate, reorder, save, reload, section/block selection, setting changes, app block insertion/removal, and empty slots.
- **Storefront:** empty, missing, long, translated, and unavailable content; desktop/tablet/mobile; font zoom; overflow; and token/radius/motion variations.
- **Accessibility:** semantic landmarks, heading order, labels, contrast, keyboard/focus order, touch targets, and reduced motion.
- **Runtime:** no duplicate listeners, stale state, layout shift, or instance cross-talk after Theme Editor lifecycle events.

Release only when schema, editor behavior, storefront behavior, accessibility, responsive behavior, and runtime lifecycle all pass. Record any accepted exception with its owner and release impact before using the section as a catalogue reference.

## Theme Editor: thứ tự nhóm

Áp dụng cho QA mọi theme và variant: sidebar phải theo thứ tự **Header → Template → Footer → Overlay**.

- Kiểm tra `layout/theme.liquid`: render `header-group`, rồi `content_for_layout` trong main content, tiếp theo `footer-group`, cuối cùng `overlay-group`. Giữ tên nhóm và tên schema section tương ứng với base `main`, kể cả key dịch; không dùng tên như `Overlay group` nếu base là `Overlay`.
- Kiểm tra cả thời điểm Liquid thực thi trong Theme Editor, không chỉ vị trí HTML đầu ra. Không đọc/render `content_for_layout` trước Header trong design mode để lấy preload hoặc dò module. Nếu storefront cần đọc sớm, bảo vệ nhánh đó bằng điều kiện loại trừ `request.design_mode`, theo cách của base `main`. Không capture section group ở đầu layout chỉ để ép thứ tự sidebar.
- Mở Theme Editor, kiểm tra thứ tự và tên nhóm trên template đích sau save/reload và khi chuyển template; kiểm tra add/remove/reorder section vẫn thuộc đúng nhóm. Sửa thứ tự nhóm không được làm mất composition, resource, animation policy hoặc hành vi drawer/overlay hiện có.
- Gate fail khi nhóm sai thứ tự hoặc tên lệch base không có yêu cầu riêng. Evidence ghi template đã kiểm tra, thứ tự quan sát được và ảnh chụp nếu có. Schema validation/Theme Check và kiểm tra thứ tự trong source không thay thế xác minh sidebar; nếu chưa mở Theme Editor, ghi rõ chỉ xác minh local và runtime chưa kiểm tra.

## Add section: category theo base `main`

Áp dụng cho QA mọi theme variant, kể cả khi build hoặc đồng bộ preset từ template.

- Đối chiếu từng entry trong `sections/*.liquid` → schema `presets[]` với section/preset tương ứng trên base `main`; giữ nguyên `category`, kể cả key dịch `t:...`. Nếu preset gốc không có category, giữ trạng thái đó.
- Với section/preset riêng của theme không có preset tương ứng trên `main`, chọn category phù hợp về chức năng trong tập category đã có ở base `main`. Không tạo category mới theo tên theme hoặc tên thiết kế; không tự thêm biến thể chữ hoa/thường hay bản dịch khác của category base.
- Khi thay composition bằng dữ liệu template, bảo toàn metadata preset, đặc biệt `name` và `category`; không lấy việc template không chứa category làm lý do xóa category trong schema.
- Kiểm tra Add section trong đúng template/section group: preset xuất hiện ở nhóm mong đợi, tên nhóm dịch đúng, không có nhóm mới ngoài base. Phân nhóm bằng `presets[].category`, không đổi tên file, tên preset hay placement guard để ép thứ tự. Không khẳng định thứ tự hiển thị trong cùng nhóm nếu chưa kiểm tra Theme Editor.
- Evidence QA ghi ref/SHA của base `main`, file/preset/category đã đối chiếu và category được chọn cho section riêng. Gate fail khi category lệch base không có yêu cầu riêng, thiếu category vốn có trên base hoặc phát sinh category mới. Sau sửa, xác nhận chỉ category thay đổi nếu đó là phạm vi yêu cầu; giữ nguyên composition, resource và template, chạy schema validation và Theme Check. Nếu chưa mở Theme Editor, ghi rõ chỉ xác minh cấu hình local.
