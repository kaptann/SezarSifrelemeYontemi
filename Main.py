import Crypto as crptyo

flag = True
while(flag == True):

    choice = input("Sifre olusturmak icin 1'e, sifre cozmek icin 2'ye basiniz : ")

    if(choice == "1"):
        text = input("Sifrelemek istediginiz mesaji yaziniz : ")
        scrl = int(input("Sifre oteleme miktarini giriniz : "))
        crptyo.crp(text, scrl)
        flag = False

    elif(choice == "2"):
        ppsw = input("Sifresini cozmek istediginiz sifreyi yaziniz : ")
        scrl = int(input("Sifre oteleme miktarini giriniz : "))
        crptyo.dcrp(ppsw, scrl)
        flag = False

    else:
        print("Hatali giris ! Lutfen tekrar deneyiniz...")