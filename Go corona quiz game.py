#------------------------------------------------------Imported libraries----------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pygame
from pygame.locals import *
from functools import partial

#-----------------------------------------------------main_application window---------------------------------------------------------------------------------------
FPS=32
SCREENWIDTH=750
SCREENHEIGHT=500
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
Instructions="Images_used\game_instructions.jpg"
pygame.init()
FPSCLK=pygame.time.Clock()
pygame.display.set_caption('GO CORONA QUIZ GAME INSTRUCTIONS WINDOW')
instruction_img=pygame.image.load(Instructions).convert_alpha()
SCREEN.blit(instruction_img,(0,0))
pygame.display.update()
FPSCLK.tick(FPS)
running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            running=False



main_application=tk.Tk()
main_application.geometry('1352x675+0+0')
main_application.title('GO CORONA QUIZ GAME')
main_application.configure(bg='green')
main_application.wm_iconbitmap("icon_quiz_game.ico")
pygame.init()

#------------------------------------------------------Frames added to the window--------------------------------------------------------------------------------------
#1)quiz frame
quiz_frame=tk.Frame(main_application,bg='orange',width=900,height=669)
quiz_frame.grid(row=0,column=0,sticky=tk.N)
#2)result_frame
result_frame=tk.Frame(main_application,bg='#d50000',width=460,height=674)
result_frame.grid(row=0,column=1,sticky=tk.N)
#frames on quiz frame
#1)Facility frame
facility_frame=tk.Frame(quiz_frame,bg='orange',width=900,height=200)
facility_frame.grid(row=0,column=0,padx=0,pady=0,sticky=tk.W)
#2)Corona display frame
corona_frame=tk.Frame(quiz_frame,bg='white',width=900,height=200)
corona_frame.grid(row=1,column=0,padx=0,pady=0,sticky=tk.W)
#3)question frame
question_frame=tk.Frame(quiz_frame,bg='green',width=900,height=200)
question_frame.grid(row=2,column=0,padx=0,pady=0,sticky=tk.W)


if __name__ == "__main__":

#---------------------------------------------pygame window----------------------------------------------------------------------------------------------------------
   


#--------------------------------------sounds----------------------------------------------------------------------------------------------------------------------
    score_music=pygame.mixer.Sound("Music used\score.wav")
    oops_music=pygame.mixer.Sound("Music used\oops.wav")
    next_button_music=pygame.mixer.Sound("Music used\\next_button.wav")
    lifeline_music=pygame.mixer.Sound("Music used\lifeline.wav")
    
#---------------------------------------------------------Game Design for result frame---------------------------------------------------------------------------
#Image for Game score
    game_score_img=ImageTk.PhotoImage(Image.open("Images_used\score.jpg"))
    canvas=tk.Canvas(result_frame,bg='yellow',width=300,height=100)
    canvas.grid(row=0,column=0,padx=77,pady=10)
    canvas.delete('all')
    canvas.create_image(152,52,image=game_score_img)
    canvas.image=game_score_img

#Entry box for score
    score_var=tk.IntVar()
    score_entry=tk.Entry(result_frame,textvariable=score_var,font=("Times", "24", "bold italic"),bg='#d50000',fg='white',bd=5,width=7)
    score_entry.grid(row=1,column=0,padx=0,pady=0)


#-----------------------------------------------------------function for calculation of score--------------------------------------------------------------------------------
    def score(count=[0]):
        if count[0]==0:
            score_var.set(10)
            score_value=score_var.get()
        elif count[0]==1:
            score_var.set(30)
            score_value=score_var.get()
        elif count[0]==2:
            score_var.set(90)
            score_value=score_var.get()
        elif count[0]==3:
            score_var.set(270)
            score_value=score_var.get()
        elif count[0]==4:
            score_var.set(810)
            score_value=score_var.get()
        elif count[0]==5:
            score_var.set(810*3)
            score_value=score_var.get()
        elif count[0]==6:
            score_var.set(810*3*3)
            score_value=score_var.get()
        elif count[0]==7:
            score_var.set(810*3*3*3)
            score_value=score_var.get()
        elif count[0]==8:
            score_var.set(810*3**4)
            score_value=score_var.get()
        elif count[0]==9:
            score_var.set(810*3**5)
            score_value=score_var.get()
        count[0]+=1
        return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#image for high score
    high_score_img=ImageTk.PhotoImage(Image.open("Images_used\high_score.jpg"))
    canvas=tk.Canvas(result_frame,bg='yellow',width=195,height=50)
    canvas.grid(row=2,column=0,padx=0,pady=10)
    canvas.delete('all')
    canvas.create_image(100,27,image=high_score_img)
    canvas.image=high_score_img

