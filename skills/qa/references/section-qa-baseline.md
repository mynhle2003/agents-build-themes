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
