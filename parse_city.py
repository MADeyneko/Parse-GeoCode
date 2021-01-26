def parse_city(Corner):   #Делим город по секторам
    global step
    current_num_sector=0  #Текущий сектор в обработке

    LON={'lower':float(Corner['lowerCorner'].split(' ')[0]),'upper':float(Corner['upperCorner'].split(' ')[0])}
    LAT={'lower':float(Corner['lowerCorner'].split(' ')[1]),'upper':float(Corner['upperCorner'].split(' ')[1])}

    count_sector=math.ceil(((LON['upper']-LON['lower'])/step)+1)*math.ceil(((LAT['upper']-LAT['lower'])/step)+1)
                               
    print('Кол-во секторов:',count_sector)
    time.sleep(1)
    LON_current=LON['lower']
    LAT_current=LAT['lower']
    result={}
    while current_num_sector<=count_sector:
        result[current_num_sector]={
            'lower_LON':LON_current,
            'upper_LON':(LON_current+step),
            'lower_LAT':LAT_current,
            'upper_LAT':(LAT_current+step)
        }

        LON_current+=step
        current_num_sector+=1
        if LON_current>LON['upper']:
            LAT_current+=step
            LON_current=LON['lower']
#         if current_num_sector>9:
#             return result            
    return result