#For by default display of highscore
with open('Text\highscore.txt','r') as rf:
    display_highscore=int(rf.read())

#Entry box for high score
    highscore_var=tk.IntVar()
    highscore_var.set(display_highscore)
    high_score_entry=tk.Entry(result_frame,textvariable=highscore_var,font=("Times", "24", "bold italic"),bg='#d50000',fg='white',bd=5,width=7)
    high_score_entry.grid(row=3,column=0,pady=10)

#Functions for development of high score
    def get_highscore():
        try:
            with open('Text\highscore.txt','r') as rf:
                highscore=int(rf.read())
        except:
            return
        return highscore

    def save_highscore(new_high_score):
        try:
            with open('Text\highscore.txt','w') as wf:
                high_score=wf.write(str(new_high_score))
        except:
            return

#Image for audience poll
    audience_poll_img=ImageTk.PhotoImage(Image.open("Images_used\Audience_poll.png"))
    canvas=tk.Canvas(result_frame,bg='yellow',width=300,height=60)
    canvas.grid(row=4,column=0,padx=0,pady=0)
    canvas.delete('all')
    canvas.create_image(152,32,image=audience_poll_img)
    canvas.image=audience_poll_img

#Entry box for audience poll
    audiencepoll_var=tk.StringVar()
    audiencepoll_entry=tk.Entry(result_frame,textvariable=audiencepoll_var,font=("Times", "22", "bold italic"),bg='#d50000',fg='white',bd=5,width=26)
    audiencepoll_entry.grid(row=5,column=0,padx=0,pady=10)

#Image for phone a friend
    phone_a_friend_img=ImageTk.PhotoImage(Image.open("Images_used\phone_a_friend.jpg"))
    canvas=tk.Canvas(result_frame,bg='yellow',width=200,height=32)
    canvas.grid(row=6,column=0,padx=0,pady=0)
    canvas.delete('all')
    canvas.create_image(102,18,image=phone_a_friend_img)
    canvas.image=phone_a_friend_img

#Entry box for phone a friend
    phoneafriend_var=tk.StringVar()
    phoneafriend_entry=tk.Entry(result_frame,textvariable=phoneafriend_var,font=("Times", "22", "bold italic"),bg='#d50000',fg='white',bd=5,width=26)
    phoneafriend_entry.grid(row=7,column=0,padx=0,pady=10)

#Image for check answer
    check_img=ImageTk.PhotoImage(Image.open("Images_used\check.png"))
    canvas=tk.Canvas(result_frame,bg='yellow',width=300,height=65)
    canvas.grid(row=8,column=0,padx=0,pady=0)
    canvas.delete('all')
    canvas.create_image(152,34,image=check_img)
    canvas.image=check_img

#Entry box for check answer
    check_var=tk.StringVar()
    check_entry=tk.Entry(result_frame,textvariable=check_var,font=("Times", "22", "bold italic"),bg='#d50000',fg='white',bd=5,width=17)
    check_entry.grid(row=9,column=0,padx=0,pady=9)

