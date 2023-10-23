def content(cat,by,to,college):
    content_text = f"""
Dear {to},

I hope this message finds you well. My name is Vardan Mittal, and I am an undergraduate student at the National Institute of Technology (NIT), Surat, India. I am writing to express my keen interest in the possibility of joining your esteemed research group at ETH Zurich for a research internship in the field of Machine Learning and Deep Learning, commencing in January 2024 and extending for a duration of 4 to 6 months.

My journey into the world of machine learning and deep learning has been one filled with excitement and a fervent desire to contribute to innovative research endeavors. I have always been deeply passionate about the potential of these technologies to address complex real-world challenges. Over the years, I have honed my skills and knowledge, particularly in the domains of robotics, mechatronics, and computer vision.

One of the most significant projects I have undertaken is in the realm of robotics and mechatronics. I had the privilege of designing and implementing an autonomously navigating robot, leveraging Visual Simultaneous Localization and Mapping (VSLAM) algorithms and computer vision techniques. This project was a testament to my commitment to applying machine learning concepts in practical applications and demonstrated my ability to integrate cutting-edge technology into physical systems.

In addition to my robotics work, I have also gained substantial experience in data analysis and automation. Proficient in programming languages such as Python, C, C++, JavaScript, SQL, and MATLAB, I have utilized these tools to analyze data and create automation scripts. My familiarity with Selenium Web Drivers has enabled me to engage in web scraping and various automation tasks, further enhancing my skill set.

I have attached my resume and cover letter to provide you with a comprehensive overview of my qualifications and experiences, which I believe align well with the research activities at ETH Zurich. While my academic pursuits have focused on electronics and communication engineering, my true passion lies in the practical applications of machine learning and deep learning.

I respectfully request your consideration for an internship opportunity within your research group. I believe that the experience I would gain at ETH Zurich under your mentorship would be invaluable in my academic and research journey. Your guidance would provide me with the opportunity to contribute meaningfully to ongoing projects while furthering my understanding of the intricate world of machine learning and deep learning.

Thank you for your time and consideration.

Warm regards,

{by}
"""
    content_html = f"""\
        <html>
            <body>
                <p align=justify>
                    Dear <strong>{to}</strong>,<br>
<br>
I hope this message finds you well. My name is Vardan Mittal, and I am an undergraduate student at the <strong>National Institute of Technology (NIT), Surat, India</strong>. I am writing to express my keen interest in the possibility of joining your esteemed research group at {college} for a research internship in the field of <strong>Machine Learning and Deep Learning</strong>, commencing in January 2024 and extending for a duration of 4 to 6 months.<br>
<br>

My journey into the world of machine learning and deep learning has been one filled with excitement and a fervent desire to contribute to innovative research endeavors. I have always been deeply passionate about the potential of these technologies to address complex real-world challenges. Over the years, I have honed my skills and knowledge, particularly in the domains of robotics, mechatronics, and computer vision.<br>
<br>

One of the most significant projects I have undertaken is in the realm of robotics and mechatronics. I had the privilege of designing and implementing an autonomously navigating robot, leveraging <strong>Visual Simultaneous Localization and Mapping (VSLAM) algorithms</strong> and <strong>computer vision</strong> techniques. This project was a testament to my commitment to applying machine learning concepts in practical applications and demonstrated my ability to integrate cutting-edge technology into physical systems.<br>
<br>

In addition to my robotics work, I have also gained substantial experience in data analysis and automation. Proficient in programming languages such as<strong> Python, C, C++, JavaScript, SQL, and MATLAB</strong>, I have utilized these tools to analyze data and create automation scripts. My familiarity with Selenium Web Drivers has enabled me to engage in web scraping and various automation tasks, further enhancing my skill set.<br>
<br>

I have attached my resume and cover letter to provide you with a comprehensive overview of my qualifications and experiences, which I believe align well with the research activities at {college}. While my academic pursuits have focused on electronics and communication engineering, my true passion lies in the practical applications of machine learning and deep learning.<br>
<br>

I respectfully request your consideration for an internship opportunity within your research group. I believe that the experience I would gain at {college} under your mentorship would be invaluable in my academic and research journey. Your guidance would provide me with the opportunity to contribute meaningfully to ongoing projects while furthering my understanding of the intricate world of machine learning and deep learning.<br>
<br>

Thank you for your time and consideration.<br>
<br>

Warm regards,<br>
{by}
                </p>
            </body>
        </html>
    """
    
    if(cat == "Text"):
        return content_text
    else:
        return content_html
