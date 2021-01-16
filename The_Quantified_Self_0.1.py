###############################################################
# 
# Written by Chris Karwin, December 25, 2020; Clemson University
#
# The Quantified Self
#  Optimizing health by learning from the past
# 
###############################################################

#########################
#!/usr/bin/env python
#imports
import PySimpleGUI as sg
import os,sys
import pandas as pd
import numpy as np
import datetime
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#########################

#register new user:
def Register_User():

    ################################
    #define defaults:
    
    value_list = ['sleep','read','mindfulness','work',\
            'yoga','gym','diet','restraint',\
            'steps','water','weight','body fat','BMI']

    unit_list = ["hr","min","min","hr","0/1","0/1","0/1","0/1","count","oz","lb","%","count"]

    #path to iCloud drive:
    #update_main = ["NA"]
    update_main = "/Users/chriskarwin/Library/Mobile Documents/iCloud~com~ifunography~HealthExport/Documents/"
    
    #synce value list:
    synce_value_list = ["water","steps","mindfulness","weight","sleep"]


    ###############################

    #get info for returning user:
    if os.path.exists("My_Info/info.txt")==True:
    
        f = open("My_Info/info.txt","r")
        info_dict = eval(f.read())
        username=info_dict["username"]
        value_list = info_dict["value_list"]
        unit_list = info_dict["unit_list"]
        update_main = info_dict["synce_path"]
        synce_value_list = info_dict["synce_list"]

        return username, value_list, unit_list, update_main, synce_value_list

    #register new user:
    if os.path.exists("My_Info/info.txt")==False:

        if os.path.exists("My_Info")==False:
        
            os.system("mkdir My_Info")
    
        layout = [
        [sg.Text('Welcome to The Quantified Self!', font=("Times",35))],
        [sg.Text('Please register below\n\n', font=("Times",20))],
        [sg.Text('Name:',size=(10, 1),font=("Times",25)), sg.InputText(size=(25, 1.5), font=("Times",25))],
        [sg.Text("\n\n")],
        [sg.Text('The inputs below are optional', font=("Times",25))],
        [sg.Text('If nothing is entered the defaults will be used', font=("Times",25))],
        [sg.Text('When entering a list, the values must be separated by commas\n', font=("Times",25))],
        [sg.Text('Enter the values to track and corresponding units\n', font=("Times",25))],
        [sg.Text('Value List:',size=(10, 1),font=("Times",25)), sg.InputText(size=(25, 1.5), font=("Times",25))],
        [sg.Text('Unit List:',size=(10, 1),font=("Times",25)), sg.InputText(size=(25, 1.5), font=("Times",25))],
        [sg.Text("\n")],
        [sg.Text('Enter the full path to your exported data\n', font=("Times",25))],
        [sg.Text('Synce Path:',size=(10, 1),font=("Times",25)), sg.InputText(size=(25, 1.5), font=("Times",25))],
        [sg.Text("\n")],
        [sg.Text('Enter the values that you want to synce with your exported data', font=("Times",25))],
        [sg.Text('(these must be contained in the value list)\n', font=("Times",25))],
        [sg.Text('Synce List:',size=(10, 1),font=("Times",25)), sg.InputText(size=(25, 1.5), font=("Times",25))],
        [sg.Text("\n")],
        [sg.Submit(size=(12,1.5), font=("Times",15)), \
                sg.Cancel(size=(12, 1.5), font=("Times",15))]]

        window = sg.Window('Window Title', layout)

        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                sys.exit()
        
            if event == "Submit":

                #get username:
                username = str(values[0])

                #get value list:
                value_string = values[1]
                if value_string:
                    new_value_list = value_string.split(",")
                    new_value_list = np.char.strip(new_value_list)
                    value_list = new_value_list.tolist()
                    
                #get corresponding units:
                unit_string = values[2]
                if unit_string:
                    new_unit_list = unit_string.split(",")
                    new_unit_list = np.char.strip(new_unit_list)
                    unit_list = new_unit_list.tolist()
                    
                if value_string and len(str(unit_string)) == 0:
                    unit_list = ["NA"]*len(value_list)

                #get synce path:
                this_synce_path = values[3]
                if this_synce_path:
                    update_main = this_synce_path

                #get synce value:
                this_synce_list = values[4]
                if this_synce_list:
                    synce_value_list = this_synce_list

                d = {"username":username, "value_list":value_list, "unit_list":unit_list, "synce_path":update_main, "synce_list":synce_value_list}
                f = open("My_Info/info.txt","w")
                f.write(str(d))
                f.close()

                window.close()

                return username, value_list, unit_list, update_main, synce_value_list

############### Start Initial Setup ###############

#set GUI theme:
sg.theme('LightGrey6')

#register user:
username, value_list, unit_list, update_main, synce_value_list  = Register_User()

#get today:
today = date.today()
today_print = today.strftime("%B %d, %Y")
month = today.month
year = today.year
day = today.day
    
#get tomorrow:
tomorrow = today + datetime.timedelta(days = 1)

