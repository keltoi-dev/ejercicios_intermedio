# Practicando POO
# Germán Fraga

from tkinter.messagebox import showerror, askokcancel
from manejo_base import ManageBase
from aux_modelo import Auxiliares
from verifica_campos import RegexCampos


# ***** FUNCIONES PARA ALTAS - BAJAS - MODIFICACIONES *****
# ----- FUNCION ALTA DE REGISTRO -----
class ManageData:
    def __init__(self, l_status, tree, var_filtro):
        self.l_status = l_status
        self.tree = tree
        self.var_filtro = var_filtro
        self.aux = Auxiliares()
        self.base = ManageBase()
        self.control = RegexCampos()

    def create_record(self, data: list):
        self.data = data
        if not self.data[0] or not self.data[1] or not self.data[2] or not self.data[3]:
            self.l_status.config(
                text="Complete todos los campos.", background="#FF5656"
            )
            return [["-" for _ in range(11)] for _ in range(1)]
        else:
            if self.control.verificar(
                "^\d{7,8}$", self.data[0]
            ) and self.control.verificar("^\d{11}$", self.data[1]):
                sql = "SELECT * from empleados WHERE dni='" + self.data[0] + "';"
                data_list = self.base.update_table(sql)
                if not data_list:
                    sql = """INSERT INTO empleados(dni, cuil, nombres, apellidos, 
                            domicilio, f_nacimiento, f_alta, obra, art, jornal) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    self.base.modify_table(sql, data)
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
                return [["-" for _ in range(11)] for _ in range(1)]

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
                self.base.modify_table(sql, (self.data[0],))
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
                self.base.modify_table(sql, data)
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