#------------------------------------Question, Answers,Correct answers-------------------------------------------------------------------------------------------------
#Questions
    question1=tk.StringVar()
    question1.set('What are the main symptoms of someone infected with coronavirus?')

    question2=tk.StringVar()
    question2.set('Which of the following diseases are releated to coronavirus?')

    question3=tk.StringVar()
    question3.set('From where corona virus got its name?')

    question4=tk.StringVar()
    question4.set('What are the precautions that need to be taken to protect from the coronavirus?')

    question5=tk.StringVar()
    question5.set('The first case of novel coronavirus was identified in....')

    question6=tk.StringVar()
    question6.set('On which logic Aarogya setu app(By Govt.) work?')

    question7=tk.StringVar()
    question7.set('Coronavirus stays in ______ for Hours,_____for days')

    question8=tk.StringVar()
    question8.set('How long will coronavirus survive in the air around you?')

    question9=tk.StringVar()
    question9.set('Why it is advised to drink normal warm water to protect feom corona virus upto some extent?')

    question10=tk.StringVar()
    question10.set('How long is the most estimates of incubation period for covid-19?')

#Answers
    #answer1
    answer1_A=tk.StringVar()
    answer1_A.set('FEVER')
    answer1_B=tk.StringVar()
    answer1_B.set('COUGH')
    answer1_C=tk.StringVar()
    answer1_C.set('Shortness OF Breath')
    answer1_D=tk.StringVar()
    answer1_D.set('ALL OF THE ABOVE')

    correct_1=tk.StringVar()
    correct_1.set('ALL OF THE ABOVE')

    #answer2
    answer2_A=tk.StringVar()
    answer2_A.set('MERS')
    answer2_B=tk.StringVar()
    answer2_B.set('SARS')
    answer2_C=tk.StringVar()
    answer2_C.set('Both A and B')
    answer2_D=tk.StringVar()
    answer2_D.set('Neither A nor B')

    correct_2=tk.StringVar()
    correct_2.set('Both A and B')

    #answer3
    answer3_A=tk.StringVar()
    answer3_A.set('Due to their crown like projections')
    answer3_B=tk.StringVar()
    answer3_B.set('Due to their leaf like projections')
    answer3_C=tk.StringVar()
    answer3_C.set('Due to their surface structure of bricks')
    answer3_D=tk.StringVar()
    answer3_D.set('NONE OF THESE')

    correct_3=tk.StringVar()
    correct_3.set('Due to their crown like projections')

    #answer4
    answer4_A=tk.StringVar()
    answer4_A.set('Add more garlic into your diet')
    answer4_B=tk.StringVar()
    answer4_B.set('Cover your nose and mouth when sneezing')
    answer4_C=tk.StringVar()
    answer4_C.set('Visit your doctor for antibiotic')
    answer4_D=tk.StringVar()
    answer4_D.set('Wash your hands after every hour')

    correct_4=tk.StringVar()
    correct_4.set('Cover your nose and mouth when sneezing')

    #answer5
    answer5_A=tk.StringVar()
    answer5_A.set('BEIJING')
    answer5_B=tk.StringVar()
    answer5_B.set('SHANGHAI')
    answer5_C=tk.StringVar()
    answer5_C.set('WUHAN,HUBEI')
    answer5_D=tk.StringVar()
    answer5_D.set('TIANJIN')

    correct_5=tk.StringVar()
    correct_5.set('WUHAN,HUBEI')

    #answer6
    answer6_A=tk.StringVar()
    answer6_A.set('Based on Machine learning model')
    answer6_B=tk.StringVar()
    answer6_B.set('Based on Scanning')
    answer6_C=tk.StringVar()
    answer6_C.set('Based on comparison of testing set with training set data')
    answer6_D=tk.StringVar()
    answer6_D.set('Both A and C are correct')

    correct_6=tk.StringVar()
    correct_6.set('Both A and C are correct')

    #answer7
    answer7_A=tk.StringVar()
    answer7_A.set('Water,Aerosols')
    answer7_B=tk.StringVar()
    answer7_B.set('Alchols,vinegar')
    answer7_C=tk.StringVar()
    answer7_C.set('Aerosols,Surfaces')
    answer7_D=tk.StringVar()
    answer7_D.set('Vegetables,Air')

    correct_7=tk.StringVar()
    correct_7.set('Aerosols,Surfaces')

    #answer8
    answer8_A=tk.StringVar()
    answer8_A.set('one hour')
    answer8_B=tk.StringVar()
    answer8_B.set('Two hour')
    answer8_C=tk.StringVar()
    answer8_C.set('Zero hour')
    answer8_D=tk.StringVar()
    answer8_D.set('Half-hour')

    correct_8=tk.StringVar()
    correct_8.set('Half-hour')

    #answer9
    answer9_A=tk.StringVar()
    answer9_A.set('Corona virus can\'t witthstand that temperature ')
    answer9_B=tk.StringVar()
    answer9_B.set('For easy movement of corona virus to stomach')
    answer9_C=tk.StringVar()
    answer9_C.set('Both A and B are correct')
    answer9_D=tk.StringVar()
    answer9_D.set('None of these')

    correct_9=tk.StringVar()
    correct_9.set('For easy movement of corona virus to stomach')

    #answer10
    answer10_A=tk.StringVar()
    answer10_A.set('1-14 days')
    answer10_B=tk.StringVar()
    answer10_B.set('1-5 days')
    answer10_C=tk.StringVar()
    answer10_C.set('1-2 days')
    answer10_D=tk.StringVar()
    answer10_D.set('All of the above')

    correct_10=tk.StringVar()
    correct_10.set('1-14 days')

    questions=[question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]
    answers_A=[answer1_A,answer2_A,answer3_A,answer4_A,answer5_A,answer6_A,answer7_A,answer8_A,answer9_A,answer10_A]
    answers_B=[answer1_B,answer2_B,answer3_B,answer4_B,answer5_B,answer6_B,answer7_B,answer8_B,answer9_B,answer10_B]
    answers_C=[answer1_C,answer2_C,answer3_C,answer4_C,answer5_C,answer6_C,answer7_C,answer8_C,answer9_C,answer10_C]
    answers_D=[answer1_D,answer2_D,answer3_D,answer4_D,answer5_D,answer6_D,answer7_D,answer8_D,answer9_D,answer10_D]

    correct=[correct_1,correct_2,correct_3,correct_4,correct_5,correct_6,correct_7,correct_8,correct_9,correct_10]

