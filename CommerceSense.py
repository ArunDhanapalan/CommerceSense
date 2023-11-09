#-----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
#By Arush S, Arun D and Krishna S of Grade XII A, NHSS Thane


items = [{'name':"Item's Name",'quantity':"In units",'price':"In Rupees"}]
paycount = itemcount = 0
print("\n")
print("...........Loading CommerceSense...........")
print("\n")
print(' :) Welcome to CommerceSense!\n\nI am a Customer - 1\nI am a Manager - 2\nExit - 3\n')

mastercontrols = input("Please choose an option: ")

if mastercontrols == '3':
    print("\nPlease note that all unsaved instances/data will be lost.")
    print("   Bye! ;)\n...........Closing CommerceSense...........")
    print("\nYou may now close this window safely.")


elif mastercontrols == '2':
    print("\n\nWelcome, Manager!")
    
    while mastercontrols == '2':
        display = input('\nPress Enter to continue.')
        defbanner = '------------------Scanning stock, just a sec------------------\n'
        print('\n------------------Welcome to the Manager Console------------------')
        print('1. View items in stock\n2. Add items for sale\n3. Search for an item in stock \n4. Edit items\n5. Exit Manager Console and enter Consumer mode')
        choice = input('\nEnter the function of your choice: ')
        

        if choice == '1' :
            print(defbanner)
            print('The number of items in stock are : ',len(items)-1)
            if len(items)-1 > 0:
                print('\nHere are all the items available in stock at the supermarket:\n')
                for item in items:
                    print(item)
            else:
                print("\nIt seems there are no items in stock.")


        elif choice == '2' :
            tag2 = 'yes'
            while tag2 == "yes":
                print(defbanner)
                print('To add an item, fill in the form: ')
                item = {}
                item['name'] = input('Item name: ')
                count1 = 0
                for i in items:
                    if i['name'].lower() == item['name'].lower():
                        print("\nSorry, adding a duplicate record is not possible.\nTo make changes to this item, please use the 'Edit Item' option in the Manager Console Menu.")
                        count1 = 1
                        tag2 = input("\nDo you want to add more items? (Yes/No): ").lower()
                if count1 == 0:
                    item['quantity'] = int(input("Enter quantity in figures: "))
                    item['price'] = float(input("Enter price (per unit quantity) in Rupees: "))
                    print("\nThe item record was added.")
                    items.append(item)
                    tag2 = input("Do you want to add more items? (Yes/No): ").lower()
                    

        elif choice == '3' :
            find_item = input("\nEnter the item's name to search in Supermarket's stock : ")
            print(defbanner)
            count2 = 0
            for item in items:
                if item['name'].lower() == find_item.lower():
                    count2 = 1
                    break
            if count2 == 1:
                print('\nThe item named ', find_item, ' is displayed below with its details:')
                print(item)
            else:
                print('Item not found in stock.')
            
            
        

        elif choice == '4' :
            print(defbanner)
            count3 = 0
            item_name = input('\nEnter the name of the item that you want to edit : ')
            for item in items:
                if item_name.lower() == item['name'].lower():
                    count3 = 1
                    break
            if count3 == 1:
                print('\nHere are the current details of ', item_name)
                print(item)
                ask1 = input("\nDo you want to delete or edit this record? (Del/Edit): ")
                if ask1.lower() == 'del' or ask1.lower == "delete":
                    indl = items.index(item)
                    del items[indl]
                    print("Item record successfully deleted.")
                else:
                    print("Update the record:")
                    namebuffer = input('New Item name: ')
                    count4 = 0
                    for i in items :
                        if i['name'].lower() == namebuffer.lower():
                            count4 = 1
                            break
                    if count4 == 1:
                        print("\nIMPORTANT!: Existing record with the same name was found.\nTo prevent duplication of item records, CommerceSense will make changes to this record:")
                        print(i)
                        print('\n!!! Please make edits to this record accordingly.\n')
                        i['quantity'] = int(input('New Item quantity in figures: '))
                        i['price'] = float(input('New Price in Rupees (in figures): '))
                        print('\nItem has been successfully updated.\n\nHere\'s the updated record: ')
                        print(i)
                    else:
                        item['name'] = namebuffer
                        item['quantity'] = int(input('New Item quantity in figures: '))
                        item['price'] = float(input('New Price in Rupees (in figures): '))
                        print('\nItem has been successfully updated.\n\nHere\'s the updated record: ')
                        print(item)
            else:
                print('Item not found in stock.')
                    
            
        elif choice == '5':
            print("\n...........Closing Manager Console...........\n")
            print("   See you later! :)")
            print("\n\n...Switching to Customer mode. Hold on for a sec...\n\n")
            mastercontrols = '1'
            break

        else:
            print("Invalid Choice. Try again.")


