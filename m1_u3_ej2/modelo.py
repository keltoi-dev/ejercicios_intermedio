import re
from tkinter.messagebox import showerror, askokcancel
from manejo_base import ManageBase

base = ManageBase()


# ***** FUNCIONES PARA ALTAS - BAJAS - MODIFICACIONES *****
# ----- FUNCION ALTA DE REGISTRO -----
class ManageData:
    def __init__(self, l_status, tree, var_filtro):
        self.l_status = l_status
        self.tree = tree
        self.var_filtro = var_filtro
        self.aux = Auxiliares()

    def create_record(self, data: list):
        self.data = data
        if not self.data[0] or not self.data[1] or not self.data[2] or not self.data[3]:
            self.l_status.config(
                text="Complete todos los campos.", background="#FF5656"
            )
        else:
            cadena_dni, cadena_cuil = self.data[0], self.data[1]
            patron_dni, patron_cuil = "^\d{7,8}$", "^\d{11}$"
            if (re.match(patron_dni, cadena_dni)) and (
                re.match(patron_cuil, cadena_cuil)
            ):
                sql = "SELECT * from empleados WHERE dni='" + self.data[0] + "';"
                data_list = base.update_table(sql)
                if not data_list:
                    sql = """INSERT INTO empleados(dni, cuil, nombres, apellidos, 
                            domicilio, f_nacimiento, f_alta, obra, art, jornal) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    base.modify_table(sql, data)
                    self.l_status.config(
                        text="Los datos han sido guardados correctamente.",
                        background="#B9F582",
                    )
                    self.aux.update_treeview(self.tree, self.var_filtro)
                else:
                    self.l_status.config(
                        text="El DNI ingresado ya está cargado en la base de datos.",
                        background="#FF5656",
                    )
                    showerror("ATENCIÓN!!", "El DNI ingresado ya fue cargado.")
                return [["" for _ in range(11)] for _ in range(1)]
            else:
                self.l_status.config(
                    text="Verifique los datos ingresados.", background="#FF5656"
                )
                showerror("ATENCIÓN!!", "La informacion cargada es incorrecta.")
                return [["a" for _ in range(11)] for _ in range(1)]

    # ----- FUNCION DE BAJA DE REGISTRO -----
    def delete_record(self, data: list):
        self.data = data
        if not self.data[0]:
            showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
            self.l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
        else:
            sql = "DELETE FROM empleados WHERE dni = ?;"
            option = askokcancel(
                "Borra registro", "¿Está seguro que quiere eliminar ese registro?"
            )
            if option:
                base.modify_table(sql, (self.data[0],))
                self.aux.update_treeview(self.tree, self.var_filtro)
                self.l_status.config(
                    text="Los datos han sido eliminados correctamente.",
                    background="#B9F582",
                )
            else:
                self.l_status.config(
                    text="Se ha cancelado la eliminación de los datos.",
                    background="#B9F582",
                )
        return [["" for _ in range(11)] for _ in range(1)]

    # ----- FUNCION DE MODIFICACION DE REGISTROS -----
    def modify_record(self, data: list):
        self.data = data
        if not self.data[0]:
            showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
            self.l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
        else:
            sql = """UPDATE empleados SET nombres = ?, apellidos = ?, domicilio = ?, 
                    f_nacimiento = ?, f_alta = ?, obra = ?, art = ?, 
                    jornal = ? WHERE dni = ?;"""
            data.append(self.data[0])
            option = askokcancel(
                "Modifica registro", "¿Está seguro que quiere modificar ese registro?"
            )
            if option:
                for _ in range(2):
                    data.pop(0)
                base.modify_table(sql, data)
                #            set_entry([["" for _ in range(11)] for _ in range(1)])
                self.l_status.config(
                    text="Los datos han sido modificados correctamente.",
                    background="#B9F582",
                )
                self.aux.update_treeview(self.tree, self.var_filtro)
            else:
                self.l_status.config(
                    text="Se ha cancelado la modificación de los datos.",
                    background="#B9F582",
                )
        return [["" for _ in range(11)] for _ in range(1)]


# ***** FUNCIONES PARA CONSULTAS Y TREEVIEW *****
# ----- FUNCION DE CONSULTA DESDE TREEVIEW -----
class Auxiliares(ManageData):
    def __init__(self):
        pass

    def consult_record(self, tree):
        self.tree = tree
        item = self.tree.item(self.tree.selection())
        data = int(item["text"])
        sql = "SELECT * FROM empleados WHERE id = " + str(data)
        data_list = base.update_table(sql)
        return data_list

    # ----- FUNCION DE BUSQUEDA -----
    def search_record(self, indice: str, l_status):
        self.indice = indice
        self.l_status = l_status
        sql = "SELECT * from empleados WHERE dni='" + self.indice + "';"
        data_list = base.update_table(sql)
        if not data_list:
            self.l_status.config(
                text="No se encontró el DNI solicitado en la base de datos.",
                background="#ff1b1b",
            )
            showerror("ATENCIÓN!!", "Este DNI no existe en la base de datos")
        else:
            self.l_status.config(
                text="La búsqueda se concreto correctamente.", background="#B9F582"
            )
        return data_list

    def conect_database(self):
        try:
            base.create_table()
            return "Se ha creado correctamente la base de datos."
        except:
            return "La base de datos ya está creada. Se ha accedido correctamente."

    # ----- FUNCION ACTUALIZAR TREEVIEW -----
    def update_treeview(self, mitreview, var_filtro, parameter=None):
        self.mitreview = mitreview
        self.var_filtro = var_filtro
        self.parameter = parameter
        if not parameter:
            sql = "SELECT id, dni, nombres, apellidos, obra, jornal FROM empleados ORDER BY id DESC;"
        else:
            sql = (
                "SELECT id, dni, nombres, apellidos, obra as 'Obra', jornal FROM empleados WHERE obra='"
                + parameter
                + "' ORDER BY id DESC;"
            )
        data_list = base.update_table(sql)

        records = self.mitreview.get_children()
        for element in records:
            self.mitreview.delete(element)

        for row in data_list:
            self.mitreview.insert(
                "", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5])
            )
        self.var_filtro.set("")

    # ----- FUNCION DE CIERRE DE LA APLICACION -----
    def close_app(self, window):
        option = askokcancel("Cerrar la aplicación", "¿Está seguro que quiere salir?")
        if option:
            window.destroy()
