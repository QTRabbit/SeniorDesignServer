import csv

def TemperatureCSV():
    send_data = ""
    #with open('MAX30205EVKit_2019-11-27_13-09-38.csv') as csv_file:
    with open('MAX30205EVKit_2019-11-27_13-09-38.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print("Column names are" + row[0] + row[1] )
                line_count += 1
            else:
                #print(row[0] + row[1])
                send_data += row[0] + row[1] + "~"
                line_count += 1
        #print(f'Processed {line_count} lines.')
        #& is in between time and temperature and ~ marks end of row
    send_data += "!"     #! marks the end of the string
    #print(send_data)
    return send_data

def ECGCSV(filename):
    send_data = ""
    time = 0.01
    holder = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print("Column names are" + row[0] + row[1] )
                line_count += 1
            elif(line_count > 22 and line_count < 300 and (holder[21] != str(row[0][21]) ) ):
                #print(row[4] + "  " + row[0][21]+ row[0] + "    H" + holder[21])
                send_data += str(time) + " "+ row[8] + "~"
                line_count += 1
                time += 0.01
                holder = str(row[0])
            elif(line_count> 300):
                break
            else:
                line_count += 1
        #print(f'Processed {line_count} lines.')
        #& is in between time and temperature and ~ marks end of row
    send_data += "!"     #! marks the end of the string
    #print(send_data)
    return send_data



def PPGCSV(filename):
    send_data = ""
    time = 0.01
    holder = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print("Column names are" + row[0] + row[1] )
                line_count += 1
            elif(line_count > 22 and line_count < 300 and (holder[21] != str(row[0][21]) ) ):
                #print(row[4] + "  " + row[0][21]+ row[0] + "    H" + holder[21])
                send_data += str(time) + " "+ row[4] + "~"
                line_count += 1
                time += 0.01
                holder = str(row[0])
            elif(line_count> 300):
                break
            else:
                line_count += 1
        #print(f'Processed {line_count} lines.')
        #& is in between time and temperature and ~ marks end of row
    send_data += "!"     #! marks the end of the string
    #print(send_data)
    return send_data



def Load_Heart_Rate(filename, iden):
    data = ""
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count < 3:   
                #First Two Heart-Rate Are Empty
                line_count += 1
            else:
                #print(row[1])
                if row[1] == iden:
                    data = row[1] + " " +  row[0] + " " + row[2] + " " +row[3] + "~" + "!"
                    return data
                line_count += 1
    #print(data)
    data += "!"     #! marks the end of the string
    return "None"





def Load_Body_Temp(filename, iden):
    data = ""
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count < 1:   
                #First Two Heart-Rate Are Empty
                line_count += 1
            else:
                #print(row[1])
                if row[1] == iden:
                    data = row[1] + " " +  row[0] + " " + row[2] + " " +row[3] + "~" + "!"
                    return data
                line_count += 1
    #print(data)
    data += "!"     #! marks the end of the string
    return "None"
