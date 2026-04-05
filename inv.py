
file_path = "/mnt/data/Sahasrachandra_Darshan_Nimantran.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()

center_style = ParagraphStyle(
    name="Center",
    parent=styles["Normal"],
    alignment="center",
    fontSize=12
)

title_style = ParagraphStyle(
    name="Title",
    parent=styles["Normal"],
    alignment="center",
    fontSize=16,
    spaceAfter=12
)

content = []

content.append(Paragraph("🌙 <b>सहस्रचंद्र दर्शन सोहळ्याचे आमंत्रण</b> 🌙", title_style))
content.append(Paragraph("<b>समस्त रानडे कुटुंबीय</b> यांच्या वतीने", center_style))
content.append(Spacer(1, 12))

content.append(Paragraph("<b>आदरणीय: श्री. रमेश रामकृष्ण रानडे</b>", styles["Normal"]))
content.append(Spacer(1, 6))

content.append(Paragraph(
    "यांच्या <b>सहस्रचंद्र दर्शन</b> या मंगलमय सोहळ्यानिमित्त आयोजित केलेल्या कौटुंबिक समारंभासाठी "
    "आपणास आणि आपल्या परिवारास आग्रहाचे आमंत्रण आहे.",
    styles["Normal"]
))

content.append(Spacer(1, 12))

table_data = [
    ["दिनांक", "१० जानेवारी २०२६"],
    ["वार", "शनिवार"],
    ["वेळ", "सकाळी ०८:०० ते दुपारी ०३:०० वाजता"],
    ["स्थळ", "देव-सुधा (Deo-Sudha), बिजली नगर, चिंचवड, शाहू उद्यानजवळ, पुणे ४११०३३"],
]

table = Table(table_data, colWidths=[100, 350])
table.setStyle(TableStyle([
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("BACKGROUND", (0,0), (-1,0), colors.whitesmoke),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))

content.append(table)
content.append(Spacer(1, 12))

content.append(Paragraph(
    "या शुभदिनी, परमेश्वराच्या कृपेने पूज्य व्यक्तीस दीर्घायुष्य लाभो, "
    "या कामनांसह आयोजित केलेल्या या सोहळ्यात आपण उपस्थित राहून "
    "आपल्या शुभाशीर्वादांनी कार्यक्रमाची शोभा वाढवावी, ही नम्र विनंती.",
    styles["Normal"]
))

content.append(Spacer(1, 12))

content.append(Paragraph("<b>निमंत्रक व स्वागतोत्सुक</b>", center_style))
content.append(Paragraph("<b>श्री व सौ मुगधा मंगेश रानडे</b>", center_style))
content.append(Paragraph("<b>श्री व सौ स्नेहा नितिन आपटे</b>", center_style))
content.append(Paragraph("(संपर्क: ९९२३१०८४४२, ९९२३५९७४४७)", center_style))

doc.build(content)

file_path