import tkinter as tk
from tkinter.constants import FALSE

#45, 26, 38, 92, 67, 13, 56, 71
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
 count1=-1

 first = tk.Label(window,text='原始未經排序資料:',background="skyblue")
 first.pack
 first.place(x=5,y=60)

 for k in range(len(arr)):
     D=arr[k]
     data = tk.Label(window, text=D,background="skyblue")
     data.pack()
     data.place(x=150+40*k,y=60)
     if(k==len(arr)-1): break
     comma = tk.Label(window,text=',',background="skyblue")
     comma.pack()
     comma.place(x=175+40*k,y=60)

 
 n=len(arr)
 h=n//2
 count=0

 while h > 0:#shell sort
     for i in range(h, n):
         tmp = arr[i]
         j = i
         while j >= h and arr[j - h] > tmp:
             arr[j] = arr[j - h]
             j = j - h
             
         arr[j] = tmp  
     h =h//2 
     count = count + 1
     count1 += 1

     for k in range(len(arr)):
         D=arr[k]
         data = tk.Label(window, text=D,background="skyblue")
         data.pack()
         data.place(x=150+k*40,y=60+count*40)

         temp='第'+num[count1]+'輪排序結果:'
         numlist= tk.Label(window,text=temp,background="skyblue")
         numlist.pack()
         numlist.place(x=5,y=60+count*40)

         if(k==len(arr)-1): break
         comma = tk.Label(window,text=',',background="skyblue")
         comma.pack()
         comma.place(x=175+40*k,y=60+count*40)

 for k in range(len(arr)):
     D=arr[k]
     data = tk.Label(window, text=D,background="skyblue")
     data.pack()
     data.place(x=150+k*40,y=60+(count+1)*40)
     if(k==len(arr)-1): break
     comma = tk.Label(window,text=',',background="skyblue")
     comma.pack()
     comma.place(x=175+40*k,y=60+(count+1)*40)    

 last = tk.Label(window,text='最終排序結果：',background="skyblue")
 last.pack()
 last.place(x=5,y=60+(count+1)*40)

#設定畫布
window = tk.Tk()
window.title('Shell Sort')
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
