# مشروع AppMarket - دليل إضافة زر الدعم "Buy Me a Coffee"

هذا المشروع يدعم إضافة أداة تفاعلية للدعم المالي عبر "Buy Me a Coffee". يمكن لأي صاحب متجر أو مطور إضافتها بسهولة.

## طريقة الإضافة

لإضافة زر الدعم العائم إلى متجرك، قم بنسخ ولصق الكود التالي في ملف HTML الرئيسي لموقعك (مثل `index.html`)، ويفضل وضعه قبل إغلاق وسم `</body>`:

\`\`\`html
<div id="support-button"></div>
<script data-name="BMC-Widget"
        data-cfasync="false"
        src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js"
        data-id="<معرف-حسابك-هنا>"
        data-description="ادعم مشروعي على Buy Me a Coffee!"
        data-message="شكراً لزيارتك، هل ترغب بدعمي بفنجان قهوة؟ ☕"
        data-color="#FF5F5F"
        data-position="right"
        data-x_margin="18"
        data-y_margin="18">
</script>
\`\`\`

**شرح الخصائص:**
*   `data-id`: **إجباري**. ضع هنا معرف حسابك على منصة Buy Me a Coffee.
*   `data-color`: لون الزر (يمكنك استخدام أي كود HEX).
*   `data-message`: الرسالة الترحيبية التي تظهر للزائر الجديد.
*   `data-position`: موضع الزر (`right` لليمين أو `left` لليسار).

## تفعيل الأداة

بمجرد حفظ الملف وتحديث الصفحة، ستظهر الأداة بشكل تلقائي وتعمل فوراً.
