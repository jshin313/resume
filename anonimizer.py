#!/usr/bin/python3

import re

def anonymzie(inputfile, outputfile):
    with open(inputfile, "r") as reg_resume:
        reg_resume_txt = reg_resume.read()

    regex = re.compile("Jacob", re.IGNORECASE)
    reg_resume_txt = regex.sub("First", reg_resume_txt)

    regex = re.compile("Shin", re.IGNORECASE)
    reg_resume_txt = regex.sub("Last", reg_resume_txt)

    regex = re.compile("Temple", re.IGNORECASE)
    reg_resume_txt = regex.sub("Jawn", reg_resume_txt)

    regex = re.compile("313", re.IGNORECASE)
    reg_resume_txt = regex.sub("", reg_resume_txt)

    regex = re.compile("267 393 0368", re.IGNORECASE)
    reg_resume_txt = regex.sub("123 456 7890", reg_resume_txt)

    regex = re.compile("(https:\/\/).[^\s}]*", re.IGNORECASE)
    reg_resume_txt = regex.sub("https://youtu.be/dQw4w9WgXcQ", reg_resume_txt)

    regex = re.compile("Pwn Intended", re.IGNORECASE)
    reg_resume_txt = regex.sub("Random", reg_resume_txt)

    print(reg_resume_txt)

    with open(outputfile, "w") as anon_resume:
        anon_resume.write(reg_resume_txt)

anonymzie("./jacob_shin.tex", "anon.tex")
anonymzie("./security_resume_jacob_shin.tex", "anon_security_resume.tex")
