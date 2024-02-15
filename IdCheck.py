first_place_id={'A':'臺北市','B':'臺中市','C':'基隆市','D':'臺南市','E':'高雄市','F':'新北市','G':'宜蘭縣','H':'桃園市','I':'嘉義市','J':'新竹縣','K':'苗栗縣','L':'臺中縣','M':'南投縣',
         'N':'彰化縣','O':'新竹市','P':'雲林縣','Q':'嘉義縣','R':'臺南縣','S':'高雄縣','T':'屏東縣','U':'花蓮縣','V':'臺東縣','W':'金門縣','X':'澎湖縣','Y':'陽明山','Z':'連江縣'}
first_place_num={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'34','J':'18','K':'19','L':'20','M':'21',
         'N':'22','O':'35','P':'23','Q':'24','R':'25','S':'26','T':'27','U':'28','V':'29','W':'32','X':'30','Y':'31','Z':'33'}
list_weights = [1,9,8,7,6,5,4,3,2,1,1]
       
def ver_first_place(list_id):
    if list_id[0] in first_place_id:
        print("您的出生地在:",first_place_id[list_id])
    else:
        print("無法判斷您的出生地!!")
        
def ver_gender(list_id):
    if list_id[1] == '1':
        print("先生，您好!",end=" ")
        ver_first_place(list_id[0])
    elif list_id[1] == '2':
        print("女士，您好!",end=" ")
        ver_first_place(list_id[0])
    else:
        print("請輸入正確性別!!")

def ver_check(list_id):
  sum = i = 0
  if list_id[0] in first_place_num:
    first_place_list = list(first_place_num[list_id[0]])
    first_place_list.extend(list_id[1:])
    first_place_list = list(map(int, first_place_list))
    product = [x * y for x, y in zip(list_weights, first_place_list)]
    while i < len(product):
        sum += product[i]
        i+=1
    if sum % 10 == 0:
        print("合法之身分證字號")
        ver_gender(list_id)
    else:
        print("此為無效之身分證字號!!")
  else:
    print("此為無效之身分證字號!!")

list_id = input("身分證字號驗證: ")
list_id = list_id.upper()
ver_check(list_id)