#----------------------------------------------play national anthem----------------------------------------------------------------------------------------------------------
    def national_anthem(count=[0]):
        Peaceful_sound=pygame.mixer.Sound("Music used\instrumental.wav")
        if count[0]==0:
            Peaceful_sound.play()
            check_var.set('Stay home,Stay safe')
            count[0]=count[0]+1
#----------------------------------------Disable and Enable buttons functions------------------------------------------------------------------------------------------------   
    def disable(button):
        button['state']='disabled'

    
    def enable(button):
        button['state']='active'
#---------------------------------------------------Virtual lifelines for quiz------------------------------------------------------------------------------------------------
    def change_50_50_lifeline():
        lifeline_music.play()
        #for removing 50 50 lifeline
        canvas=tk.Canvas(facility_frame,bg='orange',width=200,height=150)
        canvas.grid(row=0,column=0,padx=45,pady=28)
        canvas.delete('all')
        Img_50=ImageTk.PhotoImage(Image.open("Images_used\\50_50_1.jpg"))
        canvas.create_image(101,77,image=Img_50)
        canvas.image=Img_50
        #for removing two options


    def change_audience_poll():
        lifeline_music.play()
        canvas=tk.Canvas(facility_frame,bg='orange',width=200,height=150)
        canvas.grid(row=0,column=1,padx=45,pady=28)
        canvas.delete('all')
        Img_50=ImageTk.PhotoImage(Image.open("Images_used\Audience_1.jpg"))
        canvas.create_image(101,77,image=Img_50)
        canvas.image=Img_50
        #tell the answer to player

    def change_phone_a_friend():
        lifeline_music.play()
        canvas=tk.Canvas(facility_frame,bg='orange',width=200,height=150)
        canvas.grid(row=0,column=2,padx=45,pady=28)
        canvas.delete('all')
        Img_50=ImageTk.PhotoImage(Image.open("Images_used\phone_1.jpg"))
        canvas.create_image(101,77,image=Img_50)
        canvas.image=Img_50
        #tell the answer to player

    #---------------------------------------------------- Functions for choosing correct answers------------------------------------------------------------------------------
    def Answer_A(question_no_selected,correct,answers_A):
        if answers_A[question_no_selected].get()==correct[question_no_selected].get():
            label_A_button.configure(bg='#00e676')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Correct Answer')
            score()
            score_music.play()
            #sound_play
        elif answers_A[question_no_selected].get()!=correct[question_no_selected].get():
            label_A_button.configure(bg='red')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Incorrect Answer')
            oops_music.play()


    def Answer_B(question_no_selected,correct,answers_B):
        if answers_B[question_no_selected].get()==correct[question_no_selected].get():
            label_B_button.configure(bg='#00e676')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Correct Answer')
            score()
            score_music.play()
            #sound_play
        elif answers_B[question_no_selected].get()!=correct[question_no_selected].get():
            label_B_button.configure(bg='red')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Incorrect Answer')
            oops_music.play()

    def Answer_C(question_no_selected,correct,answers_C):
        if answers_C[question_no_selected].get()==correct[question_no_selected].get():
            label_C_button.configure(bg='#00e676')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Correct Answer')
            score()
            score_music.play()
            #sound_play
        elif answers_C[question_no_selected].get()!=correct[question_no_selected].get():
            label_C_button.configure(bg='red')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Incorrect Answer')
            oops_music.play()

    def Answer_D(question_no_selected,correct,answers_D):
        if answers_D[question_no_selected].get()==correct[question_no_selected].get():
            label_D_button.configure(bg='#00e676')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Correct Answer')
            score()
            score_music.play()
            #sound_play
        elif answers_D[question_no_selected].get()!=correct[question_no_selected].get():
            label_D_button.configure(bg='red')
            disable(label_A_button)
            disable(label_B_button)
            disable(label_C_button)
            disable(label_D_button)
            check_var.set('Incorrect Answer')
            oops_music.play()