#default for main eval list:
eval_list = ["Physical Health","Mental Health","Spiritual Health","Happiness"]

#define synce values:
update_path = os.path.join(update_main,str(year),str(today.strftime("%B")),str(today),"")

#get sync info:
sync_df = pd.read_csv("sync.csv")
code_name = sync_df["name"]
sync_name = sync_df["sync_name"]
sync_col_name = sync_df["col_name"]

synce_value_list = np.array(synce_value_list)
file_root = "-" + str(today) + ".csv"

#setup data directory:
if os.path.exists("My_Data")==False:
    os.system("mkdir My_Data")

this_file = "My_Data/mydata.dat" 
if os.path.exists(this_file) == False:
        
    #write main data frame:
    d_input = {"date":today}
    for i in range(0,len(value_list)):
        d_input[value_list[i]] = ""
    df = pd.DataFrame(data=d_input,index=[0])
    df.to_csv("%s" %this_file,index=False, sep=",")

this_file = "My_Data/myeval.dat"
if os.path.exists(this_file) == False:
        
    #write main data frame:
    d_input = {"date":today}
    for i in range(0,len(eval_list)):
        d_input[eval_list[i]] = 0
    df = pd.DataFrame(data=d_input,index=[0])
    df.to_csv("%s" %this_file,index=False, sep=",")

############### End Initial Setup ###############
    

#Main Program Window & Event Loop 
def create_main_window():
    
    #main window:
    layout = [[sg.Text('The Quantified Self',font=("Times",65))],
            [sg.Text('Optimizing health by learning from the past\n',font=("Times",25))],
            [sg.Text('Welcome %s' %username,font=("Times",45))],
            [sg.Text('Today is %s\n' %str(today_print),font=("Times",45))],
            [sg.Text('What would you like to do?',font=("Times",35))],
            [sg.B("Input Data", size=(14,1.5), font=("Times",15)), \
                    sg.B("Evaluate Self", size=(14,1.5), font=("Times",15)), \
                    sg.B("Self-Reflection", size=(14,1.5), font=("Times",15)), \
                    sg.B('Exit', size=(14,1.5), font=("Times",15))]]

    return sg.Window('Main Application', layout)

#main program:
def main():

    window = None

    while True:
        if window is None:
            window = create_main_window()

        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    
        if event == "Input Data":
            Input_Data()

        if event == "Self-Reflection":
            Self_Reflection()

        if event == "Evaluate Self":
            Evaluate_Self()

    window.close()

