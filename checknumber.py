import phonenumbers
from phonenumbers import NumberParseException, carrier, geocoder
from tkinter import messagebox, Tk,Label,Entry,Button

def check_number():
    #Captura o número do celular
    try:
        cel= cel_entry.get()
        celular = phonenumbers.parse(cel)

        #Verifica se o número é Valido
        celular_validate = phonenumbers.is_valid_number(celular)
        if celular_validate:
            numero = f"Este número '{cel}' é valido e existe!"
        else:
            numero = f"Este número '{cel} não existe"
            
        #Verifica a operadora do celular
        operadora = carrier.name_for_number(celular,lang='pt-br')

        #Verifica o estado a que aquele número pertence
        state_number = geocoder.description_for_number(celular,lang='pt-br')
        
        messagebox.showinfo(
            title=f"Número {cel}",
            message=f"O número {cel} é válido e existe. \n "
                    f"Este número é da operadora {operadora}. \n"
                    f"E é do estado/província {state_number}."
        )
    except NumberParseException:
        messagebox.showinfo(
            title=f"Campo vazio",
            message="Por favor, digite um número válido.")

if __name__=='__main__':
    window = Tk()
    window.title("Verificador de Celular")
    window.config(padx=10,pady=100)
    
    # Labels
    label_cel = Label(window,text="Digite o número do Celular \n (padrão +XXXX9XXXXXXXX):")
    label_cel.grid(row=2,column=0)
    
    # Entradas
    cel_entry = Entry(width=35)
    cel_entry.grid(row=2,column=1, columnspan=2)
    cel_entry.focus()
    add_button = Button(text="Verificar número", width=36, command=check_number)
    add_button.grid(row=4,column=1, columnspan=2)
    
    window.mainloop()
