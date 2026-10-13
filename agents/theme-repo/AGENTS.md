# Hướng dẫn agent cho repo theme

Đây là mẫu dùng cho repo theme. Ghép những phần phù hợp vào AGENTS.md repo đích; không ghi đè quy tắc riêng, remote/store hoặc branch policy đang có.

## Chọn nhóm skill

- Build mới/sửa implementation: build-theme; kiểm tra foundation repo đích trước áp dụng.
- Build preset từ section/block có sẵn: build-preset.
- Cấu hình style guide/Theme Settings từ Figma: theme-style-guide.
- Setup store/cập nhật product, content và media: store-content-media.
- Update base và QA: thư mục chuẩn bị, chưa có skill. Dùng workflow và kiểm tra của repo đích đến khi có skill riêng.

## Quy tắc chung

Các yêu cầu build, rebuild, custom, fix, tối ưu hoặc cập nhật giao diện, **ngoại trừ build preset**, đều áp dụng [Ưu tiên option trước CSS custom](../../skills/build/new/build-theme/references/foundation.md#ưu-tiên-option-trước-css-custom). Khi ghép mẫu vào repo theme, trỏ link đến `.agents/skills/build-theme/references/foundation.md` hoặc vị trí skill thực tế. Đọc option trước, điều chỉnh range hợp lệ khi cần, rồi mới xử lý CSS custom cho phần không có option.

Preset/template chỉ chỉnh trong file repo. Content/media có thể tạo hoặc upload trên store trong phạm vi đã yêu cầu, rồi gắn URL/reference hoặc handle vào preset/template local. Không chỉnh/lưu preset trên store bằng Shopify bot/API hay Theme Editor nếu chưa được người dùng cho phép rõ ràng riêng cho thao tác đó; quyền build/upload/push không tự cấp quyền này. Chi tiết theo [ranh giới store content và preset local](../../skills/setup-store/store-content-media/SKILL.md#ranh-giới-store-content-và-preset-local); khi ghép mẫu, trỏ đến vị trí skill thực tế.

Giữ thay đổi người dùng, inspect diff trước sửa. Phân biệt implementation và cấu hình preset/template theo policy repo. Ghi customization khi sửa code đặc thù. Không suy ra store ghi dữ liệu từ theme tham khảo; xác minh domain và ID đích. Không ghi credential vào code hoặc receipt.

Theo branch/delivery policy repo đích. Chạy git diff --check và Shopify Theme Check cho code/schema/config trước delivery. Chỉ commit/push/publish trong phạm vi người dùng yêu cầu hoặc workflow đã cho phép. Không dùng force-push/reset hard để đồng bộ.

Không tự mở rộng quyền ghi store từ yêu cầu build local. Không suy QA hoàn thành từ Theme Check; báo đúng evidence đã kiểm tra.
