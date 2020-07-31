import pandas as pa
import numpy as nu
import seaborn as sea
import matplotlib.pyplot as plt
import math
from fpdf import FPDF
import sys

def two_a(stud_cpy):
    plt.subplots(figsize=(20,10))
    sea.countplot(x="Areas of interest",data=stud_cpy)
    plt.xticks(rotation=25)
    plt.savefig('2.a.png')



def two_c(stud_cpy):
    plt.subplots(figsize=(20,10))
    sea.countplot(x="How Did You Hear About This Internship?",data=stud_cpy)
    plt.savefig('2.c.png')

def two_d(stud_cpy):
    df=pa.DataFrame(stud_cpy)
    df1=df[df['Which-year are you studying in?'] == 'Fourth-year']
    df2=df1[df1['CGPA/ percentage'] > 8.0 ]
    plt.subplots(figsize=(20,10))
    sea.countplot(x="Major/Area of Study",data=df2)
    plt.savefig('2.d.png')

def two_e(stud_cpy):
    df=pa.DataFrame(stud_cpy)
    df3=df[df['Areas of interest'] == 'Digital Marketing ']
    df3=df3[df3['Rate your written communication skills [1-10]'] > 8 ]
    df3=df3[df3['Rate your verbal communication skills [1-10]'] > 8 ]
    df3.shape
    plt.subplots(figsize=(20,10))
    sea.countplot(x="Major/Area of Study",data=df3)
    plt.savefig('2.e.png')

def two_f(stud_cpy):
    plt.subplots(figsize=(20,10))
    sea.countplot(x="Major/Area of Study",hue="Which-year are you studying in?",data=stud_cpy)
    plt.savefig('2.f.png')

def two_g(stud_spy):
    plt.subplots(figsize=(20, 10))
    sea.countplot(x="City", hue="Gender", data=stud_cpy)
    plt.savefig('2.g-a.png')
    plt.subplots(figsize=(20, 10))
    sea.countplot(x="College name", hue="Gender", data=stud_cpy)
    plt.savefig('2.g-b.png')

def two_h(stud_cpy):
    plt.subplots(figsize=(10,10))
    sea.scatterplot(x="Label", y="CGPA/ percentage",hue="Gender", data=stud_cpy)
    plt.savefig('2.h.png')

def two_i(stud_cpy):
    plt.subplots(figsize=(20,10))
    sea.countplot(x="Label",hue="Areas of interest", data=stud_cpy)
    plt.savefig('2.i.png')

def two_j(stud_cpy):
    var12=df['Major/Area of Study']
    major_f = df.groupby(['Major/Area of Study', 'Which-year are you studying in?', 'Label'])['Major/Area of Study'].size()[lambda x: x < 1000]
    fig, ax = plt.subplots(figsize=(20, 20))
    major_f = major_f.to_frame()
    major_f.unstack().plot.bar(ax=ax)
    plt.savefig('2.j.png')

def two_b(stud_cpy):
    result=df[df['Areas of interest'] == 'Data Science ']
    rf=result[result['Programming Language Known other than Java (one major)'] == 'Python']
    rf1=result[result['Programming Language Known other than Java (one major)'] != 'Python']
    index_p=rf.index
    index_n=rf1.index
    python=len(index_p)
    not_python=len(index_n)
    Label="Python","Not Python"
    d_count=[python,not_python]
    piecolor=["red","green"]
    explode=(0.1,0.1)
    plt.subplots(figsize=(20,10))
    plt.pie(d_count,explode=explode,labels=Label,colors=piecolor,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.axis('equal')
    plt.savefig("2.b.png")

if __name__ == "__main__":
    stud_cpy = pa.read_csv(sys.argv[1])
    stud_cpy.drop(['Certifications/Achievement/ Research papers'], axis=1, inplace=True)
    stud_cpy.drop(['Link to updated Resume (Google/ One Drive link preferred)'], axis=1, inplace = True)
    stud_cpy.drop("link to Linkedin profile", axis=1, inplace=True)
    df = pa.DataFrame(stud_cpy)
    two_a(stud_cpy)
    two_c(stud_cpy)
    two_d(stud_cpy)
    two_e(stud_cpy)
    two_f(stud_cpy)
    two_g(stud_cpy)
    two_h(stud_cpy)
    two_i(stud_cpy)
    two_j(stud_cpy)
    two_b(stud_cpy)
    pdf_g=FPDF(orientation='L',unit='mm',format='letter')
    imagelist = ["2.a.png", "2.b.png", "2.c.png", "2.d.png", "2.e.png", "2.f.png", "2.g-a.png", "2.g-b.png", "2.h.png",
                 "2.i.png", "2.j.png"]
    textlist = ["2.A No of student applied for Different Technology",
                "2.B Data Science student who knew python and who did not",
                "2.C Different ways student learned about this program",
                "2.D Students who are in 4th year and CGPA >8.0",
                "2.E Digital Marketing Student with Verbal and Written score > 8.0",
                "2.F Year-wise and Area of Study wise Classification of Student",
                "2.G-A City wise classification of student", "2.G-B College wise classification of student",
                "2.H Relationship between CGPA and Label", "2.I Relationship between Area of Interest and Label",
                "2.J Relationship between Year of study, Major and Label"]
for (image,text) in zip(imagelist,textlist):
        pdf_g.add_page()
        pdf_g.set_font("Arial",size=25)
        pdf_g.cell(0,0,txt=text,ln=1,align="C")
        pdf_g.ln(50)
        pdf_g.image(image,x=5,y=20,w=300,h=200)
pdf_g.output("Visualization-Output.pdf")