import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

window = tk.Tk()
window.title("재고 관리 프로그램")
window.geometry("600x400")

# 업체명
label_name = tk.Label(window, text="업체명:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

# 단가
label_price = tk.Label(window, text="단가:")
label_price.pack()
entry_price = tk.Entry(window)
entry_price.pack()

# 개수
label_quantity = tk.Label(window, text="개수:")
label_quantity.pack()
entry_quantity = tk.Entry(window)
entry_quantity.pack()

# 입고날짜 (연월)
label_date_year_month = tk.Label(window, text="입고날짜 (연월):")
label_date_year_month.pack()
date_options_year_month = [f"2023-{month:02d}" for month in range(1, 13)]
combo_date_year_month = ttk.Combobox(window, values=date_options_year_month, state="readonly")
combo_date_year_month.pack()

# 총금액
label_total = tk.Label(window, text="총금액:")
label_total.pack()
entry_total = tk.Entry(window, state="readonly")
entry_total.pack()

# 저장 버튼
def save_data():
    name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    
    # 선택된 날짜 확인
    selected_date = combo_date_year_month.get()
    if not selected_date:
        messagebox.showwarning("경고", "입고날짜를 선택하세요.")
        return
    
    # 숫자 입력 확인
    if not (price.isdigit() and quantity.isdigit()):
        messagebox.showwarning("경고", "단가와 개수는 숫자로 입력하세요.")
        return
    
    price = float(price)
    quantity = int(quantity)

    total = price * quantity
    entry_total.configure(state="normal")
    entry_total.delete(0, tk.END)
    entry_total.insert(0, total)
    entry_total.configure(state="readonly")

    file_exists = os.path.isfile('inventory.csv')
    with open('inventory.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["업체명", "입고날짜", "단가", "개수", "총금액"])
        writer.writerow([name, selected_date, price, quantity, total])

    # CSV 내용 표시 업데이트
    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # 리스트 박스 초기화
    listbox_data.delete(0, tk.END)

    # CSV 내용 추가
    for row in data:
        listbox_data.insert(tk.END, " | ".join(row))

# CSV 내용 표시
label_data = tk.Label(window, text="CSV 내용:")
label_data.pack()
listbox_data = tk.Listbox(window, height=10, width=40)
listbox_data.pack()

# 저장 버튼
save_button = tk.Button(window, text="저장", command=save_data)
save_button.pack()

window.mainloop()
