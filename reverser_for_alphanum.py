def my_reverser():
    # inputla kullanicidan istedigini girmesini sagliyoruz.
    my_input=input('hello, please write something that you want me to reverse :')
    index_list=[] # harf yada numara olmayanlarin index numaralarini aliyoruz.
    index_alp=[] # harf yada numara olmayan karakterleri listeye eklemek icin bos liste olusturduk.
    without_alphanum=[] # else blogunu calistirarak alpha num olmayanlarida buraya ekleyelim.
    for alp in range(len(my_input)):
        if my_input[alp].isalnum():
            index_list.append(alp)
            index_alp.append(my_input[alp])
        else:
            without_alphanum.append(my_input[alp])

    index_alp.reverse() # alpha numlari terse ceviriyoruz.
    counter=0 #bu counter karakterleri sifirdan baslayarak kullanmamizi saglayacak.
    for i in index_list:
        without_alphanum.insert(i,index_alp[counter]) # i ninci siraya tersten yazdirdigimiz harfleri ekliyoruz.
        counter+=1 # tersteki harf listesinin bir sonrasina gecmek icin counter i artirdik.
    print(''.join(without_alphanum)) # bununlada listemizi str e cevirdik.


my_reverser() # yazdigimiz fonksiyonu cagiriyoruz.