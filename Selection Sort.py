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

 for i in range (len(arr)-1):
     min=i
     for j in range (i+1,len(arr)):
         if arr[j] < arr[min]:
            min=j
     arr[i], arr[min] = arr[min], arr[i]
     count+=1
            
     for k in range(len(arr)):
         D=arr[k]
         data = tk.Label(window, text=D,background="skyblue")
         data.pack()
         data.place(x=150+k*40,y=100+i*40)
        
         temp='第'+num[count]+'輪排序結果:'
         numlist= tk.Label(window,text=temp,background="skyblue")
         numlist.pack()
         numlist.place(x=5,y=100+i*40)

         if(k==len(arr)-1): break
         comma = tk.Label(window,text=',',background="skyblue")
         comma.pack()
         comma.place(x=175+40*k,y=100+i*40)


 for k in range(len(arr)):
             D=arr[k]
             data = tk.Label(window, text=D,background="skyblue")
             data.pack()
             data.place(x=150+k*40,y=100+(i+1)*40)
             if(k==len(arr)-1): break
             comma = tk.Label(window,text=',',background="skyblue")
             comma.pack()
             comma.place(x=175+40*k,y=100+(i+1)*40)

 last = tk.Label(window,text='最終排序結果：',background="skyblue")
 last.pack()
 last.place(x=5,y=100+(i+1)*40)
 
 
 



#設定畫布
window = tk.Tk()
window.title('Selection Sort')
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
