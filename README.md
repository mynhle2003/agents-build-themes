# Agents Build Themes

Bộ skill local tách từ theme-base để tái sử dụng và bảo trì riêng. Repo remote: https://github.com/mynhle2003/agents-build-themes.

```text
agents/
  theme-repo/AGENTS.md                Mẫu agent cho repo theme
skills/
  build/
    new/build-theme/                 Build implementation mới
    preset/
      build-preset/                  Build preset/composition có sẵn
      theme-style-guide/             Cấu hình Theme Settings từ Figma
  update-base/                       Bổ sung skill sau
  qa/                                Bổ sung skill sau
  setup-store/
    store-content-media/             Product, content, ảnh và video
scripts/
  install.py                         Cài skill, không ghi đè bản local
```

## Cài vào repo theme

Chạy từ checkout này:

```sh
python3 scripts/install.py /absolute/path/to/theme --group build --dry-run
python3 scripts/install.py /absolute/path/to/theme --group build
python3 scripts/install.py /absolute/path/to/theme --group setup-store
```

Bỏ --group để cài mọi skill đã hoàn thiện. Script copy từng skill vào `.agents/skills/<skill-name>` của repo đích; giữ thư mục reference/metadata. Nếu đích đã có skill giống hệt thì bỏ qua; nếu khác thì dừng trước khi copy, không ghi đè hoặc xóa. So sánh và sao lưu bản local trước khi quyết định thay thế. Update base và QA chỉ có folder/tài liệu nền, không được cài.

Cách đóng gói/cài đặt theo [tài liệu skill chính thức](https://developers.openai.com/codex/skills). Cấu trúc nhóm trong repo này dùng để bảo trì; script đưa từng skill về thư mục discovery phẳng. Nếu phiên hiện tại chưa thấy skill mới, mở phiên Codex mới tại repo đích.

## Agent và quy tắc repo

`agents/theme-repo/AGENTS.md` là mẫu chỉ dẫn, không phải subagent đã được cấu hình. Ghép vào repo đích khi cần. `agents/openai.yaml` bên trong từng skill là metadata UI của skill.

AGENTS.md cá nhân trong theme-base được giữ local; không sao chép nguyên bản, stage hoặc commit vào repo này. Remote, main/theme branch policy, log base và preview store vẫn thuộc theme-base. Không cài store mặc định vào mọi dự án.

## Bảo trì

Sửa skill trong đúng nhóm. Giữ tên và default_prompt tương ứng. Tách chi tiết vào references và link từ SKILL.md. Chỉ tạo skill mới cho update-base/qa khi workflow được xây sau. Kiểm tra frontmatter và link trước delivery.

Quy tắc catalog mới nhất lấy từ docs/content-creation-workflow.md local ngày 07/10/2026: ít nhất 4 ảnh/product, stock demo 20/variant còn hàng và blog riêng theo template. Quy tắc AVIF/video của skill cũ được giữ. Essen chỉ là profile minh họa, không phải default chung.

Bản skill cũ trong theme-base đã được dọn sau khi chuyển. AGENTS.md cá nhân vẫn giữ quy tắc repo và trỏ tới skill ở checkout này. Không duy trì hai bản skill riêng biệt; có thể dùng script cài vào repo khác khi cần discovery tự động.
