---
layout: post
title:  "Code Review"
title:  "What Makes for a Good Code Review?"
date:   2023-05-12 05:00:00 -0700
categories: capstone narratives
---
##### In software development, code review is the process of evaluating the source code of a software project to detect bugs, security vulnerabilities, coding errors, and to ensure that the code adheres to the established coding standards and best practices. In general, code reviews involve inspecting code to ensure it adheres to best practices, coding standards, and security controls. CodeProject states that, “Code review is systematic examination (often known as peer review) of computer source code. It is intended to find and fix mistakes overlooked in the initial development phase, improving both the overall quality of software and the developers’ skills”(Ludovicianul, 2013). During the code review process, the code is typically examined by other developers, who provide feedback and suggestions for improvement. Code review allows for improvements in code organization, code correctness, error handling, security, maintainability, efficiency, scalability, and performance. When creating code for software, it is pointless to exert a lot of effort to produce something that does not work as intended, or which works but is packaged with a lot of unanticipated liabilities. Reviewing the code I write, and integrating the feedback of others, has shown itself to be an essential part of producing quality works. 

##### There are numerous practical benefits to conducting code reviews, including improved code quality, better knowledge sharing among team members, and a reduction of errors and bugs. Code reviews improve code quality, functional correctness, and maintainability while improving the ability to catch errors early in the development process. Neil Daswani, a member of Twitter’s security engineering team said, "When you can solve a problem at the [software design] phase, it automatically solves a bunch of problems later on in the stages… It's very cost-effective to solve security at the design stage" (Higgins, 2014). Before I was properly educated, I attempted to write several programs without reviewing the code. It was only near the completion of the code that I realized I had to scrap the code and start over due to fatal flaws that were now baked into the program. This could have been avoided with the appropriate code review practices. 

##### Code reviews are typically performed before the code is merged or released to production, but can also occur at any time throughout the software development lifecycle. Code reviews can be conducted through various methods, such as pair programming, formal code reviews, lightweight code reviews, and automated testing. I have found that the more complicated a piece of software is, the more it benefits from frequent code review. When a complicated program is written to be modular, it can help to ensure that code review efforts can be similarly compartmentalized. 

##### Some best practices that are important for code review include focusing on high risk parts of the code, reviewing the code logic and algorithms, checking for readability, and adhering to established coding standards. Reviews should be targeted to a manageable quantity of code, should be conducted in a timely manner, and should involve multiple reviewers to both minimize bias and to increase the diversity of constructive feedback. Code review can also benefit from the use of automated code review tools, which help to identify potential issues more quickly and efficiently, while allowing reviewers to more effectively address other issues. Overall, code review works to improve software, developers, and organizational outcomes, making it a vital component of software engineering and development.

Higgins, K. J. (2014, August 27). 10 common software security design flaws. Dark Reading. 	
  https://www.darkreading.com/application-security/10-common-software-security-design-flaws 

Ludovicianul. (2013, January 8). Code review guidelines. CodeProject. 	
  https://www.codeproject.com/Articles/524235/Codeplusreviewplusguidelines 


This site was built using [GitHub Pages](https://pages.github.com/)
You can find the source code for [Jekyll][jekyll-organization] at GitHub



[jekyll-organization]: https://github.com/jekyll
