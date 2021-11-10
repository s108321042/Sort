import tkinter as tk

#55, 23, 87, 62, 16
def sort():  
     
 try:
     arr = list(map(int,D_input.get().split(',')))
 except:
    #設定輸入格式錯誤
    error = tk.StringVar()
    error_label = tk.Label(window,text='記得輸入!!or格式錯誤!!')
    error_label.pack()
    error_label.place(x=350,y=35)
 
 num = ['一','二','三','四','五','六','七','八','九','十']
 count=-1
 temp2 = ", ".join([str(i) for i in arr])


 first = tk.Label(window,text='原始未經排序資料:'+temp2,background="skyblue")
 first.pack
 first.place(x=5,y=60)



 for i in range (len(arr)):

     count+=1

     for j in range (len(arr)-i-1):
         if arr[j] > arr[j+1]:
            tmp=arr[j+1]
            arr[j+1]=arr[j]#change
            arr[j]=tmp
         temp1 = "第" + num[count] + "輪排序結果:" + ", ".join([str(i) for i in arr])

         for k in range(len(arr)):
             numlist= tk.Label(window,text=temp1,background="skyblue")
             numlist.pack()
             numlist.place(x=5,y=100+i*40)

 temp3=", ".join([str(i) for i in arr])
 last = tk.Label(window,text='最終排序結果：'+ temp3,background="skyblue")
 last.pack()
 last.place(x=5,y=100+i*40)
 
 



#設定畫布
window = tk.Tk()
window.title('Bubble sort')
window.geometry("500x500")
canvas = tk.Canvas(window, width=1000, height=1000, bg="skyblue")
canvas.pack()
canvas.place(x=-10, y=-10)

#設定input
D = tk.Label(window,text="Please enter the data with comma : ",fg="black")
D.pack()
D.place(x=0,y=10)
D_input = tk.Entry(window)
D_input.pack()
D_input.place(x=220,y=10)

#設定按鈕
count_button = tk.Button(window, text="GO", command=sort)
count_button.pack()
count_button.place(x=400,y=5)





window.mainloop()
