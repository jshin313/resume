#!/usr/bin/python3

import os
import re

def anonymzie(inputfile, outputfile):
    with open(inputfile, "r") as reg_resume:
        reg_resume_txt = reg_resume.read()

    regex = re.compile("Jacob", re.IGNORECASE)
    reg_resume_txt = regex.sub("First", reg_resume_txt)

    regex = re.compile("Shin", re.IGNORECASE)
    reg_resume_txt = regex.sub("Last", reg_resume_txt)

    regex = re.compile("Temple", re.IGNORECASE)
    reg_resume_txt = regex.sub("Some", reg_resume_txt)

    regex = re.compile("313", re.IGNORECASE)
    reg_resume_txt = regex.sub("", reg_resume_txt)

    regex = re.compile("267 393 0368", re.IGNORECASE)
    reg_resume_txt = regex.sub("123 456 7890", reg_resume_txt)

    regex = re.compile("(https:\/\/).[^\s}]*", re.IGNORECASE)
    reg_resume_txt = regex.sub("https://youtu.be/dQw4w9WgXcQ", reg_resume_txt)

    regex = re.compile("Pwn Intended", re.IGNORECASE)
    reg_resume_txt = regex.sub("Random", reg_resume_txt)

    regex = re.compile("Security Innovation", re.IGNORECASE)
    reg_resume_txt = regex.sub("Small Security Company", reg_resume_txt)

    regex = re.compile("Princeton Plasma Physics", re.IGNORECASE)
    reg_resume_txt = regex.sub("DOE", reg_resume_txt)

    regex = re.compile("Princeton", re.IGNORECASE)
    reg_resume_txt = regex.sub("Location", reg_resume_txt)

    regex = re.compile("Philly", re.IGNORECASE)
    reg_resume_txt = regex.sub("Location", reg_resume_txt)

    regex = re.compile("American Water", re.IGNORECASE)
    reg_resume_txt = regex.sub("Company", reg_resume_txt)

    print(reg_resume_txt)

    # Write anonymized output to file
    with open(outputfile, "w") as anon_resume:
        anon_resume.write(reg_resume_txt)

    # Convert tex file to pdf
    os.system("pdflatex " + outputfile + " && rm -f *.aux *.log *.synctex.gz *.out")

    # Convert pdf to png
    os.system("convert -flatten -density 300 " + outputfile.split(".")[0] + ".pdf " +  outputfile.split(".")[0]  +".png")

anonymzie("./jacob_shin.tex", "anon.tex")
anonymzie("./security_resume_jacob_shin.tex", "anon_security_resume.tex")
