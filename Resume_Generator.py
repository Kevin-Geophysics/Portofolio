
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
def generate_resume():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    story = []
    styles = getSampleStyleSheet()
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=6,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    # Header
    story.append(Paragraph("John Doe", title_style))
    story.append(Paragraph("Full Stack Developer &amp; Data Scientist", subtitle_style))
    story.append(Paragraph("john.doe@email.com | linkedin.com/in/johndoe | github.com/johndoe", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    # Professional Summary
    story.append(Paragraph("Professional Summary", heading_style))
    summary_text = """Dedicated software developer with 5+ years of experience building scalable
    web applications and data-driven solutions. Strong foundation in both frontend and backend
    technologies with a passion for creating elegant solutions to complex problems."""
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    # Skills
    story.append(Paragraph("Technical Skills", heading_style))
    skills_data = [
        ['Programming Languages:', 'Python, JavaScript, TypeScript, Java, SQL'],
        ['Frameworks &amp; Libraries:', 'React, Node.js, Django, Flask, Streamlit, TensorFlow'],
        ['Tools &amp; Platforms:', 'Git, Docker, AWS, PostgreSQL, MongoDB, REST APIs']
]
skills_table = Table(skills_data, colWidths=[2*inch, 4.5*inch])
skills_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(skills_table)
story.append(Spacer(1, 0.2*inch))
# Experience
story.append(Paragraph("Professional Experience", heading_style))
story.append(Paragraph("&lt;b&gt;Senior Full Stack Developer&lt;/b&gt; - Tech Company Inc.", styles['Normal']))
story.append(Paragraph("&lt;i&gt;2021 - Present&lt;/i&gt;", styles['Normal']))
exp1 = """• Led development of e-commerce platform serving 10,000+ users&lt;br/&gt;
• Implemented microservices architecture reducing system latency by 40%&lt;br/&gt;
• Mentored junior developers and conducted code reviews"""
story.append(Paragraph(exp1, styles['Normal']))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("&lt;b&gt;Software Developer&lt;/b&gt; - StartUp Solutions", styles['Normal']))
story.append(Paragraph("&lt;i&gt;2019 - 2021&lt;/i&gt;", styles['Normal']))
exp2 = """• Built data analytics dashboard processing millions of records daily&lt;br/&gt;
• Developed REST APIs serving mobile and web applications&lt;br/&gt;
• Optimized database queries improving performance by 60%"""
story.append(Paragraph(exp2, styles['Normal']))
story.append(Spacer(1, 0.2*inch))
# Education
story.append(Paragraph("Education", heading_style))
story.append(Paragraph("&lt;b&gt;Bachelor of Science in Computer Science&lt;/b&gt;", styles['Normal']))
story.append(Paragraph("University Name - 2019", styles['Normal']))
story.append(Spacer(1, 0.1*inch))
# Certifications
story.append(Paragraph("Certifications", heading_style))
certs = """• AWS Certified Solutions Architect&lt;br/&gt;
• Professional Data Scientist Certification&lt;br/&gt;
• Full Stack Web Development Certification"""
story.append(Paragraph(certs, styles['Normal']))
# Build PDF
doc.build(story)
buffer.seek(0)
return buffer

