from tkinter import *
import joblib
gui = Tk()
gui.geometry("735x300")
gui.title("Customer Segmentation")
model = joblib.load("C:\\Users\\Akanksha Uniyal\\MY_Projects\\CustomerSegementaion\\customer_segmentation")

def predict():
    textBox3.delete("1.0", END);
    income = textBox1.get("1.0", "end-1c")
    spending = textBox2.get("1.0", "end-1c")
    val = [[income,spending]]
    res = model.predict(val)
    print(res[0])
    if(res[0]==0):
        textBox3.insert(INSERT,"Customer with Middle class annual income and Middle class annual spend")
    elif(res[0]==1):
        textBox3.insert(INSERT,"Customer with high annual income and low annual spend")
    elif(res[0]==2):
        textBox3.insert(INSERT,"Customer with low annual income and low annual spend")
    elif(res[0]==3):
        textBox3.insert(INSERT,"Customer with low annual income and high annual spend")
    elif(res[0]==4):
        textBox3.insert(INSERT,"Customer with high annual income and high annual spend")

label1 = Label(gui,text="Annual Income",font = "15")
textBox1 = Text(gui,height=1,width=15,font = "lucida");

label2 = Label(gui,text="Spending Score",font = "15")
textBox2 = Text(gui,height=1,width=15,font = "lucida");

label3 = Label(gui,text="Prediction",font = "15")
textBox3 = Text(gui,height=1,width=50,font = "lucida");

button1 = Button(gui,text="Predict",font = "15",command = predict)

label1.grid(row=0, column=1,pady=20, padx=35,)
label2.grid(row=1, column=1,pady=15, padx=35)

textBox1.grid(row=0, column=2,pady=15, padx=15,sticky = W)
textBox2.grid(row=1, column=2,pady=15, padx=15,sticky = W)

button1.grid(row=3,column=2,pady=15, padx=15,sticky = W)

label3.grid(row=4,column=1,padx=35,pady=15)
textBox3.grid(row=4,column=2,pady=15, padx=15,sticky = W)


gui.mainloop()
