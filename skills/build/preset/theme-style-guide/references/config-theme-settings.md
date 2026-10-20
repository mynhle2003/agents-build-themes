# Hướng dẫn config Theme settings theo Figma

Nguồn quy tắc chung cho theme-style-guide, bước Style Guide của init-theme và phần Theme Settings của build-preset. Đọc mục 1–4 trước mutation; sau đó đọc mục đúng tác vụ. Các tên token là điểm tra cứu để xác nhận một lần ở repo đích, không phải quyền tự tạo hoặc hardcode mọi theme theo ví dụ.

## 1. Giới hạn bắt buộc

Các giới hạn sau có ưu tiên cao hơn mọi ví dụ, bảng mapping hoặc plan cũ trong sheet.

**Được thực hiện các thay đổi sau trong phạm vi config người dùng đã yêu cầu:**

1. Chỉnh **giá trị của setting đã tồn tại** trong `config/settings_data.json` của theme đích.
2. Chỉnh **giá trị của CSS token đã tồn tại**, đúng nơi khai báo và scope của token đó, khi cần để khớp Figma.
3. Hiệu chỉnh **min/max/step của range hiện có** để chứa giá trị Figma, giữ ID, kiểu, unit, ý nghĩa, default và mọi giá trị đã lưu chịu tác động còn hợp lệ.
4. Sửa **runtime mapping của setting hiện có** trong Liquid/CSS để lựa chọn đó điều khiển đúng token/output, gồm resolver hoặc binding trong consumer đã có. Không cần hỏi lại riêng cho range/runtime mapping trong phạm vi này.
5. Riêng **theme-style-guide và bước Style Guide của init-theme**, được custom ba thuộc tính hiện hữu của `.price__compare-at` khi chưa có option tương ứng: color, font-size và opacity theo mục 6.4.2. Đây là ngoại lệ đã được người dùng cho phép, không cần hỏi lại quyền cho đúng ba thuộc tính này.

Giá trị đã khớp thì **bỏ qua**, không ghi lại, không chuẩn hóa tên hoặc refactor cho đẹp.

**Không được tự ý:**

- Thêm option/setting mới ngoài bộ nâng cấp đã duyệt tại mục 1.2, kể cả khi Figma có thêm thuộc tính.
- Sửa schema ngoài range được phép ở trên và bộ nâng cấp tại mục 1.2; đổi locale/nhãn UI, kiểu setting, thêm/xóa/gộp setting hoặc đổi ID.
- Thêm value vào select, thêm token, alias, namespace hoặc hệ biến riêng theo nhóm khi chưa được duyệt.
- Viết implementation/layout mới, sửa markup/class, thêm selector hoặc đổi breakpoint, cấu trúc section/block/template hay JavaScript. Runtime mapping được phép chỉ nối đúng setting hiện có vào output; không tạo feature/variant/scope mới.
- Tạo file CSS mới, chèn CSS vào `custom_css`, thêm inline style/local override hoặc dùng `!important` để né giới hạn.
- Tải family font mới hoặc đổi hệ thống nạp font ngoài việc nạp variant Button/Badge từ family đã chọn theo mục 1.2. Nếu font/weight không có trong thư viện font đang hỗ trợ, báo thiếu khả năng.
- Đặt key chưa được schema hỗ trợ vào `settings_data.json` và coi đó là config hợp lệ.
- Copy toàn bộ preset mẫu, reset các scheme, cập nhật mọi preset hoặc push/publish/Save theme trên store khi chưa được yêu cầu.

**Ngoại lệ phải hỏi trước:** Nếu tập value/token hiện tại không biểu diễn đủ Figma, báo rõ phần thiếu và đề xuất **thêm value cho setting hiện có + CSS token tương ứng**. Chỉ làm sau khi người dùng đồng ý đúng phạm vi đó. Không thêm một option/setting mới để giải quyết việc thiếu value.

Nếu việc thêm value cần chạm schema/locale/resolver, phải liệt kê chính xác các file và thay đổi đó trong câu hỏi xin duyệt. Đồng ý thêm một value không có nghĩa là được refactor foundation hoặc mở thêm setting.

### 1.1. Range/runtime mapping: làm đúng, không phải thêm option

- Range cần `min < max`, `step > 0`, `(max - min) / step` nguyên và không quá 100, tức tối đa 101 giá trị gồm hai đầu. Các số Figma, default và giá trị đã lưu chịu tác động phải nằm đúng grid. Không chỉ nới max rồi để step sai hoặc làm tròn thiết kế.
- Chỉ thay các biên/step cần thiết; nếu không có grid hợp lệ bảo toàn các giá trị cần giữ, báo xung đột để người dùng quyết định. Không đổi unit hoặc kiểu setting để lách giới hạn.
- Sửa resolver/binding khi data đúng nhưng runtime whitelist/clamp, alias hoặc override hiện hữu làm output sai. Trace setting → enum/range → token → consumer và xác minh cả desktop/mobile; giữ ngữ nghĩa setting.
- Không đổi số của enum legacy âm thầm: snapshot output theo role/breakpoint, bảo toàn numeric output ngoài phạm vi; nếu phải chuyển dữ liệu đích, chỉ chuyển các key chịu tác động và ghi rõ lý do. Không reset saved presets.
- **Thêm số hợp lệ vào domain range bằng min/max/step đã được cho phép; thêm mục vào select hoặc tạo token/alias mới vẫn phải hỏi.** Có quyền sửa mapping không có nghĩa là được tự thêm value/setting.
- Lưu audit gọn gồm ID, range/mapping trước/sau, nguồn Figma, file/token/consumer, default/dữ liệu cũ được giữ và kết quả output. Ghi hồ sơ theo quy tắc repo đích nếu thay mapping cần được bảo toàn khi update base.

### 1.2. Bộ nâng cấp Typography đã được duyệt

Người dùng đã cho phép triển khai và dùng các control sau khi config theme. Đây là ngoại lệ hẹp cho quy tắc không thêm setting; không phải quyền mở rộng schema tùy ý. Repo đã có thì config, không tạo control trùng.

