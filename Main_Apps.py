
import streamlit as st
from resume_generator import generate_resume
from email_sender import send_contact_email
from datetime import datetime
st.set_page_config(
    page_title="My Portfolio",
    page_icon="■■■",
    layout="wide"
)
# Custom CSS for better styling
st.markdown("""
    &lt;style&gt;
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #667eea;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .skill-badge {
        display: inline-block;
        background-color: #f0f2f6;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        border-radius: 20px;
        font-weight: 500;
    }
    .project-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    .contact-info {
        text-align: center;
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-top: 1rem;
    }
    .analytics-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .analytics-number {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    &lt;/style&gt;
""", unsafe_allow_html=True)
# Initialize session state for analytics
if 'page_views' not in st.session_state:
    st.session_state.page_views = 0
    st.session_state.resume_downloads = 0
    st.session_state.contact_submissions = 0
st.session_state.page_views += 1
# Header Section
st.markdown("""
    &lt;div class="main-header"&gt;
        &lt;h1&gt;John Doe&lt;/h1&gt;
        &lt;h3&gt;Full Stack Developer &amp; Data Scientist&lt;/h3&gt;
        &lt;p&gt;Building innovative solutions with code&lt;/p&gt;
    &lt;/div&gt;
""", unsafe_allow_html=True)
# Navigation
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["About Me", "Skills", "Projects", "Blog", "Testimonials", "Contact"])
# About Me Section
with tab1:
    st.markdown('&lt;h2 class="section-header"&gt;About Me&lt;/h2&gt;', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        &lt;div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                     width: 100%;
                     aspect-ratio: 1;
                     border-radius: 50%;
                     display: flex;
                     align-items: center;
                     justify-content: center;
                     color: white;
                     font-size: 5rem;
                     margin-bottom: 1rem;"&gt;
             ■■■
        &lt;/div&gt;
        &lt;p style="text-align: center; color: #666; font-size: 0.9rem;"&gt;Profile Photo&lt;/p&gt;
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        ### Hello! I'm a passionate developer
        I'm a dedicated software developer with expertise in building scalable web applications
        and data-driven solutions. With a strong foundation in both frontend and backend technologies,
        I enjoy creating elegant solutions to complex problems.
        **What I Do:**
        - Design and develop full-stack web applications
        - Build data analysis and machine learning models
        - Create intuitive user interfaces
        - Optimize application performance and scalability
        **Education:**
        - Bachelor's Degree in Computer Science
        - Certifications in Cloud Computing and Data Science
        **Experience:**
        - 5+ years of professional development experience
        - Worked with startups and established companies
        - Led multiple successful project launches
        """)
        st.markdown("---")
        pdf_buffer = generate_resume()
        if st.download_button(
             label="■ Download Resume (PDF)",
             data=pdf_buffer,
             file_name="John_Doe_Resume.pdf",
             mime="application/pdf"
        ):
             st.session_state.resume_downloads += 1
# Skills Section
with tab2:
    st.markdown('&lt;h2 class="section-header"&gt;Skills &amp; Technologies&lt;/h2&gt;', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Programming Languages")
        skills = ["Python", "JavaScript", "TypeScript", "Java", "SQL", "HTML/CSS"]
        for skill in skills:
            st.markdown(f'&lt;div class="skill-badge"&gt;{skill}&lt;/div&gt;', unsafe_allow_html=True)
    with col2:
        st.markdown("### Frameworks &amp; Libraries")
        frameworks = ["React", "Node.js", "Django", "Flask", "Streamlit", "TensorFlow"]
        for framework in frameworks:
            st.markdown(f'&lt;div class="skill-badge"&gt;{framework}&lt;/div&gt;', unsafe_allow_html=True)
    with col3:
        st.markdown("### Tools &amp; Platforms")
        tools = ["Git", "Docker", "AWS", "PostgreSQL", "MongoDB", "REST APIs"]
        for tool in tools:
            st.markdown(f'&lt;div class="skill-badge"&gt;{tool}&lt;/div&gt;', unsafe_allow_html=True)
    st.markdown("---")
    # Skills proficiency
    st.markdown("### Technical Proficiency")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Web Development**")
        st.progress(0.9)
        st.markdown("**Data Science**")
        st.progress(0.85)
        st.markdown("**Machine Learning**")
        st.progress(0.75)
    with col2:
        st.markdown("**Cloud Computing**")
        st.progress(0.8)
        st.markdown("**Database Management**")
        st.progress(0.85)
        st.markdown("**UI/UX Design**")
        st.progress(0.7)
# Projects Section
with tab3:
    st.markdown('&lt;h2 class="section-header"&gt;Featured Projects&lt;/h2&gt;', unsafe_allow_html=True)
    # Project 1
    st.markdown("""
    &lt;div class="project-card"&gt;
        &lt;h3&gt;■ E-Commerce Platform&lt;/h3&gt;
        &lt;p&gt;&lt;strong&gt;Technologies:&lt;/strong&gt; React, Node.js, MongoDB, Stripe API&lt;/p&gt;
        &lt;p&gt;A full-featured e-commerce platform with user authentication, product catalog,
        shopping cart, and payment integration. Implemented real-time inventory management
        and order tracking system.&lt;/p&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("■ View Demo", key="demo1")
    with col2:
        st.button("■ GitHub Repo", key="repo1")
    st.markdown("---")
    # Project 2
    st.markdown("""
    &lt;div class="project-card"&gt;
        &lt;h3&gt;■ Data Analytics Dashboard&lt;/h3&gt;
        &lt;p&gt;&lt;strong&gt;Technologies:&lt;/strong&gt; Python, Streamlit, Pandas, Plotly&lt;/p&gt;
        &lt;p&gt;An interactive dashboard for analyzing business metrics and KPIs. Features include
        real-time data visualization, custom report generation, and predictive analytics
        using machine learning models.&lt;/p&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
         st.button("■ View Demo", key="demo2")
    with col2:
         st.button("■ GitHub Repo", key="repo2")
    st.markdown("---")
    # Project 3
    st.markdown("""
    &lt;div class="project-card"&gt;
         &lt;h3&gt;■ AI Chatbot Assistant&lt;/h3&gt;
         &lt;p&gt;&lt;strong&gt;Technologies:&lt;/strong&gt; Python, TensorFlow, Flask, Natural Language Processing&l
         &lt;p&gt;An intelligent chatbot using NLP and machine learning to provide customer support.
         Trained on custom datasets with context-aware responses and multi-language support.&lt;/p&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
         st.button("■ View Demo", key="demo3")
    with col2:
         st.button("■ GitHub Repo", key="repo3")
    st.markdown("---")
    # Project 4
    st.markdown("""
    &lt;div class="project-card"&gt;
         &lt;h3&gt;■ Task Management App&lt;/h3&gt;
         &lt;p&gt;&lt;strong&gt;Technologies:&lt;/strong&gt; React Native, Firebase, Redux&lt;/p&gt;
         &lt;p&gt;A mobile-first task management application with features like task prioritization,
         team collaboration, deadline reminders, and progress tracking. Cross-platform support
         for iOS and Android.&lt;/p&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
         st.button("■ View Demo", key="demo4")
    with col2:
         st.button("■ GitHub Repo", key="repo4")
# Blog Section
with tab4:
    st.markdown('&lt;h2 class="section-header"&gt;Blog &amp; Articles&lt;/h2&gt;', unsafe_allow_html=True)
    st.markdown("""
         Welcome to my blog! Here I share insights, tutorials, and thoughts on software development,
         data science, and technology trends.
    """)
    # Blog Post 1
    with st.container():
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h3&gt;■ Building Scalable Microservices with Python&lt;/h3&gt;
              &lt;p&gt;&lt;i&gt;Published on January 15, 2025&lt;/i&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         Learn how to design and implement microservices architecture using Python, FastAPI, and Docker.
         This comprehensive guide covers service communication, data consistency, and deployment strategies.
         **Key Topics:**
         - Microservices design patterns
         - API Gateway implementation
         - Message queues and event-driven architecture
         - Containerization with Docker
         """)
         col1, col2 = st.columns([1, 4])
         with col1:
              st.button("Read More", key="blog1")
         st.markdown("---")
    # Blog Post 2
    with st.container():
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h3&gt;■ Data Visualization Best Practices&lt;/h3&gt;
              &lt;p&gt;&lt;i&gt;Published on December 20, 2024&lt;/i&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         Discover the principles of effective data visualization and learn how to create compelling charts
         that tell meaningful stories. Includes practical examples using Python libraries.
         **Key Topics:**
         - Choosing the right chart type
         - Color theory and accessibility
         - Interactive dashboards with Streamlit
         - Common visualization mistakes to avoid
         """)
         col1, col2 = st.columns([1, 4])
         with col1:
              st.button("Read More", key="blog2")
         st.markdown("---")
    # Blog Post 3
    with st.container():
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h3&gt;■ Introduction to Machine Learning with TensorFlow&lt;/h3&gt;
              &lt;p&gt;&lt;i&gt;Published on November 10, 2024&lt;/i&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         A beginner-friendly guide to getting started with machine learning using TensorFlow.
         Build your first neural network and understand the fundamentals of deep learning.
         **Key Topics:**
         - Neural network basics
         - Training and validation
         - Model optimization techniques
         - Practical applications and use cases
         """)
         col1, col2 = st.columns([1, 4])
         with col1:
              st.button("Read More", key="blog3")
# Testimonials Section
with tab5:
    st.markdown('&lt;h2 class="section-header"&gt;Testimonials&lt;/h2&gt;', unsafe_allow_html=True)
    st.markdown("""
         Here's what colleagues and clients have said about working with me.
    """)
    col1, col2 = st.columns(2)
    with col1:
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h4&gt;■■■■■&lt;/h4&gt;
              &lt;p&gt;&lt;i&gt;"John is an exceptional developer who consistently delivers high-quality work.
              His ability to solve complex problems and communicate technical concepts clearly
              makes him a valuable team member."&lt;/i&gt;&lt;/p&gt;
              &lt;p&gt;&lt;strong&gt;- Sarah Johnson&lt;/strong&gt;&lt;br&gt;
              &lt;small&gt;Senior Project Manager, Tech Company Inc.&lt;/small&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h4&gt;■■■■■&lt;/h4&gt;
              &lt;p&gt;&lt;i&gt;"Working with John was a pleasure. He transformed our data analytics system
              and helped us make data-driven decisions. His expertise in both frontend and backend
              development is impressive."&lt;/i&gt;&lt;/p&gt;
              &lt;p&gt;&lt;strong&gt;- Michael Chen&lt;/strong&gt;&lt;br&gt;
              &lt;small&gt;CEO, StartUp Solutions&lt;/small&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
    with col2:
         st.markdown("""
         &lt;div class="project-card"&gt;
              &lt;h4&gt;■■■■■&lt;/h4&gt;
              &lt;p&gt;&lt;i&gt;"John's technical skills are outstanding, but what really sets him apart is
             his dedication to understanding business requirements and delivering solutions that
             truly meet our needs."&lt;/i&gt;&lt;/p&gt;
             &lt;p&gt;&lt;strong&gt;- Emily Rodriguez&lt;/strong&gt;&lt;br&gt;
             &lt;small&gt;Product Owner, Enterprise Corp&lt;/small&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         &lt;div class="project-card"&gt;
             &lt;h4&gt;■■■■■&lt;/h4&gt;
             &lt;p&gt;&lt;i&gt;"As a mentor, John helped me grow tremendously as a developer. His code reviews
             are thorough and educational. I learned more in six months working with him than
             in years on my own."&lt;/i&gt;&lt;/p&gt;
             &lt;p&gt;&lt;strong&gt;- David Kim&lt;/strong&gt;&lt;br&gt;
             &lt;small&gt;Junior Developer, Tech Company Inc.&lt;/small&gt;&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
# Contact Section
with tab6:
    st.markdown('&lt;h2 class="section-header"&gt;Get In Touch&lt;/h2&gt;', unsafe_allow_html=True)
    st.markdown("""
         Let's connect! I'm always open to discussing new projects, creative ideas,
         or opportunities to be part of your vision.
    """)
    col1, col2 = st.columns(2)
    with col1:
         st.markdown("""
         &lt;div class="contact-info"&gt;
             &lt;h3&gt;■ Email&lt;/h3&gt;
             &lt;p&gt;john.doe@email.com&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         &lt;div class="contact-info"&gt;
             &lt;h3&gt;■ LinkedIn&lt;/h3&gt;
             &lt;p&gt;linkedin.com/in/johndoe&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
    with col2:
         st.markdown("""
         &lt;div class="contact-info"&gt;
             &lt;h3&gt;■ GitHub&lt;/h3&gt;
             &lt;p&gt;github.com/johndoe&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
         st.markdown("""
         &lt;div class="contact-info"&gt;
             &lt;h3&gt;■ Website&lt;/h3&gt;
             &lt;p&gt;www.johndoe.com&lt;/p&gt;
         &lt;/div&gt;
         """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Send me a message")
    with st.form("contact_form"):
         name = st.text_input("Your Name")
         email = st.text_input("Your Email")
         message = st.text_area("Message", height=150)
         submitted = st.form_submit_button("Send Message")
         if submitted:
             if name and email and message:
                 success, result_message = send_contact_email(name, email, message)
                 if success:
                     st.session_state.contact_submissions += 1
                     st.success(f"Thank you {name}! Your message has been sent successfully via email. I'll get back
                 else:
                     st.error(f"Failed to send message: {result_message}")
                     if "incomplete" in result_message.lower():
                         st.info("■ To enable email notifications, configure SMTP environment variables (SMTP_SERVER,
                     st.warning("Please contact me directly using the information above.")
             else:
                 st.error("Please fill in all fields before submitting.")
# Analytics Dashboard (visible in sidebar)
with st.sidebar:
    st.markdown("### ■ Analytics Dashboard")
    st.markdown("---")
    st.markdown(f"""
    &lt;div class="analytics-card"&gt;
         &lt;div&gt;■■ Page Views&lt;/div&gt;
         &lt;div class="analytics-number"&gt;{st.session_state.page_views}&lt;/div&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    st.markdown(f"""
    &lt;div class="analytics-card"&gt;
         &lt;div&gt;■ Resume Downloads&lt;/div&gt;
         &lt;div class="analytics-number"&gt;{st.session_state.resume_downloads}&lt;/div&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    st.markdown(f"""
    &lt;div class="analytics-card"&gt;
         &lt;div&gt;✉■ Contact Submissions&lt;/div&gt;
         &lt;div class="analytics-number"&gt;{st.session_state.contact_submissions}&lt;/div&gt;
    &lt;/div&gt;
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Real-time engagement metrics")
# Footer
st.markdown("---")
st.markdown("""
    &lt;div style="text-align: center; color: #666; padding: 2rem 0;"&gt;
         &lt;p&gt;© 2025 John Doe. Built with Python &amp; Streamlit&lt;/p&gt;
    &lt;/div&gt;
""", unsafe_allow_html=True)