#-------------------------------------------------------Start the quiz--------------------------------------------------------------------------------------------------------    
#--------------------------------------------------Entry boxes,text,buttons of LOWER GREEN PORTION OF FLAG----------------------------------------------------------------
    #Entry box for Questions
    
    question_no_selected=0
    print(question_no_selected)
    ques_entry=tk.Entry(question_frame,font=('Helvetica',14,),bg='Green',fg='white',bd=5,width=70,textvariable=questions[question_no_selected])
    ques_entry.grid(row=0,column=0,padx=62,pady=15)

    label_A=tk.Label(question_frame,font=('arial',14,'bold'),text='A: ',bg='green',fg='white')
    label_A.grid(row=1,column=0,padx=60,pady=5,sticky=tk.W)
    label_A_button=tk.Button(question_frame,font=('arial',14,'bold'),bg='Green',fg='white',bd=1,width=60,height=1,textvariable=answers_A[question_no_selected],command=partial(Answer_A,question_no_selected,correct,answers_A))
    label_A_button.grid(row=1,column=0,padx=90,pady=5)

    label_B=tk.Label(question_frame,font=('arial',14,'bold'),text='B: ',bg='green',fg='white')
    label_B.grid(row=2,column=0,padx=60,pady=5,sticky=tk.W)
    label_B_button=tk.Button(question_frame,font=('arial',14,'bold'),bg='Green',fg='white',bd=1,width=60,height=1,textvariable=answers_B[question_no_selected],command=partial(Answer_B,question_no_selected,correct,answers_B))
    label_B_button.grid(row=2,column=0,padx=90,pady=5)

    label_C=tk.Label(question_frame,font=('arial',14,'bold'),text='C: ',bg='green',fg='white')
    label_C.grid(row=3,column=0,padx=60,pady=5,sticky=tk.W)
    label_C_button=tk.Button(question_frame,font=('arial',14,'bold'),bg='Green',fg='white',bd=1,width=60,height=1,textvariable=answers_C[question_no_selected],command=partial(Answer_C,question_no_selected,correct,answers_C))
    label_C_button.grid(row=3,column=0,padx=90,pady=5)

    label_D=tk.Label(question_frame,font=('arial',14,'bold'),text='D: ',bg='green',fg='white')
    label_D.grid(row=4,column=0,padx=60,pady=5,sticky=tk.W)
    label_D_button=tk.Button(question_frame,font=('arial',14,'bold'),bg='Green',fg='white',bd=1,width=60,height=1,textvariable=answers_D[question_no_selected],command=partial(Answer_D,question_no_selected,correct,answers_D))
    label_D_button.grid(row=4,column=0,padx=90,pady=5)
    #-----------------------------------------------------------move the quiz forward-------------------------------------------------------------------------------
     #For moving game forward
    def next_ques(answers_A,answers_B,answers_C,answers_4,questions,correct,count=[1]):
        next_button_music.play()
        if count[0]<=9:
            question_no_selected=count[0]
            enable(label_A_button)
            enable(label_B_button)
            enable(label_C_button)
            enable(label_D_button)
            label_A_button.configure(bg='green',textvariable=answers_A[question_no_selected],command=partial(Answer_A,question_no_selected,correct,answers_A))
            label_B_button.configure(bg='green',textvariable=answers_B[question_no_selected],command=partial(Answer_B,question_no_selected,correct,answers_B))
            label_C_button.configure(bg='green',textvariable=answers_C[question_no_selected],command=partial(Answer_C,question_no_selected,correct,answers_C))
            label_D_button.configure(bg='green',textvariable=answers_D[question_no_selected],command=partial(Answer_D,question_no_selected,correct,answers_D))
            ques_entry.configure(textvariable=questions[question_no_selected])
        
    #For updating the high score
        if count[0]==10:
            def main_highscore():
                previous_score=get_highscore()
                current_score=score_var.get()
                if current_score>previous_score:
                    save_highscore(current_score)
                return get_highscore()
            highscore_var.set(main_highscore())
        count[0]+=1
        return count[0]
    #---------------------------------BUTTONS OF MIDDLE WHITE PORTION OF FLAG------------------------------------------------------------
    #Family with mask protection button
    left_img=ImageTk.PhotoImage(Image.open("Images_used\Go_corona_1.png"))
    left_img_button=tk.Button(corona_frame,image=left_img,bg='white',bd=3,width=200,height=150,command=partial(next_ques,answers_A,answers_B,answers_C,answers_D,questions,correct))
    left_img_button.grid(row=0,column=0,padx=47,pady=25)
    #Ashok chakra button addition to corona display frame
    center_img=ImageTk.PhotoImage(Image.open("Images_used\\ashoka_chakra.png"))
    center_img_button=tk.Button(corona_frame,image=center_img,bg='white',bd=3,width=200,height=150,command=national_anthem)
    center_img_button.grid(row=0,column=1,padx=47,pady=25)
    #Earth with mask protection button
    right_img=ImageTk.PhotoImage(Image.open("Images_used\Go_corona_2.png"))
    right_img_button=tk.Button(corona_frame,image=right_img,bg='white',bd=3,width=200,height=150,command=partial(next_ques,answers_A,answers_B,answers_C,answers_D,questions,correct))
    right_img_button.grid(row=0,column=2,padx=48,pady=25)

    
    #------------------------------BUTTONS OF UPPER ORANGE PORTION OF FLAG-----------------------------------------------------------------
    fifty_img=ImageTk.PhotoImage(Image.open("Images_used\\50_50.jpg"))
    fifty_img_button=tk.Button(facility_frame,image=fifty_img,bg='orange',bd=3,width=200,height=150,command=change_50_50_lifeline)
    fifty_img_button.grid(row=0,column=0,padx=45,pady=28)

    audience_img=ImageTk.PhotoImage(Image.open("Images_used\Audience.jpg"))
    audience_img_button=tk.Button(facility_frame,image=audience_img,bg='orange',bd=3,width=200,height=150,command=change_audience_poll)
    audience_img_button.grid(row=0,column=1,padx=45,pady=28)

    phone_img=ImageTk.PhotoImage(Image.open("Images_used\phone.jpg"))
    phone_img_button=tk.Button(facility_frame,image=phone_img,bg='orange',bd=3,width=200,height=150,command=change_phone_a_friend)
    phone_img_button.grid(row=0,column=2,padx=45,pady=28)

    #mainloop
    main_application.mainloop()
    #----------------------------------------------------------------Finished-------------------------------------------------------------------
