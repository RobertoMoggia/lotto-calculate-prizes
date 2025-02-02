import random
import math

class Bill:
    grossPrizesList = [[11.23],
    [5.61, 250],
    [3.74, 83.33, 4500],
    [2.80, 41.66, 1125, 120000],
    [2.24, 25, 450, 24000, 6000000],
    [1.87, 16.66, 225, 8000, 1000000],
    [1.60, 11.90, 128.57, 3428.57, 285714.28],
    [1.40, 8.92, 80.35, 1714.28, 107142.85],
    [1.24, 6.94, 53.57, 952.38, 47619.04],
    [1.12, 5.55, 37.50, 571.42, 23809.52]]

    def guessGenerator(self,guessType):
        guess=random.sample(self.availableNumbers,guessType)
        self.availableNumbers=[i for i in self.availableNumbers if not i in guess]
        return guess

    def billsPrinter(*args):
        if not all(type(bill)==Bill for bill in args):
            raise(TypeError('Only object of class Bill!'))
        billsNumber=len(args)
        billNumberColumnWidth=max(len(str(billsNumber)),len('Bill number'))
        ruotaColumnWidth=len('Ruota')
        guessColumnWidth=len('Guesses')
        for bill in args:
            if ruotaColumnWidth<len(bill.city):
                ruotaColumnWidth=len(bill.city)
            
            if guessColumnWidth<len(str(bill.guessList))-2:
                guessColumnWidth=len(str(bill.guessList))-2
        
        billsTable=[]
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format('Bill number',' '*(billNumberColumnWidth-len('Bill number')),'Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Guesses',' '*(guessColumnWidth-len('Guesses'))))
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        for i in range(len(args)):
            bill=args[i]
            guesses=', '.join(str(guess) for guess in bill.guessList)
            billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format(i+1,' '*(billNumberColumnWidth-len(str(i))),bill.city,' '*(ruotaColumnWidth-len(bill.city)),guesses,' '*(guessColumnWidth-len(str(guesses)))))
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        print('\n'.join(billsTable))

    def winningBillsPrinter(*args):
        if not all(type(bill)==Bill for bill in args):
            raise(TypeError('Only object of class Bill!'))
        billsNumber=len(args)
        billNumberColumnWidth=max(len(str(billsNumber)),len('Bill number'))
        ruotaColumnWidth=len('Ruota')
        winningGuessColumnWidth=len('Winning guesses')
        grossPrizeColumnWidth=len('Gross prize')
        netPrizeColumnWidth=len('Net prize')
        for bill in args:
            if ruotaColumnWidth<len(bill.city):
                ruotaColumnWidth=len(bill.city)
            
            if winningGuessColumnWidth<len(str(bill.winsList))-2:
                winningGuessColumnWidth=len(str(bill.winsList))-2
            
            if grossPrizeColumnWidth<len(str(bill.grossPrize)):
                grossPrizeColumnWidth=len(str(bill.grossPrize))
            
            if netPrizeColumnWidth<len(str(bill.netPrize)):
                netPrizeColumnWidth=len(str(bill.netPrize))
        
        billsTable=[]
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*winningGuessColumnWidth,'-'*grossPrizeColumnWidth,'-'*netPrizeColumnWidth))
        billsTable.append('|  {}{}  |  {}{}  |  {}{}  |  {}{}  |  {}{}  |'.format('Bill number',' '*(billNumberColumnWidth-len('Bill number')),'Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Winning guesses',' '*(winningGuessColumnWidth-len('Winning guesses')),'Gross prize',' '*(grossPrizeColumnWidth-len('Gross prize')),'Net prize',' '*(netPrizeColumnWidth-len('Net prize'))))
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*winningGuessColumnWidth,'-'*grossPrizeColumnWidth,'-'*netPrizeColumnWidth))
        for i in range(len(args)):
            bill=args[i]
            winningGuesses=', '.join(str(guess) for guess in bill.winsList)
            billsTable.append('|  {}{}  |  {}{}  |  {}{}  |  {}{}  |  {}{}  |'.format(i+1,' '*(billNumberColumnWidth-len(str(i))),bill.city,' '*(ruotaColumnWidth-len(bill.city)),winningGuesses,' '*(winningGuessColumnWidth-len(str(winningGuesses))),bill.grossPrize,' '*(grossPrizeColumnWidth-len(str(bill.grossPrize))),bill.netPrize,' '*(netPrizeColumnWidth-len(str(bill.netPrize)))))
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*winningGuessColumnWidth,'-'*grossPrizeColumnWidth,'-'*netPrizeColumnWidth))
        print('\n'.join(billsTable))

    def __init__(self,city,amount,*args):
        self.availableNumbers=list(range(1,91))
        if len(args)<1:
            raise(SyntaxError('At least one guess type is needed!'))
        elif not all(type(guess)==int for guess in args):
            raise(TypeError('Only int values for guessType!'))
        elif type(amount)!=float:
            raise(TypeError('Only float values for amount!'))
        elif not all(guess in range(1,6) for guess in args):
            raise(SyntaxError('Review your guess types! One or more of them are not an existing guess type!'))
        elif sum(args)>10:
            raise(SyntaxError('At most 10 numbers for each bill!'))
        elif not city.lower() in ["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia","tutte"]:
            raise(SyntaxError('{} is not an existing "ruota"'.format(city)))
        elif not amount in [1+i*0.5 for i in range(1,400)]:
            raise(SyntaxError('Only amount between 1€ and 200€ with a step of 0.5€ are admitted!'))
        else:
            guessList=[]
            for i in range(len(args)):
                guessList.append(self.guessGenerator(args[i]))
            self.guessList=guessList
            self.city=city
            self.amount=amount
            self.winsList=[]
            self.grossPrize=0
            self.netPrize=0
    
    def __str__(self):
        return 'Bill: Ruota di {} - {}'.format(self.city.capitalize(),self.guessList)

