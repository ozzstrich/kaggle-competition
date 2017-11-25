'''
solution.py
'''

class SalesRecord :
    '''
    [0] store = int
    [1] dayofweek = int
    [2] date = string
    [3] sales = int
    [4] customers = int
    [5] open = int
    [6] promo = int
    [7] stateholiday = string
    [8] schoolholiday = int
    '''
    def __init__(self, data) :
        stringPos = [2, 7] # Positions in data arr where we don't convert to int
        for x in range(0, len(data)) :
            if x in stringPos : continue
            data[x] = data[x].replace("\n", "").strip("'").strip('"')
            try :
                data[x] = int(data[x])
            except ValueError :
                data[x] = None
        self.Store = data[0]
        self.DayOfWeek = data[1]
        self.Date = data[2]
        self.Sales = data[3]
        self.Customers = data[4]
        self.Open = data[5]
        self.Promo = data[6]
        self.StateHoliday = data[7]
        self.SchoolHoliday = data[8]

    def __str__(self) :
        return "{Store=" + str(self.Store) + ",DayOfWeek=" + \
               str(self.DayOfWeek) + ",Date=" + str(self.Date) + ",Sales=" + \
               str(self.Sales) + ",Customers=" + str(self.Customers) + \
               ",Open=" + str(self.Open) + ",Promo=" + str(self.Promo) + \
               ",StateHoliday=" + str(self.StateHoliday) + ",SchoolHoliday=" + \
               str(self.SchoolHoliday) + "}"

trainData = []

trainFile = open("./train.csv", "r")
for line in trainFile :
    salesRecord = SalesRecord(line.split(","))
    # If the SalesRecord Store id is None then we don't have a valid store so
    # throw the object away
    if salesRecord.Store != None : trainData.append(salesRecord)
trainFile.close()

# Print first 100 sales records for testing purposes
for x in trainData[0:100] : print(x)
