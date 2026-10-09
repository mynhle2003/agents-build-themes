# Hướng dẫn bảo trì agents-build-themes

Repo này chứa skill và mẫu hướng dẫn agent, không chứa implementation theme.

- Tên thư mục, name trong SKILL.md và lời gọi $skill-name phải đồng bộ. Khi đổi tên, cập nhật toàn bộ reference và UI prompt.
- SKILL.md chứa phạm vi/routing/guard chính; reference chứa chi tiết theo tác vụ; agents/openai.yaml là metadata skill, không phải agent chạy riêng.
- Phân nhóm: skills/build/new, skills/build/preset, skills/update-base, skills/qa, skills/setup-store.
- Nhóm chưa có skill chỉ có README/tài liệu nền. Không thêm SKILL.md placeholder; chỉ tạo khi người dùng yêu cầu xây skill.
- Không đưa AGENTS.md cá nhân từ repo theme vào Git. agents/theme-repo/AGENTS.md là mẫu đã tách quy tắc chung; không ghi đè AGENTS.md repo sử dụng.
- Không import cache plugin hoặc skill hệ thống vào repo này. Không lưu credential, media thật, stock thật hoặc log đồng bộ base.
- Khi sửa workflow, giữ một nguồn quy tắc chính và cập nhật link/UI prompt; validate frontmatter, liên kết và script liên quan. Không commit test/kết quả test trừ khi được yêu cầu.
- Không tự commit/push chỉ vì yêu cầu tổ chức file local.
