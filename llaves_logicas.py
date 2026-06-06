import tkinter as tk
import os

# --- CONFIGURACIÓN DE COLORES Y ESTILO ---
BG_COLOR = '#1c8ada'  
FG_COLOR = '#ffffff'  
ON_COLOR = '#ffd700'  
OFF_COLOR = '#333333' 
SWITCH_BG_OFF = '#555555'
SWITCH_BG_ON = '#4caf50'

FONT_TITLE = ("Consolas", 20, "bold")
FONT_TEXT = ("Consolas", 16, "bold")
FONT_TT = ("Consolas", 12)

class ToggleSwitch(tk.Canvas):
    """Interruptor deslizable realista V/F."""
    def __init__(self, parent, command=None, *args, **kwargs):
        super().__init__(parent, width=60, height=30, bg=BG_COLOR, highlightthickness=0, *args, **kwargs)
        self.state = False
        self.command = command
        self.bg_oval = self.create_oval(2, 2, 58, 28, fill=SWITCH_BG_OFF, outline="#222222", width=2)
        self.slider = self.create_oval(4, 4, 26, 26, fill="#dddddd", outline="#ffffff")
        self.text = self.create_text(40, 15, text="F", fill="white", font=("Consolas", 10, "bold"))
        self.bind("<Button-1>", self.toggle)
        
    def toggle(self, event=None):
        self.state = not self.state
        if self.state:
            self.itemconfig(self.bg_oval, fill=SWITCH_BG_ON)
            self.coords(self.slider, 34, 4, 56, 26)
            self.itemconfig(self.text, text="V")
            self.coords(self.text, 20, 15)
        else:
            self.itemconfig(self.bg_oval, fill=SWITCH_BG_OFF)
            self.coords(self.slider, 4, 4, 26, 26)
            self.itemconfig(self.text, text="F")
            self.coords(self.text, 40, 15)
        if self.command: self.command()

    def get(self): return self.state

class LogicGateSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Puertas Lógicas PROFESIONAL")
        self.root.configure(bg=BG_COLOR)
        
        # Pantalla completa activada por defecto
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))
        
        # Configuración de grilla para aprovechar todo el ancho y distribuir el alto
        for col in range(6): self.root.grid_columnconfigure(col, weight=1)
        # 8 filas totales: Título, Cabeceras, 5 Compuertas, Nota al pie.
        for row in range(8): self.root.grid_rowconfigure(row, weight=1)

        # 1. Título principal
        tk.Label(root, text="SIMULADOR DE PUERTAS LÓGICAS-GRUPO 5", 
                 bg=BG_COLOR, fg=FG_COLOR, font=FONT_TITLE).grid(row=0, column=0, columnspan=6, pady=2)
        
        self.gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR']
        self.gate_data = {}
        
        # Diccionario para mantener en memoria las imágenes cargadas y que Tkinter no las borre
        self.photo_images = {}
        
        HEADERS = ["Símbolo", "Puerta", "Llave A", "Llave B", "Lámpara (Y)", "Tabla de Verdad"]
        for col, text in enumerate(HEADERS):
            tk.Label(root, text=text, bg=BG_COLOR, fg=FG_COLOR, font=FONT_TEXT).grid(row=1, column=col)

        for i, gate in enumerate(self.gates):
            row = i + 2
            
            # 1. Cargar el Símbolo
            img_filename = f"{gate.lower()}.png"
            if os.path.exists(img_filename):
                try:
                    img = tk.PhotoImage(file=img_filename)
                    self.photo_images[gate] = img  
                    lbl_sym = tk.Label(root, image=img, bg=BG_COLOR)
                except Exception as e:
                    lbl_sym = tk.Label(root, text=f"Error cargando\n{img_filename}", bg=BG_COLOR, fg="red", font=FONT_TT)
            else:
                lbl_sym = tk.Label(root, text=f"[Falta {img_filename}]", bg=BG_COLOR, fg=ON_COLOR, font=FONT_TT)
                
            lbl_sym.grid(row=row, column=0)
            
            # 2. Nombre de la puerta
            tk.Label(root, text=gate, bg=BG_COLOR, fg=FG_COLOR, font=FONT_TEXT).grid(row=row, column=1)
            
            # 3. Llave A 
            sw_a = ToggleSwitch(root, command=lambda g=gate: self.update_gate(g))
            sw_a.grid(row=row, column=2)
            
            # 4. Llave B 
            if gate == 'NOT':
                tk.Label(root, text="---", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TEXT).grid(row=row, column=3)
                sw_b = None
            else:
                sw_b = ToggleSwitch(root, command=lambda g=gate: self.update_gate(g))
                sw_b.grid(row=row, column=3)
            
            # 5. Lámpara con resplandor visual
            canvas_bulb = tk.Canvas(root, width=80, height=80, bg=BG_COLOR, highlightthickness=0)
            glow = canvas_bulb.create_oval(10, 10, 70, 70, fill=BG_COLOR, outline=BG_COLOR)
            bulb = canvas_bulb.create_oval(25, 25, 55, 55, fill=OFF_COLOR, outline="#111111", width=2)
            canvas_bulb.create_rectangle(32, 55, 48, 65, fill="#888888", outline="#111111")
            canvas_bulb.grid(row=row, column=4)
            
            # 6. Tabla de Verdad
            tt_label = tk.Label(root, bg="#0f4c75", fg=FG_COLOR, font=FONT_TT, justify="left", 
                                padx=20, pady=10, relief="ridge", bd=2)
            tt_label.grid(row=row, column=5)
            
            self.gate_data[gate] = {
                'sw_a': sw_a, 'sw_b': sw_b, 'canvas_bulb': canvas_bulb,
                'bulb': bulb, 'glow': glow, 'tt_label': tt_label
            }
            self.update_gate(gate)

        # 8. Nota al pie sobre IA
        tk.Label(
            root, 
            text="Nota: El código fuente de este simulador fue desarrollado con la asistencia de la inteligencia artificial Gemini.", 
            bg=BG_COLOR, 
            fg=FG_COLOR, 
            font=("Consolas", 9)
        ).grid(row=7, column=0, columnspan=6, pady=2, sticky="s")

    def update_gate(self, gate):
        """Calcula la lógica Booleana, actualiza la lámpara y la tabla de verdad V/F."""
        data = self.gate_data[gate]
        a = data['sw_a'].get()
        b = data['sw_b'].get() if data['sw_b'] else False
        
        # Evaluación lógica pura
        if gate == 'AND': out = a and b
        elif gate == 'OR': out = a or b
        elif gate == 'NAND': out = not (a and b)
        elif gate == 'NOR': out = not (a or b)
        elif gate == 'NOT': out = not a
            
        # Actualización visual de la lámpara
        if out:
            data['canvas_bulb'].itemconfig(data['bulb'], fill=ON_COLOR)
            data['canvas_bulb'].itemconfig(data['glow'], fill="#e6c200", outline="#e6c200") 
        else:
            data['canvas_bulb'].itemconfig(data['bulb'], fill=OFF_COLOR)
            data['canvas_bulb'].itemconfig(data['glow'], fill=BG_COLOR, outline=BG_COLOR) 
            
        data['tt_label'].config(text=self.gen_table_text(a, b, gate))
        
    def gen_table_text(self, curr_a, curr_b, gate):
        """Genera el texto de la tabla de verdad usando V/F y marca la fila activa con ►."""
        def to_vf(val): return "V" if val else "F"
        def evaluate_logic(x, y, g):
            if g == 'AND': return x and y
            if g == 'OR': return x or y
            if g == 'NAND': return not (x and y)
            if g == 'NOR': return not (x or y)
            if g == 'NOT': return not x
            
        lines = []
        if gate != 'NOT':
            lines.append(" A   B | Y ")
            lines.append("-" * 11)
            for i in [True, False]:
                for j in [True, False]:
                    res = evaluate_logic(i, j, gate)
                    prefix = "►" if (i == curr_a and j == curr_b) else " "
                    lines.append(f"{prefix}{to_vf(i)}   {to_vf(j)} | {to_vf(res)}")
        else:
            lines.append(" A | Y ")
            lines.append("-" * 7)
            for i in [True, False]:
                res = evaluate_logic(i, None, gate)
                prefix = "►" if (i == curr_a) else " "
                lines.append(f"{prefix}{to_vf(i)} | {to_vf(res)}")
        return "\n".join(lines)

if __name__ == "__main__":
    root = tk.Tk()
    app = LogicGateSimulator(root)
    root.mainloop()