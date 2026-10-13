---
name: build-theme
description: "Build or change Shopify theme foundations, sections and reusable blocks using the target repository's token, ownership, schema and Theme Editor contracts. Use for implementation work, not preset-only configuration, store content or base synchronization."
---

# Build Theme

Dùng khi xây mới hoặc sửa implementation trong repo theme có foundation tương ứng. Đọc `AGENTS.md` và code repo đích trước; không áp đường dẫn máy, nhánh hoặc store của repo nguồn sang dự án khác. Nếu foundation khác các reference dưới đây, ưu tiên contract repo đích và ghi rõ phần cần điều chỉnh.

## Preflight


Do not start a section from markup. Before implementation, create a short Section Build Plan that records the decisions below. If placement or resource context is missing, stop at the plan and ask for the missing contract instead of guessing.

```text
role          -> content, main/resource, navigation, utility, or global surface
placement     -> JSON template, section group, static render, or other approved surface
context       -> resource/data source supplied by the template or parent
ownership     -> Theme Settings, section, block, Shopify context, or runtime
slots         -> allowed block types, capacity, default order, app policy, empty state
output        -> shell, stable classes/data attributes, accessibility responsibility
runtime       -> Liquid path, JS owner, editor lifecycle, loading/error states
responsive    -> parent layout modes, alignment/order/overflow rules, focus behavior
qa            -> schema, editor, storefront, accessibility, responsive, and runtime cases
```

Every decision must have one owner. A section must not invent a data context, copy a block contract, or add a setting that is already owned by Theme Settings.


## Đọc theo phần đang xây

- Theme Settings, token, shared CSS: [Foundation](references/foundation.md).
- Icon Figma và SVG trong snippet: [Quy tắc icon](references/foundation.md#icon-figma-và-svg).
- Ghi doc hoặc cập nhật giữa các theme biến thể: [Variant updates](references/variant-updates.md).
- Section, placement, schema, DOM và quyền sở hữu: [Section contract](references/section-contract.md).
- Kernel/compound block, alignment và JavaScript/editor lifecycle: [Blocks and runtime](references/blocks-and-runtime.md).

Reference chứa contract của base nguồn; kiểm tra consumer thực tế trước khi áp dụng. Không tự tạo registry, mở placement hoặc thêm setting ngoài brief. Cấu hình preset bằng implementation có sẵn thuộc skill `build-preset`.

## Kiểm tra trong lúc build

Giữ thay đổi có sẵn. Kiểm tra schema/JSON, `git diff --check`, Theme Check và các trạng thái responsive/editor chịu tác động. Ghi customization theo policy repo nếu thay Liquid/HTML/CSS/JS. Không checkout nhánh, commit, push, publish hoặc mở watcher ngoài phạm vi đã được yêu cầu.

Skill QA độc lập sẽ được xây sau. Báo đúng các bước đã kiểm tra và giới hạn còn lại; kiểm tra build không tự chứng minh đã qua toàn bộ QA.
