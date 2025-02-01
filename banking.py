                            print("Press 1 To Update Your Name : ")
                            print("Press 2 To Update Your UserName : ")                        
                            print("Press 3 To Update Your PassWord : ")
                            print("Press 4 To Update Your Phone Number : ")
                            print("Press 5 To Update Address : ")
                        
                            try:
                                ch2=int(input("Enter Your CHoice : "))
                                if(ch2>=6):
                                    raise ValueError ("")
                                    
                            except Exception:
                                print("___________________________________________________")
                                print("      ****OOP's That's Was an invalid input****    ")
                                print("___________________________________________________")
                                continue
                            break
                        if(ch2==1):
                            try:
                                name=input ("Enter Your New Name : ")
                                ns="update bank set name='{}' where UserName='{}'".format(name,u)
                    
                                mycur.execute(ns)
                                mycon.commit()
                                print("_________________________________________________________________________")
                                print ("   ****Hurrey !!! Name is Updated Successfully***   :) ")
                                print("_________________________________________________________________________")
                            except IndexError:
                                print("Oh Something Went Wrong !!!")
                        elif(ch2==2):
                            try:
                                gf="SET FOREIGN_KEY_CHECKS=0"
                                mycur.execute(gf)
                                mycon.commit()

                                mp=input("Enter Your New UserName : ")
                                nm="update bank set UserName='{}' where password='{}'".format(mp,p)
                                mycur.execute(nm)
                                mycon.commit()
                                print("_________________________________________________________________________")
                                print ("   ****Hurrey !!! UserName is Updated Successfully***   :) ")
                                print("_________________________________________________________________________")
                        

                                gf1="SET FOREIGN_KEY_CHECKS=1"
                                mycur.execute(ns)
                                mycon.commit(gf1)
                        
                            except Exception:
                                print("")
                        elif(ch2==3):
                            try:
                                newpassword=input("Enter Your New Password : ")
                                us="update bank set Password='{}' where UserName='{}'".format(newpassword,u)
                                mycur.execute(us)
                                mycon.commit()
                                print ("Hurrey !!! Password is Updated Successfully")
                            except IndexError:
                                print("Oh Something Went Wrong")
                        elif(ch2==4):
                            while True:
                                try:
                                    newphone=(input("Enter Your New Phone Number : "))
                                    if(len(newphone)!=10) or newphone.isalpha():
                                        raise ValueError ("")
                                    
                            

                                    us="update bank set Mobile_Number='{}' where  UserName='{}'".format(newphone,u)
                                    mycur.execute(us)
                                    mycon.commit()
                                    print("_________________________________________________________________________")
                                    print ("   ****Hurrey !!! Mobile Number is Updated Successfully***   :) ")
                                    print("_________________________________________________________________________")
                                    
                                except ValueError:
                                    print("________________________________________________________")
                                    print("**** Please Enter a valid 10 digit Number ******")
                                    print("________________________________________________________")
                                    print("\n")
                                    continue
                                break
                          
                        elif(ch2==5):
                            try:
                                newadd=input("Enter Your New Address : ")
                                ns1="update bank set address='{}' where UserName='{}'".format(newadd,u)
                                mycur.execute(ns1)
                                mycon.commit()
                                print("_________________________________________________________________________")
                                print("   *** Hurrey !!! Address is Updated Successfully ***  :) ") 
                                print("_________________________________________________________________________")
                            except IndexError:
                                print("OOPS Something Went Swrong !!! ")
                    elif(ch1==6):
                        ns="SET FOREIGN_KEY_CHECKS=0"
                        mycur.execute(ns)
                        mycon.commit()
                        ps="delete from bank where password='{}'".format(p)
                        mycur.execute(ps)
                        mycon.commit()

                        gs="delete from transaction where UserName1='{}'".format(u)
                        mycur.execute(gs)
                        mycon.commit()
                        


                        ns1="SET FOREIGN_KEY_CHECKS=1"
                        mycur.execute(ns1)
                        mycon.commit()


                        print("\n")
                        print("_________________________________________________________________________")
                        print("************* ACCOUNT HAS BEEN DELETED SUCCESSFULLY *******************")
                        print("_________________________________________________________________________")
                        print("\n")
                        exit()

                    elif(ch1==7):
                        print("\n")
                        print("_____________________________________________________________________________")
                        print("*************Thanks For Choosing Colony Bank Of India *****************")
                        print("____________________________________________________________________________")
                        exit()
                    

            else:
                print("\n")
                print("_______________________________________________")
                print("        Login Failed Please Try Again       :( ")
                print("_______________________________________________")
                print("\n")

    


            
