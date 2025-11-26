import tkinter as tk
from tkinter import messagebox

# --- Класи (Model) ---
class Character:
    def __init__(self, name, base_strength, crit_chance, crit_multiplier):
        self.name = name
        self.base_strength = base_strength
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier

class Weapon:
    def __init__(self, name, damage, speed):
        self.name = name
        self.damage = damage
        self.speed = speed

class Build:
    def __init__(self, character, weapon):
        self.character = character
        self.weapon = weapon

    def calculate_dps(self):
        # Формула: (БазоваСила + ШкодаЗброї) * Швидкість * (1 + (Шанс * Множник))
        base_dmg = self.character.base_strength + self.weapon.damage
        attack_speed = self.weapon.speed
        
        crit_part = 1 + (self.character.crit_chance / 100) * (self.character.crit_multiplier - 1)
        
        final_dps = base_dmg * attack_speed * crit_part
        return round(final_dps, 2)

# --- Інтерфейс (View) ---
def on_calculate():
    try:
        # Отримуємо дані з полів
        str_val = float(entry_str.get())
        crit_c_val = float(entry_crit_c.get())
        crit_m_val = float(entry_crit_m.get())
        
        dmg_val = float(entry_dmg.get())
        spd_val = float(entry_spd.get())
        
        # Створюємо об'єкти
        hero = Character("Hero", str_val, crit_c_val, crit_m_val)
        sword = Weapon("Sword", dmg_val, spd_val)
        current_build = Build(hero, sword)
        
        # Рахуємо
        result = current_build.calculate_dps()
        label_result.config(text=f"DPS: {result}")
        
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа!")

# Налаштування вікна
root = tk.Tk()
root.title("RPG DPS Calculator")
root.geometry("300x400")

tk.Label(root, text="Сила персонажа:").pack()
entry_str = tk.Entry(root)
entry_str.pack()

tk.Label(root, text="Шанс криту (%):").pack()
entry_crit_c = tk.Entry(root)
entry_crit_c.pack()

tk.Label(root, text="Множник криту (x):").pack()
entry_crit_m = tk.Entry(root)
entry_crit_m.pack()

tk.Label(root, text="----- ЗБРОЯ -----").pack(pady=10)

tk.Label(root, text="Шкода зброї:").pack()
entry_dmg = tk.Entry(root)
entry_dmg.pack()

tk.Label(root, text="Швидкість атаки:").pack()
entry_spd = tk.Entry(root)
entry_spd.pack()

btn = tk.Button(root, text="Розрахувати DPS", command=on_calculate, bg="green", fg="white")
btn.pack(pady=20)

label_result = tk.Label(root, text="DPS: 0", font=("Arial", 14, "bold"))
label_result.pack()

root.mainloop()