class Extraction:
    ruoteList=["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia"]
    def __init__(self):
        extraction={}
        for ruota in Extraction.ruoteList:
            extraction[ruota]=random.sample(range(1,91),5) 
        self.extractions=extraction
    
    def __str__(self):
        extraction=self.extractions
        ruotaColumnWidth=len('Ruota')
        numbersColumnWidth=len('Extracted numbers')
        for ruota in Extraction.ruoteList:
            if ruotaColumnWidth<len(ruota):
                ruotaColumnWidth=len(ruota)
            
            if numbersColumnWidth<len(str(list(extraction[ruota])))-2:
                numbersColumnWidth=len(str(list(extraction[ruota])))-2
        
        extractionsTable=[]
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        extractionsTable.append('|  {}{}  |  {}{}  |'.format('Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Extracted numbers',' '*(numbersColumnWidth-len('Extracted numbers'))))
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        for ruota in extraction:
            extractedNumbers=', '.join(str(number) for number in extraction[ruota])
            extractionsTable.append('|  {}{}  |  {}{}  |'.format(ruota.capitalize(),' '*(ruotaColumnWidth-len(ruota)),extractedNumbers,' '*(numbersColumnWidth-len(extractedNumbers))))
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        return '\n'.join(extractionsTable)

def winCheck(bill,extraction):
    if type(bill)!=Bill:
        raise(TypeError('Only bill objects for bill argument!'))
    elif type(extraction)!=Extraction:
        raise(TypeError('Only extraction objects for extraction argument!'))
    
    guessList=bill.guessList
    totalNumbers=0
    for guess in guessList:
        totalNumbers+=len(guess)
    ruota=bill.city.lower()
    if ruota=='tutte':
        extractions=extraction.extractions
        for ruota in extractions:
            for guess in guessList:
                if set(guess).issubset(set(extractions[ruota])):
                    bill.winsList.append(guess)
                    bill.grossPrize+=Bill.grossPrizesList[totalNumbers-1][len(guess)-1]*bill.amount/len(guessList)
                    bill.grossPrize=round(bill.grossPrize,2)
                    bill.netPrize=round(bill.grossPrize*0.92,2)
    else:
        for guess in guessList:
            if set(guess).issubset(set(extractions[ruota])):
                bill.winsList.append(guess)
                if len(guess)>1:
                    for i in range(2,len(guess)+1):
                        bill.grossPrize+=round(Bill.grossPrizesList[totalNumbers][i-1]*bill.amount/len(guessList),2)*(math.factorial(len(guess))/(math.factorial(i)*math.factorial(len(guess)-i)))
                    else:
                        bill.grossPrize+=round(Bill.grossPrizesList[totalNumbers][0]*bill.amount/len(guessList),2)
                bill.netPrize=round(bill.grossPrize*0.92,2)

    if len(bill.winsList)>0:
        return True
    else:
        return False