#enter input data:
def Input_Data():

    layout_list = []
    layout_list.append([sg.Text("Today's Data", font=("Times",45))])
    for j in range(0,len(value_list)):

        each = value_list[j]
        unit = unit_list[j]

        #user input data:
        if each not in synce_value_list:

            layout_list.append([sg.Text('%s (%s)' %(each,unit), size=(22, 1), font=("Times",35)), sg.InputText(size=(8, 1), font=("Times",25))])
    
        #automatic data:
        if each in synce_value_list:
           
            try: 
                #get auto data:
                update_index = code_name == each
                update_df_file = update_path + sync_name[update_index] + file_root
                update_df = pd.read_csv(update_df_file.tolist()[0])
                update_value = np.sum(update_df[sync_col_name[update_index].tolist()[0]])
                update_value = "{:.1f}".format(update_value)

            except:
                update_value = ""
            
            layout_list.append([sg.Text('%s (%s)' %(each,unit), size=(22, 1), font=("Times",35)), sg.InputText(update_value,size=(8, 1), font=("Times",25))])

    layout_list.append([sg.Submit(size=(14,1.5), font=("Times",15)), sg.Cancel(size=(14, 1.5), font=("Times",15))])

    #define main layout:
    layout = layout_list

    window = sg.Window('Input Data', layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break

        if event == "Submit":

            #upload main data frame:
            this_file = "My_Data/mydata.dat" 
            df = pd.read_csv(this_file)

            #add input data:
            d_input = {"date":today}
            for i in range(0,len(value_list)):
                d_input[value_list[i]] = values[i]
            
            df_input = pd.DataFrame(data=d_input,index=[0])

            #get last entry:
            entry_date = df["date"]
            last_entry = str(entry_date[entry_date.size-1])
            
            if last_entry == str(today):
            
                #drop last entry if today:
                df = df.drop(axis=0,index=entry_date.size-1)
            
            #update main data frame
            df_new = df.append(d_input,ignore_index=True)
            df_new.to_csv(this_file,index=False, sep=",", )

            window.close()

    window.close()

    return

#enter health evaluation data:
def Evaluate_Self():
    
    layout_list = []
    layout_list.append([sg.Text('Health Evaluation', font=("Times",45))])
    layout_list.append([sg.Text('Scale 0-10', font=("Times",15))])
    for each in eval_list:
        layout_list.append([sg.Text('%s' %each, size=(14, 1), font=("Times",35)), sg.InputText(size=(3, 1), font=("Times",25))])
    layout_list.append([sg.Submit(size=(14,1.5), font=("Times",15)), sg.Cancel(size=(14, 1.5), font=("Times",15))])

    #define main layout:
    layout = layout_list

    window = sg.Window('Evaluate Self', layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break

        if event == "Submit":

            #upload main data frame:
            this_file = "My_Data/myeval.dat" 
            df = pd.read_csv(this_file)

            #add input data:
            d_input = {"date":today}
            for i in range(0,len(eval_list)):
                d_input[eval_list[i]] = values[i]
            
            df_input = pd.DataFrame(data=d_input,index=[0])

            #get last entry:
            entry_date = df["date"]
            last_entry = str(entry_date[entry_date.size-1])
            
            if last_entry == str(today):
                
                #drop last entry if today:
                df = df.drop(axis=0,index=entry_date.size-1)
                
            df_new = df.append(d_input,ignore_index=True)
            df_new.to_csv(this_file,index=False, sep=",")

            window.close()

    window.close()

    return

def Self_Reflection():

    def draw_plot(this_value,kind,plot_range):

        #upload my data:
        if kind == "input":
            this_file = "My_Data/mydata.dat"
        
        if kind == "eval":
            this_file = "My_Data/myeval.dat"
        
        mydata = pd.read_csv(this_file)
        
        x_list = mydata["date"]
        y_list = mydata[this_value]
        
        #only use days with data enties:
        data_index = ~np.isnan(y_list)
        x_list = x_list[data_index]
        y_list = y_list[data_index]
        
        #set plot range:
        df_time = pd.DatetimeIndex(x_list)
        this_day = df_time.day
        this_month = df_time.month
        this_year = df_time.year
        
        if plot_range == "plot_day":
            plot_index = this_day == day
            x_list = x_list[plot_index]
            y_list = y_list[plot_index]

        if plot_range == "plot_week":
            upper = len(x_list)
            if upper >= 7:
                lower = upper - upper
            if upper < 7:
                lower = 0
            x_list = x_list[lower:upper]
            y_list = y_list[lower:upper]
        
        if plot_range == "plot_month":
            plot_index = this_month == month 
            x_list = x_list[plot_index]
            y_list = y_list[plot_index]

        if plot_range == "plot_year":
            plot_index = this_year == year
            x_list = x_list[plot_index]
            y_list = y_list[plot_index]

        #make plot:
        fig = plt.figure(figsize=(10,6))
        ax = plt.gca()
        ax.set_facecolor("black")

        if (plot_range == "plot_day") | (len(x_list) == 1):
            plt.plot(x_list,y_list,ls="-",marker='s',ms=8,lw=3,color="cornflowerblue")
        else: plt.plot(x_list,y_list,ls="-",lw=3,color="cornflowerblue")
 
        #limit the number of x ticks to 5:
        if len(x_list) > 5:
            ax.xaxis.set_major_locator(ticker.MaxNLocator(5))
        #set number of y ticks to 5:
        ax.yaxis.set_major_locator(ticker.MaxNLocator(5))

        #plot properties:
        mean = np.mean(y_list)
        mean = "{:.1f}".format(mean)
        if np.isnan(np.mean(y_list)) == False:
            plt.title("Average: %s" %str(mean),fontsize=25)
        plt.xlabel("date",fontsize=25)
        plt.ylabel(this_value,fontsize=25)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.grid(ls="-.",color="grey",alpha=0.2)
        plt.show(block=False)

    #make GUI for self-reflection:
    reflection_list = value_list + eval_list
    layout = [[sg.Text('Self-Reflection',font=("Times",55))],
          [sg.Text('Click a tracker',font=("Times",25))],
          [sg.Listbox(values=reflection_list, font=("Times",25), size=(20,12), key='-LIST-', enable_events=True)],
          [sg.Radio('D',"RADIO1", enable_events=True,font=("Times",20)),\
                   sg.Radio('W', "RADIO1", enable_events=True,font=("Times",20)), \
                   sg.Radio('M', "RADIO1", enable_events=True,font=("Times",20)), \
                   sg.Radio('Y',"RADIO1", enable_events=True,font=("Times",20)), \
                   sg.Radio('A', "RADIO1", enable_events=True,default=True, font=("Times",20))],
          [sg.Button('Exit',size=(14,1.5), font=("Times",15))]]
    window = sg.Window('Self-Reflection', layout)

    while True:
        
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            
            plt.close("all")
            break
        
        if values['-LIST-']:

            #get plot range:
            input_time = np.array([values[0],values[1],values[2],values[3],values[4]])
            time_selection = np.array(["plot_day","plot_week","plot_month","plot_year","plot_all"])
            this_selection = time_selection[input_time][0]

            this_value = str(values['-LIST-'][0])
            
            if this_value in eval_list:
                plt.close("all")
                draw_plot(this_value,"eval",this_selection)
            
            else:
                plt.close("all")
                draw_plot(this_value,"input",this_selection)

    window.close()

    return

#run main:
main()
