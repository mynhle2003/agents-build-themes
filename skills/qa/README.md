# QA

[qa-section](qa-section/SKILL.md) kiểm tra section/preset đã build so với node Figma desktop/mobile và Style Guide: layout, typography, wrap, media/crop, màu và scheme. Trả bảng sai lệch có evidence, nguyên nhân và hướng sửa; không tự thay theme khi chỉ được yêu cầu QA.

Gọi `$qa-section` kèm section/template, preview và link Figma. Cài riêng bằng `python3 scripts/install.py /absolute/path/to/theme --group qa` từ root repo này. Khi đọc Figma, cần dependency `theme-style-guide` để dùng contract truy cập chung; không nhân bản contract vào nhóm QA.

[Checklist section đầy đủ](qa-section/references/section-qa-baseline.md) dùng khi yêu cầu thêm schema/placement, Theme Editor lifecycle, accessibility hoặc runtime; QA hình ảnh không tự đồng nghĩa đã vượt release gate. Checklist chưa phải kết quả QA.

Các skill build vẫn phải chạy kiểm tra phù hợp với thay đổi; không được coi QA chưa xây là lý do bỏ validation.

Khi QA Theme Editor, kiểm tra [thứ tự nhóm](qa-section/references/section-qa-baseline.md#theme-editor-thứ-tự-nhóm): **Header → Template → Footer → Overlay**, cùng tên nhóm/section theo base `main`.

Khi QA preset/Add section, kiểm tra [category theo base `main`](qa-section/references/section-qa-baseline.md#add-section-category-theo-base-main), kể cả section riêng của theme và preset vừa đồng bộ từ template. Chưa mở editor phải ghi chưa xác minh runtime.
