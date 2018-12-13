"""
A programe that computes the net amount of a bank account based on a transaction log from console input.
The transaction log format is shown as following;
D100
W200
D for deposite and W for withdraw
"""
amount =0
def calc(transaction=input('enter  transaction:\n').split(',')):

    try:
        depo=[]
        withd=[]
        withdraw =0
        deposite=0
        temporaly=[]
        my_transaction=[]
        my_transaction.extend([transaction])

        for transaction in my_transaction:

           for num in range(0,len(transaction)):
               temporaly.append(transaction[num])
               if 'd' in temporaly[num].lower():
                    string = temporaly[num]
                    d =string[1:]
                    d=int(d)
                    depo.append(d)


               elif 'w' in temporaly[num].lower():
                   string = temporaly[num]
                   w = string[1:]
                   w=int(w)
                   withd.append(w)

               else:
                   print(f'\n{temporaly[num]} is invalid input'.upper())
                   break

        for de in depo:
            deposite += de
        for we in withd:
            withdraw += we

        if deposite > withdraw:
            amount = deposite - withdraw
            print(f'\n\nYour account ballance is UGshs {amount}/- \n\n')
            return amount
        elif deposite < withdraw :
            print('\n\ninsurficient ballance \n\n'.upper())


    except(ValueError):
        print(f'the input "{temporaly[num]}" is incorrect')



