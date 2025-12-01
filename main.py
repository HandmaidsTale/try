from tkinter import *
from employees import employee_form
from products import product_form
#GUI Part
window =Tk()

window.title(&#39;Dashboard&#39;)
window.geometry(&#39;1270x668+0+0&#39;)
window.resizable(0,0)
window.config(bg=&#39;white&#39;)

bg_image=PhotoImage(file=&#39;inventory.png&#39;)
titleLabel=Label(window,image=bg_image,compound=LEFT,text=&#39; Sales and Inventory System
&#39;,font=(&#39;times new roman&#39;,40,&#39;bold&#39;),bg=&#39;#010c48&#39;,fg=&#39;white&#39;,anchor=&#39;w&#39;)
titleLabel.place(x=0,y=0,relwidth=1)
logoutButton=Button(window,text=&#39;Logout&#39;,font=(&#39;times new roman&#39;,20,&#39;bold&#39;),fg=&#39;#010c48&#39;)
logoutButton.place(x=1100,y=10)

subtitleLabel=Label(window,text=&#39;Welcome Admin\t\t Date: 11-29-2025\t\t Time: 1:02:19 pm&#39;,
font=(&#39;times new roman&#39;,15,),bg=&#39;#4d636d&#39;,fg=&#39;white&#39;)
subtitleLabel.place(x=0,y=70,relwidth=1)
leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)
logoImage=PhotoImage(file=&#39;logo.png&#39;)
ImageLabel=Label(leftFrame,image=logoImage)
ImageLabel.pack()

menuLabel=Label(leftFrame,text=&#39;Menu&#39;,font=(&#39;times new roman&#39;,20),bg=&#39;#009688&#39;)
menuLabel.pack(fill=X)
employee_icon=PhotoImage(file=&#39;employee.png&#39;)
employee_button=Button(leftFrame,image=employee_icon, compound=LEFT, text=&#39;
Employees&#39;, font=(&#39;times new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;,padx=10,command=lambda
:employee_form(window))
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file=&#39;supplier.png&#39;)
supplier_button=Button(leftFrame,image=supplier_icon, compound=LEFT, text=&#39; Suppliers&#39;,
font=(&#39;times new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;)
supplier_button.pack(fill=X)
product_icon=PhotoImage(file=&#39;product.png&#39;)
product_button=Button(leftFrame,image=product_icon, compound=LEFT, text=&#39; Products&#39;,
font=(&#39;times new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;,padx=10,command=lambda
:product_form(window))
product_button.pack(fill=X)
order_icon=PhotoImage(file=&#39;order.png&#39;)
order_button=Button(leftFrame,image=order_icon, compound=LEFT, text=&#39; Orders&#39;, font=(&#39;times
new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;)
order_button.pack(fill=X)
stock_icon=PhotoImage(file=&#39;stock.png&#39;)
stock_button=Button(leftFrame,image=stock_icon, compound=LEFT, text=&#39; Stocks&#39;, font=(&#39;times
new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;)
stock_button.pack(fill=X)
sales_icon=PhotoImage(file=&#39;sales.png&#39;)
sales_button=Button(leftFrame,image=order_icon, compound=LEFT, text=&#39; Sales&#39;, font=(&#39;times
new roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;)
sales_button.pack(fill=X)

exit_icon=PhotoImage(file=&#39;exit.png&#39;)
exit_button=Button(leftFrame,image=exit_icon, compound=LEFT, text=&#39; Exit&#39;, font=(&#39;times new
roman&#39;,20,&#39;bold&#39;),anchor=&#39;w&#39;)
exit_button.pack(fill=X)

emp_Frame=Frame(window, bg=&#39;#2C3E50&#39;,bd=3,relief=RIDGE)
emp_Frame.place(x=400,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file=&#39;total_emp.png&#39;)
total_emp_icon_label=Label(emp_Frame,image=total_emp_icon,bg=&#39;#2C3E50&#39;)
total_emp_icon_label.pack(pady=10)
total_emp_icon_label=Label(emp_Frame,text=&#39;Total Employees&#39;,bg=&#39;#2C3E50&#39;,fg=&#39;white&#39;,
font=(&#39;times new roman&#39;,15,&#39;bold&#39;))
total_emp_icon_label.pack()
total_emp_icon_label=Label(emp_Frame,text=&#39;0&#39;,bg=&#39;#2C3E50&#39;,fg=&#39;white&#39;, font=(&#39;times new
roman&#39;,15,&#39;bold&#39;))
total_emp_icon_label.pack()

sup_Frame=Frame(window, bg=&#39;#8E44AD&#39;,bd=3,relief=RIDGE)
sup_Frame.place(x=800,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file=&#39;total_sup.png&#39;)
total_sup_icon_label=Label(sup_Frame,image=total_sup_icon,bg=&#39;#8E44AD&#39;)
total_sup_icon_label.pack(pady=10)
total_sup_icon_label=Label(sup_Frame,text=&#39;Total Suppliers&#39;,bg=&#39;#8E44AD&#39;,fg=&#39;white&#39;,
font=(&#39;times new roman&#39;,15,&#39;bold&#39;))
total_sup_icon_label.pack()
total_sup_icon_label=Label(sup_Frame,text=&#39;0&#39;,bg=&#39;#8E44AD&#39;,fg=&#39;white&#39;, font=(&#39;times new
roman&#39;,15,&#39;bold&#39;))
total_sup_icon_label.pack()

stock_Frame=Frame(window, bg=&#39;#27AE60&#39;,bd=3,relief=RIDGE)
stock_Frame.place(x=400,y=310,height=170,width=280)
total_stocks_icon=PhotoImage(file=&#39;total_stocks.png&#39;)
total_stocks_icon_label=Label(stock_Frame,image=total_stocks_icon,bg=&#39;#27AE60&#39;)
total_stocks_icon_label.pack(pady=10)
total_stocks_icon_label=Label(stock_Frame,text=&#39;Total Stocks&#39;,bg=&#39;#27AE60&#39;,fg=&#39;white&#39;,
font=(&#39;times new roman&#39;,15,&#39;bold&#39;))
total_stocks_icon_label.pack()
total_stocks_icon_label=Label(stock_Frame,text=&#39;0&#39;,bg=&#39;#27AE60&#39;,fg=&#39;white&#39;, font=(&#39;times new
roman&#39;,15,&#39;bold&#39;))
total_stocks_icon_label.pack()
prod_Frame=Frame(window, bg=&#39;#2C3E50&#39;,bd=3,relief=RIDGE)
prod_Frame.place(x=800,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file=&#39;total_prod.png&#39;)
total_prod_icon_label=Label(prod_Frame,image=total_prod_icon,bg=&#39;#2C3E50&#39;)
total_prod_icon_label.pack(pady=10)
total_prod_icon_label=Label(prod_Frame,text=&#39;Total Products&#39;,bg=&#39;#2C3E50&#39;,fg=&#39;white&#39;,
font=(&#39;times new roman&#39;,15,&#39;bold&#39;))
total_prod_icon_label.pack()
total_prod_count_label=Label(prod_Frame,text=&#39;0&#39;,bg=&#39;#2C3E50&#39;,fg=&#39;white&#39;, font=(&#39;times new
roman&#39;,15,&#39;bold&#39;))
total_prod_count_label.pack()

sales_Frame=Frame(window, bg=&#39;#E74C3C&#39;,bd=3,relief=RIDGE)
sales_Frame.place(x=600,y=495,height=170,width=280)





