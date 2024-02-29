from tkinter import *
import tkinter.messagebox

def entertask():
    input_text = ""

    # Definindo a função `add` dentro da função `entertask`
    def add():
        nonlocal input_text  # Isso permite que a variável `input_text` seja modificada na função `add`
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="warning!", message="Por favor, digite seu texto")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    # Criando a janela para adicionar uma nova tarefa
    root1 = Tk()
    root1.title("Adicionar Tarefa")
    entry_task = Text(root1, width=40, height=4)  # Ajustado de `text` para `Text`
    entry_task.pack()
    button_temp = Button(root1, text="Adicionar Tarefa", command=add)  # Ajustado de `button` para `Button`
    button_temp.pack()
    root1.mainloop()


def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + "✔️​"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


window = Tk()
window.title("Aplicativo To-Do DataFlair")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Adicionar tarefa", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text='Deletar tarefa selecionada', width=50,
                       command=deletetask)  # Corrigido de `entry_button` para `delete_button`
delete_button.pack(pady=3)

mark_button = Button(window, text="Marcar como concluída", width=50,
                     command=markcompleted)  # Corrigido de `entry_button` para `mark_button`
mark_button.pack(pady=3)

window.mainloop()