- **Heading tracking riêng từng cấp:** `type_heading_1_letter_spacing` … `type_heading_6_letter_spacing`, nằm trong từng nhóm Display / Extra large / Large / Medium / Small / Extra small. Cả sáu chọn cùng 11 enum/token `--letter-spacing-*`; không tạo sáu scale hoặc hardcode theo class. Thay control chung `type_letter_spacing`: migrate giá trị cũ sang các cấp chưa có giá trị, rồi xóa key/schema cũ. Được migrate đúng các key liên quan trong current và saved presets để không để dữ liệu mồ côi; giữ nguyên phần khác. Với current đích, cấu hình mỗi cấp theo Figma. Alias `--font-heading-{display,xl,lg,md,sm,xs}-letter-spacing` nhận control tương ứng; alias generic `--font-heading-letter-spacing` và Custom kế thừa Medium, không giữ một control chung cạnh tranh.
- **Weight riêng Button/Badge:** `button_font_weight`, `badge_font_weight`, kiểu select `body` và chuỗi `300` … `700` bước100; default `body`, nhãn UI **Default**. Bỏ lựa chọn `inherit` / Default (font picker weight) cũ; migrate giá trị đã lưu `inherit` sang `body`. `body` lấy weight từ Body picker (`--font-body-weight`), vẫn giữ family/style của role Button/Badge và nạp variant cùng family theo weight đó; variant không hỗ trợ thì fallback và ghi gap. Không hiển thị helper text về fallback dưới hai control. Giữ family/style từ role đã chọn; không đổi Body/Accent để bù weight. Ánh xạ vào `--button-font-weight` / `--badge-font-weight`. Các loại Primary/Secondary/Tertiary vẫn dùng chung Button weight; Badge độc lập. Current đọc weight thực tế từ component Figma, preset cũ thêm `body` nếu chưa có.
- Được sửa schema/locale/resolver và loader hiện hữu đúng bộ control này. Resolve weight bằng `font_modify` trên font object của role đã chọn, nạp variant thực bằng `font_face` trong loader chung, loại trùng khi Button và Badge cùng family/style/weight. Theo [Shopify font_modify](https://shopify.dev/docs/api/liquid/filters/font_modify), variant không tồn tại trả nil; phải fallback về font picker role và ghi gap; không báo đã khớp, không yêu cầu browser giả lập weight. Không tải family mới hoặc thêm font picker/role mới.
- **Heading tablet không phải tiêu chí config/QA:** dùng cơ chế responsive desktop/mobile đã có; không thêm tablet control/breakpoint, không hỏi hoặc chặn vì các cỡ Heading tablet chưa khớp.
- Ghi migration schema/data/runtime và kiểm tra từng cấp độc lập, weight riêng, reset `body` (Default), variant thiếu và font-face trùng. Đây là nâng cấp reusable cần ghi trong tài liệu rebuild base của repo đích; không đưa giá trị Figma của một theme thành default mọi theme.

## 2. Đầu vào và nguồn Figma

Áp dụng [Figma MCP và cấp quyền tài khoản](figma-access.md) trước khi đọc nguồn; chờ Accept nếu thiếu quyền tài khoản; hết quota thì tự dùng CUA trên Chrome/tài khoản đã xác minh theo contract.

| Phần cần config | Nguồn bắt buộc |
| --- | --- |
| Heading, Text, Button, Badges | Style Guide do người dùng chỉ định |
| Eyebrow | URL frame chứa Eyebrow do người dùng cung cấp |
| Product card title và Product card price | URL chứa ít nhất một product card do người dùng cung cấp; cùng một card có thể đủ cho cả hai |
| Colors | URL frame bảng màu Figma, có nhãn màu/HEX hoặc tham chiếu Generated |
| Theme đích | Repo/theme, phạm vi config và preset/scheme đích nếu cần |

Thiếu URL Eyebrow thì hỏi: “Bạn gửi link Figma của frame chứa Eyebrow cần lấy Typography nhé.” Thiếu URL card thì hỏi: “Bạn gửi link Figma chứa một product card để mình đọc Typography của tên sản phẩm và giá nhé.” Câu trả lời chỉ ghi “frame chứa Eyebrow” chưa phải URL.

Không tự chọn tab Figma đang mở, dùng file của theme khác hoặc lấy Heading Style Guide thay cho title card. Nếu node không đọc được, báo thiếu quyền/giới hạn công cụ; không giả vờ đã đọc.

Trong khi thiếu nguồn, tiếp tục các phần độc lập đã có dữ liệu. **Chưa chốt hoặc ghi đè scale spacing chung** khi còn thiếu dữ liệu của một consumer bị ảnh hưởng.

## 3. Quy trình ngắn, tránh dò repo lặp lại

1. Dùng bảng token/setting dưới đây làm điểm bắt đầu, tìm chính xác tên trong repo đích.
2. Đọc hẹp schema/resolver/consumer liên quan để xác nhận token, enum, đơn vị và scope. Chỉ sửa range/mapping thật sự cần theo mục 1.1, không coi việc đọc file là quyền sửa toàn file.
3. Lưu một bảng mapping cho lượt config: setting ID, token, file khai báo, scope/breakpoint, giá trị hiện tại và consumer. Dùng lại bảng này cho những bước sau.
4. Đọc Figma, so với **giá trị cuối cùng đang render**, không chỉ so tên enum. Ví dụ Normal cũ của Body có thể là 1.5 trong khi Normal của scale mới là 1.3.
5. Khớp thì bỏ qua. Chưa khớp: ưu tiên chọn value đang có trong `settings_data.json`; chỉ custom trị số token hiện hữu nếu các lựa chọn chưa khớp và thay đổi không làm sai consumer dùng chung.
6. Range chưa phủ hoặc binding hiện hữu sai thì hiệu chỉnh theo mục 1.1. Thiếu token/setting, select value hoặc cần thêm scope/selector/feature mới thì báo và hỏi đúng phần mở rộng; tiếp tục phần độc lập.

Các vị trí đã xác minh trong Mara ngày 20/10/2026:

| File đọc ban đầu | Nội dung cần tra |
| --- | --- |
| `config/settings_data.json` | Dữ liệu config theme đích |
| `config/settings_schema.json` | ID/kiểu/enum; được hiệu chỉnh min/max/step của range hiện có theo mục 1.1 |
| `snippets/css-variables-typography.liquid` | Size, line height, tracking/case Heading và Eyebrow |
| `snippets/css-variables-controls.liquid` | Token Button |
| `snippets/css-variables-commerce.liquid` | Token Product card title, badge/commerce resolver |
| `snippets/css-variables.liquid` | Font role, Body, badge, price và scheme colors |
| `assets/critical.css`, `assets/product-information.css` | Consumer/override/scope; chỉ chỉnh binding hiện hữu khi cần sửa mapping, không thêm style/scope mới |

Path là điểm tra cứu, không phải quyền sửa toàn file. Nếu token được emit từ biến Liquid, được chỉnh literal hoặc nhánh resolver/binding hiện hữu để setting tạo output đúng theo mục 1.1. Không đổi nghĩa enum cũ âm thầm, thêm nhánh cho select value chưa được duyệt hoặc dùng mapping để tạo một setting mới trá hình.

**Cảnh báo hiện trạng:** Repo được đọc vẫn có mapping riêng theo cấp và các giá trị hardcode; chưa xác nhận đã có đủ primitive `--letter-spacing-*` và `--line-height-*` của plan. Không tự tạo các token chưa có. Khi dùng repo khác hoặc sau update, xác nhận lại tên một lần rồi tái dùng mapping.

## 4. Ghi `config/settings_data.json` đúng phạm vi

- Dùng đúng tên file `config/settings_data.json`, không phải file mới `config/settings_data` không có đuôi.
- Nếu `current` là object, chỉnh các setting hiện có thuộc `current`. Nếu `current` trỏ tới preset, resolve preset đang dùng trước; không tự đổi cấu trúc `current`.
- Chỉ chỉnh preset được yêu cầu. Không đồng bộ mọi entry trong `presets` theo theme đang config.
- Màu scheme nằm tại `current.color_schemes[scheme_id].settings` hoặc cấu trúc preset thực tế tương ứng. Giữ scheme ID, section assignment và default scheme.
- Dùng đúng kiểu dữ liệu: range là số, enum là string hợp lệ, font picker là handle thực tế được hỗ trợ, màu giữ định dạng/alpha schema chấp nhận.
- Không đoán font handle từ tên font. Không sửa giá trị schema default để thay cho config theme đích.
- Chỉnh token không được làm các preset/consumer ngoài phạm vi đổi ngoài ý định. Nếu không bảo toàn được chúng với thay đổi cho phép, báo xung đột và chờ quyết định.

## 5. Dữ liệu cần đọc cho mỗi text

Lưu URL/node/style, vai trò, font family/style/weight, size px, line height cùng đơn vị, letter spacing cùng đơn vị, text case, breakpoint và trạng thái **đọc trực tiếp / suy luận / thiếu dữ liệu**.

Không lấy chiều cao text box làm line height. Paragraph spacing khác line height và letter spacing. Phân biệt thuộc tính transform với nội dung vốn đã viết hoa. Gặp mixed font/size thì đọc theo text run, không ép thành một giá trị giả.

## 6. Typography: setting và token cần config

Ba font role dùng chung là Heading, Body, Accent. Không tạo font role mới theo mỗi nhóm.

| Nhóm | Setting ID hiện hữu để tra trước | Token đích cần xác nhận trong repo |
| --- | --- | --- |
| Heading font | `type_heading_font` | `--font-heading-family`, `--font-heading-style`, `--font-heading-weight` |
| Body font | `type_primary_font` | `--font-body-family`, `--font-body-style`, `--font-body-weight` |
| Accent font | `type_accent_font` | `--font-accent-family`, `--font-accent-style`, `--font-accent-weight` |
| Paragraph | `type_body_size`, `type_body_leading` | `--font-body-size` hoặc `--font-body-md` theo repo, `--font-body-line-height`, `--font-body-letter-spacing` |
| Heading từng cấp | `type_heading_1…6_size_desktop`, `_size_mobile`, `_line_height`, `_case`, `_letter_spacing`; không cần tablet | `--font-heading-{display,xl,lg,md,sm,xs}` và các hậu tố `-line-height`, `-letter-spacing`, `-text-transform` |
| Heading tracking từng cấp | `type_heading_1…6_letter_spacing` | `--font-heading-{display,xl,lg,md,sm,xs}-letter-spacing`; generic kế thừa Medium |
| Eyebrow | `type_eyebrow_size`, `type_eyebrow_line_height`, `type_eyebrow_letter_spacing`, `type_eyebrow_case`; font role nếu bản update đã có | `--font-eyebrow-size`, `--font-eyebrow-line-height`, `--font-eyebrow-letter-spacing`, `--font-eyebrow-text-transform`, weight/font role đang bind |
| Button | `button_font_size`, `button_font_size_mobile`, `button_letter_spacing`, `button_font_weight`, font/case setting hiện hữu | `--button-font-family`, `--button-font-style`, `--button-font-weight`, `--button-font-size`, `--button-font-size-mobile`, `--button-letter-spacing`, `--button-text-case` hoặc tên case thực tế |
| Button height/padding | `button_height_desktop`, `button_height_mobile`, `button_padding_inline_desktop`, `button_padding_inline_mobile` | `--button-height`, `--button-height-mobile`, `--button-padding-inline-desktop`, `--button-padding-inline-mobile` |
| Tertiary underline | `button_tertiary_show_underline`, `button_tertiary_underline_offset` | `--button-tertiary-underline-display`, `--button-tertiary-underline-offset`, `--button-tertiary-underline-space`; decoration token nếu consumer thực tế dùng |
| Badges | `badge_font_weight` và ID Typography Badge thực tế theo mục 1.2 | `--badge-font-family`, `--badge-font-size`, `--badge-font-weight`, `--badge-letter-spacing`; style/case chỉ khi token đã tồn tại |
| Product card title | `product_card_title_font`, `product_card_title_size_desktop`, `product_card_title_size_mobile`; LH/spacing/case nếu đã có | `--product-card-title-font-family`, `--product-card-title-size`, `--product-card-title-size-mobile`; `--product-card-title-line-height`, `--product-card-title-letter-spacing`, `--product-card-title-text-transform` chỉ nếu đã tồn tại |
| Product card price | Chỉ dùng các setting card price thực tế đã có | `--price-font-family`, `--price-font-style`, `--price-font-weight`, `--price-font-size`, `--price-line-height` trong scope card hiện hữu |

Các hậu tố/ID trong bảng là mẫu tra cứu, không phải yêu cầu tạo đầy đủ key còn thiếu. Không tạo bộ `--pcard-title-*` hoặc `--pcard-price-*` song song. Giữ các alias role hiện có; một alias không phải một scale mới.

### 6.0. Font family/style/weight theo role

| Font role | Nguồn Figma của family/style/weight | Output hiện hữu cần xác nhận |
| --- | --- | --- |
| Heading | Các Heading trong Style Guide | `--font-heading-family`, `--font-heading-style`, `--font-heading-weight` |
| Body | Body/16 – Body text trong Style Guide | `--font-body-family`, `--font-body-style`, `--font-body-weight` |
| Accent | Frame Eyebrow người dùng chỉ định | `--font-accent-family`, `--font-accent-style`, `--font-accent-weight` |

- Chọn đúng **family + biến thể weight/style trong font picker** và lưu font handle hợp lệ vào setting role hiện hữu. Weight không chỉ là tên family: Regular, Medium, Semibold… phải đối chiếu trị số thực tế của font Figma và danh mục Shopify; không suy số chỉ từ nhãn. Font picker quyết định weight của role. Riêng Button/Badge dùng control weight độc lập đã duyệt ở mục 1.2; không hardcode `font-weight` trên consumer.
- Theme mẫu đã quan sát ngày 20/10/2026: Body picker là Instrument Sans Regular, `--font-body-weight: 400`; Accent là Instrument Sans Medium, `--font-accent-weight: 500`; Heading là Instrument Serif, `--font-heading-weight: 400`. Đây là bằng chứng về cơ chế role, **không phải default phải chép** cho theme khác. Ở mẫu, URL picker Body xác nhận ID `type_body_font`; ở repo đích có thể là `type_primary_font`. Giữ ID thật sau trace, không đổi tên hoặc tạo key theo mẫu.
- Thiếu URL Eyebrow thì hỏi trước khi quyết định Accent family/style/weight. Không lấy weight Button hoặc Body làm bằng chứng Eyebrow; Heading lấy nguồn Heading của chính nó. Chỉ đổi role khi có bằng chứng Figma tương ứng.
- Audit Button, Badge, card title/price và các consumer đang chọn role đó: chúng phải nhận family/style/weight từ cùng role, trừ control weight riêng đã có và có bằng chứng. Nếu nhiều Heading hoặc consumer dùng cùng role nhưng Figma khác weight, dùng control/variant hiện hữu nếu hỗ trợ; không đổi weight global để khớp một phần tử rồi làm sai phần còn lại. Thiếu khả năng thì báo gap, không tạo font role/setting hoặc CSS override riêng.
- Đọc font được nạp cùng runtime binding và computed weight; token đúng nhưng font face/biến thể không có vẫn chưa đạt. Chỉ nạp thêm variant cùng family cho Button/Badge qua loader hiện hữu theo mục 1.2. Thiếu font/weight được hỗ trợ thì báo rõ. Ghi node nguồn → handle → role token → consumer → weight runtime trong manifest; không tuyên bố khớp chỉ từ tên picker.

### 6.1. Heading

| Figma | Nhãn UI giữ nguyên | Token size |
| --- | --- | --- |
| Heading 1 | Display | `--font-heading-display` |
| Heading 2 | Extra large | `--font-heading-xl` |
| Heading 3 | Large | `--font-heading-lg` |
| Heading 4 | Medium | `--font-heading-md` |
| Heading 5 | Small | `--font-heading-sm` |
| Heading 6 | Extra small | `--font-heading-xs` |

- Giữ nhãn UI và semantic HTML tag. Không sửa block/template để đổi visual size.
- Có H6 thì đọc trực tiếp. Không có H6: suy size Extra small bằng H5 trừ khoảng 2px, thử trừ 2px trước; giữ family/style/weight, tracking, case và tỷ lệ line height của H5. Đánh dấu suy luận.
- Nếu H5 có desktop/mobile, suy riêng từng cỡ. Size mới ngoài range thì hiệu chỉnh min/max/step theo mục 1.1, không clamp; không có grid hợp lệ thì báo xung đột.
- Cấu hình tracking riêng từng cấp bằng `type_heading_1…6_letter_spacing` theo mục 1.2, kể cả khi hai cấp hiện có cùng số. Không ép các cấp qua một lựa chọn global. Không cần đọc/đối chiếu Heading tablet; giữ responsive desktop/mobile hiện hữu.

### 6.2. Text và Eyebrow

- Text: đọc **font, base size, line height và letter spacing từ Body/16 – Body text** trong Style Guide; tên “16” không thay cho số đo thực tế. Body dùng font role Body. Giữ cỡ phụ nếu Figma không yêu cầu thay.
- Gắn tracking của style Body này vào alias hiện hữu **`--font-body-letter-spacing`** qua primitive `--letter-spacing-*` khớp trong scale chung ở mục 8. Thu thập Body cùng các role khác trước khi căn chỉnh scale; không đặt một số riêng cho Price hoặc ghi đè Normal khác 0 để đáp ứng Body. Chỉ custom trị số primitive cần thiết; sửa binding hiện hữu theo mục 1.1 nếu alias chưa resolve đúng. Thiếu value/token thì theo mục 9.
- Size nền của theme mẫu có thể là `--font-body-size`, repo đích có thể dùng `--font-body-md` hoặc alias tương đương. Trace khai báo và consumer một lần, giữ tên thật; không tạo token mới hoặc đổi tên để giống mẫu. Font/size/line height/tracking là các thuộc tính độc lập.
- Audit các phần tử kế thừa `letter-spacing: var(--font-body-letter-spacing, 0)`, gồm body copy và Price. Thay Body tracking tác động mọi consumer kế thừa, kể cả giá PDP/cart nếu chúng dùng Body; đây không phải quyền đổi font/size riêng của các scope đó. Phân biệt property `letter-spacing` kế thừa computed value từ cha với việc consumer tự khai báo `letter-spacing: var(--font-body-letter-spacing, 0)`; chỉ trường hợp sau mới tính em theo size của consumer. Kiểm tra computed style của cả cha và price node.
- Eyebrow: đọc đúng frame được gửi; lấy family/style/weight, size, tracking, case và line height. Đối chiếu font role Accent. Nếu setting chọn Accent đã có nhưng CSS vẫn bind Body, được sửa mapping hiện hữu theo mục 1.1. Nếu chưa có lựa chọn/font control cần dùng, hỏi phần value thiếu; không tự tạo setting hoặc đổi nghĩa Body.
- Không suy Eyebrow chỉ từ chữ uppercase. Thiếu link thì giữ cấu hình hiện tại, không lấy font của button/badge thay thế.

### 6.3. Button và Badges

- Đọc Font, Font size, Letter spacing, Text case từ component/style đúng nhóm trong **Style Guide**; đọc weight/style và line height. Gán weight thực tế vào `button_font_weight` hoặc `badge_font_weight` theo mục 1.2; family/style vẫn theo role. Xác minh variant được nạp, không chỉ kiểm tra CSS có số500.
- Button: đọc Primary/Secondary/Tertiary nếu có; giữ ba loại style. Chọn font role khớp trong các enum đã hỗ trợ. Không tự gộp hoặc tách setting theo variant.
- Badge: phân biệt Sale/Sold out/New, đọc label thay vì khung màu. Không đổi badge color khi chỉ config Typography.
- Letter spacing của cả hai nhóm chọn từ cùng scale chung. Nếu select chưa có lựa chọn cần dùng, hỏi trước khi thêm value; không thêm option mới. Range cần mở rộng thì xử lý theo mục 1.1.
- Giữ `--badge-letter-spacing`; không đổi sang lỗi chính tả `--badge-letting-spacing` của theme mẫu.

### 6.4. Product card title và Product card price

- Hỏi URL Figma chứa một card; dùng cùng card để đọc title và price. Không lấy title section hoặc giá PDP làm dữ liệu thay thế.
- Title: đọc family/style/weight, size, line height, tracking và case. Giới hạn số dòng/ellipsis thuộc layout Product cards ở mục 6.7, chỉ config khi có bằng chứng và control hiện hữu.
- Price: đọc font và size, phân biệt giá thường/sale/compare-at/unit price; đọc thêm LH/tracking/case để kiểm tra kế thừa nhưng chỉ config các setting/token đã hỗ trợ. **Tracking mặc định kế thừa Body từ `--font-body-letter-spacing`**, còn font role/size riêng vẫn theo setting Price hiện hữu. Nguồn gán Body tracking là Body/16 – Body text, không suy từ giá trên card.
- Trace cascade đến từng price node: khai báo cứng như `.price--product-card { letter-spacing: 0.1px; }` chặn kế thừa. Trong phạm vi sửa binding hiện hữu ở mục 1.1, gỡ literal/override tracking sai để khôi phục kế thừa Body; chỉ sửa declaration liên quan, không thay color/gap hay thêm selector/CSS bù. Nếu đã có control tracking riêng có chủ đích, xác minh contract và nguồn Figma trước khi giữ local override; không âm thầm xóa control hoặc đổi nghĩa nó.
- Nếu tracking Price trong Figma khác kết quả kế thừa Body, ghi chênh lệch và gap cần quyết định. Không đổi Body theo Price, tạo scale/setting tracking riêng hay dùng gap/`--compare-at-price-spacing` để giả letter spacing. CSS variable xuất hiện không chứng minh có option UI tương ứng.
- Giữ bộ `--product-card-title-*` và `--price-*` đang có. Không tự thêm token spacing/case cho price nếu chưa tồn tại.
- Price token phải đã có scope card phù hợp. Được sửa binding hiện hữu của option card theo mục 1.1 nếu output sai, giữ các scope PDP/cart. Nếu cần tạo scope/selector hoặc setting mới để tách giá, báo xung đột; không dùng CSS riêng của theme để bù control thiếu.

Mapping Virelle đã cập nhật ngày 20/10/2026: size nền `--font-body-size` (`--font-body-md` alias); title dùng `--product-card-title-font-size` cho mọi viewport, không còn `--product-card-title-size`/`--product-card-title-size-mobile`. Price settings emit `--product-card-price-font-family/style/weight/size`; critical CSS map chúng vào `--price-font-*` tại `.price--product-card`. Không tìm hoặc tạo `--price-letter-spacing`: tracking kế thừa Body. Single/Compact/Shop the look/Video popup và card badge phải nhận control chung, không khôi phục literal cũ. Đây là mapping repo đã xác minh sau một task refactor được cho phép riêng, không phải quyền mặc định đổi tên/thêm token cho theme khác.

### 6.4.1. Khoảng cách giá bán – compare-at price

- Đọc **horizontal gap giữa giá bán và giá gạch** trên cùng card Figma được chỉ định; đọc riêng desktop/mobile và trạng thái sale. Ưu tiên Auto Layout gap; với spacing variable đã xác nhận theo Tailwind mặc định, quy đổi `n × 4px`: `1`=4px, `2`=8px, `1.5`=6px. Giữ tên token và số px resolved trong audit; không coi `1` là1px. Scale custom/mode khác cần đọc resolved value, không áp công thức mù quáng. Nếu không có Auto Layout thì đo từ cạnh bounding box hai text node và ghi rõ suy luận. Không lấy letter spacing, gap title–price, padding card hoặc khoảng cách unit price làm số này. Không có compare-at price/không đủ nguồn thì hỏi frame phù hợp; chưa đo được không tự lấy 6px làm bằng chứng Figma.
- Gắn độ dài px đo được vào **`--compare-at-price-spacing`** tại nơi khai báo token hiện hữu. Consumer dùng `column-gap: var(--compare-at-price-spacing, 6px)` theo cơ chế theme mẫu. Fallback chỉ để component hoạt động nếu thiếu biến, không phải giá trị Figma. Khớp thì bỏ qua; không viết `gap: 6px` riêng trên từng card, không thêm Theme Settings option chỉ để điều khiển gap.
- Token dùng chung nên phải audit các Price consumer card/PDP/cart; không đổi token global theo một card khi các nguồn còn mâu thuẫn. Ưu tiên scope/breakpoint binding hiện hữu nếu đã hỗ trợ. Nếu desktop/mobile hoặc context cần số khác nhau mà chưa biểu diễn được, ghi gap và đề xuất phần value/token/binding cần duyệt; không tự thêm token responsive, selector hay breakpoint.
- Lưu node/breakpoint, khoảng cách đo được, token/file/scope trước–sau và column-gap runtime. Kiểm tra sale-first/compare-first, một giá không có compare-at, wrap và unit-price xuống dòng; giữ row-gap theo contract component. CSS token này không chứng minh có option UI.
- Virelle ngày 20/10/2026 khai báo token này ở root của `snippets/css-variables.liquid`, `.price` tiêu thụ trong `assets/critical.css`; sau xác nhận của người dùng, card mới dùng Tailwind spacing `1` = **4px**, thay trị số6px từ nguồn cũ. Không áp4px làm default cho theme khác. Được hiệu chỉnh trị số hiện hữu khi config Figma; token thiếu ở repo khác vẫn phải hỏi trước khi thêm theo mục 9.

### 6.4.2. Ngoại lệ compare-at: color, font-size, opacity

Áp dụng khi chạy **theme-style-guide** hoặc bước Style Guide của **init-theme** theo Figma. Nếu đã có option đúng thuộc tính thì dùng option trước. Khi chưa có option, được chỉnh đúng ba thuộc tính hiện hữu của `.price__compare-at` trong stylesheet dùng chung và/hoặc khai báo token màu hiện hữu; không cần hỏi lại quyền custom này. Quy tắc không viết CSS Price riêng ở các mục khác có ngoại lệ hẹp này, không mở quyền custom các thuộc tính/consumer khác.

| Thuộc tính | Cách đọc Figma và cấu hình |
| --- | --- |
| `color: var(--price-compare-color)` | Đọc fill HEX/RGBA và opacity riêng của compare-at text. Ưu tiên giữ binding token này, chỉnh giá trị/alias ở đúng scheme/scope hiện hữu nếu chưa khớp. Trace cascade vì scheme có thể ghi đè token root. Không đổi Body color hoặc Sale price color để bù màu compare-at. |
| `font-size: 0.9em` | Đọc size px compare-at và size thực của phần tử cha tại điểm áp dụng em; tính `ratio = compare_at_px / parent_font_size_px`. Cha thường dùng size Price nhưng phải xác nhận DOM/computed style. Gắn ratio vào declaration font-size hiện hữu; không mặc định 0.9 cho mọi Figma. Kiểm tra desktop/mobile và tính ngược px. |
| `opacity: 0.72` | Đọc opacity của layer/text và alpha fill; đối chiếu hiệu ứng opacity cha nếu có. Gắn opacity 0–1 phù hợp vào declaration hiện hữu. Không nhân alpha/opacity hai lần hoặc coi màu đã được làm nhạt là bằng chứng layer opacity cũng giảm. |

Các số 0.9em và 0.72 là trạng thái CSS được nêu trong yêu cầu, không phải giá trị bắt buộc của thiết kế. Đã khớp thì bỏ qua. Không có compare-at ở frame hoặc không đọc được fill/size/opacity thì hỏi nguồn cần thiết, chưa tự suy từ sale price/theme mẫu.

- Chỉ sửa rule/token hiện hữu trong repo; không thêm option UI, selector, stylesheet/include, inline/custom_css, `!important`, token mới hay breakpoint mới dưới ngoại lệ này. Nếu cần tạo các phần đó thì đề xuất và hỏi riêng. Không sửa gạch ngang, font family/weight, tracking, gap, money format, sale-first/compare-first hoặc logic commerce bằng ngoại lệ compare-at.
- Rule chung ảnh hưởng mọi `.price__compare-at`, gồm card/PDP/cart. Thu thập consumer và đối chiếu các nguồn có liên quan; chỉ tái dùng scope/binding responsive đã có để thể hiện khác biệt. Khi cần màu/size/opacity khác nhau mà chưa có scope/control phù hợp, ghi xung đột và hỏi phần mở rộng, không áp một card lên toàn theme âm thầm.
- Ghi URL/node/breakpoint, raw fill/alpha/opacity/size px, parent size, ratio em, token/declaration/file/scope và trước–sau vào audit/customization theo repo. Kiểm tra sale state có cả hai giá, không sale/thiếu compare-at, đổi variant và desktop/mobile; chỉ `.price__compare-at` thay đổi trực tiếp, regular/sale/unit giữ contract. Thiếu preview thì ghi `configured-unverified`.
- Biến thể init vẫn kế thừa Style Guide từ nguồn; không tự chạy lại custom compare-at nếu người dùng chưa yêu cầu đổi style.

### 6.5. Button height và spacing desktop/mobile

Nguồn: component Button trong Style Guide, đọc riêng bản desktop và mobile. Nếu Style Guide không có đủ biến thể responsive, hỏi URL frame chứa phần thiếu; không tự suy mobile từ desktop. Tablet dùng setting desktop/tablet theo contract hiện hữu, không tự tạo breakpoint hoặc setting tablet mới.

Với mỗi variant Primary/Secondary/Tertiary có trong thiết kế, ghi:

| Thuộc tính Figma cần đọc | Ý nghĩa |
| --- | --- |
| Height của frame Button | Chiều cao toàn nút, gồm vùng padding/border; không phải chiều cao text label |
| Fixed height / Hug contents / Min height | Cách bố cục thực tế, để phân biệt với CSS `height`/`min-height` |
| Auto Layout padding trái/phải | Khoảng cách ngang bên trong nút |
| Auto Layout padding trên/dưới | Khoảng cách dọc bên trong nút; đọc để kiểm tra tổng height |
| Item spacing giữa icon và label | Gap bên trong nút, chỉ có ý nghĩa khi nút có icon/element tương ứng |
| Khoảng cách giữa các nút | Gap của group/container bên ngoài, không phải button padding |
| Font size, line height, icon size và border width | Các thành phần cần kiểm tra khi height cuối khác Figma |

Không dùng bounding box của label để config chiều cao nút. Không coi Item spacing hoặc khoảng cách giữa hai nút là Letter spacing; Letter spacing vẫn theo scale chung tại mục 8.

Mapping cụ thể vào data/token hiện có:

| Figma | Setting trong `config/settings_data.json` | Token đích | Lưu ý |
| --- | --- | --- | --- |
| Button height desktop | `button_height_desktop` | `--button-height` | Desktop/tablet theo breakpoint hiện hữu |
| Button height mobile | `button_height_mobile` | `--button-height-mobile` | Chỉ dùng số mobile đã đọc được |
| Padding trái/phải desktop | `button_padding_inline_desktop` | `--button-padding-inline-desktop` | Nhãn UI mục tiêu Desktop padding; vẫn chỉ là padding ngang |
| Padding trái/phải mobile | `button_padding_inline_mobile` | `--button-padding-inline-mobile` | Nhãn UI mục tiêu Mobile padding; vẫn chỉ là padding ngang |
| Gap icon–label | Chỉ dùng setting gap nếu repo đã có | Chỉ dùng token gap hiện hữu đúng consumer nếu có | Không tự tạo `--button-gap` hoặc option mới |
| Padding dọc / gap giữa các nút | Chỉ dùng setting/token tương ứng đã tồn tại và thuộc phạm vi config | Xác minh đúng owner | Không biến padding ngang thành padding bốn phía hoặc sửa layout group |

Ưu tiên ghi số phù hợp vào các key data hiện có để resolver emit token. Được hiệu chỉnh range hoặc mapping khi setting chưa biểu diễn đúng số Figma, theo mục 1.1. Chỉ custom trị số token khi thực sự cần, token đã tồn tại, đúng scope và không làm sai consumer khác. Đã khớp thì bỏ qua.

Mara ngày 20/10/2026 emit bốn token height/padding tại `snippets/css-variables-controls.liquid`. `.btn` trong `assets/critical.css` dùng `min-height: var(--button-height)` và `padding: 0 var(--button-padding-inline-desktop)`; mobile đổi sang token mobile. Gap icon–label ở rule này đang là literal `0.5rem`, chưa phải token gap độc lập. Vì vậy không sửa trực tiếp declaration gap hoặc tự tạo token để khớp Figma trong lượt config giới hạn này; nếu cần, báo thiếu và hỏi trước theo mục 9.

Các trường hợp phải báo:

- Figma padding trái và phải không bằng nhau nhưng theme chỉ có một value ngang: không tự lấy trung bình hoặc tạo setting trái/phải.
- Button Hug contents có padding dọc khác biệt, trong khi theme chỉ hỗ trợ min-height và padding ngang: kiểm tra height cuối trước; không tự đổi `min-height` thành `height`, thêm padding dọc hoặc sửa selector.
- Các variant có height/padding khác nhau nhưng setting đang dùng chung: ghi xung đột, không tự tách hệ setting/token theo variant.
- Giá trị ngoài range: hiệu chỉnh range hợp lệ theo mục 1.1. Thiếu gap token/select value thì hỏi trước; cần layout/feature mới thì báo gap, không thêm option mới.

Kiểm tra desktop/mobile với font, line height, border và icon thực tế: height ngoài cùng, padding ngang, vị trí label/icon và gap. Nếu token min-height đúng nhưng nút vẫn cao hơn do nội dung, báo nguyên nhân thay vì sửa Typography hoặc thêm CSS ngoài phạm vi. Giữ nguyên breakpoint và các nút navigation/icon/checkout dùng chung token khi không thuộc thiết kế đang config.

### 6.6. Button Tertiary: Show underline và Underline offset

Nguồn: component **Tertiary button** trong Style Guide. Đọc normal và hover/focus nếu có thiết kế trạng thái, đồng thời đối chiếu desktop/mobile. Không lấy underline của text link khác để config Tertiary.

| Thuộc tính cần đọc | Setting hiện có trong `config/settings_data.json` | Giá trị / token đích |
| --- | --- | --- |
| Có hiển thị underline hay không | `button_tertiary_show_underline` | Boolean `true` / `false`; resolver hiện có điều khiển `--button-tertiary-underline-display` và `--button-tertiary-underline-space` |
| Khoảng cách underline của Tertiary | `button_tertiary_underline_offset` | Số px; token `--button-tertiary-underline-offset` và khoảng chừa `--button-tertiary-underline-space` khi underline bật |

Quy trình:

1. Kiểm tra underline là text decoration hay layer line/vector riêng trong component. Không nhầm border đáy của frame với underline của label.
2. Nếu thiết kế xác nhận Tertiary có underline, config Show underline = `true`; nếu xác nhận không có thì `false`. Không suy “không có” chỉ vì thiếu trạng thái hover hoặc layer đang bị ẩn mà chưa xác minh.
3. Khi underline bật, đọc offset/khoảng cách của đường gạch theo node/component. Lưu mốc đo, số px, font size, line height và nguồn. Khoảng từ đáy bounding box text tới line không mặc nhiên bằng CSS underline offset theo baseline; phải đối chiếu cách render hiện hữu trước khi gán số.
4. Ghi Underline offset bằng số hợp lệ vào setting hiện có để resolver emit token. Range chưa phủ thì hiệu chỉnh theo mục 1.1. Đã khớp thì bỏ qua; không sửa đồng thời setting và hardcode token của cùng thuộc tính khi data đã điều khiển đúng.
5. Show underline = `false` thì giữ giá trị offset đã lưu, không reset về 0 hoặc default. Nếu mapping bật/tắt hiện hữu vẫn hiển thị đường hoặc chừa khoảng sai, được sửa đúng binding theo mục 1.1; không thêm setting hay condition ẩn/hiện UI ngoài phạm vi.
6. Nếu desktop/mobile hoặc normal/hover cần underline/offset khác nhau nhưng chỉ có một bộ setting chung, báo xung đột. Không tự tạo setting responsive, selector hover hay override mới.

Mapping consumer đã xác minh trong Mara ngày 20/10/2026:

- `snippets/css-variables-controls.liquid` emit `--button-tertiary-underline-offset`, `--button-tertiary-underline-space`, `--button-tertiary-underline-display` và `--button-tertiary-text-decoration`.
- Tertiary trong `assets/critical.css` sử dụng pseudo-element của hệ `.link-underline`: `--link-underline-offset` alias token offset Tertiary, `--link-underline-padding` alias underline-space và `--link-underline-display` alias underline-display. Không chỉ đổi decoration token rồi cho rằng đường gạch đã cập nhật.
- Range offset được đọc trong Mara là **0–8px, step 1**. Đọc domain thực tế ở repo đích; nếu Figma ngoài domain hoặc cần bước khác, được hiệu chỉnh range theo mục 1.1. Không ghi data invalid; nếu không giữ được default/dữ liệu cũ trên grid hợp lệ thì báo xung đột.
- Tertiary hiện có `min-height: auto` và `padding: 0`, khác button có nền. Không ép nó theo height/padding của Primary/Secondary hoặc dùng underline offset thay cho padding toàn nút.

Kiểm tra đường gạch xuất hiện/ẩn đúng, khoảng cách và phần chừa không làm lệch layout, normal/hover/focus trên desktop/mobile và label có/không có icon. Không sửa animation, độ dày, màu hoặc phạm vi đường gạch nếu không có setting/token hiện hữu phù hợp và chưa được yêu cầu.

### 6.7. Product cards: cấu hình layout từ card Figma

Khi config từ card Figma, đọc cả nhóm **Product cards** trong Theme Settings để khớp layout, không dừng ở Typography title/price. Dùng URL card đã được cung cấp; hỏi thêm node desktop/mobile hoặc trạng thái cần đối chiếu nếu thiếu. Một frame desktop không tự chứng minh layout mobile hoặc hover. Giữ các thuộc tính chưa có bằng chứng.

**Đọc cấu trúc trước khi gán số:** chọn đúng instance card → media → content → details → title/price, rồi swatch/badge/action. Ghi Auto Layout direction, padding từng cạnh, gap, thứ tự con, alignment, tỷ lệ media, radius/border/shadow và vị trí action ở mỗi breakpoint. Resolve variable theo mode: chip tên `1`, `5` hoặc tên spacing là tên token, chưa phải số px. Chỉ gán số sau khi đọc resolved value; thiếu dữ liệu thì ghi `missing-evidence`, không đoán từ tên chip. Nếu đo cạnh bounding box, ghi rõ suy luận và loại trừ line-height, stroke, padding hoặc parent gap.

ID/token dưới đây là điểm tra cứu đã đối chiếu ở Virelle, không phải quyền tạo key hay coi mọi repo đều hỗ trợ:

| Thuộc tính Figma | Setting hiện hữu cần tìm | Runtime/token cần kiểm tra |
| --- | --- | --- |
| Card standard hoặc nền card, border, shadow, scheme | `product_card_style`, `product_card_border_width`, `product_card_shadow`, `product_card_color_scheme` | `.product-card--standard` / `--card`, `--product-card-border-width`, `--product-card-shadow`, scheme thực tế của card |
| Media ratio | `product_card_ratio` | `--product-card-image-ratio`; Virelle portrait = 4/5, landscape = 4/3, square = 1/1; natural phụ thuộc ảnh thật, không đảm bảo ratio cố định |
| Căn nội dung | `product_card_alignment` | `--product-card-alignment` và `--product-card-content-alignment`; kiểm tra cả text và swatch/action |
| Khoảng cách media → content | `product_card_content_spacing_desktop`, `_mobile` | `--product-card-content-spacing`, `--product-card-content-spacing-mobile`; Virelle standard dùng padding-top, card style có cơ chế padding khác |
| Gap giữa các nhóm con của content, ví dụ swatch → details | `product_card_content_gap_desktop`, `_mobile` | `--product-card-content-gap`, `--product-card-content-gap-mobile` trên `.product-card__content` |
| Gap giữa các dòng trong details, gồm title → price khi không có dòng khác | `product_card_info_gap_desktop`, `_mobile` | `--product-card-info-gap`, `--product-card-info-gap-mobile` trên `.product-card__details` |
| Giới hạn dòng title | `product_card_title_line_limit` | `--product-card-title-line-limit`; title ngắn một dòng chưa chứng minh cần clamp một dòng |
| Swatch trước/sau details, loại, kích thước, ratio, khoảng cách, selected state | `product_card_swatches_enabled`, `product_card_swatch_position`, `_type`, `_limit`, `_gap`, `_width_desktop`, `_width_mobile`, `_ratio`, `_selected_style` | Render order trong snippet và `--product-card-swatch-*`; phân biệt kích thước swatch với outline/ring của selected state |
| Quick add/view, mobile, icon/text, full width, scheme | `product_card_quick_add_enabled`, `_mobile`, `_style`, `_full_width`, `_color_scheme`; `product_card_quick_view_enabled`, `_mobile` | Consumer Liquid/CSS và điều kiện hover/focus/touch; không coi token boolean chưa được tiêu thụ là tính năng đã hoạt động |
| Ảnh thứ hai, vendor/type, sale/sold-out badge | `product_card_secondary`, `product_card_vendor`, `product_card_type`, `product_card_show_sale_badge`, `product_card_show_sold_out_badge` | Điều kiện render và trạng thái sản phẩm thật; thiếu ảnh/vendor/sale trong một card không chứng minh global toggle phải tắt |

- **Ba lớp spacing độc lập:** media→content, content group gap và details row gap không dùng thay nhau. Sale→compare-at dùng `--compare-at-price-spacing` theo mục 6.4.1, không lấy `info_gap` để chỉnh. `product_card_gap_device` nếu chỉ là control chọn thiết bị trong editor không phải giá trị layout.
- Card width, số cột, gutter giữa các card, carousel/peek và padding ngoài danh sách thường thuộc section/block chứa card. Không đổi Product cards global để bù grid sai. Chỉ ghi section/block settings khi nhiệm vụ bao gồm composition/instance đó; task chỉ config theme thì báo phần nằm ngoài nhóm này.
- Radius, card padding hoặc badge position có thể kế thừa group khác hay là cấu trúc cố định. Trace đúng control/token hiện hữu trước khi config; không lấy media radius thay card radius hoặc tạo key giả để biểu diễn thứ tự mới.
- Dùng `config/settings_data.json.current` cho control global. Kiểm tra collection grid, featured collection, compact/single card, shop-the-look và video popup **thực sự có trong repo**: chúng có dùng chung snippet/token, override tại instance hay layout riêng? Một card khác layout không mặc nhiên phải bị ép theo card chuẩn. Nếu nguồn cần giá trị khác nhau mà chỉ có global control, ghi xung đột, giữ context ngoài phạm vi; không tự thêm selector/variant.
- Cấu hình hiển thị khi có bằng chứng về ý định component/state; phân biệt với việc thiếu dữ liệu sản phẩm. Giữ catalog, variant, giá, tags, label thương mại và swatch limit nếu chỉ thấy một ví dụ chưa đủ chứng minh. Màu/typo theo các mục 6.3–6.4 và 10; không tái định nghĩa scale hay hardcode price để khớp layout.
- Đã khớp thì bỏ qua. Giá trị thiếu trong range được căn chỉnh theo mục 1.1; runtime bỏ qua setting thì sửa binding hiện hữu trong phạm vi được phép. Thiếu enum/token phải hỏi trước; thiếu control/thứ tự/feature thì ghi gap, không thêm option hoặc CSS/markup/JS bù.

**Readback:** ghi node/state/breakpoint → resolved Figma value → setting ID → token/consumer/file → trước/sau → output. Đối chiếu desktop/mobile ở đúng width nguồn: crop, order, media→content, swatch→details, title→price, sale/compare gap, wrapping/clamp và hover/focus/touch nếu có nguồn. Kiểm tra JSON/domain/range, saved presets và consumer dùng chung. Chỉ đánh dấu `verified` sau khi xem output; chưa preview thì `configured-unverified`, thiếu bằng chứng/khả năng phải nêu rõ, không báo layout đã khớp hoàn toàn.

## 7. Line height: đúng 6 token chung trước khi được duyệt mở rộng

Chuẩn hóa: Figma px thì `ratio = line_height_px / font_size_px`; Figma % thì `ratio = percent / 100`. Auto chưa có số đo thì ghi chưa xác định, không lấy chiều cao text box hoặc mặc định 1.3 thay thế.

| Thứ tự | Nhãn | Token cần gắn trị số nếu phải custom | Trị số nền trong plan |
| --- | --- | --- | --- |
| 1 | Tighter | `--line-height-tighter` | 1.1 |
| 2 | Tight | `--line-height-tight` | 1.2 |
| 3 | Normal | `--line-height-normal` | **1.3** |
| 4 | Relaxed | `--line-height-relaxed` | 1.4 |
| 5 | Loose | `--line-height-loose` | 1.5 |
| 6 | Extra loose | `--line-height-extra-loose` | 1.6 |

Đây là danh mục mục tiêu, không phải xác nhận token đã có. Thiếu token thì hỏi, không tự tạo.

1. Gom tỷ lệ của tất cả consumer liên quan: Heading, Text, Eyebrow, card title và các nhóm kế thừa/chọn chung scale.
2. Đã có token khớp trị số thì chỉ chọn enum tương ứng trong data. Ví dụ 24px/16px = 1.5: chọn value resolve ra 1.5, không chọn “Normal” chỉ vì tên quen.
3. Nếu phải custom một slot hiện có, giữ Normal = 1.3 và Tighter < Tight < Normal < Relaxed < Loose < Extra loose. Ghi **token cụ thể, giá trị cũ, giá trị mới, nguồn Figma và consumer bị ảnh hưởng**.
4. Có đúng 2 slot dưới 1.3 và 3 slot trên 1.3. “Nằm trong khoảng” không có nghĩa đã khớp; ví dụ 1.35 chưa có slot trong thang nền.
5. Nếu không đủ chỗ hoặc chỉnh slot làm sai consumer khác, báo và hỏi trước khi thêm value/token. Không thêm numeric setting hay local override để né giới hạn.

Giữ alias `--font-body-line-height`, `--font-heading-*-line-height`, `--font-eyebrow-line-height`, card title/price tương ứng. Không đổi binding enum hoặc ý nghĩa dữ liệu cũ âm thầm.

## 8. Letter spacing: một scale dùng chung

**Thu thập đủ trước, gán token sau.** Đọc Heading, Text, Eyebrow, Button, Badges, Product card title và Product card price; xác định nhóm nào có setting và nhóm nào chỉ kế thừa. Audit cả consumer chung ngoài phạm vi config để bảo toàn chúng. Không tạo scale riêng cho Button/Eyebrow/card.

### 8.1. Danh mục 11 value và CSS token chỉ định

| Thứ tự | Value hiển thị | Token cần gắn trị số nếu phải custom |
| --- | --- | --- |
| 1 | Extra tight | `--letter-spacing-extra-tight` |
| 2 | Super tight | `--letter-spacing-super-tight` |
| 3 | Ultra tight | `--letter-spacing-ultra-tight` |
| 4 | Tighter | `--letter-spacing-tighter` |
| 5 | Tight | `--letter-spacing-tight` |
| 6 | Normal | `--letter-spacing-normal` |
| 7 | Relaxed | `--letter-spacing-relaxed` |
| 8 | Loose | `--letter-spacing-loose` |
| 9 | Extra loose | `--letter-spacing-extra-loose` |
| 10 | Ultra loose | `--letter-spacing-ultra-loose` |
| 11 | Mega loose | `--letter-spacing-mega-loose` |

Normal = 0. Năm slot trước âm, năm slot sau dương. Tất cả tăng nghiêm ngặt. Text style có cùng trị số chuẩn hóa chọn cùng token, không tạo hai slot bằng nhau.

Danh sách trên chỉ định tên cần tra và dùng **nếu token đã tồn tại**. Token chưa tồn tại là phần thiếu cần hỏi, không phải quyền tự thêm. Mở rộng thang sau khi được duyệt phải cập nhật cùng một scale, giữ thứ tự và Normal = 0.

### 8.2. Chuẩn hóa px/em

- Giữ px hoặc đổi em theo font size tương ứng đều được. Luôn lưu số gốc.
- `spacing_em = spacing_px / font_size_px`; Figma % thì `spacing_em = percent / 100`.
- Chọn một đơn vị cho thang để so sánh thứ tự. Token px cho cùng số px ở mọi size; token em cho cùng tỷ lệ, số px có thể khác theo font size.
- Kiểm tra từng breakpoint. Thiết kế giữ tracking px cố định nhưng size thay đổi có thể không khớp bằng một token em chung.
- Khi Body và Price khác size, kiểm tra cách áp dụng CSS: Body tracking 0.1px tại 16px = 0.00625em. Nếu Price 14px tự khai báo `letter-spacing: var(--font-body-letter-spacing)` với alias ra 0.00625em thì output là 0.0875px; nếu Price chỉ kế thừa property từ cha có computed tracking 0.1px thì nó nhận 0.1px. Token px giữ cùng số px khi được áp lại ở size khác. Chọn đơn vị và xác minh cascade theo bằng chứng của toàn bộ consumer; không thêm declaration chỉ để ép ví dụ này. Đây là ví dụ tính toán, không phải default.
- Ví dụ có điều kiện: -1.28px/64px, -0.8px/40px, -0.64px/32px và -0.48px/24px đều là -0.02em; có thể cùng chọn token đang resolve ra -0.02em. Đây không phải số liệu của một file Figma mới đã được đọc.

### 8.3. Quy trình chọn và custom trị số

1. Đủ nguồn của mọi consumer bị ảnh hưởng mới lập thang cuối. Thiếu Eyebrow/card thì chưa áp dụng token global.
2. Chuẩn hóa, bỏ trùng, tách âm / 0 / dương. Kiểm tra giá trị cuối cùng của token đang dùng.
3. Có slot khớp thì config setting chọn slot đó. Nếu data và CSS đã khớp thì bỏ qua cả hai.
4. Chưa khớp nhưng có thể căn chỉnh slot hiện hữu: lập bảng thay đổi trị số token, giữ thứ tự. Các slot không cần thay giữ nguyên nếu không vi phạm thứ tự.
5. Chỉ đổi trị số token thực sự cần. Không hardcode số riêng ở từng alias role để né scale chung, được sửa mapping/binding hiện hữu theo mục 1.1 để setting resolve đúng token, nhưng không tự thêm enum hoặc consumer mới.
6. Ví dụ chọn thang px cho bộ -1.28/-0.8/-0.64/-0.48/0: một phương án là Super tight=-1.28px, Ultra tight=-0.8px, Tighter=-0.64px, Tight=-0.48px, Normal=0px; Extra tight phải nhỏ hơn -1.28px. Trị số bổ sung như -1.6px chỉ là suy luận minh họa, không tự động áp làm default.
7. Các slot suy luận phải được đánh dấu, kiểm tra toàn bộ consumer và nằm trong phạm vi custom giá trị token hiện có. Nếu cần thêm slot/token thì hỏi theo mục 9.
8. Tính ngược số px của từng role/size/breakpoint để kiểm tra Figma. Không chọn gần đúng mà vẫn ghi “khớp”. Enum legacy như `1.2px` không được coi là một scale riêng hoặc slot thứ 12 đã được duyệt.

### 8.4. Alias role phải giữ, không phải scale mới

| Consumer | Alias spacing hiện hữu cần ưu tiên |
| --- | --- |
| Heading | `--font-heading-letter-spacing`, `--font-heading-{display,xl,lg,md,sm,xs}-letter-spacing` |
| Text | `--font-body-letter-spacing` |
| Eyebrow | `--font-eyebrow-letter-spacing` |
| Button | `--button-letter-spacing` |
| Badge | `--badge-letter-spacing` |
| Card title | `--product-card-title-letter-spacing` nếu đã có |
| Card price | Kế thừa Body qua `--font-body-letter-spacing`; kiểm tra cascade, không tự thêm `--price-letter-spacing` |

Ví dụ alias đã có `--button-letter-spacing: var(--letter-spacing-loose)` thì custom giá trị Loose ở primitive duy nhất, không tạo `--button-letter-spacing-loose`. Nếu binding của setting/alias hiện hữu chưa đúng, được sửa runtime mapping theo mục 1.1 sau khi kiểm tra mọi consumer. Nếu cần token/alias mới thì hỏi theo mục 9; không tạo hệ biến khác.

## 9. Khi cần thêm select value hoặc CSS token: bắt buộc hỏi

Căn chỉnh range số và mapping hiện hữu theo mục 1.1 đã được cho phép. Chỉ chuyển sang đề xuất mở rộng sau khi việc tái dùng/căn chỉnh đó vẫn không biểu diễn được Figma. Quyền sửa range không cấp quyền thêm select value hoặc token mới.

Ưu tiên giữ chính xác **Heading → Eyebrow → Product card title**, rồi mới phân bổ slot còn lại cho Button, Badges và các consumer khác. Vẫn phải thu thập đầy đủ tất cả nhóm.

Thang 11 mức có 5 slot âm, 5 slot dương và 0. Có thể thiếu slot dù tổng trị số phân biệt chưa vượt 11; không đặt số âm vào slot dương. Nếu nhóm ưu tiên đã không đủ chỗ thì báo ngay những trị số ưu tiên chưa map được.

Trước khi thêm bất kỳ value hoặc CSS token nào, gửi bảng:

| Nội dung | Phải ghi rõ |
| --- | --- |
| Nhu cầu Figma | Trị số gốc, font size, đơn vị chuẩn hóa, nhóm/breakpoint và URL node |
| Mapping hiện có | Các slot đang phục vụ Heading, Eyebrow, card title và consumer khác |
| Phần chưa khớp | Trị số chưa có slot; vì sao không thể tái dùng/căn chỉnh token hiện hữu |
| Đề xuất thêm | Value/enum mới cho **setting đã có**, token `--letter-spacing-*` hoặc `--line-height-*` mới, trị số và vị trí trong thứ tự |
| File phải chạm | File khai báo token; schema/locale/resolver nếu cần để value mới dùng được; chỉ rõ thay đổi tối thiểu |
| Ảnh hưởng | Consumer dùng chung, compatibility và dữ liệu ngoài phạm vi cần giữ |

Hỏi cụ thể: “Các value/token hiện tại chưa biểu diễn được … Mình đề xuất thêm value … vào setting hiện có … và CSS token … = …, cần sửa các file … Bạn có đồng ý không?”

Chưa có câu trả lời đồng ý thì **không thêm**, không tạo local override/namespace khác, không thay một phần scale global làm ảnh hưởng phần chưa giải quyết. Có thể hoàn tất các config độc lập, nhưng ghi rõ phần đang chờ.

Sau khi được duyệt, chỉ thêm đúng value/token đã chốt. Các setting đang dùng chung scale nhận cùng danh sách/thứ tự, không tạo option mới. Ngoài 11 mức chỉ tồn tại sau quyết định mở rộng rõ ràng của người dùng.

## 10. Colors: đọc bảng Figma, ghi vào scheme hiện có

### 10.1. Mapping giữ ID/token

Nhãn đích theo plan là **Colors**; Accent / Eyebrow text được hiển thị là **Eyebrow**. Trong lượt config này không sửa label/locale nếu bản update chưa triển khai; dùng field hiện hữu cùng nghĩa và báo khác biệt. Font role Accent trong Typography không đổi tên.

| Nhãn Figma | Nhãn Colors đích | Setting ID trong scheme | Token hiện có |
| --- | --- | --- | --- |
| Background | Background | `background` | `--background-color`, alias `--color-background` |
| Heading / Heading color | Headings | `heading` | `--heading-color` |
| Heading highlight | Heading highlight | `heading_highlight` | `--heading-highlight-color` |
| Body text / Text | Text | `text` | `--body-color`, alias `--color-foreground` |
| Accent / Eyebrow text / Eyebrow | Eyebrow | `accent` nếu vẫn cùng nghĩa | `--accent-color`, alias `--color-accent` |
| Border | Border | `border` | `--border-color`, alias `--color-border` |
| Sale price | Sale price | `sale_price` | `--sale-price-color`, alias giá theo scope hiện hữu |
| Shadow | Shadow | `shadow` | `--shadow-color` |

Ưu tiên đổi giá trị màu trong scheme của `settings_data.json`, để resolver emit token như hiện tại. Không hardcode màu của một scheme vào root token dùng cho mọi scheme. Không tạo `eyebrow_color` hoặc hệ biến màu mới vì nhãn khác tên ID.

`--accent-color` có thể dùng chung cho link/icon/input focus; kiểm tra chúng khi đổi màu Eyebrow. Virelle đã bỏ global `badge_sale_price_color` và alias `--badge-sale-price`; Sale price lấy từ field `sale_price` của scheme → `--sale-price-color` → `--price-sale-color`. Khi kiểm tra repo khác còn global/giá local override, báo rõ owner; không khôi phục picker dư vào Virelle.

### 10.2. Đọc bảng màu dạng ảnh/frame

1. Đọc đúng URL bảng màu người dùng cung cấp, phân biệt từng palette/scheme và trạng thái.
2. Đối chiếu nhãn, swatch, HEX và alpha. Bảng raster có in HEX thì đọc ký tự chính xác; không coi màu pixel ảnh là HEX nguồn.
3. Nếu có node/style/variable tương ứng, dùng thuộc tính fill/stroke/opacity để kiểm chứng. Nếu chữ HEX và node xung đột, ghi rõ để xác minh.
4. Không bỏ alpha hoặc hiểu Transparent là đen. Không suy Sale price từ Sale badge, Border từ Shadow hoặc Eyebrow từ Heading highlight chỉ vì gần giống.
5. Ô có `Generated/N` hoặc `from Generated/N` thì tra cấp N theo mục 11; ô có HEX trực tiếp dùng đúng HEX đó.
6. Không có màu trực tiếp hoặc tham chiếu rõ ràng thì ghi thiếu dữ liệu; không tự chọn một màu Generated thay thế.

### 10.3. Button, badge và scope

- Giữ Primary button, Secondary button, Tertiary button. Config các field normal/hover đã tồn tại theo đúng palette; không đổi Tertiary thành Outline and subtle.
- Giữ Border thường riêng của Primary/Secondary nếu có. Không ép nó bằng Background vì theme mẫu không có picker border riêng.
- Sale badge/Sold out badge có thể là màu global ngoài scheme; kiểm tra scope trước khi config. Không đồng nhất chúng với Sale price.
- Giữ scheme ID, Default color scheme, section assignments và các preset ngoài phạm vi. Không tạo lại scheme hoặc chuyển override global lên mọi scheme.

### 10.4. Hover thiếu thiết kế: được tạo từ màu gốc

Khi Figma có hover rõ thì dùng thiết kế đó. Khi thiếu, người dùng đã cho phép tạo palette hover hài hòa từ màu normal; không để thiếu hover chặn config. Ghi `derived-hover`, không ghi là màu đã đo từ Figma. Chỉ cập nhật field hover có sẵn của Primary/Secondary/Tertiary trong scheme hiện hữu; không thay màu normal hoặc suy hover từ Generated/N tùy ý.

- Với nút nền đặc: bắt đầu mix màu nền gốc khoảng8–12% về trắng nếu nền tối, về đen nếu nền sáng; giữ sắc độ gần màu gốc. Border hover lấy từ border normal theo cùng hướng, không tự gộp picker border với background.
- Giữ màu label gốc nếu tương phản với nền hover đủ **4.5:1**; nếu không thì giảm mức mix hoặc chọn màu chữ sáng/tối trong palette có contrast đủ. Không giảm opacity cả nút để tạo hover vì sẽ làm text chìm. Tính relative luminance từ sRGB tuyến tính và ratio `(L sáng + .05)/(L tối + .05)`; nền/fill có alpha phải composite với background thực trước khi tính.
- Tertiary/transparent: kiểm tra màu label hover với background scheme thực, chỉ thay nhẹ màu label/underline qua field hiện hữu, giữ contrast4.5:1. Không giả định nền trắng cho dark scheme hoặc lớp overlay. Không resolve được nền thực thì giữ label đủ tương phản đã biết và ghi giới hạn, không bịa kết quả contrast.
- Kiểm tra tất cả scheme đang config, normal→hover và focus-visible hiện hữu; không sửa disabled state hay bỏ focus ring. Lưu màu normal, màu hover, công thức/mức mix và ratio; preview vẫn cần để xác nhận cảm giác hover và các lớp phủ.

## 11. Màu `Generated/N` và `from Generated/N`

Công cụ: [Layouthub Generate Color](https://remix.layouthub.com/generate-color).

**Ô “Insert a Hex color” bắt buộc dùng Heading color của palette đang config.** Không lấy Background, Eyebrow, Border hoặc màu tùy ý làm seed thay thế.

1. Đọc Heading HEX thực tế. Nếu chỉ có tham chiếu Generated chưa resolve thì tìm seed hợp lệ trước; không tạo vòng phụ thuộc.
2. Nhập đúng Heading HEX, dùng điều khiển đang hiển thị nếu công cụ yêu cầu sinh màu. Không đoán nút/endpoint hoặc tự tính màu “tương tự Generated”.
3. Đọc kết quả **Generated**, lưu mã HEX theo đúng từng cấp 100, 200, 300… cùng seed đã dùng.
4. Ô Figma ghi `Generated/200` hoặc `from Generated/200` thì lấy **cấp 200** của đúng seed. `from` chỉ nguồn tham chiếu. Có thể chuẩn hóa khoảng trắng/hoa thường, giữ nguyên chỉ số và nhãn gốc làm bằng chứng.
5. `/100`, `/200`… là cấp màu, **không phải opacity**. Alpha đọc riêng theo thiết kế/schema.
6. Vai trò ô Figma quyết định field nhận màu: Border = from Generated/200 thì gán cấp 200 vào `border`; Eyebrow = Generated/600 thì gán cấp 600 vào `accent`. Đây chỉ là ví dụ cách tra, không phải quy tắc cố định cấp 200 luôn là Border.
7. Mã HEX trực tiếp không bị thay bằng Generated. Mỗi Heading HEX khác nhau cần đúng bảng Generated tương ứng; cùng seed có thể tái dùng kết quả đã xác minh.
8. Cấp không đọc rõ, không có trên tool, hoặc placeholder `from Generated/chi_so` chưa có số cụ thể thì báo thiếu. Không lấy swatch đầu tiên hay tự nội suy một cấp khác.

Nguồn ví dụ: [bảng màu Essen, node 46249:7077](https://www.figma.com/design/v6iKvP4OuW3y0A9bbxel5U/%25E2%259C%2585-Essen---Thi%25E1%25BB%2587n?node-id=46249-7077&t=xgUvCwFS3wvlM3TJ-0). Không dùng palette ví dụ làm mặc định cho mọi theme.

URL ví dụ không thay cho bằng chứng đọc trong lượt config. Không có sẵn palette Generated mặc định trong reference này; phải đọc và xác minh đúng seed/cấp trước khi ghi màu.

## 12. Bảng thay đổi và kiểm tra trước khi kết thúc

Mỗi mục cần ghi: nguồn Figma, nhóm/scheme/breakpoint, setting ID, token chính xác, file khai báo, giá trị hiện tại, giá trị cần đạt, thao tác và trạng thái.

Chỉ dùng các trạng thái sau cho thao tác:

- **Đã khớp, bỏ qua**.
- **Đổi giá trị setting hiện hữu** trong `config/settings_data.json`.
- **Đổi trị số token hiện hữu**, nêu rõ bên phải khai báo/literal nào và mọi consumer bị ảnh hưởng.
- **Chờ URL / dữ liệu / công cụ**.
- **Chờ duyệt thêm value + token**; chưa tạo option mới.
- **Căn chỉnh range / runtime mapping hiện hữu**, ghi trước/sau, giá trị saved/default, consumer và kết quả runtime theo mục 1.1.
- **Không thực hiện trong phạm vi hiện tại** nếu cần markup, tính năng hoặc setting mới.

Đối với Generated, bảng phải có tham chiếu `Generated/N`, Heading HEX seed, HEX đầu ra cấp N và field nhận màu. Với Typography phải có số px cuối cùng đối chiếu Figma, không chỉ tên token.

Kiểm tra sau thay đổi:

1. JSON hợp lệ; chỉ key config được yêu cầu thay đổi. Preset/scheme ngoài phạm vi giữ nguyên.
2. Token được gắn đúng giá trị, scope và breakpoint; không có alias vòng hoặc một token chung bị khai báo các số khác nhau theo nhóm.
3. Line height tăng đúng thứ tự với Normal = 1.3; letter spacing tăng đúng thứ tự với Normal = 0. Token đã khớp không bị đổi.
4. Kiểm tra Heading/Text/Eyebrow/Button/Badges/card title/price cùng consumer bị ảnh hưởng. Xác minh Body/16 → primitive chung → `--font-body-letter-spacing` → tracking của Price; không còn literal chặn kế thừa ngoài control riêng đã xác nhận. Đối chiếu px runtime ở mọi size/breakpoint. Thay Body tracking phải truyền tới các giá kế thừa, trong khi font/size card/PDP/cart vẫn đúng setting và scope riêng. Button đối chiếu thêm height, padding và icon–label gap trên desktop/mobile theo mục 6.5; Tertiary kiểm tra Show underline và Underline offset theo mục 6.6.
5. Kiểm tra đúng scheme, border/alpha, Eyebrow và Sale price; normal/hover của ba type button.
6. Với ngoại lệ compare-at ở mục 6.4.2, kiểm tra đúng ba thuộc tính, ratio em ra px, màu/alpha/opacity không bị nhân hai lần và mọi consumer chung; ghi rõ custom hiện hữu trước/sau. So diff với phạm vi cho phép. Schema chỉ được đổi range hiện hữu theo mục 1.1, bộ control đã duyệt ở mục 1.2 hoặc thêm value đã được duyệt; kiểm tra min/max/step, default và dữ liệu cũ hợp lệ. Mapping hiện hữu phải có kiểm chứng output trước/sau và không đổi hành vi ngoài phạm vi. Locale/markup/JS/selector/breakpoint mới ngoài chấp thuận cụ thể thì chưa đạt.
7. Báo rõ phần đã config, phần bỏ qua vì khớp và phần chờ. Không tuyên bố đã Save/push/publish store khi chỉ sửa local.

Đây là nguồn contract config dùng chung của ba skill trong nhóm preset. Plan/sheet hoặc ngoại lệ implementation từ skill khác không tự mở rộng phạm vi. Yêu cầu bảo trì skill không phải yêu cầu chạy config theme hoặc ghi lên store.
