from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root=Tk()
root.title('address_book')
root.iconbitmap('images/deadpool.ico')


#creating a Database or connecting to a Database
conn=sqlite3.connect('address_book.db')

#creating Cursor
c=conn.cursor()

#Create Table
''''
c.execute("""CREATE TABLE addresses(
	     first_name text,
	     last_name text,
	     address text,
	     city text,
	     state text,
	     pincode integer
	     )""")
 '''

#Submit Function FOr Database
def submit():
	#creating a Database or connecting to a Database
	conn=sqlite3.connect('address_book.db')

	#creating Cursor
	c=conn.cursor()

    # Insert Into Table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :pincode)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'pincode': pincode.get()
			})

	#Commit Changes
	conn.commit()

	#Close Connection
	conn.close()

	#Clear The Text Boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	pincode.delete(0,END)

	message=messagebox.showinfo("info","Record is added to the Database")
	#message_label=Label(root,text=message)
	#message_label.grid(row=20,column=20)

def query():
	#creating a Database or connecting to a Database
	conn=sqlite3.connect('address_book.db')

	#creating Cursor
	c=conn.cursor()

	#Query the Datsbase
	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()
	#print(records)
    
    #to print directly alist
	#print_records=Label(root,text=records).grid(row=8,column=0,columnspan=2)
	print_records=''
	#to print in form of lists and tuples individually
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) +"\n" 

	query_label=Label(root,text=print_records).grid(row=12,column=0,columnspan=2)	

	#Commit Changes
	conn.commit()

	#Close Connection
	conn.close()


def delete():
	#creating a Database or connecting to a Database
	conn=sqlite3.connect('address_book.db')

	#creating Cursor
	c=conn.cursor()
	
	#Delete a Record From Database
	c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

	delete_box.delete(0,END)

	#Commit Changes
	conn.commit()

	#Close Connection
	conn.close()

	message=messagebox.showinfo("info","Record Deleted")
	#message_label=Label(root,text=message)
	#message_label.grid(row=20,column=20)


def edit():
	global editor
	editor=Tk()
	editor.title('Edit address_book')
	editor.iconbitmap('images/deadpool.ico')

	#creating a Database or connecting to a Database
	conn=sqlite3.connect('address_book.db')

	#creating Cursor
	c=conn.cursor()
	global record_id
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global pincode_editor

	#Create Text Boxes
	f_name_editor=Entry(editor,width=30)               
	f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
	l_name_editor=Entry(editor,width=30)
	l_name_editor.grid(row=1,column=1)
	address_editor=Entry(editor,width=30)
	address_editor.grid(row=2,column=1)
	city_editor=Entry(editor,width=30)
	city_editor.grid(row=3,column=1)
	state_editor=Entry(editor,width=30)
	state_editor.grid(row=4,column=1)
	pincode_editor=Entry(editor,width=30)
	pincode_editor.grid(row=5,column=1)

	#Create Text Box Labels
	f_name_label=Label(editor,text="First Name")
	f_name_label.grid(row=0,column=0,pady=(10,0))
	l_name_label=Label(editor,text="Last Name")
	l_name_label.grid(row=1,column=0)
	address_label=Label(editor,text="Address")
	address_label.grid(row=2,column=0)
	city_label=Label(editor,text="City")
	city_label.grid(row=3,column=0)
	state_label=Label(editor,text="State")
	state_label.grid(row=4,column=0)
	pincode_label=Label(editor,text="Pincode")
	pincode_label.grid(row=5,column=0)


	#Query the Datsbase
	record_id=delete_box.get()
	c.execute("SELECT * FROM addresses WHERE oid= "+record_id)
	records=c.fetchall()

	for record in records:
		f_name_editor.insert(0,record[0])
		l_name_editor.insert(0,record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		pincode_editor.insert(0, record[5])

	#Update Button
	update_button=Button(editor,text="Save Record",command=update)
	update_button.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=140)
	
def update():
	#creating a Database or connecting to a Database
	conn=sqlite3.connect('address_book.db')

	#creating Cursor
	c=conn.cursor()

	c.execute("""UPDATE addresses SET

			first_name= :first,
			last_name= :last,
			address= :address,
			city= :city,
			state= :state,
			pincode= :pincode

			WHERE oid=:oid""",
			{
			'first' : f_name_editor.get()	,
			'last' : l_name_editor.get(),
			'address' : address_editor.get(),
			'city' : city_editor.get(),
			'state' : state_editor.get(),
			'pincode' : pincode_editor.get(),
			'oid' :record_id
			})

	#Commit Changes
	conn.commit()

	#Close Connection
	conn.close()

	message=messagebox.showinfo("info","Record updated!!")
	message_label=Label(editor,text=message)
	message_label.grid(row=0,column=0)
	editor.destroy()
				


#Create Text Boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
pincode=Entry(root,width=30)
pincode.grid(row=5,column=1)
delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

#Create Text Box Labels
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label=Label(root,text="City")
city_label.grid(row=3,column=0)
state_label=Label(root,text="State")
state_label.grid(row=4,column=0)
pincode_label=Label(root,text="Pincode")
pincode_label.grid(row=5,column=0)
delete_label=Label(root,text="OID Number")
delete_label.grid(row=9,column=0,pady=5)

#Submit Button
submit_button=Button(root,text="Add Record To Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=110)


#Create a Query Button
query_button=Button(root,text="Show Records",command=query)
query_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Delete Button
delete_button=Button(root,text="Delete Record",command=delete)
delete_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=138)

#Edit Button
edit_button=Button(root,text="Edit Record",command=edit)
edit_button.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=144)


#Commit Changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()