if mastercontrols == '1':
    secl = []
    for i in items:
        secl.append(i['name'].lower())
    print("\nWelcome, Customer!")
    while True:
        display = input('\nPress Enter to continue.')
        defbanner = '------------------Scanning stock, just a sec------------------\n'
        print('\n------------------Welcome to the Supermarket!------------------')
        print('1. View items in stock\n2. Search for an item in stock\n3. Purchase items in stock\n4. Finish your purchase\n5. Exit CommerceSense')
        choice = input('\nEnter the function of your choice : ')



        if choice == '1' :
            print(defbanner)
            print('The number of items in stock are : ',len(items)-1)
            if len(items)-1 > 0:
                print('\nHere are all the items available in stock at the supermarket:\n')
                for item in items:
                    print(item)
            else:
                print("\nSorry, it seems there are no items in stock.")

        elif choice == '2' :
            find_item = input("\nEnter the item's name to search in Supermarket's stock : ")
            print(defbanner)
            count2 = 0
            for item in items:
                if item['name'].lower() == find_item.lower():
                    count2 = 1
                    break
            if count2 == 1:
                print('\nThe item named ', find_item, ' is displayed below with its details:')
                print(item)
            else:
                print('Sorry, it seems this item is not in stock.')

        elif choice == '3' :
            print(defbanner)
            for i in items:
                print(i)
            if len(items)<=1:
                print("\nSorry, there seems to be no item in stock.")
            else:
                count5 = 0
                contshop = "yes"
                while contshop.lower() == "yes":
                    purchase_item = input('\nWhich item do you want to purchase? Enter name: ')          
                    for item in items[1:]:
                        if purchase_item.lower() == item['name'].lower():
                            count5 = 1
                            if count5 == 1:
                                purchase_quant = int(input("How much do you want? Enter quantity: "))
                                if int(item['quantity']) >= purchase_quant :
                                    print('\n',purchase_quant,item['name'],"(s) worth Rs.", item['price'] * purchase_quant , 'were added to your cart.')
                                    paycount += (item['price'] * purchase_quant)
                                    itemcount += purchase_quant
                                    contshop = input("\nDo you want to continue shopping? (Yes/No): ")
                                    item['quantity'] -= purchase_quant
                                else:
                                    print('\nSorry, it seems the item is either out of stock or insufficient. :(  Come back later.')
                            else:
                                print("\nWe don't seem to have that product in stock. Try a different name variation instead.")
                        elif purchase_item not in secl:
                            print("Sorry, this item is not in stock. Try later.")
                            break


        elif choice == '4':
            print("\nYou've bought", itemcount, "items worth Rs.", paycount,"\n\n! Please note a GST of 18% will be levied on this purchase.")
            gst = paycount * 0.18
            print("\n\n***Please pay Rs.", paycount + gst, "at the counter.***")
            print("\n\nThank you for purchasing from our Supermarket.\n   See you next time! :)")
            paycount = itemcount = 0


        elif choice == '5' :
            print('\nAll data has been deleted. To power your business the next time, restart CommerceSense.\n   :) Bye!\n\n------------------Exiting CommerceSense------------------')
            break

        else:
            print("\nUh-oh :0\n\n   That was an invalid option.\nNo problem, try again.")

else:
    print("\nCommerceSense. Your business' best partner.\nDesigned and Developed in 2022 by Arush, Arun and Krishna of Grade XII A, NHSS Thane.")

