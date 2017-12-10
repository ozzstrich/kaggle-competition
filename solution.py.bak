'''
solution.py
'''

class Store :
    '''
    [0] store = int
    [1] storetype = string
    [2] assortment = string
    [3] competitiondistance = int
    [4] competitionopensincemonth = int
    [5] competitionopensinceyear = int
    [6] promo2 = int
    [7] promo2sinceweek = int
    [8] promo2sinceyear = int
    [9] promointerval = list of strings
    [x] salesrecords = list of SalesRecords
    '''
    def __init__(self, data) :
        stringPos = [1, 2]
        stringPos += list(range(9, len(data))) #Everything after 8 is str
        for x in range(0, len(data)) :
            data[x] = data[x].replace("\n", "").strip("'").strip('"')
            if x in stringPos : continue
            try :
                data[x] = int(data[x])
            except ValueError :
                data[x] = None
        self.Store = data[0]
        self.StoreType = data[1]
        self.Assortment = data[2]
        self.CompDistance = data[3]
        self.CompOpenSinceMonth = data[4]
        self.CompOpenSinceYear = data[5]
        self.Promo2 = data[6]
        self.Promo2SinceWeek = data[7]
        self.Promo2SinceYear = data[8]
        self.PromoInterval = [data[x] for x in range(9, len(data))]
        self.SalesRecords = []

    def __str__(self) :
        return "{Store=" + str(self.Store) + ",StoreType=" + \
               str(self.StoreType) + ",Assorment=" + str(self.Assortment) + \
               ",CompDistance=" + str(self.CompDistance) + \
               ",CompOpenSinceMonth=" + str(self.CompOpenSinceMonth) + \
               ",CompOpenSinceYear=" + str(self.CompOpenSinceYear) + \
               ",Promo2=" + str(self.Promo2) + ",Promo2SinceWeek=" + \
               str(self.Promo2SinceWeek) + ",Promo2SinceYear=" + \
               str(self.Promo2SinceYear) + ",PromoInterval=" + \
               str(self.PromoInterval) + ",NumberOfSalesRecords=" + \
               str(len(self.SalesRecords)) + "}"

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

class Solution :
    def __init__(self) :
        stores = []

        storeFile = open("./store.csv", "r")
        for line in storeFile :
            store = Store(line.split(","))
            # If the Store id is None then we don't have a valid store so
            # throw the object away
            if store.Store != None : stores.append(store)
        storeFile.close()

        trainFile = open("./train.csv", "r")
        for line in trainFile :
            salesRecord = SalesRecord(line.split(","))
            # If the SalesRecord Store id is None then we don't have a valid store so
            # throw the object away
            if salesRecord.Store != None :
                # This is naughty. Rely on index to find store.
                stores[salesRecord.Store - 1].SalesRecords.append(salesRecord)
        trainFile.close()

        # Print stores for testing purposes
        for x in stores : print(x)

Solution()
