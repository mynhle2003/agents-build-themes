# Ví dụ đã đối chiếu: Essen


Nguồn: [Typography Essen](https://www.figma.com/design/v6iKvP4OuW3y0A9bbxel5U/Essen?node-id=43415-6890). Đây là ví dụ, không phải giá trị mặc định cho các theme khác. Luôn đọc lại Figma được yêu cầu và schema hiện tại.

| Role | Desktop | Tablet | Mobile | Line-height | Letter-spacing |
| --- | --- | --- | --- | --- | --- |
| H1 | 64px | 52px | 40px | 120% | -1.28px |
| H2 | 40px | 32px | 32px | 120% | -0.8px |
| H3 | 32px | 26px | 24px | 130% | -0.64px |
| H4 | 24px | 22px | 20px | 140% | -0.48px |
| H5 | 18px | 16px | 16px | 150% | 0 |

Bảng chỉ định weight 400 và style normal, không chỉ định font family heading. H6 không có trong bảng nên giữ nguyên.

Trong lần đối chiếu ban đầu, chỉ 7 giá trị cần đổi trong `current`: H2 tablet/mobile thành 32; H3 tablet thành 26 và mobile thành 24; H4 mobile thành 20; H5 tablet/mobile thành 16. H4 tablet bị bỏ qua vì thiếu setting. Line-height `normal` đã khớp H1–H5 trên desktop, nhưng code override H2 tablet thành 130%; không có option hiện tại khớp 120% cho mọi breakpoint nên giữ nguyên và báo giới hạn. Đây là kết quả lịch sử, không hạn chế workflow hiện tại: khi được yêu cầu ánh xạ option, áp dụng quy tắc sửa range/mapping trong SKILL.md và ghi hồ sơ custom.
